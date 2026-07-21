# Static Nashville chart formats and storage

## Question

Which source format and storage approach best fits Setlist Viewer’s four-Bar Chart Rows, side-by-side Row Notes, fully Expanded Arrangement, direct `file://` use, GitHub Pages deployment, and generated self-contained HTML?

## Recommendation

Take a **small, documented ChordPro 6 grid profile** into the source-format prototype as the leading candidate, one UTF-8 text file per song. Do not adopt it until a representative handwritten chart proves the fit. If adopted, generate two checked-in runtime artifacts from it:

1. a normalized classic JavaScript data file for the split site; and
2. the self-contained portable HTML with normalized data, CSS, and JavaScript inlined.

Keep a small manifest as the canonical setlist/song order. Do not parse song files or fetch JSON in the browser. Generation should use repository-local/standard-library tooling, require no package install, and validate the profile before replacing outputs.

Why: ChordPro is the closest evaluated existing interchange format to the layout domain. Its official grid syntax supports rectangular chord-only layouts, bar lines, section labels, and left/right margin text; its reference implementation recognizes Nashville-number chord roots. Metadata supports standard fields such as title, key, time, and tempo plus freely named fields, covering `lead_vocal` and details. [ChordPro grids](https://www.chordpro.org/chordpro/directives-env_grid/) [ChordPro Nashville chords](https://www.chordpro.org/chordpro/chordpro-chords/) [ChordPro metadata](https://www.chordpro.org/chordpro/directives-meta/)

Use JotChord's ChordText as the strongest notation-language reference, not as the storage format. It models chart metadata, Sections, measures, split Bars, altered and slash chords, holds, pushes, ties, rests, modulations, comments, and repeat marks in musician-oriented plain text. Its preference for linear reading also supports Setlist Viewer's Expanded Arrangement. [ChordText reference](https://www.jotchord.com/reference-guide)

The browser artifacts remain deliberately app-specific. This separates musician-readable/interchange-friendly source from the exact normalized object model the UI needs.

## Proposed ChordPro profile

Illustrative source, not an implementation:

```text
{title: Example Song}
{key: D}
{tempo: 96}
{time: 4/4}
{meta: lead_vocal Example Singer}
{meta: details Keys intro}

{start_of_grid label="Intro" shape="0+4+1"}
| 1 | 4 | 5 | 1 | build
{end_of_grid}

{start_of_grid label="Chorus" shape="0+4+1"}
| 1 | 5 | 6m | 4 | all in
| 1 | 5 | 4 | 4 | hold
{end_of_grid}
```

Profile rules:

- Each grid is one performed Section; repeated Sections are repeated in full and in performance order.
- Each grid line is one Chart Row. Default profile shape is zero left-margin cells, four Bar cells, and one right-margin Row Note area.
- Each Bar is delimited by bar lines. Multiple changes inside a Bar may use a documented subdivision convention; avoid inventing it until a representative chart requires it.
- Use Nashville-number tokens and a deliberately limited token grammar. ChordPro’s file-format specification does not itself define valid chords; the reference implementation recognizes roots `1`–`7`, accidentals, qualities, extensions, and bass parts. Treat unsupported tokens as literal display content or reject them during validation. [ChordPro chord parsing](https://www.chordpro.org/chordpro/chordpro-chords/)
- Permit only required metadata, grid start/end directives, labels, comments, and agreed chord/grid tokens. Exclude compact repeats (`%`, `%%`, repeat bar lines) because the product requires an Expanded Arrangement even though ChordPro supports them. [ChordPro grid symbols](https://www.chordpro.org/chordpro/directives-env_grid/)
- Store UTF-8. OpenSong’s official format guidance also recommends UTF-8 to preserve special characters, supporting this as the safest interchange encoding. [OpenSong file formats](https://opensong.org/development/file-formats/)

Before adoption, test this profile against the representative handwritten chart ticket. In particular, verify split Bars, pushes/diamonds/holds, no-chord, mid-song key changes, and free-form Row Notes.

## Format comparison

| Option | Fit | Advantages | Costs / risks |
|---|---|---|---|
| Constrained ChordPro grid | Best source candidate | Plain text; existing metadata, labeled environments, grids, Nashville recognition, bar/repeat symbols, and margin notes. The official grid grammar directly resembles four Bars plus Row Note. [Grid directive](https://www.chordpro.org/chordpro/directives-env_grid/) | Full ChordPro is larger than needed. Nashville recognition is a reference-implementation behavior, so Setlist Viewer must publish its own narrow accepted profile. A parser/generator is required. |
| ChordText | Best notation reference | Nashville-specific plain text with explicit metadata and Sections plus broad documented chord, rhythm, articulation, instruction, and song-form vocabulary. [ChordText reference](https://www.jotchord.com/reference-guide) | Its whitespace-delimited measures and rich symbolic grammar are parser-sensitive; it does not document Setlist Viewer's exact four-Bar Chart Row plus side-by-side Row Note record. Treat its vocabulary as evidence, not an adopted dependency. |
| OnSong text | Useful interchange reference | Plain text; sections, metadata, chord placement, musical instructions, and Flow. [OnSong format](https://onsongapp.com/docs/features/formats/onsong/) [Sections](https://onsongapp.com/docs/features/formats/onsong/section/) | Primarily shaped around chords-plus-lyrics. Flow writes a Section once then expands references, opposing canonical Expanded Arrangement. Its syntax is product-specific; no first-class four-Bar/Row-Note record is documented. [Flow](https://onsongapp.com/docs/features/formats/onsong/metadata/flow/) |
| OpenSong XML | Poor canonical fit | Official XML song structure; fields include title, tempo, time signature, key, lyrics, and presentation. [OpenSong format](https://opensong.org/development/file-formats/) | Verbose, projection/lyrics-oriented, old published schema, and no documented first-class four-Bar/Row-Note structure. Best treated only as a possible future importer. |
| Custom JSON | Best normalized runtime model | Ordered arrays naturally preserve Sections, Chart Rows, and Bars; object fields express metadata and Row Notes exactly. JSON Schema can document and validate required properties, types, and constraints. [JSON structures](https://json.org/) [JSON Schema](https://json-schema.org/learn/getting-started-step-by-step) | Verbose for musicians, punctuation-sensitive, no comments, and no chart-tool interoperability. It remains a strong generated intermediate/runtime form. |
| Custom terse text DSL | Compact but avoid initially | Could exactly match house notation and be pleasant to type. | Creates a new grammar, escaping rules, parser, validator, documentation burden, and permanent migration surface before representative-chart requirements are known. |

ChordPro is preferable to OnSong here because ChordPro formally documents a grid: chord-only rectangular cells, bar lines, labels, and margin text. OnSong’s documented strength is lyric-oriented Sections plus a separate compact Flow instruction. [ChordPro grids](https://www.chordpro.org/chordpro/directives-env_grid/) [OnSong Flow](https://onsongapp.com/docs/features/formats/onsong/metadata/flow/)

## Storage and delivery comparison

### Separate JSON loaded with `fetch()`

Good on GitHub Pages, unsafe as the only local path. Modern browsers commonly assign opaque origins to local files, so `fetch()`/XHR of sibling files can fail under `file://`. MDN recommends a local HTTP server for that pattern. [MDN: CORS request not HTTP](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/CORS/Errors/CORSRequestNotHttp)

### ES modules / JSON modules

Avoid while direct double-click use is required. Browser module loading uses CORS rules; MDN explicitly warns that local `file://` module testing produces CORS errors. [MDN: JavaScript modules](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Modules)

### External classic JavaScript data

Best split-site runtime shape for direct opening: a checked-in generated file such as `chart-data.generated.js` assigns normalized data to one application namespace, followed by the existing classic application script. Standard HTML supports external classic scripts, and MDN recommends classic `script src` when a local server is unavailable. [WHATWG script element](https://html.spec.whatwg.org/dev/scripting.html) [MDN: adding JavaScript](https://developer.mozilla.org/en-US/docs/Web/HTML/How_to/Add_JavaScript_to_your_web_page)

This artifact is executable, not canonical authoring data. Generate it only from trusted repository content and never concatenate unescaped user input into JavaScript source.

### Inline JSON data block

Best self-contained artifact shape: embed normalized JSON in a non-JavaScript `<script type="application/json">` data block, then parse its text. WHATWG defines non-JavaScript MIME types on `script` as inert data blocks. A data block cannot use `src`; the content must be inline. [WHATWG data blocks](https://html.spec.whatwg.org/dev/scripting.html) [MDN script type](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/script/type)

The generator must safely encode any sequence that could terminate the HTML script element.

### `localStorage`

Use only for nonessential preferences, with failure handling. Behavior for `file:` URLs is undefined and varies by browser, so chart content and essential state must not depend on it. [MDN localStorage](https://developer.mozilla.org/en-US/docs/Web/API/Window/localStorage)

### GitHub Pages

The split artifact fits GitHub Pages directly: Pages publishes repository HTML, CSS, and JavaScript as a static site and may optionally use a build process. No server-side data store is needed. [GitHub Pages](https://docs.github.com/en/pages/getting-started-with-github-pages/what-is-github-pages)

## Source-of-truth layout

Conceptual only:

```text
charts/
  manifest.json              # song/set order
  songs/
    example-song.chordpro    # canonical song source
src/
  index.html
  styles.css
  script.js
  chart-data.generated.js    # checked-in runtime artifact
setlist-viewer-v1.html       # checked-in generated portable artifact
```

Generation invariants:

- one-way flow: canonical manifest + ChordPro files + split UI source → generated runtime artifacts;
- never hand-edit generated files;
- validate unique song IDs, required metadata, exactly four Bars per normal Chart Row, known Section names, and profile syntax;
- write outputs only after all inputs validate;
- include a generated-file banner and deterministic formatting so Git diffs stay reviewable;
- verify both `src/index.html` under `file://` and the portable HTML after every generation.

## Decision boundary

Adopt the ChordPro profile only if the representative handwritten chart can be expressed without opaque hacks. If it cannot, retain the same storage/delivery architecture but make per-song JSON the canonical source and document a project-specific schema. Do not expand the ChordPro profile until an observed chart requires it.
