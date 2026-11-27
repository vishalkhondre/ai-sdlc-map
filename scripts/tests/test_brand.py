"""Brand tokens and contrast (D-031, which supersedes D-021). Run: python -m unittest discover -s scripts/tests -v

The tokens in site/assets/style.css must equal the ones recorded in D-031, in both themes, and
every text pair the site uses must reach WCAG AA (4.5:1); the accent colours are for non-text
marks and must reach 3:1 against the backgrounds they sit on. The browser checks run axe on the
rendered pages as well, which catches any pair this list misses.
"""
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CSS = (ROOT / "site/assets/style.css").read_text(encoding="utf-8")

LIGHT = {"ground": "#fafafb", "surface": "#ffffff", "ink": "#18181b", "body": "#3f3f46", "muted": "#6b6b75",
         "line": "#e4e4e7", "primary": "#3b55d9", "on-primary": "#ffffff", "primary-tint": "#eef1fd",
         "link": "#3b55d9", "accent": "#b57a1e", "accent-tint": "#fdf6e9", "accent-text": "#7a4e0e"}
DARK = {"ground": "#0f0f12", "surface": "#17171b", "ink": "#f4f4f5", "body": "#d4d4d8", "muted": "#a1a1aa",
        "line": "#2a2a30", "primary": "#8b9cf4", "on-primary": "#0f0f12", "primary-tint": "#1c2033",
        "link": "#a3b1f7", "accent": "#e0a84a", "accent-tint": "#2b2416", "accent-text": "#f0c47a"}

def mix(a, b, share_a):
    """color-mix(in srgb, a share_a, b): the neutral tint --bg-3 is line mixed into surface."""
    ca = [int(a[i:i + 2], 16) for i in (1, 3, 5)]
    cb = [int(b[i:i + 2], 16) for i in (1, 3, 5)]
    return "#" + "".join(f"{round(x * share_a + y * (1 - share_a)):02x}" for x, y in zip(ca, cb))


for _theme in (LIGHT, DARK):
    _theme["neutral-tint"] = mix(_theme["line"], _theme["surface"], 0.45)

TEXT_ON = ["ground", "surface", "primary-tint", "neutral-tint"]  # backgrounds text sits on
TEXT = ["ink", "body", "muted", "link", "primary"]       # text colours
PAIRS = ([(t, b) for t in TEXT for b in TEXT_ON]
         + [("accent-text", "accent-tint"), ("accent-text", "ground"), ("accent-text", "surface"),
            ("body", "accent-tint"), ("ink", "accent-tint"), ("muted", "accent-tint"), ("link", "accent-tint"),
            ("on-primary", "primary"), ("ground", "accent-text"), ("ground", "body"), ("body", "line")])
MARKS = [("accent", "ground"), ("accent", "surface"), ("accent", "accent-tint"), ("primary", "ground"),
         ("primary", "surface"), ("primary", "neutral-tint")]
NAMES = {"ground": "ground", "surface": "surface", "ink": "ink", "body": "body text", "muted": "muted", "line": "line",
         "primary": "primary", "on-primary": "text on it", "primary-tint": "primary tint", "link": "link",
         "accent": "accent", "accent-tint": "accent tint", "accent-text": "accent text"}


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
        record = (ROOT / "project/DECISIONS.md").read_text(encoding="utf-8").split("## D-031", 1)[1].split("\n## ", 1)[0]
        light, dark = record.split("Dark tokens:", 1)
        for text, theme in ((light, LIGHT), (dark, DARK)):
            recorded = {}
            for label, value in re.findall(r"([a-z][a-z\s]*?)(?:\s+teal|\s+amber)?\s+`(#[0-9a-f]{6})`", text.split("Indigo marks", 1)[0]):
                recorded[" ".join(label.split())] = value
            for name, label in NAMES.items():
                self.assertEqual(recorded.get(label), theme[name], (name, label))
        base = {k: v for k, v in LIGHT.items() if k != "neutral-tint"}
        base_dark = {k: v for k, v in DARK.items() if k != "neutral-tint"}
        self.assertEqual(block(":root {"), base)
        self.assertEqual(block(':root:not([data-theme="light"]) {'), base_dark)
        self.assertEqual(block(':root[data-theme="dark"] {'), base_dark)

    def test_text_pairs_reach_aa(self):
        for name, theme in (("light", LIGHT), ("dark", DARK)):
            for fg, bg in PAIRS:
                with self.subTest(theme=name, pair=(fg, bg)):
                    self.assertGreaterEqual(contrast(theme[fg], theme[bg]), 4.5)

    def test_accent_marks_reach_3_to_1(self):
        for name, theme in (("light", LIGHT), ("dark", DARK)):
            for fg, bg in MARKS:
                with self.subTest(theme=name, pair=(fg, bg)):
                    self.assertGreaterEqual(contrast(theme[fg], theme[bg]), 3.0)

    def test_bundled_fonts_cover_every_character_the_site_uses(self):
        import subprocess
        import sys
        from fontTools.ttLib import TTFont
        subprocess.run([sys.executable, str(ROOT / "site/generate.py")], check=True, capture_output=True)
        covered = set()
        for font in (ROOT / "site/assets/fonts").glob("*.woff2"):
            covered |= set(TTFont(font).getBestCmap())
        used = set()
        for path in list((ROOT / "site").glob("*.html")) + [ROOT / "site/assets/app.js"]:
            text = re.sub(r"<(script|style|svg)\b.*?</\1>", " ", path.read_text(encoding="utf-8"), flags=re.S)
            used |= {ord(c) for c in text if ord(c) > 0x7e}
        used -= {0x2922}  # the zoom button's character is drawn as an icon in CSS
        self.assertEqual(sorted(hex(c) for c in used - covered), [])

    def test_fonts_are_bundled_and_licensed(self):
        fonts = ROOT / "site/assets/fonts"
        for url in re.findall(r'url\("(fonts/[^"]+)"\)', CSS):
            self.assertTrue((ROOT / "site/assets" / url).is_file(), url)
        self.assertTrue((fonts / "LICENSE-inter.txt").is_file())
        self.assertTrue((fonts / "LICENSE-jetbrains-mono.txt").is_file())
        self.assertTrue((fonts / "LICENSE-ibm-plex-mono.txt").is_file())
        self.assertNotRegex(CSS, r"fonts\.googleapis|@import\s+url\(\s*['\"]?https?:")


if __name__ == "__main__":
    unittest.main()
