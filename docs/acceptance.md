# Local Acceptance Record

## Issue #18 — 2026-07-22

Status: **incomplete; maintainer browser participation required**

Base: `origin/main` at `efce647` (`Gate Pages deployment on validation (#17)`)

## Automated gates

| Gate | Environment / command | Result |
| --- | --- | --- |
| Full standard-library suite | Python 3.9.6 via `uv run --python 3.9 --no-project python -m unittest discover -s tests -v` | Pass: 44 tests |
| Generated-artifact check | Python 3.9.6 via `uv run --python 3.9 --no-project python tools/build.py --check` | Pass; no drift |
| Split JavaScript syntax | Bundled Node.js 24.14.0, `node --check` on `src/song-data.js`, `src/chart-data.js`, and `src/script.js` | Pass |
| Portable JavaScript syntax | Bundled Node.js 24.14.0 compiled both inline scripts extracted in memory from `setlist-viewer-portable.html` | Pass: 2 scripts |

The regression suite verifies all eleven Legacy Songs and catalog order unchanged, visible Legacy labels, the complete expanded `Más` data, four Bar slots, Empty Bar Slots, Nashville events and timing, Diamonds, ordered Row Notes, replacement by Song ID, and split/portable generation alignment.

## Direct-disk Chrome matrix

Installed browser: Google Chrome 150.0.7871.130.

The available Chrome-control surface rejected navigation to local `file://` URLs before either viewer loaded. Its security response explicitly prohibited retrying through an alternate browser or computer-control surface, so Computer Use was not attempted as a workaround. This is a browser-control security restriction, not an application failure. No viewport, interaction, rendering, or console result can therefore be claimed from this session.

| Artifact | Viewport | Result | Console findings |
| --- | --- | --- | --- |
| `src/index.html` | 390 × 844 phone | Pending maintainer | Not observed |
| `src/index.html` | 768 × 1024 tablet | Pending maintainer | Not observed |
| `src/index.html` | 1440 × 900 desktop | Pending maintainer | Not observed |
| `setlist-viewer-portable.html` | 390 × 844 phone | Pending maintainer | Not observed |
| `setlist-viewer-portable.html` | 768 × 1024 tablet | Pending maintainer | Not observed |
| `setlist-viewer-portable.html` | 1440 × 900 desktop | Pending maintainer | Not observed |

Maintainer checks still required for both artifacts:

- Open directly from disk; do not substitute a local server.
- Visit every catalog entry and confirm one combined 12-song count/directory.
- Confirm Previous/Next wrap first-to-last and last-to-first.
- Confirm directory jumps, ArrowLeft, ArrowRight, `D`, and theme-button behavior.
- Reload after selecting dark mode and confirm theme persistence.
- Confirm Legacy text in all eleven Legacy headers and directory buttons.
- Compare all eleven Legacy entries with the preserved dataset.
- Confirm complete `Más` Expanded Arrangement rendering.
- At every viewport, confirm four-slot Chart Rows, explicit Empty Bar Slots, event timing, Diamonds, and readable side-by-side ordered Row Notes.
- Record any console warnings/errors; record `none` when clean.

## Physical Safari spot checks

Pending maintainer checks on a physical iPhone and iPad. Record device, OS, Safari version, artifact, viewport/orientation, result, and console findings when available. This session had no physical Safari device and makes no Safari compatibility claim.

## Cutover decision

Do **not** remove `setlist-viewer-v1.html`. Automated gates pass, but direct-disk Chrome and physical Safari gates remain unverified. Removal is permitted only after every pending row and interaction above passes and this record is updated with actual evidence.
