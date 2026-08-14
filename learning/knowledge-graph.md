# Knowledge graph

<!-- statuses: seed → introduced → practicing → understood -->
<!-- seed: not yet taught | introduced: explained once | practicing: used it with help | understood: explained in own words + passed a later review -->

## html-document-structure
- status: practicing
- depends-on: none
- introduced: before 2026-08-13
- last-reviewed: 2026-08-13
- evidence: Explained that HTML holds page content in a tree and identified `src/index.html` loading `chart-data.js` before `script.js`.

## css-cascade-and-selectors
- status: introduced
- depends-on: html-document-structure
- introduced: 2026-08-13
- last-reviewed: 2026-08-13
- evidence: Correctly separated CSS presentation from HTML content, but did not yet trace the `.song` and `.song.active` rule interaction.

## javascript-functions-and-events
- status: introduced
- depends-on: html-document-structure
- introduced: 2026-08-13
- last-reviewed: 2026-08-13
- evidence: Explained that a Next Song click triggers JavaScript and changes the existing page without loading another HTML page; exact function chain remains fuzzy.

## dom-rendering
- status: introduced
- depends-on: html-document-structure, javascript-functions-and-events
- introduced: 2026-08-13
- last-reviewed: 2026-08-13
- evidence: Asked how JavaScript creates DOM elements; learned that the DOM is the browser's live in-memory page tree and that `script.js` builds it from catalog data.

## structured-data
- status: practicing
- depends-on: none
- introduced: before 2026-08-13
- last-reviewed: 2026-08-13
- evidence: Described `chart-data.js` as nested key-value data representing songs, lyrics, and chart structure.

## chart-notation
- status: practicing
- depends-on: structured-data
- introduced: before 2026-08-13
- last-reviewed: 2026-08-13
- evidence: Explained that `.chart` is the authored entry point and described using four-Bar groups, chords, metadata, melody, and comments.

## parsing-and-validation
- status: introduced
- depends-on: chart-notation, structured-data
- introduced: 2026-08-13
- last-reviewed: 2026-08-13
- evidence: Explained that Python reads and parses `mas.chart` into structured browser data; parser internals remain unknown.

## build-pipeline
- status: introduced
- depends-on: parsing-and-validation, generated-artifacts
- introduced: 2026-08-13
- last-reviewed: 2026-08-13
- evidence: Traced `.chart` through the Python builder into `chart-data.js`, but not yet through runtime DOM rendering.

## generated-artifacts
- status: introduced
- depends-on: build-pipeline
- introduced: 2026-08-13
- last-reviewed: 2026-08-13
- evidence: Identified `chart-data.js` as generated output rather than the musician-authored source.

## static-web-app
- status: introduced
- depends-on: html-document-structure, css-cascade-and-selectors, javascript-functions-and-events
- introduced: 2026-08-13
- last-reviewed: 2026-08-13
- evidence: Explained that the viewer changes an already-loaded page without navigating to separate HTML pages.

## browser-local-storage
- status: introduced
- depends-on: javascript-functions-and-events
- introduced: 2026-08-13
- last-reviewed: 2026-08-13
- evidence: Initially inferred cookies; then learned that theme preferences use browser `localStorage` key-value storage.

## responsive-web-design
- status: seed
- depends-on: css-cascade-and-selectors
- introduced: —
- last-reviewed: —
- evidence: —

## web-accessibility
- status: seed
- depends-on: html-document-structure, dom-rendering
- introduced: —
- last-reviewed: —
- evidence: —

## unit-testing
- status: introduced
- depends-on: functions, assertions
- introduced: 2026-08-13
- last-reviewed: 2026-08-13
- evidence: Knew tests compare function input with expected output; needed help designing a validator test for a new chord suffix.

## test-driven-development
- status: introduced
- depends-on: unit-testing
- introduced: 2026-08-13
- last-reviewed: 2026-08-13
- evidence: Recalled red–green–refactor but could not yet map the stages to a concrete validator change.

## regression-testing
- status: seed
- depends-on: unit-testing
- introduced: —
- last-reviewed: —
- evidence: —

## contract-testing
- status: seed
- depends-on: unit-testing
- introduced: —
- last-reviewed: —
- evidence: —

## continuous-deployment
- status: introduced
- depends-on: git-fundamentals, unit-testing
- introduced: 2026-08-13
- last-reviewed: 2026-08-13
- evidence: Explained that GitHub runs automated validation after a push and publishes the site only through a deployment task.

## git-fundamentals
- status: seed
- depends-on: none
- introduced: —
- last-reviewed: —
- evidence: —

## git-ignore-rules
- status: seed
- depends-on: git-fundamentals
- introduced: —
- last-reviewed: —
- evidence: —

## project-documentation
- status: seed
- depends-on: none
- introduced: —
- last-reviewed: —
- evidence: —

## architecture-decision-records
- status: seed
- depends-on: project-documentation
- introduced: —
- last-reviewed: —
- evidence: —

## domain-modeling
- status: introduced
- depends-on: structured-data
- introduced: 2026-08-13
- last-reviewed: 2026-08-13
- evidence: Defined the app around the learner's four-Bar Nashville Number System workflow, including chords, lyrics, comments, metadata, and future melody cues.

## legacy-song-model
- status: seed
- depends-on: structured-data, domain-modeling
- introduced: —
- last-reviewed: —
- evidence: —

## react-components
- status: seed
- depends-on: html-document-structure, javascript-functions-and-events
- introduced: —
- last-reviewed: —
- evidence: —

## react-state-and-forms
- status: seed
- depends-on: react-components, dom-rendering
- introduced: —
- last-reviewed: —
- evidence: —

## typescript
- status: seed
- depends-on: javascript-functions-and-events
- introduced: —
- last-reviewed: —
- evidence: Prior experience was reported but not probed during adoption.

## storage-design
- status: seed
- depends-on: structured-data, domain-modeling
- introduced: —
- last-reviewed: —
- evidence: —

## sql-and-relational-databases
- status: seed
- depends-on: storage-design
- introduced: —
- last-reviewed: —
- evidence: Prior CS50 experience was reported but not probed during adoption.

## client-server-architecture
- status: seed
- depends-on: dom-rendering, storage-design
- introduced: —
- last-reviewed: —
- evidence: —

## http-apis
- status: seed
- depends-on: client-server-architecture, structured-data
- introduced: —
- last-reviewed: —
- evidence: —

## environment-variables
- status: seed
- depends-on: client-server-architecture
- introduced: —
- last-reviewed: —
- evidence: —

## application-security
- status: seed
- depends-on: client-server-architecture, environment-variables
- introduced: —
- last-reviewed: —
- evidence: —

## functions
- status: introduced
- depends-on: none
- introduced: before 2026-08-13
- last-reviewed: 2026-08-13
- evidence: Recognized functions and could follow them individually, but not yet their combined runtime flow.

## assertions
- status: introduced
- depends-on: functions
- introduced: 2026-08-13
- last-reviewed: 2026-08-13
- evidence: Described a test as passing input through a function and checking the expected output.

## python-modules
- status: seed
- depends-on: functions
- introduced: —
- last-reviewed: —
- evidence: —

## technical-research
- status: seed
- depends-on: project-documentation
- introduced: —
- last-reviewed: —
- evidence: —

## agent-instructions
- status: seed
- depends-on: project-documentation
- introduced: —
- last-reviewed: —
- evidence: —

## learning-workflow
- status: introduced
- depends-on: none
- introduced: 2026-08-13
- last-reviewed: 2026-08-13
- evidence: Chose adoption to gain ownership through evidence-based walkthroughs and progressive React/TypeScript work.

## backlog-management
- status: seed
- depends-on: learning-workflow
- introduced: —
- last-reviewed: —
- evidence: —

## acceptance-testing
- status: seed
- depends-on: unit-testing, continuous-deployment
- introduced: —
- last-reviewed: —
- evidence: —

## project-history
- status: seed
- depends-on: project-documentation
- introduced: —
- last-reviewed: —
- evidence: —

## file-map
- status: introduced
- depends-on: learning-workflow
- introduced: 2026-08-13
- last-reviewed: 2026-08-13
- evidence: Learned that every repository area will be either explained, parked for a named lesson, or marked machine-generated.

## knowledge-graph
- status: introduced
- depends-on: learning-workflow
- introduced: 2026-08-13
- last-reviewed: 2026-08-13
- evidence: Learned that demonstrated understanding controls statuses and future review; self-report alone does not.
