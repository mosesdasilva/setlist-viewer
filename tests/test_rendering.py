from __future__ import annotations

import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class RenderingContractTest(unittest.TestCase):
    def test_split_viewer_loads_generated_catalog_before_renderer(self):
        html = (ROOT / "src" / "index.html").read_text(encoding="utf-8")

        scripts = re.findall(r'<script src="([^"]+)"></script>', html)

        self.assertEqual(["chart-data.js", "script.js"], scripts)

    def test_viewer_uses_compact_section_bands_shell(self):
        html = (ROOT / "src" / "index.html").read_text(encoding="utf-8")

        self.assertIn('class="song-header"', html)
        self.assertIn('id="song-map"', html)
        self.assertIn('id="song-picker-trigger"', html)
        self.assertIn('id="song-picker"', html)
        self.assertIn('id="song-search"', html)
        self.assertIn('id="song-picker-results"', html)
        self.assertNotIn('id="song-directory"', html)
        self.assertIn('id="song-title"', html)
        self.assertNotIn('class="hero"', html)
        self.assertNotIn("prototype-warning", html)

    def test_song_picker_has_accessible_modal_contract(self):
        html = (ROOT / "src" / "index.html").read_text(encoding="utf-8")

        self.assertIn('<dialog class="song-picker" id="song-picker"', html)
        self.assertIn('aria-labelledby="song-picker-title"', html)
        self.assertIn('aria-controls="song-picker"', html)
        self.assertIn('aria-haspopup="dialog"', html)
        self.assertIn('aria-label="Close Song Picker"', html)
        self.assertIn('type="search"', html)
        self.assertIn('aria-live="polite"', html)

    def test_song_picker_filters_catalog_and_handles_all_dismissals(self):
        script = (ROOT / "src" / "script.js").read_text(encoding="utf-8")

        for behavior in (
            "showModal()",
            'addEventListener("input"',
            'addEventListener("cancel"',
            'addEventListener("close"',
            'event.target === songPicker',
            'event.key === "Escape"',
            'song.title.toLocaleLowerCase()',
            'song.artist || ""',
            'setAttribute("aria-current"',
            'song.type === "legacy"',
        ):
            with self.subTest(behavior=behavior):
                self.assertIn(behavior, script)

    def test_picker_is_desktop_overlay_and_mobile_full_screen_sheet(self):
        styles = (ROOT / "src" / "styles.css").read_text(encoding="utf-8")

        self.assertRegex(styles, r"\.song-picker::backdrop\s*\{")
        self.assertRegex(styles, r"\.song-picker\s*\{[^}]*position:\s*fixed;")
        mobile = styles[styles.index("@media (max-width: 699px)") :]
        self.assertRegex(mobile, r"\.song-picker\s*\{[^}]*width:\s*100%;[^}]*height:\s*100%;")

    def test_display_controls_expose_accessible_one_two_and_four_column_choices(self):
        html = (ROOT / "src" / "index.html").read_text(encoding="utf-8")

        self.assertIn('role="group" aria-label="Section columns"', html)
        for columns in ("one", "two", "four"):
            with self.subTest(columns=columns):
                self.assertIn(f'id="layout-{columns}"', html)
                self.assertRegex(
                    html,
                    rf'id="layout-{columns}"[^>]*aria-pressed="(?:true|false)"[^>]*title="Use {columns} Section column',
                )

        for control in ("palette-toggle", "theme-toggle"):
            with self.subTest(control=control):
                self.assertRegex(
                    html,
                    rf'id="{control}"[^>]*aria-pressed="(?:true|false)"[^>]*aria-label="[^"]+"[^>]*title="[^"]+"',
                )

    def test_chart_display_modes_are_one_accessible_exclusive_control(self):
        html = (ROOT / "src" / "index.html").read_text(encoding="utf-8")

        self.assertIn('role="radiogroup" aria-label="Chart Display Mode"', html)
        for mode, checked in (("chords", "true"), ("melody", "false"), ("lyrics", "false")):
            with self.subTest(mode=mode):
                self.assertRegex(
                    html,
                    rf'class="[^"]*display-mode-button[^"]*"[^>]*role="radio"[^>]*'
                    rf'aria-checked="{checked}"[^>]*data-chart-mode="{mode}"',
                )
        self.assertNotIn('id="melody-toggle"', html)

    def test_chart_modes_render_exclusive_content_and_a_lyrics_empty_seam(self):
        script = (ROOT / "src" / "script.js").read_text(encoding="utf-8")
        styles = (ROOT / "src" / "styles.css").read_text(encoding="utf-8")

        self.assertIn('"lyrics-block lyrics-empty-state"', script)
        self.assertIn('"Lyrics not available."', script)
        self.assertIn('body.dataset.chartMode = mode', script)
        self.assertIn('savePreference("chart-mode", mode)', script)
        self.assertIn("if (event.defaultPrevented)", script)
        self.assertRegex(
            styles,
            r'body\[data-chart-mode="chords"\] \.bar-melodies\s*\{[^}]*display:\s*none;',
        )
        self.assertRegex(
            styles,
            r'body\[data-chart-mode="melody"\] \.bar-events\s*\{[^}]*display:\s*none;',
        )
        self.assertRegex(
            styles,
            r'body\[data-chart-mode="lyrics"\] \.chart-row\s*\{[^}]*display:\s*none;',
        )
        self.assertRegex(
            styles,
            r'body\[data-chart-mode="lyrics"\] \.lyrics-block\s*\{[^}]*display:\s*flex;',
        )

    def test_renderer_preserves_ordered_occurrence_lyrics_and_empty_occurrences(self):
        script = (ROOT / "src" / "script.js").read_text(encoding="utf-8")
        styles = (ROOT / "src" / "styles.css").read_text(encoding="utf-8")

        self.assertIn('"lyrics-block"', script)
        self.assertIn('"lyric-line"', script)
        self.assertIn("section.lyrics.forEach", script)
        self.assertIn('"Lyrics not available."', script)
        self.assertIn('"lyrics-block lyrics-empty-state"', script)
        self.assertRegex(styles, r"\.lyric-line\s*\{[^}]*font-size:\s*clamp\(11px,\s*1vw,\s*13px\);")

    def test_bar_numbering_modes_are_persistent_and_invalid_values_fall_back(self):
        html = (ROOT / "src" / "index.html").read_text(encoding="utf-8")
        script = (ROOT / "src" / "script.js").read_text(encoding="utf-8")

        self.assertIn('role="radiogroup" aria-label="Bar Numbering Mode"', html)
        self.assertRegex(
            html,
            r'data-bar-numbering="section"[^>]*>Per Section<',
        )
        self.assertRegex(
            html,
            r'data-bar-numbering="global"[^>]*>Global<',
        )
        self.assertIn('"bar-number"', script)
        self.assertIn("barElement.dataset.sectionBarNumber", script)
        self.assertIn("barElement.dataset.globalBarNumber", script)
        self.assertIn('if (!["section", "global"].includes(mode))', script)
        self.assertIn('savePreference("bar-numbering", mode)', script)

    def test_four_and_eight_bar_occurrences_share_one_outer_footprint(self):
        styles = (ROOT / "src" / "styles.css").read_text(encoding="utf-8")
        script = (ROOT / "src" / "script.js").read_text(encoding="utf-8")

        self.assertIn("sectionElement.dataset.barCount", script)
        self.assertRegex(
            styles,
            r'\.section-band\[data-bar-count="4"\],\s*'
            r'\.section-band\[data-bar-count="8"\]\s*\{[^}]*height:\s*var\(--section-band-height\);',
        )
        self.assertNotIn("push(null)", script)

    def test_chart_renderer_exposes_complete_stage_reading_structure(self):
        script = (ROOT / "src" / "script.js").read_text(encoding="utf-8")

        for public_hook in (
            "section-band",
            "section-heading",
            "section-name",
            "section-code",
            "chart-row",
            "bars-and-notes",
            "bar",
            "empty-bar",
            "beat-dots",
            "no-chord",
            "diamond",
            "chord-suffix",
            "slash-bass",
            "row-notes",
            "ordered-row-note",
            "performance-direction",
            "melody-passage",
            "melody-fragment",
        ):
            with self.subTest(public_hook=public_hook):
                self.assertIn(public_hook, script)

    def test_four_bars_and_notes_remain_side_by_side_at_all_widths(self):
        styles = (ROOT / "src" / "styles.css").read_text(encoding="utf-8")

        self.assertRegex(
            styles,
            r"\.bars-and-notes\s*\{[^}]*grid-template-columns:\s*repeat\(4,\s*minmax\(0,\s*1fr\)\)\s+minmax\(",
        )
        mobile = styles[styles.index("@media (max-width: 699px)") :]
        self.assertNotRegex(mobile, r"\.bars-and-notes\s*\{[^}]*grid-template-columns:\s*1fr\s*;")

    def test_shell_supports_one_two_four_columns_with_safe_responsive_fallbacks(self):
        styles = (ROOT / "src" / "styles.css").read_text(encoding="utf-8")

        self.assertRegex(styles, r"\.song-header\s*\{[^}]*position:\s*sticky;")
        self.assertRegex(styles, r"body\.layout-columns-1 \.sections\s*\{[^}]*column-count:\s*1;")
        self.assertRegex(styles, r"body\.layout-columns-2 \.sections\s*\{[^}]*column-count:\s*2;")
        self.assertRegex(styles, r"body\.layout-columns-4 \.sections\s*\{[^}]*column-count:\s*4;")
        mobile = styles[styles.index("@media (max-width: 699px)") :]
        self.assertRegex(mobile, r"\.sections\s*\{[^}]*column-count:\s*1;")

        script = (ROOT / "src" / "script.js").read_text(encoding="utf-8")
        self.assertIn('savePreference("columns", columns)', script)
        self.assertIn('body.dataset.renderedColumns', script)
        self.assertIn('matchMedia("(min-width: 1200px)")', script)

    def test_song_map_tracks_an_accessible_active_chart_target(self):
        script = (ROOT / "src" / "script.js").read_text(encoding="utf-8")

        self.assertIn('aria-current', script)
        self.assertIn('updateActiveMapTarget', script)
        self.assertIn('songMap.hidden = song.type !== "chart"', script)

    def test_palette_state_and_section_color_link_render_in_split_and_portable_viewers(self):
        split_html = (ROOT / "src" / "index.html").read_text(encoding="utf-8")
        script = (ROOT / "src" / "script.js").read_text(encoding="utf-8")
        styles = (ROOT / "src" / "styles.css").read_text(encoding="utf-8")
        portable = (ROOT / "setlist-viewer-portable.html").read_text(encoding="utf-8")

        for viewer, html in (("split", split_html), ("portable", portable)):
            with self.subTest(viewer=viewer):
                self.assertRegex(
                    html,
                    r'id="palette-toggle"[^>]*aria-pressed="false"[^>]*'
                    r'aria-label="Section colors: Strong\. Use pastel Section colors"'
                    r'[^>]*>Strong</button>',
                )
                self.assertRegex(
                    html,
                    r'id="theme-toggle"[^>]*aria-pressed="false"[^>]*'
                    r'aria-label="Theme: Light\. Use dark mode"[^>]*>Light</button>',
                )

        self.assertIn('const paletteName = pastel ? "Pastel" : "Strong"', script)
        self.assertIn('"Section colors: " + paletteName', script)
        self.assertIn('if (!["strong", "pastel"].includes(palette))', script)
        self.assertRegex(
            styles,
            r'\.map-chip\.is-active\s*\{[^}]*background:\s*var\(--section-color\);',
        )
        self.assertRegex(
            styles,
            r'\.section-heading\s*\{[^}]*background:\s*var\(--section-color\);',
        )
        self.assertRegex(
            styles,
            r'grid-template-columns:\s*28px minmax\(34px, auto\) 28px '
            r'minmax\(64px, 1fr\) 44px 44px;',
        )

    def test_legacy_songs_render_a_summary_without_chart_rows(self):
        script = (ROOT / "src" / "script.js").read_text(encoding="utf-8")

        self.assertIn('sectionsElement.classList.add("legacy-sections")', script)
        self.assertIn('sectionsElement.setAttribute("aria-label", "Legacy Section summary")', script)
        legacy_renderer = script[
            script.index("function renderLegacySong") : script.index("const contentRenderers")
        ]
        self.assertNotIn("renderChartRow", legacy_renderer)

    def test_every_canonical_legacy_section_type_has_a_display_code(self):
        script = (ROOT / "src" / "script.js").read_text(encoding="utf-8")

        self.assertIn('flow: "FL"', script)
        self.assertIn('medley: "MD"', script)


if __name__ == "__main__":
    unittest.main()
