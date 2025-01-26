#!/usr/bin/env python3
"""0/1 knapsack — maximum value within a weight capacity.

Usage:  python3 knapsack.py <input.json> <out.json>

Input JSON:
    {"capacity": <int>, "items": [[weight, value], ...]}   # non-negative ints

Each item may be taken at most once. Output the greatest total value whose total
weight does not exceed the capacity:

    {"max_value": <int>}
"""
from __future__ import annotations

import json
import sys


def solve(data: dict) -> dict:
    cap = data["capacity"]
    items = data["items"]
    dp = [0] * (cap + 1)
    for w, v in items:
        if w > cap:
            continue
        for c in range(cap, w - 1, -1):
            cand = dp[c - w] + v
            if cand > dp[c]:
                dp[c] = cand
    return {"max_value": dp[cap]}


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        sys.stderr.write("usage: knapsack.py <input.json> <out.json>\n")
        return 2
    with open(argv[0], encoding="utf-8") as fh:
        data = json.load(fh)
    with open(argv[1], "w", encoding="utf-8") as fh:
        json.dump(solve(data), fh, indent=2)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
