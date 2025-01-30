# 🧮 tbench-algorithms — classic algorithm & optimization tasks

> A collection of **Terminal-Bench 3**-style algorithm tasks for coding agents: read a JSON instance, compute the exact optimum, graded on unseen instances.

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![Format](https://img.shields.io/badge/format-Terminal--Bench%203-6f42c1)
![Tasks](https://img.shields.io/badge/tasks-4-informational)
![Deps](https://img.shields.io/badge/dependencies-none-brightgreen)

Textbook DP and graph problems where the answer is **exact** — an approximate or
greedy shortcut is caught by an exact grader on held-out instances.

---

## 📦 Tasks

| Task | Problem |
|---|---|
| [`knapsack`](tasks/knapsack) | 0/1 knapsack — max value within a weight budget |
| [`interval-schedule`](tasks/interval-schedule) | weighted interval scheduling (max weight, no overlaps) |
| [`edit-distance`](tasks/edit-distance) | Levenshtein distance between two strings |
| [`dijkstra`](tasks/dijkstra) | single-source shortest paths (non-negative weights) |

## ✅ Verify every task (no dependencies)

```bash
python3 run_checks.py
```

```
dijkstra            Oracle=1  Nop=0  ✅
edit-distance       Oracle=1  Nop=0  ✅
interval-schedule   Oracle=1  Nop=0  ✅
knapsack            Oracle=1  Nop=0  ✅
ALL 4 TASKS GOOD ✅
```

Each task has `instruction.md`, `task.toml`, `environment/` (stub + `data/sample/`),
`solution/` (reference), and `tests/` (hidden grader + held-out instances).

## 📎 Note

Terminal-Bench 3 **task-authoring** structure with a lightweight local runner,
published as **portfolio examples of agent-task design** (original tasks, not
affiliated with any benchmark operator).

## 📝 License

MIT — see [LICENSE](LICENSE).
