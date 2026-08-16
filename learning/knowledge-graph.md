# Knowledge graph

<!-- statuses: seed → introduced → practicing → understood -->
<!-- seed: not yet taught | introduced: explained once | practicing: used it with help | understood: explained in own words + passed a later review -->

## html-document-structure
- status: practicing
- depends-on: none
- introduced: before 2026-08-13
- last-reviewed: 2026-08-14
- evidence: Explained that HTML holds page content in a tree; after safely breaking `chart-data.js`, identified the surviving shell/default title as HTML and the missing Songs as data-dependent content.

## script-loading-order
- status: practicing
- depends-on: html-document-structure, javascript-functions-and-events, structured-data
- introduced: 2026-08-14
- last-reviewed: 2026-08-14
- evidence: Predicted that renaming the first script reference would prevent catalog data from loading, observed the empty-catalog fallback and exact `ERR_FILE_NOT_FOUND`, then restored the reference and verified Songs returned with a clean console.

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
- last-reviewed: 2026-08-15
- evidence: Explained in detail that JavaScript renders catalog content, creates the temporary page tree, and controls navigation, search, modes, sizing, palette, and theme. Later authored React click handlers that set view and Section-index state, then correctly predicted disabled boundary behavior.

## dom-rendering
- status: practicing
- depends-on: html-document-structure, javascript-functions-and-events
- introduced: 2026-08-13
- last-reviewed: 2026-08-14
- evidence: Identified `document.createElement` as creating a DOM element and `appendChild` as attaching it to the page tree, then traced catalog rendering into navigation-controlled Song elements.

## array-iteration
- status: practicing
- depends-on: structured-data, functions
- introduced: 2026-08-14
- last-reviewed: 2026-08-15
- evidence: Explained that `catalog.forEach(renderSong)` runs `renderSong` 12 times for a 12-Song catalog. Later predicted eight Bar strings produce eight components, authored both Bar and Section `.map()` prop connections, and filled the arrangement lookup comparison correctly after a syntax-sized hint.

## structured-data
- status: practicing
- depends-on: none
- introduced: before 2026-08-13
- last-reviewed: 2026-08-14
- evidence: Described `chart-data.js` as nested key-value data representing songs, lyrics, and chart structure. Later explained why Más chord tokens require strings and authored the typed eight-Bar Bridge definition.

## chart-notation
- status: practicing
- depends-on: structured-data
- introduced: before 2026-08-13
- last-reviewed: 2026-08-15
- evidence: Deliberately added a fifth Bar slot to Más's Tag row, observed the exact four-slot diagnostic, restored the valid row, and predicted the final successful exit status `0`.

## parsing-and-validation
- status: practicing
- depends-on: chart-notation, structured-data
- introduced: 2026-08-13
- last-reviewed: 2026-08-15
- evidence: Explained that the malformed five-slot row is rejected, which leaves Tag with no valid rows and therefore produces both `E031` and the cascading `E028`; correctly reasoned that another valid Tag row would prevent `E028`.

## validation-boundaries
- status: practicing
- depends-on: parsing-and-validation, domain-modeling
- introduced: 2026-08-15
- last-reviewed: 2026-08-15
- evidence: Explained in own words how rejecting one invalid Chart Row changes the Section-level validation result, distinguishing the row rule from the Section rule.

## build-pipeline
- status: practicing
- depends-on: parsing-and-validation, generated-artifacts
- introduced: 2026-08-13
- last-reviewed: 2026-08-14
- evidence: Ran `python3 tools/build.py --check`, verified exit status `0`, and explained that changing `charts/mas.chart` requires rebuilding generated browser data and portable HTML.

## generated-artifacts
- status: practicing
- depends-on: build-pipeline
- introduced: 2026-08-13
- last-reviewed: 2026-08-14
- evidence: Identified `src/chart-data.js` and portable HTML as files not to hand-edit and correctly predicted that `--check` reports generated drift when they disagree with authored chart source.

## static-web-app
- status: practicing
- depends-on: html-document-structure, css-cascade-and-selectors, javascript-functions-and-events
- introduced: 2026-08-13
- last-reviewed: 2026-08-13
- evidence: Opened both split and portable viewers directly, verified navigation and theme behavior, and explained why a browser renders HTML instead of showing its raw text.

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
- status: practicing
- depends-on: functions, assertions
- introduced: 2026-08-13
- last-reviewed: 2026-08-14
- evidence: Ran all 64 tests, interpreted `OK`, and explained that they verify defined validation, generation, content, rendering-contract, and deployment expectations without proving visual browser behavior.

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
- status: practicing
- depends-on: none
- introduced: 2026-08-13
- last-reviewed: 2026-08-14
- evidence: After an unstaged commit failed, independently used `git add .`, committed four learning-document changes, and pushed commit `7538758` to `origin/main`.

## git-staging-pathspecs
- status: practicing
- depends-on: git-fundamentals, command-line-arguments, git-ignore-rules
- introduced: 2026-08-14
- last-reviewed: 2026-08-14
- evidence: Independently used `git add .` to stage and commit the lesson files; initially omitted the required space and needed correction that `.` also includes non-ignored untracked files beneath the current directory.

## terminal-navigation
- status: practicing
- depends-on: none
- introduced: 2026-08-13
- last-reviewed: 2026-08-13
- evidence: Predicted the repository's absolute path, ran `pwd`, and confirmed the terminal was in `/Users/mosesdasilva/Documents/Setlist Viewer`.

## shell-command-path
- status: practicing
- depends-on: terminal-navigation
- introduced: 2026-08-14
- last-reviewed: 2026-08-14
- evidence: Connected Unix `PATH` to prior Windows experience, explained that it lets the terminal locate programs without their full paths, and temporarily added the bundled Node and pnpm folders before running the build.

## command-line-arguments
- status: practicing
- depends-on: terminal-navigation
- introduced: 2026-08-14
- last-reviewed: 2026-08-14
- evidence: Diagnosed that typing `discover-s` as one word made Python search for that module, then added the missing space and successfully ran the suite.

## process-exit-status
- status: practicing
- depends-on: terminal-navigation
- introduced: 2026-08-14
- last-reviewed: 2026-08-14
- evidence: Ran `echo $?`, observed `0`, and explained that zero indicates the preceding build check succeeded.

## git-ignore-rules
- status: practicing
- depends-on: git-fundamentals
- introduced: 2026-08-14
- last-reviewed: 2026-08-14
- evidence: Removed and restored the `.DS_Store` rule, predicted its untracked status, then added `tmp/` and predicted that generated temporary output would disappear from Git status.

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
- status: practicing
- depends-on: html-document-structure, javascript-functions-and-events
- introduced: 2026-08-13
- last-reviewed: 2026-08-14
- evidence: Traced `Home` returning a child component; later traced `ChartView` composing `SongTitle` and `ChartSectionView`, which composes `Bar`, and accurately predicted their visible output with minor corrections about React keys and HTML placement.

## component-composition
- status: practicing
- depends-on: react-components, react-props-and-children, array-iteration
- introduced: 2026-08-14
- last-reviewed: 2026-08-14
- evidence: Connected mapped Bar strings to `Bar` props and mapped Sections to `ChartSectionView`, then explained the visible responsibilities of `ChartView` and `ChartSectionView` before verifying the rendered Más output.

## jsx
- status: practicing
- depends-on: javascript-functions-and-events, html-document-structure
- introduced: 2026-08-14
- last-reviewed: 2026-08-15
- evidence: Explained that curly braces embed JavaScript values inside HTML-like TSX and traced JSX from `Home` through `RootLayout` into the body; needed correction that React elements are not entire files. Later corrected a quoted literal React key to the `occurrenceId` variable and reused that variable as a component prop.

## react-props-and-children
- status: practicing
- depends-on: react-components, jsx
- introduced: 2026-08-14
- last-reviewed: 2026-08-14
- evidence: Initially could not distinguish the `React.ReactNode` type from the value source, then explained that vinext passes `Home`'s `<SkeletonPreview />` result into `RootLayout` as `children`. Later authored `title="Más"` in `page.tsx` and explained that a prop can pass a dynamic value for React to render.

## server-rendering-and-hydration
- status: practicing
- depends-on: dom-rendering, react-components
- introduced: 2026-08-14
- last-reviewed: 2026-08-14
- evidence: Explained that hydration lets a server-rendered counter respond to clicks and change from zero to one, then correctly traced server HTML followed by vinext `hydrateRoot`; needed correction that `"use client"` controls browser JavaScript rather than visibility.

## framework-file-routing
- status: practicing
- depends-on: html-document-structure, react-components
- introduced: 2026-08-14
- last-reviewed: 2026-08-14
- evidence: Explained that `/` reaches `worker/index.ts`, vinext selects `RootLayout` and `Home`, `Home` returns `SkeletonPreview`, and the layout places it inside the body.

## vinext-framework
- status: introduced
- depends-on: framework-file-routing, server-rendering-and-hydration, build-pipeline
- introduced: 2026-08-14
- last-reviewed: 2026-08-14
- evidence: Successfully traced vinext's role between the Worker, route files, server HTML, and hydration, while explicitly identifying vinext internals as still unclear.

## development-server
- status: practicing
- depends-on: terminal-navigation, vinext-framework
- introduced: 2026-08-14
- last-reviewed: 2026-08-14
- evidence: Started the successor at `localhost:3000`, verified it displayed `Más`, predicted that Control-C would terminate the process, then confirmed the page became unavailable afterward.

## react-state-and-forms
- status: practicing
- depends-on: react-components, dom-rendering
- introduced: 2026-08-15
- last-reviewed: 2026-08-15
- evidence: Authored both `view` and `sectionIndex` state, explained the value/setter pair, connected setters to click handlers, and diagnosed that changing state causes no visible change when JSX never reads it.

## conditional-rendering
- status: practicing
- depends-on: react-state-and-forms, jsx
- introduced: 2026-08-15
- last-reviewed: 2026-08-15
- evidence: Predicted the Song/Section ternary branches, explained why the missing state-dependent branch caused no visible update, and verified switching between nine Sections and one selected Section.

## typescript
- status: practicing
- depends-on: javascript-functions-and-events
- introduced: 2026-08-14
- last-reviewed: 2026-08-15
- evidence: Authored a string prop and typed Chart data; later explained that `ViewMode` rejects values outside `"song" | "section"`, distinguished whole-project Cloudflare diagnostics from lesson files, and completed a silent focused type check.

## typescript-object-types
- status: practicing
- depends-on: typescript, structured-data
- introduced: 2026-08-14
- last-reviewed: 2026-08-14
- evidence: Authored the Bridge object with the required `id`, `name`, and eight string Bars, and validated it against `ChartSection` with a silent strict type check.

## stable-identifiers
- status: practicing
- depends-on: structured-data, domain-modeling
- introduced: 2026-08-14
- last-reviewed: 2026-08-15
- evidence: Explained that repeated Bridge occurrences can reuse one ID and proposed a distinct `bridge-2` definition plus replacing only the changed arrangement occurrence when its chords differ. Later explained that an occurrence ID combines the Section ID with the arrangement occurrence index and correctly predicted the second Bridge link would target the second rendered Bridge.

## array-find-and-undefined
- status: introduced
- depends-on: array-iteration, structured-data
- introduced: 2026-08-15
- last-reviewed: 2026-08-15
- evidence: Filled the `.find()` comparison after a syntax-sized hint; initially expected a failed lookup to return `false`, then learned that the callback returns booleans while `.find()` returns `undefined` when no item matches.

## fragment-link-navigation
- status: practicing
- depends-on: html-document-structure, stable-identifiers, jsx
- introduced: 2026-08-15
- last-reviewed: 2026-08-15
- evidence: Authored matching occurrence-ID props and fragment `href` values, then predicted that the second Bridge link would jump to its distinct rendered occurrence because the link target and element ID match.

## dependency-management
- status: practicing
- depends-on: structured-data, generated-artifacts
- introduced: 2026-08-14
- last-reviewed: 2026-08-14
- evidence: Explained that a lockfile fixes dependency versions while installation materializes those dependencies locally, and correctly predicted a repeat install would report `Already up to date`.

## dependency-build-scripts
- status: introduced
- depends-on: dependency-management, application-security
- introduced: 2026-08-14
- last-reviewed: 2026-08-14
- evidence: Initially thought a `false` build policy prevented dependency installation; learned that it installs packages while blocking their automatic lifecycle scripts.

## sites-project-configuration
- status: practicing
- depends-on: project-documentation, dependency-management
- introduced: 2026-08-14
- last-reviewed: 2026-08-14
- evidence: Explained that `.openai/hosting.json` configures OpenAI hosting and inferred from its `null` D1/R2 values that those capabilities are not currently active.

## nested-git-repositories
- status: practicing
- depends-on: git-fundamentals
- introduced: 2026-08-14
- last-reviewed: 2026-08-14
- evidence: Explained that `successor/` should not keep its own `.git` because it belongs inside the parent Setlist Viewer repository, then moved the nested metadata to a recoverable backup.

## git-upstream-tracking
- status: practicing
- depends-on: git-fundamentals
- introduced: 2026-08-14
- last-reviewed: 2026-08-14
- evidence: Correctly predicted the remote branch name and pushed with `-u`; initially attributed later argument-free pushes only to the selected branch, then learned that Git uses its saved upstream relationship.

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
- status: introduced
- depends-on: learning-workflow
- introduced: 2026-08-14
- last-reviewed: 2026-08-14
- evidence: Explained that `TODO.md` preserves desired features from the prior development cycle and chose to include it in the recovery commit.

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
