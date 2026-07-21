# Project Notes

## Current Baseline

- Product name is **Setlist Viewer**.
- The source direction from handoff is a reusable viewer, not only one specific setlist.
- The primary portable artifact is a versioned single-file HTML build.
- The app is also maintained in split source files: `index.html`, `styles.css`, and `script.js`.
- Deployment target is a static GitHub Pages site.
- The next product direction is a stage-ready Nashville Number Chart viewer backed by manually edited structured chart data.
- Split source and chart data will be canonical; the portable single-file HTML will be generated.
- Carry a constrained ChordPro grid profile into source-format prototyping as the leading candidate; use ChordText as a notation-language reference, and require the representative chart to prove the fit before adoption.
- Avoid runtime `fetch()` or ES-module loading for essential chart data while direct `file://` use remains required; generate file-safe classic JavaScript for split runtime use and inline data for the portable artifact.

## Naming

- Working project name: **Setlist Viewer**
- Versioned portable file name starts with `setlist-viewer-v1.html`

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
- stack Sections vertically in a fully Expanded Arrangement
- preserve four Bars plus a side-by-side Row Note per Chart Row at every supported width
- prioritize phone, iPad, and laptop; rely only on normal browser printing for v1
- use [MultiTracks ChartBuilder](https://www.multitracks.com/products/chartbuilder/) as UX inspiration for number notation, visible colored Section containers, Song Map navigation, and side-positioned MD-style notes; retain Setlist Viewer's static Expanded Arrangement and scope

## Notes For Future Iteration

- Keep content edits straightforward while songs are still being revised.
- Avoid introducing a build step unless the song library or editing workflow clearly requires it.
- Treat the single-file version as the easiest handoff and prototype path.
- Keep the split files as maintainable source unless the user explicitly wants to go back to one-file-only development.
