# PROTOTYPE — Chart Source Format

## Question

Which human-editable source format best represents the `Más — Miel San Marcos` chart with low duplication, clear errors, useful diffs, and faithful Expanded Arrangement rendering?

This is throwaway decision code for the Wayfinder ticket “Prototype a human-editable chart source format.” It is not production chart data or a parser.

## Run

```sh
python3 prototypes/chart-source-format/compare.py
```

Enter `1`–`4` to inspect a format, `j`/`k` to scroll, `c` for the comparison, and `q` to quit. Each example describes the same metadata, reusable Section definitions, and full performance-order arrangement.

## Decision prompt

While inspecting, judge the edit you expect to make most often: changing one Chord Symbol, adding a Row Note, or inserting a repeated Section occurrence. Which option makes errors easiest to spot before rehearsal?

Verdict intentionally pending human reaction.
