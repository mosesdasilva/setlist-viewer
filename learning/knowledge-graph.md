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
- status: practicing
- depends-on: html-document-structure
- introduced: 2026-08-13
- last-reviewed: 2026-08-13
- evidence: Explained in detail that JavaScript renders catalog content, creates the temporary page tree, and controls navigation, search, modes, sizing, palette, and theme.

## dom-rendering
- status: practicing
- depends-on: html-document-structure, javascript-functions-and-events
- introduced: 2026-08-13
- last-reviewed: 2026-08-13
- evidence: Explained that `script.js` creates the browser's temporary in-memory page elements from `chart-data.js`; exact creation calls remain to be practiced.

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
- status: practicing
- depends-on: parsing-and-validation, generated-artifacts
- introduced: 2026-08-13
- last-reviewed: 2026-08-13
- evidence: Explained why custom `.chart` text needs the Python build today and why direct in-app authoring removes that need unless import/export remains.

## generated-artifacts
- status: introduced
- depends-on: build-pipeline
- introduced: 2026-08-13
- last-reviewed: 2026-08-13
- evidence: Identified `chart-data.js` as generated output rather than the musician-authored source.

## static-web-app
- status: practicing
- depends-on: html-document-structure, css-cascade-and-selectors, javascript-functions-and-events
- introduced: 2026-08-13
- last-reviewed: 2026-08-13
- evidence: Explained both same-page dynamic behavior and GitHub Pages' inability to run application database writes; needed correction that Pages serves separate source files unchanged.

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
- status: practicing
- depends-on: git-fundamentals, unit-testing
- introduced: 2026-08-13
- last-reviewed: 2026-08-13
- evidence: Explained that GitHub runs automated validation before publishing and why static Pages hosting cannot provide the successor's database server.

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
- status: practicing
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
- status: introduced
- depends-on: html-document-structure, javascript-functions-and-events
- introduced: 2026-08-13
- last-reviewed: 2026-08-13
- evidence: Chose React to learn component-based dynamic interfaces; components have not yet been written or explained technically.

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
- status: practicing
- depends-on: structured-data, domain-modeling
- introduced: 2026-08-13
- last-reviewed: 2026-08-13
- evidence: Compared local SQLite, hosted SQL, and PostgreSQL; chose D1, then explained searchable metadata columns versus deeply nested chart JSON after one correction.

## sql-and-relational-databases
- status: introduced
- depends-on: storage-design
- introduced: 2026-08-13
- last-reviewed: 2026-08-13
- evidence: Explained that relational storage supports manageable relationships and selective loading; prior CS50 experience remains unprobed.

## client-server-architecture
- status: practicing
- depends-on: dom-rendering, storage-design
- introduced: 2026-08-13
- last-reviewed: 2026-08-13
- evidence: Explained that browser and database-writing server code should be separate for smaller payloads and protected database access; HTML-injection claim needed correction.

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
- status: introduced
- depends-on: client-server-architecture, environment-variables
- introduced: 2026-08-13
- last-reviewed: 2026-08-13
- evidence: Recognized that database operations should not be exposed directly in browser code; learned that this boundary does not automatically prevent injection.

## d1-hosted-sqlite
- status: practicing
- depends-on: sql-and-relational-databases, client-server-architecture
- introduced: 2026-08-13
- last-reviewed: 2026-08-13
- evidence: Explained that a phone save writes to shared hosted D1 before other devices can read it, distinguishing shared persistence from live collaboration and local SQLite.

## server-routes
- status: introduced
- depends-on: client-server-architecture, http-apis
- introduced: 2026-08-13
- last-reviewed: 2026-08-13
- evidence: Learned the path browser to Sites server route to D1; implementation and request details remain unpracticed.

## authentication
- status: practicing
- depends-on: application-security, client-server-architecture
- introduced: 2026-08-13
- last-reviewed: 2026-08-13
- evidence: Explained why app-owned accounts should wait until the single-user create–save–view loop works.

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
- status: practicing
- depends-on: none
- introduced: 2026-08-13
- last-reviewed: 2026-08-13
- evidence: Chose adoption, completed evidence probes, reasoned through successor decisions, and confirmed the eight-section build sequence.

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
