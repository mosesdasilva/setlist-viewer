# AGENTS.md

## Project

This repository contains **Setlist Viewer**, a static HTML/CSS/JS song structure browser for rehearsal and live-use navigation.

## Read First

Before making changes, read these files in order:

1. [README.md](C:/Users/mrd98/OneDrive/Documents/Setlist%20Viewer/README.md)
2. [PROJECT_NOTES.md](C:/Users/mrd98/OneDrive/Documents/Setlist%20Viewer/PROJECT_NOTES.md)
3. [SETLIST_VIEWER_HANDOFF.md](C:/Users/mrd98/OneDrive/Documents/Setlist%20Viewer/SETLIST_VIEWER_HANDOFF.md)
4. [setlist-viewer-v1.html](C:/Users/mrd98/OneDrive/Documents/Setlist%20Viewer/setlist-viewer-v1.html)
5. [index.html](C:/Users/mrd98/OneDrive/Documents/Setlist%20Viewer/index.html)
6. [styles.css](C:/Users/mrd98/OneDrive/Documents/Setlist%20Viewer/styles.css)
7. [script.js](C:/Users/mrd98/OneDrive/Documents/Setlist%20Viewer/script.js)

## Project Goals

- Keep the project as a static browser-based tool.
- Preserve a portable single-file version for handoff and rapid testing.
- Preserve fast local testing with no build step.
- Make the project clean enough to maintain in GitHub Pages.
- Keep the current song content as a working dataset, not the full product definition.

## Design Direction

Maintain this visual direction unless explicitly told otherwise:

- clean grayscale UI
- clear stage-friendly readability
- quick song-to-song navigation
- restrained visual styling with color concentrated in song section boxes
- mobile-friendly layout without changing the core workflow

## Technical Constraints

- This is a static site.
- Primary portable artifact: [setlist-viewer-v1.html](C:/Users/mrd98/OneDrive/Documents/Setlist%20Viewer/setlist-viewer-v1.html)
- Main entry point: [index.html](C:/Users/mrd98/OneDrive/Documents/Setlist%20Viewer/index.html)
- Styling: [styles.css](C:/Users/mrd98/OneDrive/Documents/Setlist%20Viewer/styles.css)
- Interaction: [script.js](C:/Users/mrd98/OneDrive/Documents/Setlist%20Viewer/script.js)
- No framework or package install should be required.
- Keep edits compatible with direct browser use and GitHub Pages hosting.

## Workflow

When working on this repo:

1. Review the current project context files first.
2. Prefer updating the portable single-file version when the user is prototyping or requesting a handoff-friendly artifact.
3. Test by opening the static site in a browser.
4. Update [PROJECT_NOTES.md](C:/Users/mrd98/OneDrive/Documents/Setlist%20Viewer/PROJECT_NOTES.md) if project direction changes.
5. Commit with a clear message once the repo is under git.

## Editing Guidance

- Prefer small, targeted edits over large rewrites.
- Keep the app easy to run and easy to hand off.
- Preserve the current terminology choices from handoff.
- Preserve the current song data unless the user asks to revise content.
- If adding features, prefer static-site friendly approaches first.
- If both split and single-file variants exist, keep them behaviorally aligned.

## Done Criteria

A change is complete when:

- the site still opens directly in a browser
- the single-file version still opens directly in a browser
- song navigation still works
- the theme toggle still works
- the layout remains readable on desktop and mobile
- project notes are updated if decisions changed
