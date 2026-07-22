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

## Issue #23 — Display Controls and Song Map

Automated and feasible browser checks run 2026-07-22 against canonical split source and the generated portable viewer.

- Automated: focused rendering/build tests, full Python 3.9 suite, and `python3 tools/build.py --check` pass.
- Browser surfaces: `src/index.html` and `setlist-viewer-portable.html` served unchanged by a local static server; portable has no external scripts or styles.
- Desktop, 1366×900: one, two, and four Section columns render as selected. Four-column Chart bands measured 285 px wide with 47 px Bars and 62 px Row Notes, without Section, Chart, or page overflow.
- Tablet, 834×1112: a saved four-column preference safely renders two columns; four-column control is unavailable; no horizontal overflow.
- Phone, 390×844: a saved four-column preference safely renders one column; layout controls are hidden; no horizontal overflow.
- Responsive persistence: returning from phone/tablet to desktop restores four rendered columns, and reload retains the four-column preference.
- Chart Song Map: all 22 Expanded Arrangement entries for `Más` appear in order; the selected repeated Bridge target reports `aria-current="location"` and the correct position 16 target.
- Legacy Song: Section summary remains ordered and contains no Chart Rows; Chart Song Map is hidden.
- Display controls: Melody hiding leaves Performance Directions visible; pastel colors use dark band text; dark theme, pastel palette, Melody visibility, and column controls expose updated pressed states.
- Console: no warnings or errors from the portable viewer.

Limitations before merge acceptance:

- The in-app browser disallows `file://` navigation. Direct-file behavior was covered by the no-fetch/no-module rendering contract, generated self-contained artifact checks, and build equivalence; browser interaction used the same unchanged files over localhost.
- Safari iPhone/iPad spot checks were unavailable in this environment and remain pending under the project-wide acceptance direction.
