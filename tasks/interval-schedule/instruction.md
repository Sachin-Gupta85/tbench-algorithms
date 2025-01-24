# Weighted interval scheduling

Implement `/app/interval-schedule.py`, run as
`python3 /app/interval-schedule.py <input.json> <out.json>`. A stub exists.

`<input.json>` is `{"intervals": [[start, end, weight], ...]}` (integers,
`start < end`, `weight >= 0`). Each interval is the half-open range
`[start, end)`, so two intervals conflict only when they truly overlap — one
ending exactly where another begins does **not** conflict. Choose a subset of
pairwise non-conflicting intervals whose total weight is greatest.

Write `<out.json>` = `{"max_weight": <int>}`. Exit 0. `/app/data/sample/` has a
worked example.
