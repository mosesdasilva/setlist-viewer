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
- Use the accepted Section Bands prototype as binding visual and interaction prior art for the canonical generated viewer: compact sticky Song header, vertical Section Names, colored bands, four-Bar rows, aligned Row Notes, and responsive one/two/four-column presentation.
- Persist one-, two-, or four-column preference independently from the responsive rendered layout: phones render one column, tablet widths render at most two, and four columns render only at 1200 CSS pixels or wider.
- Evolve the viewer through spec #25: use mutually exclusive Chords, Melody, and Lyrics display modes; occurrence-specific non-Bar-aligned Lyrics Blocks; selectable Per Section or Global Bar numbering; equal-footprint four/eight-Bar Section Bands; five persistent Band-size steps; and an explicit Strong/Pastel control without a color legend.
- Expose the ordered Song Map only for complete Charts, mark exactly one active target with `aria-current="location"`, and keep Legacy Songs as readable Section summaries without Chart Rows.
- Keep the generated catalog as the only runtime Song source; browse it through the hidden searchable Song Picker opened from the sticky header.
- Keep the app static with no framework and no build step.
- Treat the website as the source of truth for song map flow unless the user explicitly calls out a correction from a sheet.
- Normalize repeated map sections by expanding them into repeated labels instead of compact notation like `2X` or `3X`.
- Treat `CH` as `Chorus` and `BD` or `B` as `Bridge` when translating sheet shorthand into the website.
- Evolve the viewer toward manually authored Nashville Number Charts rather than lyrics.
- Retain the current 11 metadata-and-section-order entries as Legacy Songs during migration; move them from HTML into structured classic JavaScript, show them alongside charts with a Legacy badge, and add new Nashville Number Charts only from complete authored chart content—never invented placeholder Bars.
- A completed `.chart` replaces its matching Legacy Song. Use `Más` as the first complete chart and preserve every unreplaced Legacy Song's metadata and section sequence.
- Acceptance combines zero-dependency Python tests and `python3 tools/build.py --check` with manual checks of split, portable, and GitHub Pages variants at phone, tablet, and desktop sizes. Cover Chrome desktop plus Safari iPhone/iPad spot checks, navigation wrapping and directory jumps, keyboard controls, theme persistence, fully expanded order, four-Bar Rows, side-by-side Row Notes, and unchanged Legacy Song content.
- Keep split source and chart data canonical; generate the portable single-file HTML from them.
- Commit generated `src/chart-data.js` and `setlist-viewer-portable.html`; regenerate both explicitly with zero-dependency `python3 tools/build.py`.
- Use `python3 tools/build.py --check` in CI before GitHub Pages deployment; fail on invalid charts or generated drift without auto-committing repairs.
- Generate atomically, with source locations in diagnostics and generated-file headers warning against manual edits.
- Use a project-owned, musician-readable `.chart` notation as canonical chart source; ChordPro and ChordText inform its vocabulary without becoming the storage format.
- Use a strict line-oriented UTF-8 `.chart` grammar: required metadata in fixed order, optional metadata next, Expanded Arrangement lines before pipe-delimited Section definitions, four-slot Chart Rows, whitespace-delimited Bar Events, suffix Beat Dots, ASCII `<chord>` Diamonds, and typed ordered Row Notes.
- Reject tabs; support exactly `\\`, `\|`, `\;`, and `\]` escapes. A Melody Passage has exactly four fragments and at least one must be nonempty.
- Validation reports stable line/column diagnostics. Unreferenced Section definitions are warnings that allow generation; errors prevent all generated output.
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
- [Choose the canonical-source and portable-build workflow](https://github.com/mosesdasilva/setlist-viewer/issues/7) is resolved: committed runtime and portable outputs are produced by an explicit Python build and checked—not repaired—by CI.
- [Specify the musician-readable .chart grammar and validation contract](https://github.com/mosesdasilva/setlist-viewer/issues/9) is resolved; its resolution and final addendum define the exact grammar, escaping, timing validation, arrangement rules, and diagnostics.
- [Define migration and acceptance checks](https://github.com/mosesdasilva/setlist-viewer/issues/8) is resolved; its resolution preserves ordered, visibly badged Legacy Songs until complete ID-matched Charts replace them and defines automated, local-browser, and deployed acceptance gates.
- The Wayfinder map is complete: its destination is now implementation-ready, with no remaining frontier tickets or fog.
- [Implement v1 static Nashville Number Chart system](https://github.com/mosesdasilva/setlist-viewer/issues/10) is the consolidated implementation spec, linked to map issue #1 and labelled `ready-for-agent`.
- Issue #10 is decomposed into implementation tickets #11–#19. The initial frontier is [#11 Move Legacy Songs into the data-driven viewer](https://github.com/mosesdasilva/setlist-viewer/issues/11) and [#12 Validate core .chart structure](https://github.com/mosesdasilva/setlist-viewer/issues/12); later tickets declare their blocking edges in their issue bodies.
- [#13 Validate Nashville events and Row Notes](https://github.com/mosesdasilva/setlist-viewer/issues/13) is implemented on its focused branch: validation now normalizes Chord Events, No Chord, Beat Dots, Diamond Chords, Performance Directions, and Melody Passages; invalid timing, notation, and escapes produce actionable diagnostics.
- [#14 Generate the canonical catalog and browser data](https://github.com/mosesdasilva/setlist-viewer/issues/14) is implemented on its focused branch: the explicit catalog preserves all 11 Legacy Songs then appends the accepted authored `Más` Chart; `tools/build.py` validates, replaces by Song ID, expands arrangements, atomically generates `src/chart-data.js`, and checks drift without writes.
- [#15 Render complete Nashville Number Charts](https://github.com/mosesdasilva/setlist-viewer/issues/15) is implemented on its focused branch: the split viewer now loads the generated catalog and renders complete Expanded Arrangements with four-slot Chart Rows, Nashville events and timing, and ordered side-by-side Row Notes while retaining shared navigation and Legacy Song behavior.
- [#16 Generate the portable single-file viewer](https://github.com/mosesdasilva/setlist-viewer/issues/16) is implemented on its focused branch: the Python 3.9 standard-library build deterministically generates and checks `setlist-viewer-portable.html` from canonical split UI and normalized catalog data, safely embeds inline data, rolls back publication failures, and recovers durable interrupted transactions on the next build. The prior `setlist-viewer-v1.html` prototype remains unchanged pending final acceptance.
- [#17 Gate GitHub Pages deployment](https://github.com/mosesdasilva/setlist-viewer/issues/17) is implemented on its focused branch: a Python 3.9 validation job runs the complete standard-library test suite and `python3 tools/build.py --check`; Pages upload and deployment require that job to pass.
- [#21 Adopt the Section Bands shell for the canonical catalog](https://github.com/mosesdasilva/setlist-viewer/issues/21) is implemented on its focused branch: canonical Chart and Legacy Song data now share the compact sticky shell, responsive Section Bands, preserved navigation and display preferences, and aligned generated portable output.
- [#22 Replace the directory with a searchable Song Picker](https://github.com/mosesdasilva/setlist-viewer/issues/22) is implemented on its focused branch: the ordered canonical catalog now opens in an accessible header-triggered picker with title/Artist filtering, visible Legacy and current-Song states, keyboard-safe modal dismissal and focus restoration, a desktop overlay, and a mobile full-screen sheet.
- [#23 Integrate prototype display controls and Song Map](https://github.com/mosesdasilva/setlist-viewer/issues/23) is implemented on its focused branch: the canonical split and generated portable viewers now provide an accessible active Chart Song Map, readable Legacy summaries, persistent theme/palette/Melody controls, and responsive one/two/four-column preferences with safe narrow-width fallback.
- [#25 Improve Section Band modes, sizing, colors, numbering, and lyrics](https://github.com/mosesdasilva/setlist-viewer/issues/25) is the active successor specification to completed foundation issues #10 and #20.
- Issue #25 is decomposed into implementation tickets #26–#30. The parallel frontier is [#26 Make palette state explicit and color active Section navigation](https://github.com/mosesdasilva/setlist-viewer/issues/26) and [#27 Add exclusive Chart modes, Bar numbering, and symmetrical Section Bands](https://github.com/mosesdasilva/setlist-viewer/issues/27). Lyrics ticket #28 and Band-size ticket #29 depend on #27; integrated acceptance ticket #30 depends on #26, #28, and #29.
- Superseded acceptance issues #18, #19, and #24 are closed in favor of #30. Completed foundation issues #10 and #20 are closed; their evidence remains in their issue histories.
- [#26 Make palette state explicit and color active Section navigation](https://github.com/mosesdasilva/setlist-viewer/issues/26) is implemented: Strong/Pastel and Light/Dark show their current state, invalid palette preferences fall back to Strong, and the active Song Map target shares its Section header color in split and generated portable viewers.
- [#27 Add exclusive Chart modes, Bar numbering, and symmetrical Section Bands](https://github.com/mosesdasilva/setlist-viewer/issues/27) is implemented: Chords, Melody, and Lyrics are exclusive accessible modes; Per Section and Global Bar numbering persist; and four/eight-Bar occurrences share one footprint in split and portable viewers.
- [#28 Integrate occurrence-specific lyrics and Más Lyrics Mode](https://github.com/mosesdasilva/setlist-viewer/issues/28) is implemented on its focused branch: validated one-based occurrence Lyrics Blocks generate into split/portable data, Lyrics Mode renders ordered lines only, and all 14 supplied blocks are mapped in source order across the 14 eight-Bar vocal occurrences while eight non-vocal occurrences remain empty.

## Next Recommended Work

- Implement #29; finish with #30 integrated deployment acceptance, including #28 lyric-mapping review and #24's remaining physical Safari and direct-file human checks.

## Update Rule

When a future session changes direction, finishes a milestone, or decides the next priority, update this file before ending the session.
