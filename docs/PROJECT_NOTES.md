# Project Notes

## Current Baseline

- Product name is **Setlist Viewer**.
- The source direction from handoff is a reusable viewer, not only one specific setlist.
- The primary portable artifact is a versioned single-file HTML build.
- The app is also maintained in split source files: `index.html`, `styles.css`, and `script.js`.
- Deployment target is a static GitHub Pages site.

## Naming

- Working project name: **Setlist Viewer**
- Versioned portable file name starts with `setlist-viewer-v1.html`

## Constraints

- No framework
- No package install
- Must open directly in a browser
- Keep the single-file distribution path available
- Keep iteration simple while content is still changing

## UX Direction

- mostly black, white, and gray UI
- section boxes carry the main color
- preserve mobile-friendly one-song-at-a-time navigation
- keep terminology normalized as `Bridge` and `Chorus`

## Notes For Future Iteration

- Keep content edits straightforward while songs are still being revised.
- Avoid introducing a build step unless the song library or editing workflow clearly requires it.
- Treat the single-file version as the easiest handoff and prototype path.
- Keep the split files as maintainable source unless the user explicitly wants to go back to one-file-only development.
