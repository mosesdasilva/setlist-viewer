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

## Issue #24 — Prototype Cutover and Deployment Acceptance

Checked 2026-07-22 from focused branch `issue-24-prototype-cutover-acceptance`, based on current `main` `2b3dca0` containing #21, #22, and #23.

### Automated and runtime evidence

- `/usr/bin/python3 --version`: Python 3.9.6.
- Focused Python 3.9 rendering, Pages-workflow, and build tests: 27 tests passed.
- Full Python 3.9 suite: 54 tests passed.
- `/usr/bin/python3 tools/build.py --check`: passed without generated drift.
- Bundled Node v24.14.0: `node --check` passed for `src/script.js` and `src/chart-data.js`.
- Bundled Node runtime evaluation loaded 12 Songs, found both Chart and Legacy content, and confirmed the `Más` Expanded Arrangement has 22 Sections.
- The old hero and always-visible Song directory are absent from canonical split and generated portable markup. `setlist-viewer-v1.html` remains retained because the physical Safari and direct-`file://` browser gates below remain unavailable.

### Local browser evidence

Codex in-app Chromium tested unchanged files through a temporary localhost static server because this browser surface blocks `file://` navigation.

- Split `src/index.html`, desktop 1366 × 900: searchable picker showed all 12 ordered Songs; `MIEL` matched Artist case-insensitively; ArrowRight while search was focused did not change `Jesus`; selecting `Más` closed the dialog, restored focus to `Choose Song`, displayed Song 12 of 12, 22 Song Map targets, exactly one `aria-current="location"`, and 39 Chart Rows.
- Split, desktop: ArrowRight wrapped Song 12 to Song 1 and ArrowLeft wrapped back to Song 12. Escape and the visible close control dismissed the picker and restored trigger focus.
- Split, desktop: one/two/four controls remained available; four columns rendered when selected. Strong/pastel palette, light/dark theme, Melody visibility, and column preference persisted after reload. Hiding Melody left six Performance Directions visible. Four-column Bars, Row Notes, Sections, and page had no measured horizontal overflow.
- Split, tablet 834 × 1112: saved four-column preference rendered two columns; the four-column button was unavailable; no horizontal overflow.
- Split, phone 390 × 844: saved four-column preference rendered one column; layout controls were hidden; picker filled the 390 × 844 viewport, search retained focus, and no horizontal overflow occurred.
- Legacy `Jesus`: visible Legacy header/picker labels and ordered Section summary; no Chart Song Map.
- Chart `Más`: complete Legacy/Chart transition, four-Bar rows, Bar Events, Beat Dots, Diamond Chords, Row Notes, palettes, theme, Melody control, and Song Map rendered. All 12 Empty Bar Slots were visible, retained the `Empty Bar Slot` accessible label, and caused no overflow. The repeated Bridge position 16 target became the sole active `aria-current="location"` target.
- Split console after the integrated interaction run: no warnings or errors.
- Portable `setlist-viewer-portable.html`: `MÁS` title search selected the same 39-row Chart and 22-target Song Map. Previous/Next and Arrow navigation wrapped Songs 1/12 and 12/12; Escape dismissed the picker and restored trigger focus. Theme, palette, Melody, and four-column preference persisted after reload. All 12 Empty Bar Slots were visible and accessibly labeled. Desktop rendered four columns, tablet two, phone one, with no page/Section/Bar overflow. It had zero external scripts and zero external stylesheets.
- Portable console after the integrated interaction run: no warnings or errors.

### GitHub Pages evidence

- Main workflow run [29911805390](https://github.com/mosesdasilva/setlist-viewer/actions/runs/29911805390) for `2b3dca0` completed successfully on 2026-07-22. Its `validate` job set up Python 3.9, passed the complete suite and generated-artifact check, then its gated `deploy` job completed successfully.
- Deployed `https://mosesdasilva.github.io/setlist-viewer/`, desktop 1366 × 900: prototype-first shell loaded; `miel` selected `Más`; selection and Escape restored focus to the trigger; ArrowLeft/ArrowRight wrapped Songs 1/12 and 12/12; theme, palette, Melody, and four-column preference persisted after reload; 39 Chart Rows, 22 Song Map targets, one active target, and four columns rendered without horizontal overflow.
- Deployed tablet 834 × 1112 rendered two columns without overflow. Deployed phone 390 × 844 rendered one column without overflow and presented a full-viewport picker focused on search.
- Deployed Song Map position 16 selected the repeated Bridge as the sole active location.
- Deployed console: no warnings or errors.

### Remaining human/environment gates

- Direct browser interaction from `file://` was unavailable because the in-app browser rejects that navigation. Direct-disk compatibility is instead covered by classic scripts, no runtime fetch/modules, portable self-containment, rendering contracts, and build equivalence; this is not claimed as a direct-file browser pass.
- Physical Safari iPhone and iPad spot checks were unavailable and remain a maintainer gate.
- Therefore `setlist-viewer-v1.html` is intentionally retained. Issue closure, merge to `main`, and post-merge deployment acceptance remain outside this branch task and/or blocked on the explicit human gates.
