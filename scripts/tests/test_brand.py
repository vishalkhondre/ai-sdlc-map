"""Brand tokens and contrast (D-021). Run: python -m unittest discover -s scripts/tests -v

The tokens in site/assets/style.css must equal the ones recorded in D-021, in both themes, and
every text pair the site uses must reach WCAG AA (4.5:1); the accent colours are for non-text
marks and must reach 3:1 against the backgrounds they sit on. The browser checks run axe on the
rendered pages as well, which catches any pair this list misses.
"""
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CSS = (ROOT / "site/assets/style.css").read_text(encoding="utf-8")

LIGHT = {"ground": "#f6f8f8", "surface": "#ffffff", "ink": "#15232b", "body": "#34434b", "muted": "#5b6b72",
         "line": "#d8e1e1", "primary": "#0b6e69", "on-primary": "#ffffff", "primary-tint": "#e2f1ef",
         "link": "#0b6e69", "accent": "#b7791f", "accent-tint": "#fbf1df", "accent-text": "#7a4e0f"}
DARK = {"ground": "#0f1a1d", "surface": "#142225", "ink": "#e4eeed", "body": "#c3d0cf", "muted": "#8fa3a3",
        "line": "#243639", "primary": "#4fc1b9", "on-primary": "#07201e", "primary-tint": "#15363a",
        "link": "#6fd3cb", "accent": "#e0a84a", "accent-tint": "#2e2718", "accent-text": "#f0c47a"}

TEXT_ON = ["ground", "surface", "primary-tint"]          # backgrounds text sits on
TEXT = ["ink", "body", "muted", "link", "primary"]       # text colours
PAIRS = ([(t, b) for t in TEXT for b in TEXT_ON]
         + [("accent-text", "accent-tint"), ("accent-text", "ground"), ("accent-text", "surface"),
            ("body", "accent-tint"), ("ink", "accent-tint"),
            ("on-primary", "primary"), ("ground", "accent-text"), ("ground", "body"), ("body", "line")])
MARKS = [("accent", "ground"), ("accent", "surface"), ("primary", "ground"), ("primary", "surface")]


def luminance(hex_colour):
    channels = [int(hex_colour[i:i + 2], 16) / 255 for i in (1, 3, 5)]
    lin = [c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4 for c in channels]
    return 0.2126 * lin[0] + 0.7152 * lin[1] + 0.0722 * lin[2]


def contrast(a, b):
    la, lb = sorted((luminance(a), luminance(b)), reverse=True)
    return (la + 0.05) / (lb + 0.05)


def block(selector):
    m = re.search(re.escape(selector) + r"(.*?)\}", CSS, re.S)
    return dict(re.findall(r"--brand-([a-z-]+):\s*(#[0-9a-f]{6})", m.group(1))) if m else {}


class Brand(unittest.TestCase):
    def test_tokens_equal_the_recorded_decision(self):
        record = (ROOT / "project/DECISIONS.md").read_text(encoding="utf-8").split("## D-021", 1)[1].split("\n## ", 1)[0]
        for value in list(LIGHT.values()) + list(DARK.values()):
            self.assertIn(value, record)
        self.assertEqual(block(":root {"), LIGHT)
        self.assertEqual(block(':root:not([data-theme="light"]) {'), DARK)
        self.assertEqual(block(':root[data-theme="dark"] {'), DARK)

    def test_text_pairs_reach_aa(self):
        for name, theme in (("light", LIGHT), ("dark", DARK)):
            for fg, bg in PAIRS:
                with self.subTest(theme=name, pair=(fg, bg)):
                    self.assertGreaterEqual(round(contrast(theme[fg], theme[bg]), 2), 4.5)

    def test_accent_marks_reach_3_to_1(self):
        for name, theme in (("light", LIGHT), ("dark", DARK)):
            for fg, bg in MARKS:
                with self.subTest(theme=name, pair=(fg, bg)):
                    self.assertGreaterEqual(round(contrast(theme[fg], theme[bg]), 2), 3.0)

    def test_fonts_are_bundled_and_licensed(self):
        fonts = ROOT / "site/assets/fonts"
        for url in re.findall(r'url\("(fonts/[^"]+)"\)', CSS):
            self.assertTrue((ROOT / "site/assets" / url).is_file(), url)
        self.assertTrue((fonts / "LICENSE-atkinson-hyperlegible.txt").is_file())
        self.assertTrue((fonts / "LICENSE-ibm-plex-mono.txt").is_file())
        self.assertNotRegex(CSS, r"fonts\.googleapis|@import\s+url\(\s*['\"]?https?:")


if __name__ == "__main__":
    unittest.main()
