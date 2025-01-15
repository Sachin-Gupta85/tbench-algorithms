# Dijkstra shortest paths

Implement `/app/dijkstra.py`, run as
`python3 /app/dijkstra.py <input.json> <out.json>`. A stub exists.

`<input.json>` has `n` (nodes `0..n-1`), `edges` as `[[u, v, w], ...]` with
`w >= 0`, a `source`, and `directed` (a bool). When `directed` is false, every
edge goes both ways. Compute the shortest-path distance from `source` to every
node.

Write `<out.json>` = `{"dist": [...]}`, a list of length `n` indexed by node; an
unreachable node is `null`. Exit 0. `/app/data/sample/` has a worked example.
