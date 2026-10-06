"""The hashed deny-list mechanism (GR-1.4, D-023), tested with invented names and keys only."""
import os
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

SCRIPTS = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(SCRIPTS))
import denylist  # noqa: E402

TEST_KEY = "invented-test-key"


def hashed(*names):
    return frozenset(denylist.digest(n) for n in names)


def keyed(*names, key=TEST_KEY):
    """Patches that put the module in keyed mode with the given names listed."""
    return [mock.patch.object(denylist, "MODE", "keyed"), mock.patch.object(denylist, "KEY", key),
            mock.patch.object(denylist, "KEY_CHECK", denylist.key_check(TEST_KEY)),
            mock.patch.object(denylist, "HASHES", frozenset(denylist.keyed_digest(TEST_KEY, n) for n in names))]


class Patched:
    def __init__(self, patches):
        self.patches = patches

    def __enter__(self):
        for p in self.patches:
            p.start()

    def __exit__(self, *exc):
        for p in reversed(self.patches):
            p.stop()


class DenyList(unittest.TestCase):
    def test_words_match_whatever_their_case(self):
        with mock.patch.object(denylist, "HASHES", hashed("zorblax")):
            self.assertEqual(denylist.matches("a Zorblax b\nZORBLAX zorblax"), [(1, 3), (2, 1), (2, 9)])
            self.assertEqual(denylist.matches("zorblaxes"), [])

    def test_two_word_names_match_as_a_pair_only(self):
        with mock.patch.object(denylist, "HASHES", hashed("quiet harbour")):
            self.assertEqual(len(denylist.matches("the Quiet Harbour team")), 1)
            self.assertEqual(len(denylist.matches("quiet-harbour and quiet\nharbour")), 2)
            self.assertEqual(denylist.matches("quiet, harbour; quiet night"), [])
            self.assertEqual(len(denylist.matches("definition: >-\n    the quiet\n    harbour way")), 1)

    def test_hashes_are_well_formed(self):
        self.assertTrue(denylist.HASHES)
        self.assertTrue(all(len(h) == 64 and int(h, 16) >= 0 for h in denylist.HASHES))

    def test_exactly_one_list_is_committed(self):
        self.assertNotEqual(denylist.KEYED_FILE.exists(), denylist.SALTED_FILE.exists())


class KeyedDenyList(unittest.TestCase):
    def test_keyed_values_match_with_the_key(self):
        with Patched(keyed("zorblax", "quiet harbour")):
            self.assertEqual(denylist.matches("Zorblax and the Quiet Harbour team"), [(1, 1), (1, 17)])

    def test_without_the_key_a_local_run_skips(self):
        with Patched(keyed("zorblax", key=None)), mock.patch.dict(os.environ, {}, clear=True), \
                mock.patch("sys.stderr"):
            self.assertEqual(denylist.matches("zorblax"), [])

    def test_without_the_key_ci_fails(self):
        with Patched(keyed("zorblax", key=None)), mock.patch.dict(os.environ, {"CI": "true"}):
            with self.assertRaises(SystemExit):
                denylist.matches("zorblax")

    def test_a_wrong_key_fails_rather_than_matching_nothing(self):
        with Patched(keyed("zorblax", key="another-key")):
            with self.assertRaises(SystemExit):
                denylist.matches("zorblax")


class Rekey(unittest.TestCase):
    def setUp(self):
        self.repo = Path(tempfile.mkdtemp())
        self.outside = Path(tempfile.mkdtemp())
        self.addCleanup(shutil.rmtree, self.repo)
        self.addCleanup(shutil.rmtree, self.outside)
        scripts = self.repo / "scripts"
        scripts.mkdir()
        for name in ("denylist.py", "denylist_rekey.py"):
            shutil.copy(SCRIPTS / name, scripts / name)
        salt = "0123456789abcdef"
        values = [denylist.salted_digest(salt, n) for n in ("zorblax", "quiet harbour")]
        (scripts / "denylist_salted.txt").write_text(f"# test\nsalt {salt}\n" + "\n".join(values) + "\n")
        self.scripts = scripts

    def rekey(self, terms, key=TEST_KEY):
        path = self.outside / "terms.txt"
        path.write_text(terms)
        env = {**os.environ, "DENYLIST_KEY": key}
        return subprocess.run([sys.executable, str(self.scripts / "denylist_rekey.py"), "--terms", str(path)],
                              capture_output=True, text=True, env=env)

    def keyed_matches(self, text, key=TEST_KEY):
        code = "import sys, denylist; print(denylist.MODE, denylist.matches(sys.stdin.read()))"
        env = {**os.environ, "DENYLIST_KEY": key, "PYTHONPATH": str(self.scripts)}
        return subprocess.run([sys.executable, "-c", code], input=text, capture_output=True, text=True,
                              env=env, cwd=self.outside).stdout.strip()

    def test_switch_writes_keyed_values_and_removes_the_salted_list(self):
        result = self.rekey("# names\nZorblax\nQuiet Harbour\nNewname\n")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertNotIn("zorblax", result.stdout.lower())
        self.assertFalse((self.scripts / "denylist_salted.txt").exists())
        written = (self.scripts / "denylist_keyed.txt").read_text()
        self.assertNotIn("zorblax", written.lower())
        self.assertNotIn(TEST_KEY, written)
        self.assertEqual(self.keyed_matches("zorblax, the quiet harbour, newname"), "keyed [(1, 1), (1, 14), (1, 29)]")

    def test_a_list_that_drops_a_current_name_writes_nothing(self):
        result = self.rekey("zorblax\n")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("1 of the 2", result.stderr)
        self.assertTrue((self.scripts / "denylist_salted.txt").exists())
        self.assertFalse((self.scripts / "denylist_keyed.txt").exists())

    def test_a_later_run_needs_the_same_key(self):
        self.assertEqual(self.rekey("zorblax\nquiet harbour\n").returncode, 0)
        self.assertNotEqual(self.rekey("zorblax\nquiet harbour\nother\n", key="another-key").returncode, 0)
        self.assertEqual(self.rekey("zorblax\nquiet harbour\nother\n").returncode, 0)

    def test_terms_inside_the_repository_are_refused(self):
        path = self.repo / "terms.txt"
        path.write_text("zorblax\n")
        result = subprocess.run([sys.executable, str(self.scripts / "denylist_rekey.py"), "--terms", str(path)],
                                capture_output=True, text=True, env={**os.environ, "DENYLIST_KEY": TEST_KEY})
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("outside the repository", result.stderr)


if __name__ == "__main__":
    unittest.main()
