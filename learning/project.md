# Project Adoption: Setlist Viewer

## About Me

I am a musician with about 450 handwritten Nashville Number System charts created over three years. Writing charts is how I learn and memorize songs. My charts use four-Bar groupings and combine chords, song structure, performance comments, metadata, lyrics, and eventually melody cues.

I have some programming experience, including TypeScript modifications and SQL through CS50, but this is my first web application. The current code was generated with AI through workflows inspired by Fabio Akita and Matt Pocock's Wayfinder. I directed the product and made its decisions, but wrote almost none of the implementation myself.

I can read HTML and structured JavaScript data comfortably. I can follow individual JavaScript functions, but do not yet own their combined design. CSS, test writing, the `.chart`-to-JavaScript build path, and deployment are the least familiar areas. This inventory is bookkeeping, not judgment; unprobed knowledge will remain uncredited until demonstrated.

## The Idea

Setlist Viewer turns my musician-specific chart workflow into a clear, dynamic interface usable during learning, rehearsal, and performance. The current static viewer proves the presentation model. The next version will be a React and TypeScript application where I create, edit, store, and retrieve charts directly instead of hand-authoring `.chart` files and running a Python generator.

React and TypeScript are decided choices: TypeScript is familiar territory, while React's component model is a skill I want to learn. The storage design is deliberately undecided. JSON, browser-local storage, SQL, or a hosted database must be compared against the first useful workflow before choosing. The current Python parser remains valuable reference code, but it is not automatically part of the new application.

## MVP

### In

- Preserve the current working viewer as the behavioral reference.
- Build the successor with React and TypeScript.
- Create and edit a personal Nashville Number System chart inside the application.
- Represent metadata, Expanded Arrangement, four-Bar groupings, chords, lyrics, and performance comments.
- Save a chart and retrieve it later through a storage design chosen during the learning journey.
- Keep the first version useful to one musician before expanding its audience.
- Maintain a readable interface for phone, iPad, and MacBook-sized screens.

### Frozen

- The static HTML/CSS/JavaScript viewer and generated portable artifact remain intact while the successor earns equivalent behavior.
- The `.chart` format, Python parser, generator, and GitHub Pages workflow remain reference implementations. They return to active scope only if importing old charts or static export proves valuable.
- Melody display remains frozen until we define a representation that actually helps the musician.

### Parking Lot

- Handwriting or OCR import.
- Metronome, playback, and guided practice behavior.
- Accounts, multiple users, and each user's private database.
- A public or commercial hosted product.
- Sharing and collaboration features.
- Migrating the full 450-song handwritten library.

## Triage Decision

**Adopt.** The current application runs, its 64 automated tests pass, and its generated files match their sources as of 2026-08-13. It contains working domain decisions and is neither broken nor unusually structured for its purpose. Rebuilding it blindly would discard useful evidence; freezing it entirely would prevent the desired product from growing.

We will treat the current app as a trusted reference and progressively build the React/TypeScript successor while learning the territory each feature touches. The learner accepted this decision on 2026-08-13.
