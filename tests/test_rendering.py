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

    def test_shell_is_sticky_two_column_capable_and_phone_single_column(self):
        styles = (ROOT / "src" / "styles.css").read_text(encoding="utf-8")

        self.assertRegex(styles, r"\.song-header\s*\{[^}]*position:\s*sticky;")
        desktop = styles[styles.index("@media (min-width: 700px)") :]
        self.assertRegex(desktop, r"\.sections\s*\{[^}]*column-count:\s*2;")
        mobile = styles[styles.index("@media (max-width: 699px)") :]
        self.assertRegex(mobile, r"\.sections\s*\{[^}]*column-count:\s*1;")

    def test_every_canonical_legacy_section_type_has_a_display_code(self):
        script = (ROOT / "src" / "script.js").read_text(encoding="utf-8")

        self.assertIn('flow: "FL"', script)
        self.assertIn('medley: "MD"', script)


if __name__ == "__main__":
    unittest.main()
