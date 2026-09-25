"""Confidentiality deny-list (GR-1.1), stored as salted hashes so it does not reveal what it
protects (GR-1.4).

Each word of the text is hashed with the salt and compared, case-sensitively, against HASHES.
A match is reported by position only. The list covers single-word names; add a name by
appending sha256(SALT + name) to HASHES, never the name itself.
"""
from __future__ import annotations

import hashlib
import re

SALT = "a2dfee79dfb27c23d3211ef0dfbdae49"
HASHES = frozenset({
    "55ce82447f354f98e24714e10542ffd0246963340cf0759c6573ee2054b9c103",
    "c1bef014d718dc3e347aeb5d0723af982d9eeac466b73fed05fe9c7a9f01e7c7",
    "e4c4b57b4b2066987eb7291f364148e0b0d46e87394b61ea7126e23df6a9b4cb",
    "eb97d72ee3f2a757412bdd6d3214feefdcecb5f91403190d229717aabf8c4002",
})
WORD = re.compile(r"[A-Za-z0-9]+")


def matches(text: str) -> list[tuple[int, int]]:
    """(line, column) of every word in text whose salted hash is on the deny-list."""
    found = []
    for m in WORD.finditer(text):
        if hashlib.sha256((SALT + m.group(0)).encode()).hexdigest() in HASHES:
            line = text.count("\n", 0, m.start()) + 1
            found.append((line, m.start() - text.rfind("\n", 0, m.start())))
    return found
