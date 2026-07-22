import json
import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


EXPECTED_SONGS = [
    ("jesus", "Jesus", "113 BPM", "A", "Matthew Morales", "Piano intro. Keyboard lines during the intro.", ["Intro", "Intro", "Verse", "Chorus", "Turnaround", "Verse", "Chorus", "Turnaround", "Bridge", "Bridge", "Bridge", "Outro"]),
    ("el-canto-de-redencion", "El Canto de Redencion", "128 BPM", "D", "Jhonny Rez", "Percussion intro. Electric guitar comes in right after.", ["Intro", "Verse", "Chorus", "Turnaround", "Verse", "Verse", "Chorus", "Chorus", "Instrumental", "Instrumental", "Bridge", "Bridge", "Bridge", "Bridge", "Chorus", "Chorus", "Tag", "Tag", "Instrumental", "Outro"]),
    ("from-the-throne-of-god", "From the Throne of God", "133 BPM", "D-flat", "Marya Adedimeji", "Brass intro. Bass solo before the bridge section.", ["Intro", "Verse", "Chorus", "Verse", "Tag", "Chorus", "Chorus", "Post-Chorus", "Chorus", "Instrumental", "Bridge", "Bridge", "Bridge", "Bridge 2", "Bridge 2", "Chorus", "Chorus", "Post-Chorus", "Chorus", "Outro"]),
    ("it-was-your-grace", "It Was Your Grace", "146 BPM", "A", "Waleska Morales", "Brass intro. Full-band hits on Verse 2.", ["Intro", "Verse", "Verse", "Pre-Chorus", "Pre-Chorus", "Chorus", "Chorus", "Instrumental", "Verse 2", "Verse 2", "Pre-Chorus", "Pre-Chorus", "Chorus", "Chorus", "Instrumental", "Bridge", "Bridge", "Bridge", "Bridge", "Chorus", "Chorus", "Chorus", "Bridge", "Bridge", "Outro"]),
    ("holy-fragance", "Holy Fragance", "114 BPM", "D", "Paloma Ramos", "Eg / keys intro", ["Intro", "Verse", "Pre-Chorus", "Chorus", "Chorus", "Turnaround", "Verse", "Pre-Chorus", "Pre-Chorus", "Chorus", "Chorus", "Instrumental", "Bridge", "Bridge", "Bridge 2", "Bridge 2", "Tag", "Chorus", "Chorus", "Bridge", "Bridge", "Tag", "Chorus"]),
    ("boast-in-the-lord", "Boast in the Lord", "96 BPM", "A", "Nick Torres", "Drum intro.", ["Intro", "Verse", "Verse", "Tag", "Chorus", "Instrumental", "Verse", "Tag", "Chorus", "Instrumental", "Bridge", "Bridge", "Bridge", "Chorus", "Tag", "Tag", "Chorus", "Bridge", "Chorus"]),
    ("covers-all-the-earth", "Covers All the Earth", "150 BPM", "D", "Genock", "No additional detail shown in the sheet.", ["Intro", "Verse", "Chorus", "Turnaround", "Verse", "Tag", "Chorus", "Instrumental", "Bridge", "Bridge", "Tag", "Chorus", "Chorus", "Tag", "Outro"]),
    ("when-i-think-about-the-lord", "When I Think About the Lord", "BPM: Not shown", "D / E", "Josh / Marya", "Verse 1 is led by Josh. Verse 2 and onward are led by Marya.", ["Flow"]),
    ("vuelve-mi-corazon", "Vuelve Mi Corazon", "103 BPM", "G", "Genock", "No additional detail shown in the sheet.", ["Intro", "Verse", "Verse 2", "Chorus", "Turnaround", "Verse", "Verse", "Chorus", "Chorus", "Post-Chorus", "Turnaround", "Bridge", "Bridge", "Bridge", "Tag", "Chorus", "Post-Chorus", "Outro"]),
    ("accion-de-gracia", "Accion de Gracia", "110 BPM", "F", "Miel San Marcos", "No additional detail shown in the sheet.", ["Intro", "Verse", "Verse 2", "Pre-Chorus", "Chorus", "Turnaround", "Verse", "Pre-Chorus", "Chorus", "Chorus", "Turnaround", "Bridge", "Bridge", "Chorus", "Chorus", "Outro"]),
    ("avivanos-regocijate-la-alegria", "Avivanos - Regocijate - La Alegria", "155 BPM", "C / G / B-flat / E-flat", "Miel San Marcos", "No additional detail shown in the sheet.", ["Medley"]),
]


def load_song_data():
    source = (ROOT / "src" / "song-data.js").read_text(encoding="utf-8")
    match = re.fullmatch(r"window\.SETLIST_SONGS = (.*);\n", source, re.DOTALL)
    if not match:
        raise AssertionError("song-data.js must contain one JSON-compatible assignment")
    return json.loads(match.group(1))


class LegacySongRegressionTests(unittest.TestCase):
    def test_all_legacy_content_and_catalog_order_are_unchanged(self):
        actual = [
            (
                song["id"],
                song["title"],
                song["tempo"],
                song["key"],
                song["leadVocal"],
                song["details"],
                [section["name"] for section in song["sections"]],
            )
            for song in load_song_data()
        ]
        self.assertEqual(EXPECTED_SONGS, actual)

    def test_every_entry_is_explicitly_legacy(self):
        songs = load_song_data()
        self.assertEqual(11, len(songs))
        self.assertTrue(all(song["type"] == "legacy" for song in songs))

    def test_split_viewer_loads_classic_data_before_renderer(self):
        html = (ROOT / "src" / "index.html").read_text(encoding="utf-8")
        self.assertNotIn('<article class="song">', html)
        self.assertRegex(
            html,
            r'<script src="chart-data\.js"></script>\s*<script src="script\.js"></script>',
        )
        self.assertNotIn('type="module"', html)
        self.assertNotIn("fetch(", (ROOT / "src" / "script.js").read_text(encoding="utf-8"))

    def test_generated_portable_viewer_keeps_visible_legacy_labels(self):
        html = (ROOT / "setlist-viewer-portable.html").read_text(encoding="utf-8")
        self.assertIn('id="legacy-badge" hidden>Legacy</span>', html)
        self.assertIn('legacyBadge.hidden = song.type !== "legacy"', html)
        self.assertIn('song.title + (song.type === "legacy" ? " — Legacy" : "")', html)

    def test_section_band_heading_is_the_single_legacy_summary_label(self):
        script = (ROOT / "src" / "script.js").read_text(encoding="utf-8")

        self.assertIn('"section-name", section.name', script)
        self.assertNotIn('"legacy-summary", section.name', script)


if __name__ == "__main__":
    unittest.main()
