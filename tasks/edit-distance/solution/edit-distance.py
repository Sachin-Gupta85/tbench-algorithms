#!/usr/bin/env python3
"""Levenshtein edit distance between two strings.

Usage:  python3 edit-distance.py <input.json> <out.json>

Input JSON:
    {"a": "<string>", "b": "<string>"}

Output the minimum number of single-character insertions, deletions, or
substitutions that turn `a` into `b`:

    {"distance": <int>}
"""
from __future__ import annotations

import json
import sys


def solve(data: dict) -> dict:
    a, b = data["a"], data["b"]
    prev = list(range(len(b) + 1))
    for i, ca in enumerate(a, start=1):
        cur = [i] + [0] * len(b)
        for j, cb in enumerate(b, start=1):
            cost = 0 if ca == cb else 1
            cur[j] = min(prev[j] + 1, cur[j - 1] + 1, prev[j - 1] + cost)
        prev = cur
    return {"distance": prev[len(b)]}


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        sys.stderr.write("usage: edit-distance.py <input.json> <out.json>\n")
        return 2
    with open(argv[0], encoding="utf-8") as fh:
        data = json.load(fh)
    with open(argv[1], "w", encoding="utf-8") as fh:
        json.dump(solve(data), fh, indent=2)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
