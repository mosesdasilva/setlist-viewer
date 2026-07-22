# Project Notes

## Current Baseline

- Product name is **Setlist Viewer**.
- The source direction from handoff is a reusable viewer, not only one specific setlist.
- The planned primary portable artifact is the stable `setlist-viewer-portable.html` single-file build; Git history provides versioning.
- The app is also maintained in split source files: `index.html`, `styles.css`, and `script.js`.
- Deployment target is a static GitHub Pages site.
- The next product direction is a stage-ready Nashville Number Chart viewer backed by manually edited structured chart data.
- Split source and chart data will be canonical; the portable single-file HTML will be generated.
- Use a project-owned, musician-readable `.chart` notation as canonical chart source, shaped by the selected small-notation prototype and informed by ChordPro and ChordText vocabulary.
- Avoid runtime `fetch()` or ES-module loading for essential chart data while direct `file://` use remains required; generate file-safe classic JavaScript for split runtime use and inline data for the portable artifact.
- Keep generated browser data structured; the resolved `.chart` grammar and line-aware validation contract live on the Wayfinder ticket and its final addendum.
- Preserve the current 11 songs as structured Legacy Songs until complete, ID-matched `.chart` files replace them; never invent placeholder Bars.
- Keep Legacy Songs and complete Charts in one ordered directory, with visible `Legacy` text in both directory and song header.

## Naming

- Working project name: **Setlist Viewer**
- The generated portable viewer is `setlist-viewer-portable.html`; retain the earlier `setlist-viewer-v1.html` prototype until final acceptance passes.
- Commit generated `src/chart-data.js` and `setlist-viewer-portable.html` so split `file://` use and instant handoff require no build.
- Use a zero-dependency `python3 tools/build.py` for explicit local generation and `python3 tools/build.py --check` for read-only validation.
- CI must validate charts and generated drift before deploying committed `src/`; failures show the rebuild command and never auto-commit changes.
- Build output is atomic and generated files identify their sources and warn against manual editing.
- Use `.chart` filename stems as stable Song IDs; replacement matches IDs rather than titles.

## Constraints

- No framework
- No package install
- Must open directly in a browser
- Keep the single-file distribution path available
- Keep iteration simple while content is still changing

## Version Control

- Commit each completed change and push it immediately so GitHub stays current.
- Keep `main` stable; use focused feature branches for implementation work.
- Low-risk documentation maintenance may go directly to `main`.
- Merge only after the project Done Criteria pass.

## UX Direction

- mostly black, white, and gray UI
- section boxes carry the main color
- preserve mobile-friendly one-song-at-a-time navigation
- keep terminology normalized as `Bridge` and `Chorus`
- treat the accepted responsive Section Bands prototype as binding prior art for the canonical generated viewer shell
- use a compact sticky Song header, vertical Section Names, Section Codes, colored bands, and a responsive one/two/four-column stage-reading surface
- preserve the chosen Section-column preference when responsive constraints temporarily render fewer columns: one on phones, at most two below 1200 CSS pixels, and four only at wider laptop/desktop sizes
- keep the ordered active Song Map for complete Charts; Legacy Songs show a readable Section summary and never imply Bar-level Chart content
- retain the compact horizontal Song directory only until the dedicated Song Picker replaces it
- stack Sections vertically in a fully Expanded Arrangement
- preserve four Bars plus a side-by-side Row Note per Chart Row at every supported width
- prioritize phone, iPad, and laptop; rely only on normal browser printing for v1
- use [MultiTracks ChartBuilder](https://www.multitracks.com/products/chartbuilder/) as UX inspiration for number notation, visible colored Section containers, Song Map navigation, and side-positioned MD-style notes; retain Setlist Viewer's static Expanded Arrangement and scope

## Acceptance Direction

- Run zero-dependency Python tests and `python3 tools/build.py --check` before merge.
- Record split/portable checks at phone, tablet, and desktop sizes in `docs/acceptance.md`, covering Chrome desktop and Safari iPhone/iPad spot checks.
- Smoke-test the deployed GitHub Pages site immediately after merge; a failed deployment check means the change remains incomplete.

## Notes For Future Iteration

- Keep content edits straightforward while songs are still being revised.
- Avoid introducing a build step unless the song library or editing workflow clearly requires it.
- Treat the single-file version as the easiest handoff and prototype path.
- Keep the split files as maintainable source unless the user explicitly wants to go back to one-file-only development.
