"""Confidentiality deny-list (GR-1.1), stored as hashes so it does not reveal what it protects
(GR-1.4).

Each word of the text, and each pair of neighbouring words, is lower-cased, hashed and compared
against the list, so a name is caught whatever its capitalisation and a two-word name is caught as
a pair. A match is reported by position only.

The list is keyed (D-023): `denylist_keyed.txt` holds HMAC-SHA-256 values made with the secret
`DENYLIST_KEY`, so a reader who guesses a name cannot confirm it. Without the key a local run warns
and skips the check, and a run in CI fails. The file's `key-check` line catches a wrong key, which
would otherwise match nothing. `scripts/denylist_rekey.py` writes the file from a list of names
that stays outside the repository. Until that file exists, the salted values of D-012 and D-017 in
`denylist_salted.txt` are used.
"""
from __future__ import annotations

import hashlib
import hmac
import os
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
KEYED_FILE = HERE / "denylist_keyed.txt"
SALTED_FILE = HERE / "denylist_salted.txt"
KEY_CHECK_MESSAGE = "ai-sdlc-map deny-list key check"
WORD = re.compile(r"[A-Za-z0-9]+")
SEPARATOR = re.compile(r"\s+|[-_]")  # between the two words of a pair, including a wrapped YAML line


def _read(path: Path) -> tuple[dict[str, str], frozenset[str]]:
    """(header fields, hashes) of a deny-list file: '# comments', 'name value' fields, one hash per line."""
    fields, hashes = {}, set()
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        if re.fullmatch(r"[0-9a-f]{64}", line):
            hashes.add(line)
        else:
            name, _, value = line.partition(" ")
            fields[name] = value.strip()
    return fields, frozenset(hashes)


def keyed_digest(key: str, value: str) -> str:
    return hmac.new(key.encode(), value.lower().encode(), hashlib.sha256).hexdigest()


def salted_digest(salt: str, value: str) -> str:
    return hashlib.sha256((salt + value.lower()).encode()).hexdigest()


def key_check(key: str) -> str:
    return keyed_digest(key, KEY_CHECK_MESSAGE)


if KEYED_FILE.exists():
    MODE = "keyed"
    _fields, HASHES = _read(KEYED_FILE)
    KEY_CHECK = _fields.get("key-check", "")
    SALT = None
else:
    MODE = "salted"
    _fields, HASHES = _read(SALTED_FILE)
    KEY_CHECK = None
    SALT = _fields["salt"]
KEY = os.environ.get("DENYLIST_KEY", "").strip() or None
_warned = False


def ready() -> bool:
    """True when the check can run. Keyed without a key: False locally (with one warning), an
    error in CI. A key that does not match the file's key-check line is always an error."""
    global _warned
    if MODE == "salted":
        return True
    if KEY is None:
        if os.environ.get("CI"):
            raise SystemExit("Deny-list: DENYLIST_KEY is not set; the check cannot run in CI (D-023).")
        if not _warned:
            print("warning: DENYLIST_KEY is not set; the deny-list check is skipped (D-023).", file=sys.stderr)
            _warned = True
        return False
    if not hmac.compare_digest(key_check(KEY), KEY_CHECK or ""):
        raise SystemExit("Deny-list: DENYLIST_KEY does not match the key-check line of denylist_keyed.txt (D-023).")
    return True


def digest(value: str) -> str:
    return keyed_digest(KEY, value) if MODE == "keyed" else salted_digest(SALT, value)


def _hit(value: str) -> bool:
    return digest(value) in HASHES


def matches(text: str) -> list[tuple[int, int]]:
    """(line, column) of every word, or word pair, in text whose hash is on the deny-list."""
    if not ready():
        return []
    found = []
    words = list(WORD.finditer(text))
    for i, m in enumerate(words):
        pair = i + 1 < len(words) and SEPARATOR.fullmatch(text[m.end():words[i + 1].start()]) is not None
        if _hit(m.group(0)) or (pair and _hit(m.group(0) + " " + words[i + 1].group(0))):
            line = text.count("\n", 0, m.start()) + 1
            found.append((line, m.start() - text.rfind("\n", 0, m.start())))
    return found
