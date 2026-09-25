"""Build-time checks for the generated site. Run: python -m unittest discover -s scripts/tests -v"""
import json
import re
import subprocess
import sys
import unittest
from collections import Counter
from pathlib import Path
from urllib.parse import unquote, urlsplit

import html5lib
import yaml

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import denylist  # noqa: E402

ROOT = Path(__file__).resolve().parents[2]
SITE = ROOT / "site"
CONTENT = ROOT / "content"


class Generated(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        subprocess.run([sys.executable, str(SITE / "generate.py")], check=True, capture_output=True)
        cls.toc = yaml.safe_load((CONTENT / "toc.yml").read_text(encoding="utf-8"))

    def test_expected_pages_exist(self):
        for name in ("index.html", "workflow-catalog.html", "glossary.html", "references.html", "404.html"):
            self.assertTrue((SITE / name).exists(), name)

    def test_series_links_point_at_the_series_site(self):
        series = self.toc["series"]["url"].rstrip("/")
        home = (SITE / "index.html").read_text(encoding="utf-8")
        for part in self.toc["series"]["parts"]:
            self.assertIn(f'href="{series}/{part["slug"]}.html"', home, part["id"])
        for page in SITE.glob("*.html"):
            source = page.read_text(encoding="utf-8")
            for part in self.toc["series"]["parts"]:
                self.assertNotIn(f'href="{part["slug"]}.html"', source, f"{page.name}: relative link to {part['slug']}")

    def test_internal_links_resolve(self):
        pages = list(SITE.glob("*.html"))
        ids_by_page = {p.name: set(re.findall(r'id="([^"]+)"', p.read_text(encoding="utf-8"))) for p in pages}
        catalog = yaml.safe_load((CONTENT / "workflows/catalog.yml").read_text(encoding="utf-8"))
        ids_by_page["workflow-catalog.html"].update(w["id"] for w in catalog["workflows"])
        for p in pages:
            for href in re.findall(r'href="([^"]+)"', p.read_text(encoding="utf-8")):
                url = urlsplit(href)
                if url.scheme or url.netloc or (url.path and not url.path.endswith(".html")):
                    continue
                target = Path(url.path).name if url.path else p.name
                self.assertIn(target, ids_by_page, f"{p.name} -> {href}")
                if url.fragment:
                    self.assertIn(unquote(url.fragment), ids_by_page[target], f"{p.name} -> {href}")

    def test_home_page_parses_and_carries_the_map(self):
        parser = html5lib.HTMLParser(namespaceHTMLElements=False)
        doc = parser.parse((SITE / "index.html").read_text(encoding="utf-8"))
        figures = [el.get("data-diagram") for el in doc.iter() if el.tag == "figure"]
        self.assertEqual(figures, ["ai-sdlc-map", "ai-sdlc-adoption-path"])
        self.assertFalse([error for error in parser.errors if error[1] == "unexpected-start-tag-implies-end-tag"])

    def test_diagram_ids_and_references_are_unique(self):
        for page in SITE.glob("*.html"):
            source = page.read_text(encoding="utf-8")
            counts = Counter(re.findall(r'\bid="([^"]+)"', source))
            self.assertFalse({key: n for key, n in counts.items() if n > 1}, page.name)
            for svg in re.findall(r"<svg\b.*?</svg>", source, re.S):
                local_ids = set(re.findall(r'\bid="([^"]+)"', svg))
                for target in re.findall(r'url\(#([^)]+)\)', svg):
                    self.assertIn(target, local_ids, f"{page.name}: SVG reference {target}")
                for target in re.findall(r'aria-labelledby="([^"]+)"', svg):
                    self.assertIn(target, counts, f"{page.name}: SVG caption {target}")

    def test_diagrams_referenced_exist(self):
        for p in SITE.glob("*.html"):
            for did in re.findall(r'data-diagram="([^"]+)"', p.read_text(encoding="utf-8")):
                self.assertTrue((SITE / "diagrams" / f"{did}.svg").exists(), did)

    def test_no_keep_out_names_in_pages(self):
        banned = ["Cursor", "Copilot", "Lovable"]
        for p in list(SITE.glob("*.html")) + list(SITE.glob("*.txt")) + [SITE / "search-index.json"]:
            text = p.read_text(encoding="utf-8")
            for b in banned:
                self.assertNotRegex(text, rf"\b{b}\b", f"{p.name} contains {b}")
            self.assertEqual(denylist.matches(text), [], f"{p.name} contains a name on the deny-list")

    def test_no_deny_listed_name_in_any_tracked_file(self):
        files = subprocess.run(["git", "-C", str(ROOT), "ls-files"], capture_output=True, text=True, check=True).stdout.split()
        for name in files:
            try:
                text = (ROOT / name).read_text(encoding="utf-8")
            except (UnicodeDecodeError, FileNotFoundError):
                continue
            self.assertEqual(denylist.matches(text), [], f"{name} contains a name on the deny-list")

    def test_search_index_and_llms(self):
        idx = json.loads((SITE / "search-index.json").read_text(encoding="utf-8"))
        self.assertGreater(len(idx), 40)
        llms = (SITE / "llms.txt").read_text(encoding="utf-8")
        self.assertIn("AI SDLC on one page", llms)
        self.assertIn(self.toc["series"]["url"], llms)

    def test_catalog_data(self):
        cat = yaml.safe_load((CONTENT / "workflows" / "catalog.yml").read_text(encoding="utf-8"))
        ids = [w["id"] for w in cat["workflows"]]
        self.assertEqual(len(ids), len(set(ids)))
        phases = {p["key"] for p in cat["phases"]}
        for w in cat["workflows"]:
            self.assertIn(w["phase"], phases, w["id"])
            self.assertIn(w["maturity"], cat["maturity"], w["id"])
            for k in ("decision", "trigger", "agent", "checks", "people", "evidence"):
                self.assertTrue(w[k], f"{w['id']} missing {k}")
        for r in cat["traditional_map"]:
            for part in str(r["lands_in"]).split("/"):
                part = part.strip()
                if part.startswith("W"):
                    self.assertIn(part, ids, r["activity"])

    def test_citation_gate(self):
        res = subprocess.run([sys.executable, str(ROOT / "scripts" / "check_citations.py")], capture_output=True, text=True)
        self.assertEqual(res.returncode, 0, res.stdout + res.stderr)


if __name__ == "__main__":
    unittest.main()
