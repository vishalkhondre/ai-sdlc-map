"""Reference pages in the citation gate and the generator (Core plan, order of work step 1)."""
import contextlib
import importlib.util
import io
import re
import shutil
import sys
import tempfile
import unittest
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]
PAGE = """---
id: harness-engineering
type: concept
band: core
map_box: Harness engineering
title: Harness engineering
summary: The discipline of designing what a coding agent can read and do.
key_terms: [{terms}]
sources: [bockeler-harness]
related: [harness-engineering]
review_record: content/reviews/r.md
---

## Definition

{body}
"""


def page_text(terms, body, **meta):
    text = PAGE.format(terms=terms, body=body)
    for field, value in meta.items():
        text = "\n".join(f"{field}: {value}" if line.startswith(f"{field}:") else line for line in text.split("\n"))
    return text


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def drop_references_only_real_pages_cite(content: Path) -> None:
    """Without the real pages, the references only they cite would be dead; drop them from the copy."""
    cited = set()
    for page in (ROOT / "content/pages").rglob("*.md"):
        cited |= set(re.findall(r"\[\^([a-z0-9\-]+)\]", page.read_text(encoding="utf-8")))
    elsewhere = (content / "glossary.yml").read_text(encoding="utf-8") + (ROOT / "scripts/outdated_terms.yml").read_text(encoding="utf-8")
    elsewhere += "".join(p.read_text(encoding="utf-8") for p in (content / "diagrams/svg").glob("*.svg"))
    path = content / "references.yml"
    refs = yaml.safe_load(path.read_text(encoding="utf-8"))
    kept = {k: v for k, v in refs.items() if k not in cited or re.search(rf"(?<![\w-]){re.escape(k)}(?![\w-])", elsewhere)}
    path.write_text(yaml.safe_dump(kept, allow_unicode=True, sort_keys=False), encoding="utf-8")


class GateReadsPages(unittest.TestCase):
    def run_gate(self, terms, body, **meta):
        with tempfile.TemporaryDirectory() as temporary:
            gate = load("citation_gate", ROOT / "scripts/check_citations.py")
            gate.CONTENT = Path(temporary) / "content"
            # the real content without its pages, so the fixture is the only page
            shutil.copytree(ROOT / "content", gate.CONTENT, ignore=lambda d, names: ["pages"] if Path(d) == ROOT / "content" else [])
            drop_references_only_real_pages_cite(gate.CONTENT)
            (gate.CONTENT / "pages/core").mkdir(parents=True, exist_ok=True)
            (gate.CONTENT / "pages/core/harness-engineering.md").write_text(page_text(terms, body, **meta), encoding="utf-8")
            with contextlib.redirect_stdout(io.StringIO()) as out:
                result = gate.main()
            return result, out.getvalue()

    def test_a_page_that_cites_its_terms_passes_and_counts(self):
        result, out = self.run_gate("harness", "Everything in an agent except the model.[^bockeler-harness]")
        self.assertEqual(result, 0, out)
        self.assertIn("1 pages", out)

    def test_a_page_using_a_borrowed_term_must_cite_its_source(self):
        result, out = self.run_gate("harness", "Everything in an agent except the model.")
        self.assertEqual(result, 1)
        self.assertIn("harness-engineering: uses 'Harness'", out)

    def test_unknown_citations_and_keep_out_names_in_pages_fail(self):
        result, out = self.run_gate("", "A claim.[^no-such-key] Built with Copilot.")
        self.assertEqual(result, 1)
        self.assertIn("[^no-such-key]", out)
        self.assertIn("'Copilot' is on the keep-out list", out)

    def test_a_footnote_key_that_is_not_a_reference_key_fails(self):
        result, out = self.run_gate("harness", "A claim.[^bockeler-harness] Another.[^Bockeler_Missing] More.[^Fowler 2024]")
        self.assertEqual(result, 1)
        self.assertIn("[^Bockeler_Missing] is not a reference key", out)
        self.assertIn("[^Fowler 2024] is not a reference key", out)

    def test_a_borrowed_term_in_prose_needs_its_source_even_if_undeclared(self):
        result, out = self.run_gate("", "Checks close the feedback path for the agent.")
        self.assertEqual(result, 1)
        self.assertIn("uses 'Feedback path'", out)

    def test_a_link_target_is_not_a_use_of_a_term(self):
        result, out = self.run_gate("harness", "The model.[^bockeler-harness] See [the checks](validators.html) and [the entry](glossary.html#validator).")
        self.assertEqual(result, 0, out)

    def test_keep_out_names_in_the_title_and_product_names_anywhere_fail(self):
        result, out = self.run_gate("harness", "The model.[^bockeler-harness] Built on GitHub Actions.",
                                    title="Harness engineering with Copilot")
        self.assertEqual(result, 1)
        self.assertIn("title, summary or map box: 'Copilot'", out)
        self.assertIn("'GitHub' is a product name", out)

    def test_citations_inside_code_fences_do_not_count(self):
        result, out = self.run_gate("harness", "The model.\n\n```\nexample[^bockeler-harness]\n```\n")
        self.assertEqual(result, 1)
        self.assertIn("never cites bockeler-harness", out)

    def test_an_outdated_term_on_a_page_fails(self):
        with tempfile.TemporaryDirectory() as temporary:
            gate = load("citation_gate_terms", ROOT / "scripts/check_citations.py")
            pages = Path(temporary) / "content/pages/core"
            pages.mkdir(parents=True)
            (pages / "harness-engineering.md").write_text(page_text("", "Plan each program increment."), encoding="utf-8")
            found = " ".join(gate.check_outdated_terms(Path(temporary) / "content"))
            self.assertIn("pages/core/harness-engineering.md", found)
            self.assertIn("Planning Interval", found)


class GeneratorRendersPages(unittest.TestCase):
    def test_render_page_carries_title_breadcrumb_and_citations(self):
        generate = load("site_generate", ROOT / "site/generate.py")
        import check_pages
        meta, body = check_pages.split_page(PAGE.format(terms="harness", body="Everything except the model.[^bockeler-harness]"))
        pg = {**meta, "body": body, "href": "harness-engineering.html"}
        generate.PAGES = {"core": [pg]}
        html = generate.render_page(pg)
        self.assertIn("<h1>Harness engineering</h1>", html)
        self.assertIn('<span aria-current="page">Harness engineering</span>', html)
        self.assertIn("martinfowler.com/articles/harness-engineering.html", html)
        page = generate.docs_page(html, "harness-engineering.html")
        self.assertIn('class="onpage"', page)


if __name__ == "__main__":
    sys.path.insert(0, str(ROOT / "scripts"))
    unittest.main()
