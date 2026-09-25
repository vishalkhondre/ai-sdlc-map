"""Confidentiality deny-list (GR-1.1), stored as salted hashes so it does not reveal what it
protects (GR-1.4).

Each word of the text, and each pair of neighbouring words, is lower-cased, hashed with the salt
and compared against HASHES, so a name is caught whatever its capitalisation and a two-word name
is caught as a pair. A match is reported by position only. Add a name by appending
sha256(SALT + name.lower()) to HASHES (a two-word name with one space), never the name itself.
"""
from __future__ import annotations

import hashlib
import re

SALT = "c56125cd97e1c5f5f18fbb21d181de3c"
HASHES = frozenset({
    "064b3b80a32aeb7dae1fd8dcd4fd8809c14813254afcd7208c2f498a6d782f0c",
    "0fb5a37ce126e3a60ffcc059fe4524ecdaa2cab167b99fdd3b780c7980bf7d4c",
    "1a458901542710ca75d6b022bededadfa472f6589199a89e1b60683e11d0ed54",
    "2aab8e1b460435acf09c639d64cc7fc5db48c133b7ec8cfab13b01822a32e308",
    "39baabaa5fceea7d8469d971ca6a3d5524cd8b4040f9fc8c68dbac480f6f6926",
    "3ba8ebccf08dba2aa0b48484c49fdb6ca0f5e86f8ee363139f56ca7d538c2caf",
    "664e3e295920b6e8eca53481b1a1f88a8281a4100f789db8958d0a3bb0d4614f",
    "66d1b881b81434850f649e4f1af84d284b64a0590d86182be8871bc987cadb40",
    "6c89047a003f9e954c81e80e06baa992e475a315f48ec2b8515fca5abb400c8b",
    "6de9782dbc5f76fe4f4befe673f9ff95a28c9d4c45eca999996b352d10b345b5",
    "724bbf3c5221dd1c09002eec3f073823667aba76c70f4b554d7f3b98427e524c",
    "7c32e601a01aba0364d1325ce0ed3ff26e70a51959370d9b2b27f42d88c93dc2",
    "ab18f6e849aed50e7f1e98ec78e38985f9e4628dbc475ae41a216de0a63eefcc",
    "acc4ecffac622a130a2337efe22031d0c652ff4d76dcc9d2fcc81a5e106717c9",
})
WORD = re.compile(r"[A-Za-z0-9]+")


def _hit(value: str) -> bool:
    return hashlib.sha256((SALT + value.lower()).encode()).hexdigest() in HASHES


def matches(text: str) -> list[tuple[int, int]]:
    """(line, column) of every word, or word pair, in text whose salted hash is on the deny-list."""
    found = []
    words = list(WORD.finditer(text))
    for i, m in enumerate(words):
        pair = i + 1 < len(words) and text[m.end():words[i + 1].start()] in (" ", "\n", "-", "_")
        if _hit(m.group(0)) or (pair and _hit(m.group(0) + " " + words[i + 1].group(0))):
            line = text.count("\n", 0, m.start()) + 1
            found.append((line, m.start() - text.rfind("\n", 0, m.start())))
    return found
