# Learning plan: Setlist Viewer

## Locked decisions

- **Current HTML/CSS/JavaScript viewer:** inherited and retained as the behavioral reference. JavaScript's rendering and interaction role was explained; CSS internals return in Section 7.
- **Current Python `.chart` build:** inherited and understood at the pipeline level. Frozen for the successor unless import/export becomes valuable; validation ideas return in Section 6.
- **Current file-backed data:** inherited and understood as the reason in-app multi-device saves are impossible. Replaced by persistent storage in Section 5.
- **Current GitHub Pages hosting:** inherited and understood as static hosting without an application server or database. Revisited in Section 8.
- **Frontend:** React with TypeScript using the Sites-supported project structure — chosen to learn components while keeping familiar TypeScript.
- **Application server:** Sites server routes written in TypeScript — one codebase and host; no separate Express service for the MVP.
- **Database:** Sites D1, a hosted SQLite-style SQL database — shared persistence across devices without an external PostgreSQL service.
- **Data shape:** searchable song metadata in normal columns; nested Sections, Bars, chords, lyrics, and notes in validated `chart_json`.
- **Access:** private Sites deployment with no app-owned accounts in the MVP — prove one musician's create–save–view loop before multi-user ownership.
- **Melody:** frozen until a representation proves useful to the musician.

## Sections

### 1. Make the ground solid  [x] complete

**Deliverable:** The current viewer runs and tests locally, Git has a verified recovery point, and all `learning/` artifacts are committed—your project can never be lost again.

**Concepts:** terminal navigation, source versus generated files, Git status, commits, test commands, build checks

**Reclaim:** `.gitignore` — explain why it exists, break one safe ignore rule, predict the Git-status change, then restore it.

**Receipt:** Required first section for adopted projects; current repository health was verified during triage.

#### Tasks

- [x] Locate the repository and read `git status` without changing files.
- [x] Open both current viewer artifacts and verify core navigation and theme behavior.
- [x] Run the automated tests and explain what a passing result proves.
- [x] Run the build drift check and distinguish source files from generated files.
- [x] Reclaim `.gitignore`, review the final diff, and create a verified Git recovery point.

### 2. Start the React/TypeScript successor  [ ] not started

**Deliverable:** A Sites-compatible React/TypeScript page runs locally beside the unchanged reference viewer and displays one real song title.

**Concepts:** React components, JSX, TypeScript props, development server, project entry point, browser DOM

**Reclaim:** `src/index.html` — explain its script-loading order, break one reference safely, predict the missing behavior, then restore it.

**Receipt:** React and TypeScript were explicitly chosen by the user; Sites is the chosen host.

#### Tasks

- [x] Reclaim `src/index.html`: trace script-loading order, break one reference safely, observe the missing behavior, then restore it.
- [ ] Create the minimal Sites-compatible React/TypeScript project beside the unchanged reference viewer.
- [ ] Trace the successor entry point from HTML to React's browser render call.
- [ ] Build a typed Song Title component with one learner-authored prop.
- [ ] Run the successor locally and verify it displays one real song title without changing either reference artifact.

### 3. Render and navigate one real chart  [ ] not started

**Deliverable:** The React viewer renders Más from typed sample data and moves between Song and Section views through working controls.

**Concepts:** component composition, arrays and mapping, React state, event handlers, conditional rendering, stable identifiers

**Reclaim:** `src/script.js` — explain the current DOM-rendering path, break one navigation handler, predict the failure, then fix it.

**Receipt:** Preserves the working viewer's core behavior while replacing direct DOM construction with React.

### 4. Create a chart inside the app  [ ] not started

**Deliverable:** A musician can create and edit song metadata plus four-Bar Sections in an in-memory form, then preview the resulting chart.

**Concepts:** domain types, controlled forms, nested state, immutable updates, validation boundaries, editor/viewer separation

**Reclaim:** the inherited `.chart` model — explain one four-Bar rule, violate it deliberately, predict the validator diagnostic, then restore the Chart.

**Receipt:** In-app authoring is the user's primary requested workflow; four-Bar grouping comes from the 450-song handwritten system.

### 5. Save and load with Sites D1  [ ] not started

**Deliverable:** Saving a chart writes it through a TypeScript server route to D1; reopening the app loads that same chart from another device session.

**Concepts:** client/server boundary, HTTP requests, server routes, SQL tables, D1 binding, JSON serialization, durable identifiers

**Reclaim:** `src/song-data.js` — explain the legacy record shape, remove one required field, predict the regression failure, then restore it before designing the D1 row.

**Receipt:** Multi-device persistence was requested; D1 was chosen specifically to keep Sites hosting simple for one user.

### 6. Protect the chart rules with TDD  [ ] not started

**Deliverable:** Invalid chart edits show useful messages, and automated tests prove valid saves succeed while invalid saves fail.

**Concepts:** red–green–refactor, unit tests, assertions, pure validation, test fixtures, error messages, regression protection

**Reclaim:** `tests/test_chart_validator.py` — explain one existing case, break its expectation, predict the red result, then repair it.

**Receipt:** The user wants TDD ownership and could name the cycle but not yet design a concrete validator test.

### 7. Make the editor stage-ready on every device  [ ] not started

**Deliverable:** Viewer and editor remain readable and operable at phone, iPad, and MacBook widths while theme and display preferences persist locally.

**Concepts:** CSS cascade, class selectors, responsive breakpoints, layout systems, accessibility, local preferences, visual testing

**Reclaim:** `src/styles.css` — explain one visibility/layout rule, break it deliberately, predict the visual result, then fix it.

**Receipt:** Device support is a core musician workflow; CSS was the strongest fear identified during inventory.

### 8. Publish the private personal tool  [ ] not started

**Deliverable:** A private Sites URL runs the tested React app and reads/writes the same D1 chart library from phone, iPad, and MacBook.

**Concepts:** production builds, environment configuration, database migrations, private deployment, deployment verification, recovery

**Reclaim:** `.github/workflows/deploy-pages.yml` — explain its validation gate, break one dependency safely, predict why deployment becomes unsafe, then restore it.

**Receipt:** The user explicitly chose ChatGPT Sites as the internal-tool host; app-owned authentication remains parked.
