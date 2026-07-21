"""PROTOTYPE — terminal viewer for chart source-format alternatives."""

from pathlib import Path
import os


HERE = Path(__file__).parent
PAGE_SIZE = 20
OPTIONS = {
    "1": {
        "name": "Strict JSON",
        "file": "formats/strict-json.json",
        "scores": (4, 5, 4, 5),
        "tradeoff": "Verbose and punctuation-heavy; strongest standard parsing and schema validation.",
    },
    "2": {
        "name": "JavaScript data",
        "file": "formats/javascript-data.js",
        "scores": (5, 3, 4, 5),
        "tradeoff": "Concise helpers and comments; executable input permits behavior and weakens validation.",
    },
    "3": {
        "name": "Small chart notation",
        "file": "formats/small-notation.chart",
        "scores": (5, 2, 5, 4),
        "tradeoff": "Fastest musician-facing edits; requires a new grammar, parser, escaping, and diagnostics.",
    },
    "4": {
        "name": "Hybrid JSON + row notation",
        "file": "formats/hybrid.json",
        "scores": (5, 4, 5, 5),
        "tradeoff": "Structured document with compact rows; only row and Row Note strings need custom parsing.",
    },
}


def clear():
    os.system("cls" if os.name == "nt" else "clear")


def render_comparison():
    clear()
    print("PROTOTYPE — human-editable chart source")
    print("Scores are hypotheses for discussion, not the verdict. 5 = strongest.\n")
    print("   Format                     Dup  Err  Diff Faith Total")
    for key, option in OPTIONS.items():
        duplication, errors, diffs, fidelity = option["scores"]
        print(
            f"{key}  {option['name']:<26} {duplication}    {errors}    "
            f"{diffs}    {fidelity}     {sum(option['scores'])}"
        )
    print("\nAll variants encode the same Section definitions and Expanded Arrangement.")
    print("\n[1-4] inspect  [q] quit")


def render_source(option, lines, offset):
    clear()
    end = min(offset + PAGE_SIZE, len(lines))
    print(f"{option['name']}  {option['file']}  lines {offset + 1}-{end}/{len(lines)}")
    print(f"{option['tradeoff']}\n")
    for number, line in enumerate(lines[offset:end], start=offset + 1):
        print(f"{number:>3}  {line}")
    print("\n[j/k] scroll  [c] comparison  [1-4] switch  [q] quit")


def main():
    selected = None
    lines = []
    offset = 0
    render_comparison()
    while True:
        command = input("> ").strip().lower()
        if command == "q":
            return
        if command == "c":
            selected = None
            render_comparison()
            continue
        if command in OPTIONS:
            selected = OPTIONS[command]
            lines = (HERE / selected["file"]).read_text(encoding="utf-8").splitlines()
            offset = 0
        elif selected and command == "j":
            offset = min(max(0, len(lines) - PAGE_SIZE), offset + PAGE_SIZE)
        elif selected and command == "k":
            offset = max(0, offset - PAGE_SIZE)
        if selected:
            render_source(selected, lines, offset)


if __name__ == "__main__":
    main()
