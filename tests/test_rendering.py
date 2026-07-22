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
        self.assertIn('id="song-directory"', html)
        self.assertIn('id="song-title"', html)
        self.assertNotIn('class="hero"', html)
        self.assertNotIn("prototype-warning", html)

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

        for control in ("melody-toggle", "palette-toggle", "theme-toggle"):
            with self.subTest(control=control):
                self.assertRegex(
                    html,
                    rf'id="{control}"[^>]*aria-pressed="(?:true|false)"[^>]*aria-label="[^"]+"[^>]*title="[^"]+"',
                )

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
