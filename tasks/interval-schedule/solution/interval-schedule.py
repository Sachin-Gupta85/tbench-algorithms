#!/usr/bin/env python3
"""Weighted interval scheduling — maximum total weight of non-overlapping jobs.

Usage:  python3 interval-schedule.py <input.json> <out.json>

Input JSON:
    {"intervals": [[start, end, weight], ...]}   # integers, start < end, weight >= 0

Each interval is the half-open range [start, end): two intervals conflict only
when they actually overlap, so one ending exactly where another begins is fine.
Choose a subset of pairwise non-conflicting intervals whose total weight is
greatest:

    {"max_weight": <int>}
"""
from __future__ import annotations

import bisect
import json
import sys


def solve(data: dict) -> dict:
    jobs = sorted((e, s, w) for s, e, w in data["intervals"])
    ends = [e for e, _, _ in jobs]
    best = [0] * (len(jobs) + 1)   # best[i] = best using first i jobs (by end)
    for i, (e, s, w) in enumerate(jobs, start=1):
        # latest job (among first i-1) that ends <= this job's start
        k = bisect.bisect_right(ends, s, 0, i - 1)
        take = best[k] + w
        best[i] = max(best[i - 1], take)
    return {"max_weight": best[len(jobs)]}


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        sys.stderr.write("usage: interval-schedule.py <input.json> <out.json>\n")
        return 2
    with open(argv[0], encoding="utf-8") as fh:
        data = json.load(fh)
    with open(argv[1], "w", encoding="utf-8") as fh:
        json.dump(solve(data), fh, indent=2)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
