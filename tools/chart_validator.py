#!/usr/bin/env python3
"""Validate the structural portion of Setlist Viewer ``.chart`` files."""

from __future__ import annotations

import argparse
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


REQUIRED_METADATA = ("title", "artist", "key", "tempo", "time")
OPTIONAL_METADATA = ("lead-vocal", "details")
ALL_METADATA = REQUIRED_METADATA + OPTIONAL_METADATA
STANDARD_CODES = {"IN", "IS", "VS", "TG", "PC", "PS", "CH", "BR", "TR", "EN", "OU"}
ID_PATTERN = re.compile(r"[a-z][a-z0-9-]*\Z")
KEY_PATTERN = re.compile(r"[A-G](?:b|#)?m?\Z")
CODE_PATTERN = re.compile(r"[A-Z]{2}\Z")
TIME_PATTERN = re.compile(r"([1-9][0-9]*)/(1|2|4|8|16|32|64)\Z")


@dataclass(frozen=True)
class Diagnostic:
    path: str
    line: int
    column: int
    code: str
    message: str
    source: str
    length: int = 1
    severity: str = "error"

    def format(self) -> str:
        caret = " " * (max(self.column, 1) - 1) + "^" * max(self.length, 1)
        return f"{self.path}:{self.line}:{self.column} [{self.code}] {self.message}\n  {self.source}\n  {caret}"


@dataclass(frozen=True)
class ChartRow:
    slots: tuple[str | None, str | None, str | None, str | None]
    notes: str
    line: int


@dataclass(frozen=True)
class Section:
    id: str
    code: str
    name: str
    ordinal: int | None
    rows: tuple[ChartRow, ...]
    line: int


@dataclass(frozen=True)
class Chart:
    metadata: dict[str, str]
    arrangement: tuple[str, ...]
    sections: tuple[Section, ...]


@dataclass(frozen=True)
class ValidationResult:
    chart: Chart | None
    diagnostics: list[Diagnostic]

    @property
    def errors(self) -> list[Diagnostic]:
        return [item for item in self.diagnostics if item.severity == "error"]

    @property
    def warnings(self) -> list[Diagnostic]:
        return [item for item in self.diagnostics if item.severity == "warning"]


@dataclass
class _SectionBuilder:
    id: str
    code: str
    name: str
    ordinal: int | None
    rows: list[ChartRow]
    line: int
    column: int
    source: str


class _Validator:
    def __init__(self, path: Path, text: str) -> None:
        self.path = str(path)
        self.lines = text.split("\n")
        if self.lines and self.lines[-1] == "":
            self.lines.pop()
        self.diagnostics: list[Diagnostic] = []
        self.metadata: dict[str, str] = {}
        self.arrangement: list[str] = []
        self.arrangement_positions: list[tuple[str, int, int, str]] = []
        self.sections: list[_SectionBuilder] = []
        self.current_section: _SectionBuilder | None = None
        self.phase = "metadata"

    def diagnostic(
        self,
        line: int,
        column: int,
        code: str,
        message: str,
        source: str,
        length: int = 1,
        severity: str = "error",
    ) -> None:
        self.diagnostics.append(
            Diagnostic(self.path, line, column, code, message, source, length, severity)
        )

    def run(self) -> ValidationResult:
        for number, source in enumerate(self.lines, 1):
            if "\t" in source:
                for match in re.finditer("\t", source):
                    self.diagnostic(number, match.start() + 1, "E003", "tabs are not allowed", source)
            stripped = source.strip()
            if not stripped or stripped.startswith("#"):
                continue
            column = len(source) - len(source.lstrip()) + 1
            if stripped.startswith("@"):
                self._parse_directive(number, column, stripped, source)
            elif stripped.startswith("["):
                self._parse_section(number, column, stripped, source)
            elif stripped.startswith("|"):
                self._parse_row(number, column, stripped, source)
            else:
                self.diagnostic(number, column, "E018", "expected a directive, Section, or Chart Row", source, len(stripped))

        self._finish_section()
        self._finish_metadata()
        self._finish_structure()
        self.diagnostics.sort(key=lambda item: (item.line, item.column, item.code))
        chart = None
        if not any(item.severity == "error" for item in self.diagnostics):
            chart = Chart(
                dict(self.metadata),
                tuple(self.arrangement),
                tuple(
                    Section(item.id, item.code, item.name, item.ordinal, tuple(item.rows), item.line)
                    for item in self.sections
                ),
            )
        return ValidationResult(chart, self.diagnostics)

    def _parse_directive(self, line: int, column: int, text: str, source: str) -> None:
        match = re.match(r"@([^\s]+)(?:\s+(.*))?\Z", text)
        if not match:
            self.diagnostic(line, column, "E010", "invalid directive", source, len(text))
            return
        name, value = match.group(1), (match.group(2) or "").strip()
        name_column = column + 1
        value_column = column + (match.start(2) if match.start(2) >= 0 else len(text))
        if name in ALL_METADATA:
            self._parse_metadata(line, name_column, value_column, name, value, source)
        elif name == "arrangement":
            self._parse_arrangement(line, column, value_column, value, source)
        else:
            self.diagnostic(line, name_column, "E010", f"unknown directive '@{name}'", source, len(name))

    def _parse_metadata(
        self, line: int, name_column: int, value_column: int, name: str, value: str, source: str
    ) -> None:
        if self.phase != "metadata":
            self.diagnostic(line, name_column, "E011", "metadata must precede arrangements and Sections", source, len(name))
            return
        if name in self.metadata:
            self.diagnostic(line, name_column, "E012", f"duplicate metadata '@{name}'", source, len(name))
            return
        position = ALL_METADATA.index(name)
        prior_positions = [ALL_METADATA.index(item) for item in self.metadata]
        if prior_positions and position < max(prior_positions):
            self.diagnostic(line, name_column, "E011", f"metadata '@{name}' is out of order", source, len(name))
        missing_before = [item for item in REQUIRED_METADATA[: min(position, len(REQUIRED_METADATA))] if item not in self.metadata]
        if missing_before:
            self.diagnostic(
                line,
                name_column,
                "E011",
                f"metadata '@{name}' appears before required '@{missing_before[0]}'",
                source,
                len(name),
            )
        self.metadata[name] = value
        if not value:
            self.diagnostic(line, value_column, "E013", f"metadata '@{name}' requires a value", source)
        elif name == "key" and not KEY_PATTERN.fullmatch(value):
            self.diagnostic(line, value_column, "E014", f"invalid key '{value}'", source, len(value))
        elif name == "tempo" and (not value.isdigit() or int(value) < 1):
            self.diagnostic(line, value_column, "E015", "tempo must be a positive integer", source, len(value))
        elif name == "time" and not TIME_PATTERN.fullmatch(value):
            self.diagnostic(line, value_column, "E016", "time must use a positive numerator and supported denominator", source, len(value))

    def _parse_arrangement(
        self, line: int, column: int, value_column: int, value: str, source: str
    ) -> None:
        if self.phase == "sections":
            self.diagnostic(line, column, "E050", "arrangements must precede Sections", source, len(source.strip()))
            return
        self.phase = "arrangement"
        if not value:
            self.diagnostic(line, value_column, "E052", "Expanded Arrangement cannot be empty", source)
            return
        search_from = value_column - 1
        for section_id in value.split():
            offset = source.find(section_id, search_from)
            item_column = offset + 1
            search_from = offset + len(section_id)
            if not ID_PATTERN.fullmatch(section_id):
                self.diagnostic(line, item_column, "E051", f"invalid Section ID '{section_id}'", source, len(section_id))
            else:
                self.arrangement.append(section_id)
                self.arrangement_positions.append((section_id, line, item_column, source))

    def _parse_section(self, line: int, column: int, text: str, source: str) -> None:
        self._finish_section()
        self.phase = "sections"
        if not _has_unescaped_closing_bracket(text):
            self.diagnostic(line, column, "E021", "invalid Section header", source, len(text))
            return
        inside = text[1:-1]
        fields = [item.strip() for item in _split_unescaped(inside, "|")]
        if len(fields) not in (3, 4):
            self.diagnostic(line, column, "E021", "Section header requires ID, Code, Name, and optional Ordinal", source, len(text))
            return
        section_id, code, name = fields[:3]
        ordinal_text = fields[3] if len(fields) == 4 else ""
        if not ID_PATTERN.fullmatch(section_id):
            self.diagnostic(line, column + 1, "E022", f"invalid Section ID '{section_id}'", source, max(len(section_id), 1))
        if not CODE_PATTERN.fullmatch(code):
            code_column = source.find(code, column) + 1
            self.diagnostic(line, code_column, "E023", f"invalid Section Code '{code}'", source, max(len(code), 1))
        if not name:
            self.diagnostic(line, column, "E024", "Section Name cannot be empty", source, len(text))
        ordinal = None
        if len(fields) == 4:
            if not ordinal_text.isdigit() or int(ordinal_text) < 1:
                self.diagnostic(line, column, "E025", "Section Ordinal must be a positive integer", source, len(text))
            else:
                ordinal = int(ordinal_text)
        self.current_section = _SectionBuilder(section_id, code, name, ordinal, [], line, column, source)

    def _parse_row(self, line: int, column: int, text: str, source: str) -> None:
        if self.current_section is None:
            self.diagnostic(line, column, "E030", "Chart Row must belong to a Section", source, len(text))
            return
        parsed = _split_row(text)
        if parsed is None:
            self.diagnostic(line, column, "E031", "Chart Row must contain exactly four pipe-delimited Bar slots", source, len(text))
            return
        raw_slots, notes = parsed
        slots: list[str | None] = []
        empty_seen = False
        for index, (raw_slot, offset) in enumerate(raw_slots):
            slot = raw_slot.strip()
            slot_column = column + offset + len(raw_slot) - len(raw_slot.lstrip())
            slot_length = max(len(slot), 1)
            if not slot:
                self.diagnostic(line, slot_column, "E032", "write '_' for an Empty Bar Slot", source)
                slots.append(None)
                empty_seen = True
            elif slot == "_":
                if index == 0:
                    self.diagnostic(line, slot_column, "E033", "the first Bar slot must contain a Bar", source, slot_length)
                slots.append(None)
                empty_seen = True
            else:
                if empty_seen:
                    self.diagnostic(line, slot_column, "E034", "Empty Bar Slots may only trail filled slots", source, slot_length)
                slots.append(slot)
        self.current_section.rows.append(ChartRow(tuple(slots), notes.strip(), line))

    def _finish_section(self) -> None:
        if self.current_section is None:
            return
        if not self.current_section.rows:
            self.diagnostic(
                self.current_section.line,
                self.current_section.column,
                "E028",
                f"Section '{self.current_section.id}' requires at least one Chart Row",
                self.current_section.source,
                len(self.current_section.source.strip()),
            )
        self.sections.append(self.current_section)
        self.current_section = None

    def _finish_metadata(self) -> None:
        line = len(self.lines) + 1
        for name in REQUIRED_METADATA:
            if name not in self.metadata:
                self.diagnostic(line, 1, "E013", f"missing required metadata '@{name}'", "")

    def _finish_structure(self) -> None:
        if not self.sections:
            self.diagnostic(len(self.lines) + 1, 1, "E020", "chart requires at least one Section", "")
        ids: dict[str, _SectionBuilder] = {}
        code_groups: dict[str, list[_SectionBuilder]] = {}
        for section in self.sections:
            if section.id in ids:
                self.diagnostic(section.line, section.column + 1, "E026", f"duplicate Section ID '{section.id}'", section.source, len(section.id))
            else:
                ids[section.id] = section
            code_groups.setdefault(section.code, []).append(section)
        for code, group in code_groups.items():
            if len(group) < 2:
                continue
            if code not in STANDARD_CODES:
                for section in group[1:]:
                    self.diagnostic(section.line, section.column, "E027", f"custom Section Code '{code}' must be unique", section.source, len(section.source.strip()))
                continue
            ordinals: set[int] = set()
            for section in group:
                if section.ordinal is None:
                    self.diagnostic(section.line, section.column, "E025", f"repeated standard Code '{code}' requires a unique Ordinal", section.source, len(section.source.strip()))
                elif section.ordinal in ordinals:
                    self.diagnostic(section.line, section.column, "E025", f"duplicate Ordinal {section.ordinal} for Code '{code}'", section.source, len(section.source.strip()))
                else:
                    ordinals.add(section.ordinal)
        if not self.arrangement:
            self.diagnostic(len(self.lines) + 1, 1, "E052", "chart requires a nonempty Expanded Arrangement", "")
        referenced = set(self.arrangement)
        for section_id, line, column, source in self.arrangement_positions:
            if section_id not in ids:
                self.diagnostic(line, column, "E053", f"unknown Section ID '{section_id}'", source, len(section_id))
        for section in self.sections:
            if section.id not in referenced:
                self.diagnostic(
                    section.line,
                    section.column + 1,
                    "W051",
                    f"Section '{section.id}' is not referenced by the Expanded Arrangement",
                    section.source,
                    len(section.id),
                    "warning",
                )


def _is_escaped(text: str, index: int) -> bool:
    backslashes = 0
    index -= 1
    while index >= 0 and text[index] == "\\":
        backslashes += 1
        index -= 1
    return backslashes % 2 == 1


def _split_unescaped(text: str, delimiter: str) -> list[str]:
    fields: list[str] = []
    start = 0
    for index, character in enumerate(text):
        if character == delimiter and not _is_escaped(text, index):
            fields.append(text[start:index])
            start = index + 1
    fields.append(text[start:])
    return fields


def _has_unescaped_closing_bracket(text: str) -> bool:
    return len(text) >= 2 and text[-1] == "]" and not _is_escaped(text, len(text) - 1)


def _split_row(text: str) -> tuple[list[tuple[str, int]], str] | None:
    if not text.startswith("|"):
        return None
    boundaries = [index for index, character in enumerate(text) if character == "|" and not _is_escaped(text, index)]
    if len(boundaries) < 5:
        return None
    slots = [
        (text[boundaries[index] + 1 : boundaries[index + 1]], boundaries[index] + 1)
        for index in range(4)
    ]
    notes = text[boundaries[4] + 1 :]
    note_boundaries = [
        index for index, character in enumerate(notes) if character == "|" and not _is_escaped(notes, index)
    ]
    if any(
        index + 1 >= len(note_boundaries)
        or note_boundaries[index + 1] != note_boundaries[index] + 1
        for index in range(0, len(note_boundaries), 2)
    ):
        return None
    return slots, notes


def _decode(path: Path, data: bytes) -> tuple[str | None, list[Diagnostic]]:
    try:
        text = data.decode("utf-8-sig")
    except UnicodeDecodeError as error:
        prefix = data[: error.start].decode("utf-8", errors="replace")
        line = prefix.count("\n") + 1
        source = prefix.rsplit("\n", 1)[-1]
        column = len(source) + 1
        diagnostic = Diagnostic(str(path), line, column, "E001", "input must be valid UTF-8", source)
        return None, [diagnostic]
    lone_cr = re.search(r"\r(?!\n)", text)
    if lone_cr:
        prefix = text[: lone_cr.start()]
        line = prefix.count("\n") + 1
        source = text.split("\n")[line - 1]
        column = len(prefix.rsplit("\n", 1)[-1]) + 1
        return None, [Diagnostic(str(path), line, column, "E002", "use LF or CRLF line endings", source)]
    return text.replace("\r\n", "\n"), []


def validate_chart(path: str | Path) -> ValidationResult:
    source_path = Path(path)
    try:
        data = source_path.read_bytes()
    except OSError as error:
        diagnostic = Diagnostic(str(source_path), 1, 1, "E001", str(error), "")
        return ValidationResult(None, [diagnostic])
    text, diagnostics = _decode(source_path, data)
    if text is None:
        return ValidationResult(None, diagnostics)
    return _Validator(source_path, text).run()


def validate_charts(paths: Iterable[str | Path]) -> list[ValidationResult]:
    return [validate_chart(path) for path in paths]


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("paths", nargs="+", type=Path)
    arguments = parser.parse_args(argv)
    results = validate_charts(arguments.paths)
    for result in results:
        for diagnostic in result.diagnostics:
            print(diagnostic.format())
    return 1 if any(result.errors for result in results) else 0


if __name__ == "__main__":
    raise SystemExit(main())
