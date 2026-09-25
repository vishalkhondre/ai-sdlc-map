"""Release notes and tag checks (D-016). Run: python -m unittest discover -s scripts/tests -v"""
import shutil
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import release_snapshot  # noqa: E402

ROOT = Path(__file__).resolve().parents[2]


def repo(version="1.3.0", changelog="## 1.3.0 — 2026-10-01\n\n- Core section.\n\n## 1.2.0\n\n- Rename.\n",
         sections='"1.3":\n  section: "Core"\n  pages: [index.html]\n') -> Path:
    root = Path(tempfile.mkdtemp())
    unittest.addModuleCleanup(shutil.rmtree, root, ignore_errors=True)
    (root / "content").mkdir()
    (root / "release").mkdir()
    (root / "content/VERSION").write_text(version + "\n", encoding="utf-8")
    (root / "content/CHANGELOG.md").write_text("# Changelog\n\n" + changelog, encoding="utf-8")
    (root / "release/sections.yml").write_text(sections, encoding="utf-8")
    return root


class ReleaseSnapshot(unittest.TestCase):
    def test_notes_carry_the_section_and_only_its_changelog_entry(self):
        text = release_snapshot.notes("v1.3.0", repo())
        self.assertIn("**Core**", text)
        self.assertIn("- Core section.", text)
        self.assertNotIn("Rename", text)

    def test_tag_must_match_the_edition(self):
        with self.assertRaisesRegex(ValueError, "does not match"):
            release_snapshot.notes("v1.4.0", repo())
        with self.assertRaisesRegex(ValueError, "does not match"):
            release_snapshot.notes("1.3.0", repo())

    def test_missing_changelog_entry_or_section_fails(self):
        with self.assertRaisesRegex(ValueError, "no entry"):
            release_snapshot.notes("v1.3.0", repo(changelog="## 1.2.0\n\n- Rename.\n"))
        with self.assertRaisesRegex(ValueError, "sections.yml"):
            release_snapshot.notes("v1.3.0", repo(sections='"1.2":\n  section: "x"\n  pages: [index.html]\n'))

    def test_follow_up_patch_editions_release_under_their_section(self):
        text = release_snapshot.notes("v1.3.2", repo(version="1.3.2", changelog="## 1.3.2\n\n- Fix.\n\n## 1.3.0\n\n- Core.\n"))
        self.assertIn("**Core**", text)
        self.assertIn("- Fix.", text)
        self.assertIn("- Core.", text)
        self.assertLess(text.index("1.3.2"), text.index("1.3.0"))

    def test_current_edition_is_releasable(self):
        version = (ROOT / "content/VERSION").read_text(encoding="utf-8").strip()
        text = release_snapshot.notes(f"v{version}")
        self.assertTrue(text.strip())
        for page in release_snapshot.release_section(version)["pages"]:
            self.assertTrue(page.endswith(".html"), page)


if __name__ == "__main__":
    unittest.main()
