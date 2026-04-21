# Session Context

## Purpose

This file is the persistent cross-session starting point for Codex work on this repository.

Any future Codex session should read this file first to understand:

- what the project is
- what the current source of truth is
- what has already been decided
- what still needs to be done next

## Project Identity

- Project name: **Setlist Viewer**
- Repo purpose: reusable static song-structure viewer for browsers and phones
- Hosting target: GitHub Pages

## Current File Roles

- [setlist-viewer-v1.html](C:/Users/mrd98/OneDrive/Documents/Setlist%20Viewer/setlist-viewer-v1.html): portable single-file prototype and easiest handoff artifact
- [src/index.html](C:/Users/mrd98/OneDrive/Documents/Setlist%20Viewer/src/index.html): split HTML source
- [src/styles.css](C:/Users/mrd98/OneDrive/Documents/Setlist%20Viewer/src/styles.css): split CSS source
- [src/script.js](C:/Users/mrd98/OneDrive/Documents/Setlist%20Viewer/src/script.js): split JS source
- [SETLIST_VIEWER_HANDOFF.md](C:/Users/mrd98/OneDrive/Documents/Setlist%20Viewer/docs/SETLIST_VIEWER_HANDOFF.md): imported context from earlier session
- [PROJECT_NOTES.md](C:/Users/mrd98/OneDrive/Documents/Setlist%20Viewer/docs/PROJECT_NOTES.md): broader project decisions
- [AGENTS.md](C:/Users/mrd98/OneDrive/Documents/Setlist%20Viewer/AGENTS.md): instructions for future agents

## Current Decisions

- Keep the product named `Setlist Viewer`.
- Keep a versioned single-file HTML artifact available for prototyping and sharing.
- Maintain the split-file version in parallel for easier editing.
- Preserve the grayscale UI direction, with color concentrated in the section blocks.
- Keep the app static with no framework and no build step.

## Current Status

- Repository has been created and pushed to GitHub manually by the user.
- GitHub Pages workflow exists in `.github/workflows/deploy-pages.yml`.
- The current portable version is `setlist-viewer-v1.html`.
- Split website source now lives under `src/`.

## Next Recommended Work

- confirm GitHub Pages is enabled and publishing correctly
- decide whether future changes should treat the single-file or split-file version as the edit-first source
- define a simple versioning workflow for future portable releases
- decide whether song data should remain embedded or move into a reusable data format later

## Update Rule

When a future session changes direction, finishes a milestone, or decides the next priority, update this file before ending the session.
