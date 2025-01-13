#!/usr/bin/env python3
"""Dijkstra single-source shortest paths on a non-negative weighted graph.

Usage:  python3 dijkstra.py <input.json> <out.json>

Input JSON:
    {
      "n": <int>,                       # nodes are 0..n-1
      "edges": [[u, v, w], ...],        # w >= 0
      "source": <int>,
      "directed": <bool>                # if false, each edge goes both ways
    }

Output the shortest-path distance from `source` to every node, as a list of
length n indexed by node. A node that cannot be reached is `null`:

    {"dist": [0, 3, 7, null, ...]}
"""
from __future__ import annotations

import heapq
import json
import sys


def solve(data: dict) -> dict:
    n = data["n"]
    src = data["source"]
    directed = data.get("directed", True)
    adj = [[] for _ in range(n)]
    for u, v, w in data["edges"]:
        adj[u].append((v, w))
        if not directed:
            adj[v].append((u, w))

    INF = float("inf")
    dist = [INF] * n
    dist[src] = 0
    pq = [(0, src)]
    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]:
            continue
        for v, w in adj[u]:
            nd = d + w
            if nd < dist[v]:
                dist[v] = nd
                heapq.heappush(pq, (nd, v))

    return {"dist": [None if d == INF else int(d) for d in dist]}


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        sys.stderr.write("usage: dijkstra.py <input.json> <out.json>\n")
        return 2
    with open(argv[0], encoding="utf-8") as fh:
        data = json.load(fh)
    with open(argv[1], "w", encoding="utf-8") as fh:
        json.dump(solve(data), fh, indent=2)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
