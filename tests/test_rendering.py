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

    def test_chart_renderer_exposes_complete_stage_reading_structure(self):
        script = (ROOT / "src" / "script.js").read_text(encoding="utf-8")

        for public_hook in (
            "chart-section",
            "chart-row",
            "bar-grid",
            "bar-slot",
            "empty-bar-slot",
            "beat-dots",
            "no-chord",
            "diamond-chord",
            "chord-suffix",
            "slash-bass",
            "row-notes",
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
            r"\.chart-row\s*\{[^}]*grid-template-columns:\s*minmax\(0,\s*1fr\)[^;]*;",
        )
        self.assertRegex(
            styles,
            r"\.bar-grid\s*\{[^}]*grid-template-columns:\s*repeat\(4,\s*minmax\(0,\s*1fr\)\)",
        )
        mobile = styles[styles.index("@media (max-width: 640px)") :]
        self.assertNotRegex(mobile, r"\.chart-row\s*\{[^}]*grid-template-columns:\s*1fr\s*;")


if __name__ == "__main__":
    unittest.main()
