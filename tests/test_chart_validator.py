from __future__ import annotations

import tempfile
import unittest
from pathlib import Path
from subprocess import run

from tools.chart_validator import validate_chart


VALID_CHART = """\
@title Más
@artist Miel San Marcos
@key D
@tempo 140
@time 4/4
@lead-vocal Paloma Ramos
@details Original arrangement

@arrangement intro chorus-1 intro

[intro | IN | Intro]
| 4 | 2 | 6 | 3 |

[chorus-1 | CH | Chorus | 1]
| 1 | 4 | _ | _ |
"""


class ChartValidatorTest(unittest.TestCase):
    def validate(self, content: str | bytes):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory, "mas.chart")
            path.write_bytes(content if isinstance(content, bytes) else content.encode("utf-8"))
            return validate_chart(path)

    def test_valid_chart_accepts_bom_crlf_comments_and_forward_references(self):
        source = "# comment\n\n" + VALID_CHART
        result = self.validate(b"\xef\xbb\xbf" + source.replace("\n", "\r\n").encode("utf-8"))

        self.assertEqual([], result.diagnostics)
        self.assertEqual("Más", result.chart.metadata["title"])
        self.assertEqual(("intro", "chorus-1", "intro"), result.chart.arrangement)
        self.assertEqual(("intro", "chorus-1"), tuple(section.id for section in result.chart.sections))
        self.assertEqual(
            ("1", "4", None, None),
            tuple(
                slot.events[0].chord if slot is not None else None
                for slot in result.chart.sections[1].rows[0].slots
            ),
        )

    def test_metadata_must_be_complete_ordered_and_valid(self):
        source = VALID_CHART.replace("@artist Miel San Marcos\n@key D", "@key H\n@artist Miel San Marcos")
        result = self.validate(source)

        self.assertIsNone(result.chart)
        self.assertEqual(
            [(2, 2, "E011"), (2, 6, "E014"), (3, 2, "E011")],
            [(item.line, item.column, item.code) for item in result.diagnostics],
        )

        missing = self.validate(VALID_CHART.replace("@artist Miel San Marcos\n", ""))
        missing_artist = next(item for item in missing.errors if item.message == "missing required metadata '@artist'")
        self.assertEqual((15, 1, "E013"), (missing_artist.line, missing_artist.column, missing_artist.code))

    def test_sections_enforce_identity_ordinals_and_nonempty_rows(self):
        source = VALID_CHART.replace(
            "[intro | IN | Intro]\n| 4 | 2 | 6 | 3 |",
            "[intro | CH | Intro]\n[chorus-1 | CH | Duplicate | 1]\n| 4 | 2 | 6 | 3 |",
        )
        result = self.validate(source)

        self.assertIsNone(result.chart)
        self.assertEqual(
            ["E025", "E028", "E025", "E026"],
            [item.code for item in result.errors],
        )

    def test_rows_require_four_slots_with_only_trailing_empty_slots(self):
        source = VALID_CHART.replace(
            "| 4 | 2 | 6 | 3 |",
            "| _ | 2 | _ | 3 |\n| 1 | 2 | 3 |",
        )
        result = self.validate(source)

        self.assertEqual(["E033", "E034", "E034", "E031"], [item.code for item in result.errors])

    def test_unresolved_arrangement_is_error_and_unreferenced_section_is_warning(self):
        source = VALID_CHART.replace("@arrangement intro chorus-1 intro", "@arrangement intro missing")
        result = self.validate(source)

        self.assertIsNone(result.chart)
        self.assertEqual(["E053"], [item.code for item in result.errors])
        self.assertEqual(["W051"], [item.code for item in result.warnings])
        self.assertIn("mas.chart:9:20 [E053]", result.errors[0].format())

    def test_tabs_and_multiple_recoverable_errors_are_sorted(self):
        source = VALID_CHART.replace("@key D", "@key H\t").replace("| 1 | 4 | _ | _ |", "| _ | 4 | _ | 7 |")
        result = self.validate(source)

        self.assertEqual(
            [(3, 6, "E014"), (3, 7, "E003"), (15, 3, "E033"), (15, 7, "E034"), (15, 15, "E034")],
            [(item.line, item.column, item.code) for item in result.errors],
        )

    def test_optional_metadata_may_be_omitted_but_not_reordered(self):
        without_lead = VALID_CHART.replace("@lead-vocal Paloma Ramos\n", "")
        self.assertEqual([], self.validate(without_lead).errors)

        reordered = VALID_CHART.replace(
            "@lead-vocal Paloma Ramos\n@details Original arrangement",
            "@details Original arrangement\n@lead-vocal Paloma Ramos",
        )
        self.assertEqual(["E011"], [item.code for item in self.validate(reordered).errors])

    def test_multiple_arrangements_concatenate_and_row_notes_are_typed(self):
        source = VALID_CHART.replace(
            "@arrangement intro chorus-1 intro",
            "@arrangement intro\n@arrangement chorus-1 intro",
        ).replace(
            "| 4 | 2 | 6 | 3 |",
            "| 4 | 2 | 6 | 3 | direction: Rakes || melody: a ; b ; c ; d",
        )
        result = self.validate(source)

        self.assertEqual([], result.errors)
        self.assertEqual(("intro", "chorus-1", "intro"), result.chart.arrangement)
        self.assertEqual(
            (
                ("direction", "Rakes"),
                ("melody", ("a", "b", "c", "d")),
            ),
            tuple((note.kind, note.value) for note in result.chart.sections[0].rows[0].notes),
        )

        invalid_note = source.replace(
            "direction: Rakes || melody: a ; b ; c ; d",
            "cue: validate this in issue 13",
        )
        self.assertEqual(["E041"], [item.code for item in self.validate(invalid_note).errors])

    def test_lyrics_belong_to_numbered_arrangement_occurrences(self):
        source = VALID_CHART.replace(
            "@arrangement intro chorus-1 intro",
            "@arrangement intro chorus-1 intro\n"
            "@lyrics 2 chorus-1 | Más de Tu presencia | Más de Tu poder",
        )

        result = self.validate(source)

        self.assertEqual([], result.errors)
        self.assertEqual(
            ((), ("Más de Tu presencia", "Más de Tu poder"), ()),
            result.chart.lyrics,
        )

    def test_lyrics_validate_occurrence_identity_content_and_uniqueness(self):
        source = VALID_CHART.replace(
            "@arrangement intro chorus-1 intro",
            "@arrangement intro chorus-1 intro\n"
            "@lyrics 0 intro | Invalid occurrence\n"
            "@lyrics 2 intro | Wrong Section\n"
            "@lyrics 2 chorus-1 | Duplicate\n"
            "@lyrics 4 intro | Out of range\n"
            "@lyrics 3 intro |",
        )

        result = self.validate(source)

        self.assertEqual(
            [
                (10, 9, "E061"),
                (11, 11, "E062"),
                (12, 9, "E063"),
                (13, 9, "E061"),
                (14, 9, "E064"),
            ],
            [(item.line, item.column, item.code) for item in result.errors],
        )

    def test_arrangements_must_precede_lyrics_blocks(self):
        source = VALID_CHART.replace(
            "@arrangement intro chorus-1 intro",
            "@arrangement intro chorus-1 intro\n"
            "@lyrics 2 chorus-1 | Más de Tu presencia\n"
            "@arrangement intro",
        )

        result = self.validate(source)

        self.assertEqual(["E050"], [item.code for item in result.errors])

    def test_every_supported_chord_suffix_and_slash_form_is_accepted(self):
        source = VALID_CHART.replace(
            "| 4 | 2 | 6 | 3 |",
            "| 1 2m 3m7 4maj7 | 5sus2 6sus4 7dim 1aug | 2add9 3/5 b4 #5m7/b7 | X |",
        )
        result = self.validate(source)

        self.assertEqual([], result.errors)
        self.assertEqual(
            (
                ("1", "2m", "3m7", "4maj7"),
                ("5sus2", "6sus4", "7dim", "1aug"),
                ("2add9", "3/5", "b4", "#5m7/b7"),
                (None,),
            ),
            tuple(tuple(event.chord for event in slot.events) for slot in result.chart.sections[0].rows[0].slots),
        )

    def test_bar_timing_rejects_ambiguous_partial_and_wrong_dot_totals(self):
        source = VALID_CHART.replace(
            "| 4 | 2 | 6 | 3 |",
            "| 1 2 3 | 1. 2 | 1. 2.. | 1.. 2... |",
        )
        result = self.validate(source)

        self.assertIsNone(result.chart)
        self.assertEqual(["E038", "E037", "E038", "E038"], [item.code for item in result.errors])

    def test_diamonds_are_solo_dotless_chords(self):
        source = VALID_CHART.replace(
            "| 4 | 2 | 6 | 3 |",
            "| <3>. | <1> X | <8> | <1m7/3> |",
        )
        result = self.validate(source)

        self.assertIsNone(result.chart)
        self.assertEqual(["E039", "E039", "E036"], [item.code for item in result.errors])

    def test_invalid_events_suggest_canonical_case_and_ascii_accidentals(self):
        source = VALID_CHART.replace(
            "| 4 | 2 | 6 | 3 |",
            "| x | ♭2 | ♯4 | 8 |",
        )
        result = self.validate(source)

        self.assertEqual(["E036", "E036", "E036", "E036"], [item.code for item in result.errors])
        self.assertIn("uppercase 'X'", result.errors[0].message)
        self.assertIn("ASCII 'b'", result.errors[1].message)
        self.assertIn("ASCII '#'", result.errors[2].message)

    def test_row_notes_reject_empty_unknown_bad_arity_and_bad_escapes(self):
        source = VALID_CHART.replace(
            "| 4 | 2 | 6 | 3 |",
            r"| 4 | 2 | 6 | 3 | direction: || melody: ; ; ; || melody: a ; b ; c "
            r"|| direction: bad\n || cue: unknown",
        )
        result = self.validate(source)

        self.assertIsNone(result.chart)
        self.assertEqual(
            ["E042", "E044", "E043", "E045", "E041"],
            [item.code for item in result.errors],
        )

    def test_free_text_escapes_apply_to_metadata_and_section_names(self):
        source = VALID_CHART.replace(
            "@title Más",
            r"@title Más \| Live \] Set\; A\\B",
        ).replace(
            "[intro | IN | Intro]",
            r"[intro | IN | Intro \| Pickup \] End]",
        )
        result = self.validate(source)

        self.assertEqual([], result.errors)
        self.assertEqual("Más | Live ] Set; A\\B", result.chart.metadata["title"])
        self.assertEqual("Intro | Pickup ] End", result.chart.sections[0].name)

        invalid = source.replace(r"@title Más \| Live \] Set\; A\\B", r"@title Bad\q")
        self.assertEqual(["E045"], [item.code for item in self.validate(invalid).errors])

    def test_valid_events_and_ordered_row_notes_are_normalized(self):
        source = VALID_CHART.replace(
            "| 4 | 2 | 6 | 3 |",
            "| b2m7... 5/7. | X. #4sus2... | <1maj7/3> | 6add9 | "
            r"direction: Rakes \| hold \] semi\; slash\\ || melody: 1 ; ; 3\;4 ; 5",
        )
        result = self.validate(source)

        self.assertEqual([], result.errors)
        row = result.chart.sections[0].rows[0]
        self.assertEqual(
            (
                (("chord", "b2m7", 3, False), ("chord", "5/7", 1, False)),
                (("no-chord", None, 1, False), ("chord", "#4sus2", 3, False)),
                (("chord", "1maj7/3", None, True),),
                (("chord", "6add9", None, False),),
            ),
            tuple(
                tuple((event.kind, event.chord, event.beats, event.diamond) for event in bar.events)
                for bar in row.slots
            ),
        )
        self.assertEqual(
            (
                ("direction", "Rakes | hold ] semi; slash\\"),
                ("melody", ("1", "", "3;4", "5")),
            ),
            tuple((note.kind, note.value) for note in row.notes),
        )

    def test_invalid_utf8_and_lone_carriage_return_report_encoding_family(self):
        self.assertEqual(["E001"], [item.code for item in self.validate(b"\xff").errors])
        self.assertEqual(["E002"], [item.code for item in self.validate(VALID_CHART.replace("\n", "\r")).errors])

    def test_cli_returns_nonzero_and_prints_source_diagnostic(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory, "bad.chart")
            path.write_text(VALID_CHART.replace("@key D", "@key H"), encoding="utf-8")
            completed = run(
                ["python3", "tools/chart_validator.py", str(path)],
                check=False,
                capture_output=True,
                text=True,
            )

        self.assertEqual(1, completed.returncode)
        self.assertIn("bad.chart:3:6 [E014] invalid key 'H'", completed.stdout)
        self.assertIn("  @key H\n       ^", completed.stdout)

    def test_warning_is_nonblocking_for_chart_and_cli(self):
        source = VALID_CHART.replace("@arrangement intro chorus-1 intro", "@arrangement intro")
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory, "warning.chart")
            path.write_text(source, encoding="utf-8")
            result = validate_chart(path)
            completed = run(
                ["python3", "tools/chart_validator.py", str(path)],
                check=False,
                capture_output=True,
                text=True,
            )

        self.assertIsNotNone(result.chart)
        self.assertEqual(["W051"], [item.code for item in result.warnings])
        self.assertEqual(0, completed.returncode)
        self.assertIn("[W051]", completed.stdout)

    def test_section_identifier_code_and_custom_code_rules(self):
        malformed = VALID_CHART.replace("[intro | IN | Intro]", "[Intro | in | Intro]")
        self.assertEqual(
            ["E053", "E053", "E022", "E023"],
            [item.code for item in self.validate(malformed).errors],
        )

        duplicate_custom = VALID_CHART.replace("[intro | IN | Intro]", "[intro | ZZ | Intro]").replace(
            "[chorus-1 | CH | Chorus | 1]",
            "[intro | ZZ | Duplicate]",
        ).replace("@arrangement intro chorus-1 intro", "@arrangement intro")
        self.assertEqual(
            ["E027", "E026"],
            [item.code for item in self.validate(duplicate_custom).errors],
        )

    def test_repeated_standard_codes_require_distinct_positive_ordinals(self):
        source = VALID_CHART.replace("@arrangement intro chorus-1 intro", "@arrangement intro intro-2").replace(
            "[intro | IN | Intro]",
            "[intro | IN | Intro | 1]",
        ).replace(
            "[chorus-1 | CH | Chorus | 1]",
            "[intro-2 | IN | Intro | 2]",
        )
        self.assertEqual([], self.validate(source).errors)

        duplicate = source.replace("[intro-2 | IN | Intro | 2]", "[intro-2 | IN | Intro | 1]")
        self.assertEqual(["E025"], [item.code for item in self.validate(duplicate).errors])

    def test_arrangement_must_exist_before_sections_and_sections_are_required(self):
        metadata = "\n".join(VALID_CHART.splitlines()[:5]) + "\n"
        self.assertEqual(
            ["E020", "E052"],
            [item.code for item in self.validate(metadata).errors],
        )

        arrangement = "@arrangement intro chorus-1 intro\n\n"
        after_sections = VALID_CHART.replace(arrangement, "") + arrangement
        result = self.validate(after_sections)
        self.assertIn("E050", [item.code for item in result.errors])
        self.assertIn("E052", [item.code for item in result.errors])

    def test_inline_hash_is_preserved_as_metadata_content(self):
        source = VALID_CHART.replace("@title Más", "@title Más # live version")
        result = self.validate(source)

        self.assertEqual([], result.errors)
        self.assertEqual("Más # live version", result.chart.metadata["title"])


if __name__ == "__main__":
    unittest.main()
