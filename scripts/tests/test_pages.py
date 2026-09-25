"""Page templates and the page gate (GR-4.1, GR-3.2). Run: python -m unittest discover -s scripts/tests -v"""
import re
import shutil
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import check_pages  # noqa: E402

ROOT = Path(__file__).resolve().parents[2]
PROSE = ("The harness is everything around the model that a team designs on purpose: what the agent can read, "
         "what it may do, how its work is checked and when a person decides. ")


def approach_table() -> dict[str, list[str]]:
    text = (ROOT / "project/APPROACH.md").read_text(encoding="utf-8")
    table = text.split("## Page types and templates", 1)[1].split("\n## ", 1)[0]
    rows = {}
    for line in table.splitlines():
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) == 2 and "·" in cells[1]:
            rows[cells[0].lower().replace(" ", "-")] = [s.strip() for s in cells[1].split("·")]
    return rows


def page(sections: list[str], **meta) -> str:
    fields = {"id": "harness-engineering", "type": "concept", "band": "core", "map_box": "Harness engineering",
              "title": "Harness engineering", "summary": "The discipline of designing the agent's environment.",
              "key_terms": "[harness]", "sources": "[bockeler-harness]", "related": "[harness-engineering]",
              "review_record": "content/reviews/r.md", **meta}
    front = "\n".join(f"{k}: {v}" for k, v in fields.items() if v is not None)
    body = ""
    for s in sections:
        text = {"Related": "- [Harness engineering](harness-engineering.html)",
                "Sources": "Böckeler sets out the vocabulary.[^bockeler-harness]"}.get(s, PROSE)
        body += f"## {s}\n\n{text}\n\n"
    return f"---\n{front}\n---\n\n{body}"


class Templates(unittest.TestCase):
    def test_templates_match_the_approach_table(self):
        templates, problems = check_pages.load_templates()
        self.assertEqual(problems, [])
        self.assertEqual(templates, approach_table())

    def test_the_repository_passes(self):
        self.assertEqual(check_pages.check()[0], [])


class Pages(unittest.TestCase):
    def setUp(self):
        self.root = Path(tempfile.mkdtemp())
        shutil.copytree(ROOT / "templates", self.root / "templates")
        (self.root / "content/pages/core").mkdir(parents=True)
        (self.root / "content/reviews").mkdir()
        (self.root / "content/reviews/r.md").write_text("Verdict: ACCEPT\n", encoding="utf-8")
        shutil.copy(ROOT / "content/references.yml", self.root / "content/references.yml")
        shutil.copy(ROOT / "content/glossary.yml", self.root / "content/glossary.yml")
        self.concept = check_pages.load_templates()[0]["concept"]

    def run_on(self, text: str, name: str = "core/harness-engineering.md") -> list[str]:
        (self.root / "content/pages" / name).write_text(text, encoding="utf-8")
        return check_pages.check(self.root)[0]

    def test_complete_page_passes(self):
        self.assertEqual(self.run_on(page(self.concept)), [])

    def test_missing_or_reordered_sections_fail(self):
        self.assertIn("needs exactly", " ".join(self.run_on(page(self.concept[:-2] + ["Sources"]))))
        swapped = self.concept[:]
        swapped[0], swapped[1] = swapped[1], swapped[0]
        self.assertIn("needs exactly", " ".join(self.run_on(page(swapped))))

    def test_thin_section_and_leftover_guidance_fail(self):
        text = page(self.concept).replace(PROSE, "Short.", 1)
        self.assertIn("at least 25", " ".join(self.run_on(text)))
        text = page(self.concept).replace(PROSE, PROSE + "<!-- write this -->", 1)
        self.assertIn("guidance comment", " ".join(self.run_on(text)))

    def test_provisional_language_fails(self):
        for phrase in ("Coming soon.", "Details TBD.", "This section is a draft."):
            with self.subTest(phrase=phrase):
                self.assertIn("GR-3.2", " ".join(self.run_on(page(self.concept).replace(PROSE, PROSE + phrase, 1))))
        self.assertEqual(self.run_on(page(self.concept).replace(PROSE, PROSE + "The agent writes a draft plan. ", 1)), [])

    def test_metadata_is_checked(self):
        self.assertIn("missing or empty", " ".join(self.run_on(page(self.concept, summary=None))))
        self.assertIn("placeholder", " ".join(self.run_on(page(self.concept, title="<page title>"))))
        self.assertIn("unknown type", " ".join(self.run_on(page(self.concept, type="essay"))))
        self.assertIn("sits in", " ".join(self.run_on(page(self.concept, band="assurance"))))
        self.assertIn("does not match the file name", " ".join(self.run_on(page(self.concept, id="other"))))
        self.assertIn("not in content/references.yml", " ".join(self.run_on(page(self.concept, sources="[nope]"))))
        self.assertIn("not in content/glossary.yml", " ".join(self.run_on(page(self.concept, key_terms="[nope]"))))
        self.assertIn("does not exist", " ".join(self.run_on(page(self.concept, related="[nope]"))))
        self.assertIn("review record", " ".join(self.run_on(page(self.concept, review_record="content/reviews/x.md"))))

    def test_citation_must_be_listed_in_sources(self):
        text = page(self.concept, sources="[bockeler-harness]").replace(PROSE, PROSE + "See the sensors article.[^bockeler-sensors] ", 1)
        self.assertIn("does not list it under sources", " ".join(self.run_on(text)))


if __name__ == "__main__":
    unittest.main()
