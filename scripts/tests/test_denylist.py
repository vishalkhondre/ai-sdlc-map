"""The hashed deny-list mechanism (GR-1.4), tested with invented names only."""
import hashlib
import sys
import unittest
from pathlib import Path
from unittest import mock

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import denylist  # noqa: E402


def hashed(*names):
    return frozenset(hashlib.sha256((denylist.SALT + n).encode()).hexdigest() for n in names)


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


if __name__ == "__main__":
    unittest.main()
