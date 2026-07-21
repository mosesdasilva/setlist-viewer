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
A horizontal group of exactly four consecutive Bar slots displayed together as one reading unit. It may carry multiple Row Notes.
_Avoid_: Line

**Row Note**:
A typed annotation attached to a Chart Row rather than an individual Bar. Each Row Note is explicitly either a Performance Direction or a Melody Passage.
_Avoid_: Per-bar annotation, line annotation

**Section**:
A named part of a song, such as Intro, Verse, Chorus, or Bridge, containing an ordered set of Chart Rows.
_Avoid_: Block

**Section Name**:
The full human-readable name of a Section, used as its primary display label in the chart.
_Avoid_: Section Code

**Expanded Arrangement**:
The complete performance order displayed Section by Section and Bar by Bar, including every repetition rather than repeat signs or interactive jumps.
_Avoid_: Repeat navigation, collapsed arrangement

**Section Code**:
A compact label of exactly two uppercase letters representing a Section type in chart data. Standard types have default codes; custom codes must be unique within their song.
_Avoid_: Section tag, section initial, one-letter code

Standard Section Codes are `IN` Intro, `IS` Instrumental, `VS` Verse, `TG` Tag, `PC` Pre-Chorus, `CH` Chorus, `BR` Bridge, `TR` Turnaround, `EN` Ending, and `OU` Outro.

**Section Ordinal**:
An optional number distinguishing Sections of the same type. It remains separate from the two-letter Section Code but may follow it in compact notation, such as `VS2`.
_Avoid_: Numbered Section Code

**Chord Symbol**:
A scale-degree chord representation that may include an accidental, quality, extension, or Slash Chord bass degree.
_Avoid_: Chord text

**Chord Event**:
A Chord Symbol played for a duration within a Bar. Multiple Chord Events divide the Bar equally unless Beat Dots state unequal durations.
_Avoid_: Chord token

**Beat Dot**:
A dot displayed above a Chord Symbol that assigns one beat of duration to its Chord Event. Multiple dots assign the corresponding number of beats.
_Avoid_: Duration dot

**No Chord**:
An intentional absence of played harmony during a Bar, written as `X`.
_Avoid_: `N.C.`, blank Bar

**Empty Bar Slot**:
An unused trailing position in an incomplete Chart Row. It renders empty and is distinct from a No Chord Bar.
_Avoid_: `X`, No Chord

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
