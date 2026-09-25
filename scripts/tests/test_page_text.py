"""D-020: a layout change never changes what a page says. Run: python -m unittest discover -s scripts/tests

The snapshot holds each built page's main-content text (scripts/page_text.py). A change meant to
alter text (a content edition) refreshes it with `python scripts/page_text.py --write`, and the
diff of the snapshot shows the reviewer exactly what readers will see change.
"""
import json
import subprocess
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import page_text  # noqa: E402

ROOT = Path(__file__).resolve().parents[2]


class PageText(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        subprocess.run([sys.executable, str(ROOT / "site" / "generate.py")], check=True, capture_output=True)

    def test_every_page_says_what_the_snapshot_says(self):
        expected = json.loads(page_text.SNAPSHOT.read_text(encoding="utf-8"))
        actual = page_text.snapshot()
        self.assertEqual(sorted(actual), sorted(expected), "pages added or removed")
        for name in expected:
            with self.subTest(page=name):
                self.assertEqual(actual[name], expected[name], f"{name}: main-content text changed")

    def test_chrome_is_excluded_and_content_is_kept(self):
        html = ('<main><div class="crumbs">Home / X</div><nav data-chrome="pagenav">Previous Next</nav>'
                '<h1>Title</h1><p>Body <b>text</b>.</p><script>x()</script><nav class="routes"><h3>Route</h3></nav></main>')
        self.assertEqual(page_text.main_text(html), "Title Body text . Route")

    def test_data_drawn_by_javascript_and_text_alternatives_count(self):
        html = ('<main><img alt="A diagram"><script type="application/json">{"w": [{"name": "Intake"}], "n": 3}</script>'
                '<button aria-label="Close">×</button></main>')
        self.assertEqual(page_text.main_text(html), "A diagram Intake Close ×")

    def test_only_known_chrome_may_be_excluded(self):
        with self.assertRaises(ValueError):
            page_text.main_text('<main><div data-chrome="anything">Hidden text</div></main>')


if __name__ == "__main__":
    unittest.main()
