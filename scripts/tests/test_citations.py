"""Regressions for the citation gate: canonical overrides and diagram text."""
import contextlib
import hashlib
import importlib.util
import io
import shutil
import subprocess
import tempfile
import unittest
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]


class Citations(unittest.TestCase):
    def test_sourceless_canonical_override_is_rejected(self):
        spec = importlib.util.spec_from_file_location("citation_gate", ROOT / "scripts/check_citations.py")
        gate = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(gate)
        with tempfile.TemporaryDirectory() as temporary:
            gate.CONTENT = Path(temporary) / "content"
            shutil.copytree(ROOT / "content", gate.CONTENT)
            add_chapter(gate.CONTENT, "Text.[^bockeler-harness]\n\n[^bockeler-harness]: This definition has no source URL.\n")
            with contextlib.redirect_stdout(io.StringIO()) as output:
                result = gate.main()
            self.assertEqual(result, 1)
            self.assertIn("cannot be redefined locally", output.getvalue())

    def test_generator_also_rejects_canonical_override(self):
        spec = importlib.util.spec_from_file_location("site_generator", ROOT / "site/generate.py")
        generator = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(generator)
        with self.assertRaisesRegex(SystemExit, "cannot be redefined"):
            generator.preprocess_markdown("Text.[^bockeler-harness]\n\n[^bockeler-harness]: No source.", "part-1")


def add_chapter(content: Path, text: str) -> None:
    """The site hosts no chapters yet; add one to a copied content/ so chapter checks can be exercised."""
    (content / "chapters").mkdir(exist_ok=True)
    (content / "chapters/zz-test.md").write_text(text, encoding="utf-8")
    toc_path = content / "toc.yml"
    toc = yaml.safe_load(toc_path.read_text(encoding="utf-8"))
    toc["chapters"] = [{"id": "zz-test", "number": 99, "slug": "zz-test", "file": "zz-test.md", "title": "Test"}]
    toc_path.write_text(yaml.safe_dump(toc, allow_unicode=True), encoding="utf-8")


def load_gate(temporary):
    spec = importlib.util.spec_from_file_location("citation_gate", ROOT / "scripts/check_citations.py")
    gate = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(gate)
    gate.CONTENT = Path(temporary) / "content"
    shutil.copytree(ROOT / "content", gate.CONTENT)
    return gate


def run(gate):
    with contextlib.redirect_stdout(io.StringIO()) as output:
        result = gate.main()
    return result, output.getvalue()


class DiagramText(unittest.TestCase):
    SVG = ('<svg xmlns="http://www.w3.org/2000/svg"{refs}><title>Example</title><desc>{desc}</desc>'
           '<text x="0" y="0">{text}</text></svg>')

    def write(self, gate, text="Work tracking", desc="A diagram.", refs="", credit="", credit_refs=""):
        attr = f' data-references="{refs}"' if refs else ""
        svg = self.SVG.format(refs=attr, desc=desc, text=text)
        if credit:
            svg = svg.replace("</svg>", f'<text class="credit" data-references="{credit_refs}">{credit}</text></svg>')
        (gate.CONTENT / "diagrams/svg/zz-test.svg").write_text(svg, encoding="utf-8")

    def test_keep_out_and_product_names_in_diagram_text_fail(self):
        with tempfile.TemporaryDirectory() as temporary:
            gate = load_gate(temporary)
            self.write(gate, text="Backlog in Jira / Confluence", desc="SDD with GitHub Spec Kit")
            result, output = run(gate)
            self.assertEqual(result, 1)
            for name in ("Jira", "Confluence", "GitHub", "Spec Kit"):
                self.assertIn(f"diagram zz-test: '{name}'", output)

    def test_neutral_diagram_passes_and_lowercase_urls_are_not_products(self):
        with tempfile.TemporaryDirectory() as temporary:
            gate = load_gate(temporary)
            self.write(gate, text="The AI SDLC Map · vishalkhondre.github.io/ai-sdlc-map")
            self.assertEqual(run(gate)[0], 0)

    def test_unknown_data_reference_fails(self):
        with tempfile.TemporaryDirectory() as temporary:
            gate = load_gate(temporary)
            self.write(gate, refs="bockeler-harness no-such-key")
            result, output = run(gate)
            self.assertEqual(result, 1)
            self.assertIn("data-references key 'no-such-key' is not in references.yml", output)

    def test_reference_cited_only_by_a_diagram_is_dead_without_it(self):
        with tempfile.TemporaryDirectory() as temporary:
            gate = load_gate(temporary)
            svg = gate.CONTENT / "diagrams/svg/ai-sdlc-map.svg"
            svg.write_text(svg.read_text(encoding="utf-8").replace(" dora-metrics", ""), encoding="utf-8")
            result, output = run(gate)
            self.assertEqual(result, 1)
            self.assertIn("'dora-metrics' is never cited", output)

    def test_credit_line_may_name_a_source_but_not_a_keep_out_name(self):
        with tempfile.TemporaryDirectory() as temporary:
            gate = load_gate(temporary)
            self.write(gate, text="Spec-driven development", credit="after GitHub Spec Kit", credit_refs="spec-kit")
            self.assertEqual(run(gate)[0], 0)
            self.write(gate, text="Spec-driven development", credit="after GitHub Spec Kit, tracked in Jira",
                       credit_refs="spec-kit")
            result, output = run(gate)
            self.assertEqual(result, 1)
            self.assertIn("credit line names 'Jira'", output)

    def test_standalone_diagram_must_credit_borrowed_terms(self):
        with tempfile.TemporaryDirectory() as temporary:
            gate = load_gate(temporary)
            self.write(gate, text="Suggested: 3 validators")
            result, output = run(gate)
            self.assertEqual(result, 1)
            self.assertIn("uses 'Validator' (adapted from bockeler-sensors) but no credit line names bockeler-sensors", output)
            self.write(gate, text="Suggested: 3 validators", credit="Validators: after Böckeler", credit_refs="bockeler-sensors")
            self.assertEqual(run(gate)[0], 0)

    def test_embedded_diagram_relies_on_its_chapter_for_credit(self):
        with tempfile.TemporaryDirectory() as temporary:
            gate = load_gate(temporary)
            self.write(gate, text="Suggested: 3 validators")
            add_chapter(gate.CONTENT, "![Test](diagram:zz-test)\n")
            self.assertEqual(run(gate)[0], 0)

    def test_map_generator_output_is_committed(self):
        spec = importlib.util.spec_from_file_location("build_map", ROOT / "content/diagrams/map/build_map.py")
        build_map = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(build_map)
        svg = ROOT / "content/diagrams/svg"
        self.assertEqual(build_map.page_map(), (svg / "ai-sdlc-map.svg").read_text(encoding="utf-8"))
        self.assertEqual(build_map.page_path(), (svg / "ai-sdlc-adoption-path.svg").read_text(encoding="utf-8"))


class Disconnected(unittest.TestCase):
    """D-019: nothing links to or names the earlier series. Test strings are assembled from parts so
    this file does not trip the check itself."""
    HOST = "vishalkhondre" + ".github.io/" + "ai-sdlc"
    REPO = "vishalkhondre/" + "ai-sdlc"
    TITLE = "Beyond " + "Faster Coding"

    def scan(self, files):
        with tempfile.TemporaryDirectory() as content_dir, tempfile.TemporaryDirectory() as temporary:
            gate = load_gate(content_dir)
            root = Path(temporary)
            subprocess.run(["git", "init", "-q", str(root)], check=True)
            for name, text in files.items():
                (root / name).parent.mkdir(parents=True, exist_ok=True)
                (root / name).write_text(text, encoding="utf-8")
            subprocess.run(["git", "-C", str(root), "add", "-A"], check=True)
            return gate.check_disconnected(root)

    def test_links_and_names_fail(self):
        found = self.scan({"README.md": f"See https://{self.HOST}/ and github.com/{self.REPO}.git\n",
                           "site/x.html": f"<p>{self.TITLE.upper()}</p> {self.HOST.upper()}\n",
                           "notes/é.md": f"{self.REPO}/blob/main/x\n"})
        self.assertEqual(len(found), 5)
        self.assertTrue(all("D-019" in f for f in found))

    def test_this_site_and_historical_reviews_pass(self):
        self.assertEqual(self.scan({"README.md": f"https://{self.HOST}-map/ and {self.REPO}-map\n",
                                    "project/A.md": "The Drive folder `ai-sdlc` and /home/user/ai-sdlc-map/\n",
                                    "content/reviews/old.md": f"{self.TITLE} {self.HOST}\n"}), [])

    def test_the_repository_passes(self):
        with tempfile.TemporaryDirectory() as temporary:
            self.assertEqual(load_gate(temporary).check_disconnected(), [])


class DenyList(unittest.TestCase):
    def test_deny_listed_name_in_content_fails_by_position_only(self):
        with tempfile.TemporaryDirectory() as temporary:
            gate = load_gate(temporary)
            fixture = "Zqfixturename"  # stands in for a real name, which must never appear in the repository
            hashes = gate.denylist.HASHES
            gate.denylist.HASHES = hashes | {hashlib.sha256((gate.denylist.SALT + fixture.lower()).encode()).hexdigest()}
            try:
                self.assertEqual(run(gate)[0], 0)
                glossary = gate.CONTENT / "glossary.yml"
                glossary.write_text(glossary.read_text(encoding="utf-8") + f"# note: {fixture}\n", encoding="utf-8")
                result, output = run(gate)
            finally:
                gate.denylist.HASHES = hashes
            self.assertEqual(result, 1)
            self.assertIn("content/glossary.yml:", output)
            self.assertIn("confidentiality deny-list", output)
            self.assertNotIn(fixture, output)

