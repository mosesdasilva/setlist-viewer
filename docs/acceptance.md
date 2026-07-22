# Acceptance Checks

## Issue #22 — Searchable Song Picker

Checked 2026-07-22 in the Codex in-app Chromium browser against the canonical split viewer and generated portable viewer.

- Split viewer, 1200 × 800: picker opened as a fixed 560 px desktop overlay without displacing the Chart.
- Split viewer, 390 × 844: picker occupied the full viewport and retained a scrollable ordered catalog.
- Portable viewer, 390 × 844: generated picker matched split markup, layout, filtering, and catalog order.
- Empty search showed all 12 Songs in canonical order; `miel` matched Artist and `MÁS` matched title case-insensitively.
- Legacy and Current labels were visible; selecting `Más` closed the picker, updated the header/count/Song Map, and restored focus to `Choose Song`.
- Escape, the visible close control, and desktop backdrop click each closed the picker and restored trigger focus.
- ArrowRight did not change Songs while search had focus; outside the picker it wrapped Song 12 to Song 1.
- Browser console reported no warnings or errors.

The browser harness blocks `file://` navigation, so direct-disk behavior was covered by the classic-script/no-fetch rendering contracts, generated portable equivalence tests, and `python3 tools/build.py --check`. Interactive browser checks used a temporary localhost static server.
