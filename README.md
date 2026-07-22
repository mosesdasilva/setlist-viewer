# Setlist Viewer

Setlist Viewer is a static web app for browsing song maps during rehearsal or live service prep.

## Current Scope

- reusable static site with no build step
- song-by-song navigation
- quick directory buttons
- light and dark theme toggle
- versioned single-file prototype artifact
- GitHub Pages ready deployment

## Local Use

Open `setlist-viewer-portable.html` for the generated portable single-file viewer, or [src/index.html](C:/Users/mrd98/OneDrive/Documents/Setlist%20Viewer/src/index.html) for the canonical split version. The earlier [setlist-viewer-v1.html](C:/Users/mrd98/OneDrive/Documents/Setlist%20Viewer/setlist-viewer-v1.html) remains available as a fallback until final acceptance.

Canonical chart sources and catalog order live under `charts/`. Regenerate browser data with
`python3 tools/build.py`; verify committed browser data and portable HTML without writing via `python3 tools/build.py --check`.

## Project Structure

- [setlist-viewer-v1.html](C:/Users/mrd98/OneDrive/Documents/Setlist%20Viewer/setlist-viewer-v1.html): prior portable prototype retained as a fallback through final acceptance
- `setlist-viewer-portable.html`: generated self-contained viewer built from canonical split source and normalized catalog data
- [src/](C:/Users/mrd98/OneDrive/Documents/Setlist%20Viewer/src): split website source for GitHub Pages
- [src/index.html](C:/Users/mrd98/OneDrive/Documents/Setlist%20Viewer/src/index.html): split markup source
- [src/styles.css](C:/Users/mrd98/OneDrive/Documents/Setlist%20Viewer/src/styles.css): split visual styling source
- [src/script.js](C:/Users/mrd98/OneDrive/Documents/Setlist%20Viewer/src/script.js): split behavior source
- `charts/catalog.json`: hand-authored catalog order
- `charts/*.chart`: musician-authored Nashville Number Charts
- `src/chart-data.js`: generated classic JavaScript browser data
- `tools/build.py`: zero-dependency data generation and drift check
- [docs/](C:/Users/mrd98/OneDrive/Documents/Setlist%20Viewer/docs): project notes, session continuity, and handoff history
- [PROJECT_NOTES.md](C:/Users/mrd98/OneDrive/Documents/Setlist%20Viewer/docs/PROJECT_NOTES.md): current decisions and next steps
- [SESSION_CONTEXT.md](C:/Users/mrd98/OneDrive/Documents/Setlist%20Viewer/docs/SESSION_CONTEXT.md): persistent cross-session starting point
- [SETLIST_VIEWER_HANDOFF.md](C:/Users/mrd98/OneDrive/Documents/Setlist%20Viewer/docs/SETLIST_VIEWER_HANDOFF.md): imported context from earlier session
- [AGENTS.md](C:/Users/mrd98/OneDrive/Documents/Setlist%20Viewer/AGENTS.md): contributor instructions for future agents

## GitHub Pages

The repository includes a GitHub Actions workflow that publishes this static site to GitHub Pages.

After the repo is pushed to GitHub:

1. Enable GitHub Pages to use GitHub Actions.
2. Push to the default branch.
3. GitHub will run the complete Python 3.9 test suite and `python3 tools/build.py --check`.
4. GitHub will deploy the site only after both checks pass.

## Next Likely Improvements

- define a standard song data format
- add support for multiple setlists
- add filtering or search when the setlist grows
- add print or stage-view layouts if needed
