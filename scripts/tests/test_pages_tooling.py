"""Reference pages in the citation gate and the generator (Core plan, order of work step 1)."""
import contextlib
import importlib.util
import io
import shutil
import sys
import tempfile
import unittest
from pathlib import Path

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


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class GateReadsPages(unittest.TestCase):
    def run_gate(self, terms, body):
        with tempfile.TemporaryDirectory() as temporary:
            gate = load("citation_gate", ROOT / "scripts/check_citations.py")
            gate.CONTENT = Path(temporary) / "content"
            shutil.copytree(ROOT / "content", gate.CONTENT)
            (gate.CONTENT / "pages/core").mkdir(parents=True, exist_ok=True)
            (gate.CONTENT / "pages/core/harness-engineering.md").write_text(PAGE.format(terms=terms, body=body), encoding="utf-8")
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
