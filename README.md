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

Open [setlist-viewer-v1.html](C:/Users/mrd98/OneDrive/Documents/Setlist%20Viewer/setlist-viewer-v1.html) for the portable single-file version, or [index.html](C:/Users/mrd98/OneDrive/Documents/Setlist%20Viewer/index.html) for the split source version.

## Project Structure

- [setlist-viewer-v1.html](C:/Users/mrd98/OneDrive/Documents/Setlist%20Viewer/setlist-viewer-v1.html): portable single-file prototype and current handoff-friendly artifact
- [index.html](C:/Users/mrd98/OneDrive/Documents/Setlist%20Viewer/index.html): split markup source
- [styles.css](C:/Users/mrd98/OneDrive/Documents/Setlist%20Viewer/styles.css): split visual styling source
- [script.js](C:/Users/mrd98/OneDrive/Documents/Setlist%20Viewer/script.js): split behavior source
- [PROJECT_NOTES.md](C:/Users/mrd98/OneDrive/Documents/Setlist%20Viewer/PROJECT_NOTES.md): current decisions and next steps
- [AGENTS.md](C:/Users/mrd98/OneDrive/Documents/Setlist%20Viewer/AGENTS.md): contributor instructions for future agents

## GitHub Pages

The repository includes a GitHub Actions workflow that publishes this static site to GitHub Pages.

After the repo is pushed to GitHub:

1. Enable GitHub Pages to use GitHub Actions.
2. Push to the default branch.
3. GitHub will deploy the site automatically.

## Next Likely Improvements

- define a standard song data format
- add support for multiple setlists
- add filtering or search when the setlist grows
- add print or stage-view layouts if needed
