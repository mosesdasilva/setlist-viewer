# Setlist Viewer

Setlist Viewer presents performance-ready song charts and navigation for rehearsal and live use.

## Language

**Nashville Number Chart**:
A song chart that represents harmony using scale-degree numbers so it can be used in different keys.
_Avoid_: Natural number chart, lyrics chart

**Artist**:
The person or band credited for the song version represented by a Nashville Number Chart.
_Avoid_: Lead Vocal

**Bar**:
A measure of musical time represented as one cell in a Nashville Number Chart.
_Avoid_: Box

**Chart Row**:
A horizontal group of exactly four consecutive Bar slots displayed together as one reading unit.
_Avoid_: Line

**Row Note**:
Optional content attached to a Chart Row rather than an individual Bar. A Row Note is explicitly either a Performance Direction or a Melody Passage.
_Avoid_: Per-bar annotation, line annotation

**Section**:
A named part of a song, such as Intro, Verse, Chorus, or Bridge, containing an ordered set of Chart Rows.
_Avoid_: Block

**Expanded Arrangement**:
The complete performance order displayed Section by Section and Bar by Bar, including every repetition rather than repeat signs or interactive jumps.
_Avoid_: Repeat navigation, collapsed arrangement

**Section Code**:
A compact label derived from a Section's authored full name: `I` Intro, `V` Verse, `T` Tag, `P` Pre-Chorus, `C` Chorus, `B` Bridge, and `E` Ending.
_Avoid_: Section initial

**Chord Symbol**:
A scale-degree chord representation that may include an accidental, quality, extension, or Slash Chord bass degree.
_Avoid_: Chord text

**No Chord**:
An intentional absence of played harmony during a Bar, written as `X`.
_Avoid_: `N.C.`, blank Bar

**Slash Chord**:
A chord whose chord degree and bass degree differ, written as chord degree over bass degree, such as `1/3`.
_Avoid_: Fraction chord

**Diamond Chord**:
A chord held as one sustained event rather than played with the regular rhythmic pattern, shown by enclosing its number in a diamond.
_Avoid_: Diamond number

**Performance Direction**:
A short playing instruction carried by a Row Note, such as `Rakes`.
_Avoid_: Comment

**Melody Passage**:
A compact number-based melody reference carried by a Row Note. It contains four Bar-aligned Melody Fragments and remains distinct from a Performance Direction.
_Avoid_: Red comment

**Melody Fragment**:
The opaque text for one Bar of a Melody Passage. V1 preserves the text without interpreting individual melody notes.
_Avoid_: Melody Bar, parsed melody
