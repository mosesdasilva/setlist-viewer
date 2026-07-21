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
- Treat the website as the source of truth for song map flow unless the user explicitly calls out a correction from a sheet.
- Normalize repeated map sections by expanding them into repeated labels instead of compact notation like `2X` or `3X`.
- Treat `CH` as `Chorus` and `BD` or `B` as `Bridge` when translating sheet shorthand into the website.
- Evolve the viewer toward manually authored Nashville Number Charts rather than lyrics.
- Keep split source and chart data canonical; generate the portable single-file HTML from them.
- Use a project-owned, musician-readable `.chart` notation as canonical chart source; ChordPro and ChordText inform its vocabulary without becoming the storage format.
- Essential chart data must load under `file://` without runtime `fetch()` or ES modules; generated classic JavaScript is the split-runtime candidate and inline data is the portable-artifact candidate.
- Render an Expanded Arrangement: every repeated Section appears in full performance order.
- Preserve four Bars and a side-by-side Row Note per Chart Row at phone, iPad, and laptop widths.
- Model each Row Note as either a Performance Direction or Melody Passage; a Melody Passage preserves four Bar-aligned Melody Fragments as opaque text in v1.
- Require song title, Artist, key, tempo, and time signature metadata; keep lead vocal and details optional.
- Display full Section Names in colored blocks. In chart data, use exactly two uppercase letters for each Section Code: `IN`, `IS`, `VS`, `TG`, `PC`, `PS`, `CH`, `BR`, `TR`, `EN`, or `OU`; custom codes must be unique within the song.
- Keep the optional Section Ordinal separate from the two-letter code, combining them only as compact notation such as `VS2`.
- Keep exactly four Bar slots per Chart Row; unused trailing slots remain empty, while `X`, not `N.C.`, means an intentional timed No Chord event.
- Require every Section to contain at least one Chart Row and every Chart Row to contain at least one Bar; a Bar contains one or more timed Bar Events.
- Allow multiple typed Row Notes on one Chart Row, including a Melody Passage and Performance Direction together; preserve their authored order.
- Divide multiple Bar Events—Chord Events or `X`—within a Bar equally by default; for unequal timing, display one Beat Dot above the Chord Symbol or `X` per assigned beat.
- Require Beat Dots when equal division would not yield whole time-signature denominator units.
- Treat each Beat Dot as one time-signature denominator unit. A Diamond Chord fills its entire Bar and needs no Beat Dots.
- Store keys as a letter with optional `b`/`#` and optional `m`, such as `D`, `Db`, `F#`, or `Am`.
- Keep four Melody Fragment slots per Melody Passage while allowing individual fragments to be empty.
- Permit any Chord Symbol, including altered, extended, or Slash Chords, to become a full-Bar Diamond Chord.
- Use MultiTracks ChartBuilder as UX inspiration for number notation, visible colored Section containers, Song Map navigation, and side-positioned performance notes without copying its subscription or playback scope.
- Support scale degrees `1`–`7`; `b`/`#` accidentals; `m`, `7`, `maj7`, `m7`, `sus2`, `sus4`, `dim`, `aug`, and `add9` suffixes; Slash Chords; multiple ordered Chord Symbols per Bar; free-text Performance Directions; and Diamond marks. Defer pushes, ties, repeats, and modulations until observed.
- Keep browser editing, handwriting/OCR import, melody tracking, cloud services, and dedicated PDF generation outside v1.
- Push every completed commit immediately; use focused feature branches for implementation and keep `main` stable.

## Current Status

- Repository has been created and pushed to GitHub manually by the user.
- GitHub Pages workflow exists in `.github/workflows/deploy-pages.yml`.
- The current portable version is `setlist-viewer-v1.html`.
- Split website source now lives under `src/`.
- `Jesus` metadata has been updated to key `A` and lead vocal `Matthew Morales`.
- `Holy Fragance` metadata has been updated to key `D`, lead vocal `Paloma Ramos`, and sheet-aligned detail text `Eg / keys intro`.
- Engineering-skill configuration lives under `docs/agents/`; domain language lives in root `CONTEXT.md`.
- Wayfinder map: [Map a static Nashville chart system](https://github.com/mosesdasilva/setlist-viewer/issues/1).
- The representative handwritten chart is `Más — Miel San Marcos`, key D, 140 BPM, 4/4; its source image and notation notes live under `docs/assets/` and `docs/research/`.
- [Define the v1 Nashville chart language](https://github.com/mosesdasilva/setlist-viewer/issues/4) is resolved; canonical terms live in `CONTEXT.md`, and its detailed resolution is recorded on the ticket.
- [Prototype a human-editable chart source format](https://github.com/mosesdasilva/setlist-viewer/issues/5) is resolved: the small `.chart` notation won because musician readability outweighed JSON/JavaScript familiarity; ADR 0001 records the choice.

## Next Recommended Work

- Resolve [Specify the musician-readable .chart grammar and validation contract](https://github.com/mosesdasilva/setlist-viewer/issues/9) before implementation; it blocks migration and acceptance planning.
- Continue through the unblocked frontier of the Wayfinder map; do not implement the destination during planning.

## Update Rule

When a future session changes direction, finishes a milestone, or decides the next priority, update this file before ending the session.
