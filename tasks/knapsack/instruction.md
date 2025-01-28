# 0/1 knapsack

Implement `/app/knapsack.py`, run as
`python3 /app/knapsack.py <input.json> <out.json>`. A stub exists.

`<input.json>` is `{"capacity": <int>, "items": [[weight, value], ...]}` with
non-negative integers. Each item may be taken **at most once**. Find the greatest
total value whose total weight does not exceed the capacity.

Write `<out.json>` = `{"max_value": <int>}`. Exit 0. `/app/data/sample/` has a
worked example.
