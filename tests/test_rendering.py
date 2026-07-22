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
