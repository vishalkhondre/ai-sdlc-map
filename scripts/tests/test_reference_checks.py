"""GR-2.5 access dates and the GR-5.3 outdated-terms list. Run: python -m unittest discover -s scripts/tests -v"""
import importlib.util
import tempfile
import unittest
from datetime import date
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]
spec = importlib.util.spec_from_file_location("citation_gate", ROOT / "scripts/check_citations.py")
gate = importlib.util.module_from_spec(spec)
spec.loader.exec_module(gate)


class AccessDates(unittest.TestCase):
    def ref(self, **fields):
        return {"k": {"title": "T", "url": "https://example.org/", **fields}}

    def full(self, **fields):
        return self.ref(author="A", **fields)

    def test_reference_without_accessed_fails(self):
        self.assertIn("no accessed date", " ".join(gate.check_reference_fields(self.ref())))

    def test_malformed_impossible_and_future_dates_fail(self):
        today = date(2026, 9, 25)
        self.assertTrue(gate.check_reference_fields(self.ref(accessed="25 Sep 2026"), today))
        self.assertIn("not a real date", " ".join(gate.check_reference_fields(self.ref(accessed="2026-02-30"), today)))
        self.assertIn("in the future", " ".join(gate.check_reference_fields(self.ref(accessed="2026-09-26"), today)))

    def test_complete_reference_passes_and_title_and_url_are_required(self):
        self.assertEqual(gate.check_reference_fields(self.full(accessed="2026-09-25"), date(2026, 9, 25)), [])
        broken = {"k": {"accessed": "2026-09-25"}}
        self.assertEqual(len(gate.check_reference_fields(broken, date(2026, 9, 25))), 3)
        self.assertIn("author or organisation", " ".join(gate.check_reference_fields(self.ref(accessed="2026-09-25"), date(2026, 9, 25))))

    def test_every_reference_in_the_repository_has_one(self):
        refs = yaml.safe_load((ROOT / "content/references.yml").read_text(encoding="utf-8"))
        self.assertEqual(gate.check_reference_fields(refs), [])


class OutdatedTerms(unittest.TestCase):
    def scan(self, files: dict[str, str]) -> list[str]:
        root = Path(tempfile.mkdtemp())
        for name, text in files.items():
            (root / name).parent.mkdir(parents=True, exist_ok=True)
            (root / name).write_text(text, encoding="utf-8")
        return gate.check_outdated_terms(root)

    def test_superseded_terms_fail_where_readers_see_them(self):
        files = {"glossary.yml": ("Each Program Increment ends with a demo.\n", "Planning Interval"),
                 "diagrams/svg/x.svg": ("<svg><text>the four key metrics</text></svg>\n", "five metrics"),
                 "pages/core/p.md": ("Track mean time to recovery.\n", "failed deployment recovery time"),
                 "pages/core/q.md": ("Watch the change failure rate.\n", "change fail rate")}
        for name, (text, replacement) in files.items():
            with self.subTest(name=name):
                found = self.scan({name: text})
                self.assertEqual(len(found), 1, found)
                self.assertIn(replacement, found[0])

    def test_ordinary_phrases_are_not_superseded_terms(self):
        self.assertEqual(self.scan({"pages/core/p.md": "The four key ideas. Time to restore a backup. "
                                                       "MTTR as mean time to repair a machine.\n"}), [])

    def test_history_and_quoted_titles_are_exempt(self):
        self.assertEqual(self.scan({"references.yml": 'title: "The four keys"\n', "CHANGELOG.md": "program increment\n",
                                    "reviews/r.md": "program increment\n"}), [])

    def test_current_terms_pass(self):
        self.assertEqual(self.scan({"glossary.yml": "PI planning each Planning Interval; failed deployment recovery time.\n"}), [])

    def test_every_listed_term_names_a_known_source(self):
        refs = yaml.safe_load((ROOT / "content/references.yml").read_text(encoding="utf-8"))
        for term in yaml.safe_load((ROOT / "scripts/outdated_terms.yml").read_text(encoding="utf-8")):
            self.assertIn(term["source"], refs, term["use"])


if __name__ == "__main__":
    unittest.main()
