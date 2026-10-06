"""Write the keyed deny-list (D-023) from a list of names. Run by the author, locally.

    python scripts/denylist_rekey.py --terms <file outside the repository>

The terms file holds one name per line, two-word names with one space; lines starting with # and
blank lines are ignored. The script asks for DENYLIST_KEY without echoing it (or reads it from the
environment), and refuses to write anything unless every value on the current list is matched by
a name in the file, so nothing is dropped: the salted list (scripts/denylist_salted.txt) on the
first run, which switches the deny-list to keyed hashes, and the keyed list on later runs, which add
names. It writes scripts/denylist_keyed.txt (hashes and a key-check value only) and deletes
scripts/denylist_salted.txt. No name is printed, and nothing it writes reveals a name or the key.
"""
from __future__ import annotations

import argparse
import getpass
import os
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import denylist  # noqa: E402


def names(path: Path) -> list[str]:
    found = []
    for number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        words = denylist.WORD.findall(line)
        if not 1 <= len(words) <= 2:
            raise SystemExit(f"{path.name} line {number}: a name has one or two words; list longer names as pairs.")
        found.append(" ".join(words).lower())
    return sorted(set(found))


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--terms", type=Path, required=True, help="names file, kept outside the repository")
    args = ap.parse_args()
    terms = args.terms.resolve()
    if terms.is_relative_to(denylist.HERE.parent):
        raise SystemExit("Keep the terms file outside the repository (GR-1.3, GR-1.4).")
    key = os.environ.get("DENYLIST_KEY", "").strip()
    if not key:
        key = getpass.getpass("DENYLIST_KEY (not shown): ").strip()
        # The first run has no key-check value to compare with, so a typing mistake is caught here.
        if denylist.SALTED_FILE.exists() and getpass.getpass("DENYLIST_KEY again: ").strip() != key:
            raise SystemExit("The two keys differ; nothing was written.")
    if not key:
        raise SystemExit("No key given.")
    listed = names(terms)
    if denylist.SALTED_FILE.exists():
        fields, current = denylist._read(denylist.SALTED_FILE)
        covered = {denylist.salted_digest(fields["salt"], n) for n in listed} & current
    else:
        fields, current = denylist._read(denylist.KEYED_FILE)
        if fields.get("key-check") != denylist.key_check(key):
            raise SystemExit("This key is not the one scripts/denylist_keyed.txt was made with; nothing was written.")
        covered = {denylist.keyed_digest(key, n) for n in listed} & current
    if covered != current:
        raise SystemExit(f"{len(current - covered)} of the {len(current)} current values match no name in the file. "
                         "Add the missing names and run again; nothing was written.")
    lines = ["# Deny-list (GR-1.1, GR-1.4): HMAC-SHA-256 of each lower-cased name, keyed by DENYLIST_KEY (D-023).",
             "# Written by scripts/denylist_rekey.py. Add a name by running it again with the full list.",
             f"key-check {denylist.key_check(key)}"]
    lines += sorted(denylist.keyed_digest(key, n) for n in listed)
    denylist.KEYED_FILE.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Wrote scripts/denylist_keyed.txt: {len(listed)} values ({len(current)} carried over, "
          f"{len(listed) - len(current)} new).")
    if denylist.SALTED_FILE.exists():
        denylist.SALTED_FILE.unlink()
        print("Deleted scripts/denylist_salted.txt: the deny-list is now keyed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
