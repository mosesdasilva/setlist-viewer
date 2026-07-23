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

## Issue #27 — Chart Modes, Bar Numbering, and Section Band Geometry

Automated and browser checks run 2026-07-23 against canonical split source and the generated portable viewer.

- Automated: all 58 Python 3.9 tests, `python3 tools/build.py --check`, and the Node syntax check pass.
- Phone, 390×844: one column; 4- and 8-Bar occurrences both measured 130 px high; no page overflow. The compact two-row controls remain keyboard accessible.
- Tablet, 834×1112: two columns with 400 px Section Bands; equal 130 px 4/8-Bar footprints; no page overflow.
- Desktop, 1440×900: four columns with 285 px Section Bands; equal 130 px 4/8-Bar footprints; no page overflow.
- Chords Mode showed Bar numbers and harmony only. Melody Mode showed 80 authored Melody Fragments, 144 Bar numbers, and no chord content. Lyrics Mode showed 22 empty Lyrics Blocks and no Bars, chords, or Melody Fragments.
- Per Section numbering restarted at each occurrence. Global numbering continued from Bars 1–8 in the first occurrence to 9–16 in the second; both the selected mode and numbering mode survived reload.
- Arrow-key mode selection maintained one checked/one tabbable option without triggering Song navigation.
- Split and portable behavior matched at all three widths; browser console reported no errors.

Limitations before merge acceptance:

- The in-app browser disallows `file://` navigation. Direct-file behavior remains covered by classic-script/no-fetch contracts, self-contained portable generation, and build equivalence.
- Physical Safari iPhone/iPad checks are human-only and remain pending.

## Issue #28 — Occurrence-Specific Lyrics

Automated and browser checks run 2026-07-23 against canonical split source and the generated portable viewer.

- Automated: all 63 Python 3.9 tests, `python3 tools/build.py --check`, and the Node syntax check pass.
- Lyrics Mode renders 22 occurrence Lyrics Blocks: 14 populated in authoritative source order and eight empty intro/tag/instrumental/ending occurrences.
- Lyrics Mode showed zero Chart Rows, Bars, chords, or Melody Fragments. Keyboard Left/Right moved exclusively between Lyrics and Melody and back.
- Accents/spelling, including `Tí`, `Tú`, and the supplied `deTi`, remained exact in generated data and rendered lines.
- Split and portable viewers matched at 390×844 (one column), 834×1112 (two columns), and 1440×900 (four columns).
- Lyrics text measured 11 px at phone/tablet widths and 13 px at desktop. All widths reported zero page or Lyrics Block overflow; the browser console reported no warnings or errors.

Human-only checks:

- Visually confirm or correct the documented best-effort mapping. The accepted arrangement has 14 eight-Bar vocal occurrences, so the 14 supplied blocks were assigned to those occurrences in source order; several supplied headings intentionally differ from the preserved Section names.
- Physical Safari iPhone/iPad and direct-`file://` interaction remain pending.
