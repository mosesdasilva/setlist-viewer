# Setlist Viewer Handoff

## Project

Project name: `Setlist Viewer`

Primary project file:
- `C:\Users\mrd98\Documents\Setlist Viewer\index.html`

This project is a small single-file static web app for viewing song structures on phones and browsers. It is meant to be easy to share with a team and easy to host later with something simple like GitHub Pages.

## Current Product Direction

This is not mainly about one specific setlist. The broader idea is a reusable web app for:
- viewing song structure
- showing BPM, key, lead vocal, and notes
- displaying map sections clearly
- making it easy for a team to open on mobile
- making it easy to send as a link later

## Current Architecture

For now, everything is intentionally kept in one file:
- HTML
- CSS
- JavaScript

Current file:
- `index.html`

The user wants to keep it as a single self-contained HTML file for now and only split files later if needed.

## Current Features

The current version includes:
- one-song-at-a-time slider view
- previous / next song navigation
- quick song directory at the top
- keyboard navigation with left and right arrows
- dark mode toggle
- dark mode preference saved in browser local storage
- mobile-friendly layout
- two-column song layout
- map sections that flow top-to-bottom in the first column, then continue in the second
- consistent section colors by section type

## Data / Terminology Decisions

Important naming decisions already made:
- `Breakdown` should be `Bridge`
- `Chant` should be `Chorus`

These were cleaned up both in visible labels and in the code.

## Styling Decisions

The current design direction is:
- clean and simple
- mostly black / white / gray UI
- only the section boxes use color
- section colors are intentionally stronger now, not pale

## Known File State

Main working file:
- `C:\Users\mrd98\Documents\Setlist Viewer\index.html`

Older experimental files also exist in the Codex workspace, but the main project file to continue from is the one above.

## Suggested Next Steps

Good next steps for this project:
- tighten mobile spacing so more content fits on one phone screen
- add editability or easier content updates
- define a standard song data format
- add support for loading multiple setlists
- eventually split into `index.html`, `styles.css`, and `app.js` only if needed
- optionally prepare for GitHub Pages hosting

## Suggested Prompt For Another Codex Thread

Use this prompt in a new Codex project/thread:

```text
I have a project called Setlist Viewer.

Main file:
C:\Users\mrd98\Documents\Setlist Viewer\index.html

This is a small single-file static web app for viewing song structures on phones and browsers. Please continue from the existing file instead of rebuilding from scratch.

Important context:
- Keep everything in one HTML file for now.
- This is meant to be a reusable song structure / setlist viewer, not just a one-off page.
- The app already has one-song-at-a-time navigation, a quick directory, dark mode, and mobile-friendly behavior.
- Section maps flow top-to-bottom in the first column and then continue in the second column.
- The UI should stay clean and simple: mostly black/white/gray, with color only used in the song section boxes.
- Terminology decisions already made:
  - Bridge, not Breakdown
  - Chorus, not Chant

Please first inspect the existing file and then help me continue improving the app from there.
```

## Notes For Future Continuation

If another Codex session continues this project, it should:
- treat `C:\Users\mrd98\Documents\Setlist Viewer\index.html` as the source of truth
- preserve the single-file approach unless the user explicitly asks to split it
- preserve the cleaned terminology and current UI direction
