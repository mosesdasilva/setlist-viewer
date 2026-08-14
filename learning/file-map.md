# File map

<!-- Every file/folder is either explained or parked — no mystery boxes. -->
<!-- known: explained in the learner's own words | parked: honest one-liner for now, deep dive scheduled | generated: machine-made, never edit, always rebuildable -->

## Repository root

- `.DS_Store` — generated — macOS folder metadata; never edit
- `.github/workflows/deploy-pages.yml` — known (2026-08-13) — tests and checks `main`, then publishes `src/` to GitHub Pages → [[continuous-deployment]]
- `.gitignore` — known (2026-08-14) — hides machine-made files and disposable `tmp/` output from Git status and commits → [[git-ignore-rules]]
- `AGENTS.md` — parked — working rules for coding agents; reclaim with AI-assisted project ownership → [[agent-instructions]]
- `CONTEXT.md` — parked — canonical musician-domain vocabulary; reclaim before modeling React data → [[domain-modeling]]
- `MISSION.md` — parked — earlier learning-workspace goal; reconcile during planning → [[learning-workflow]]
- `README.md` — known (2026-08-13) — explains the app, local use, build command, and repository shape → [[project-documentation]]
- `RESOURCES.md` — parked — earlier learning links; revisit when sections select resources → [[learning-workflow]]
- `TODO.md` — known (2026-08-14) — user-authored backlog of desired features carried forward from the prior development cycle → [[backlog-management]]
- `setlist-viewer-portable.html` — generated — self-contained viewer produced from canonical source; rebuild with `tools/build.py` → [[generated-artifacts]]
- `setlist-viewer-v1.html` — parked — previous single-file prototype retained as historical fallback → [[static-web-app]]

## `learning/`

- `learning/project.md` — known (2026-08-13) — adoption decision, personal context, MVP, frozen scope, and parking lot → [[learning-workflow]]
- `learning/plan.md` — known (2026-08-13) — agreed sequence from stable reference through a private React/Sites/D1 tool → [[learning-workflow]]
- `learning/file-map.md` — known (2026-08-13) — this honest ledger of why every repository area exists → [[file-map]]
- `learning/knowledge-graph.md` — known (2026-08-13) — evidence-based map that chooses future teaching and review → [[knowledge-graph]]

## `charts/`

- `charts/catalog.json` — known (2026-08-13) — orders the song IDs included by the build → [[structured-data]]
- `charts/mas.chart` — known (2026-08-13) — musician-authored source for the complete Más chart → [[chart-notation]]

## `src/`

- `src/index.html` — known (2026-08-13) — page shell that loads generated data before interaction code → [[html-document-structure]]
- `src/styles.css` — known (2026-08-13) — separate styling source makes the split viewer easier to maintain; selector internals return in Section 7 → [[css-cascade-and-selectors]]
- `src/script.js` — known (2026-08-13) — separate behavior source renders song data and controls navigation/theme; DOM calls return in Section 3 → [[dom-rendering]]
- `src/chart-data.js` — generated — browser-ready catalog produced from legacy data and `.chart` sources; never edit directly → [[generated-artifacts]]
- `src/song-data.js` — parked — hand-maintained Legacy Song data consumed by the build; reclaim during data-model design → [[legacy-song-model]]
- `src/.nojekyll` — parked — prevents GitHub Pages from applying Jekyll processing; reclaim during deployment → [[continuous-deployment]]

## `tools/`

- `tools/chart_validator.py` — known (2026-08-13) — parses `.chart` text and returns normalized chart data plus diagnostics → [[parsing-and-validation]]
- `tools/build.py` — known (2026-08-13) — validates sources and atomically generates browser data plus portable HTML → [[build-pipeline]]
- `tools/__init__.py` — parked — marks `tools` as an importable Python package; reclaim when reading Python tests → [[python-modules]]
- `tools/__pycache__/` — generated — Python bytecode cache; ignored and safely rebuildable

## `tests/`

- `tests/test_chart_validator.py` — known (2026-08-14) — examples and edge cases for `.chart` parsing; individual cases return with validator TDD → [[unit-testing]]
- `tests/test_build.py` — known (2026-08-14) — protects deterministic generation, drift checking, and atomic writes → [[unit-testing]]
- `tests/test_legacy_songs.py` — known (2026-08-14) — prevents accidental changes to retained Legacy Song content → [[regression-testing]]
- `tests/test_rendering.py` — known (2026-08-14) — checks source/rendering contracts without opening a real browser → [[contract-testing]]
- `tests/test_pages_workflow.py` — known (2026-08-14) — checks deployment workflow safety requirements → [[continuous-deployment]]
- `tests/__pycache__/` — generated — Python bytecode cache; ignored and safely rebuildable

## Teaching workspace

- `assets/lesson.css` — parked — styling shared by the existing visual lesson → [[learning-workflow]]
- `assets/quiz.js` — parked — behavior used by the existing lesson quiz → [[learning-workflow]]
- `lessons/0001-setlist-viewer-codebase-tour.html` — parked — prior generated codebase-tour lesson; compare with this evidence-based journey later → [[learning-workflow]]
- `prototypes/chart-source-format/` — parked — currently empty workspace from earlier chart-format exploration; revisit only if prototyping resumes → [[chart-notation]]

## `docs/`

- `docs/SESSION_CONTEXT.md` — parked — verified agent-session status and next-step record → [[project-documentation]]
- `docs/PROJECT_NOTES.md` — parked — accumulated product and technical decisions → [[project-documentation]]
- `docs/SETLIST_VIEWER_HANDOFF.md` — parked — historical context from the original prototype → [[project-history]]
- `docs/README.md` — parked — guide to documentation roles → [[project-documentation]]
- `docs/acceptance.md` — parked — recorded browser, portable-build, and deployment acceptance evidence → [[acceptance-testing]]
- `docs/adr/` — parked — why musician-readable `.chart` notation was chosen; revisit during storage design → [[architecture-decision-records]]
- `docs/agents/` — parked — GitHub issue, triage-label, and domain-doc conventions → [[agent-instructions]]
- `docs/research/` — parked — researched chart formats, storage options, and source-image notes; revisit during storage design → [[technical-research]]
- `docs/assets/` — parked — representative handwritten chart image used by research → [[chart-notation]]

## Temporary output

- `tmp/` — generated — untracked PDF/PNG render inspection output; disposable and not application source
