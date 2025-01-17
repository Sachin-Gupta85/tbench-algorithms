#!/usr/bin/env python3
"""Starter stub for edit-distance — NOT implemented."""
import json, sys
def main(argv):
    if len(argv) != 2: return 2
    with open(argv[1], "w") as fh: json.dump({"distance": 0}, fh)
    return 0
if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
