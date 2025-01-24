"""Hidden verifier for interval-schedule: run the candidate on the sample + held-out cases and
compare the emitted JSON exactly."""
import json
import os
import subprocess
import sys
import tempfile
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
SAMPLE_DIR = os.path.join(ROOT, "environment", "data", "sample")
HELDOUT_DIR = os.path.join(HERE, "cases")
BIN = os.environ.get("TASK_BIN", "/app/interval-schedule.py")


def load(p):
    with open(p, encoding="utf-8") as fh:
        return json.load(fh)


def run_case(case_dir):
    with tempfile.TemporaryDirectory() as tmp:
        out = os.path.join(tmp, "out.json")
        proc = subprocess.run(
            [sys.executable, BIN, os.path.join(case_dir, "input.json"), out],
            capture_output=True, text=True,
        )
        assert proc.returncode == 0, f"exit {proc.returncode}: {proc.stderr[-400:]}"
        assert os.path.exists(out), "no output written"
        return load(out)


def cases(root):
    return sorted(d for d in os.listdir(root) if os.path.isdir(os.path.join(root, d)))


class TestTask(unittest.TestCase):
    def _check(self, root):
        for name in cases(root):
            d = os.path.join(root, name)
            self.assertEqual(run_case(d), load(os.path.join(d, "expected.json")), name)

    def test_samples(self):
        self._check(SAMPLE_DIR)

    def test_heldout(self):
        found = cases(HELDOUT_DIR)
        self.assertGreaterEqual(len(found), 6)
        self._check(HELDOUT_DIR)


if __name__ == "__main__":
    unittest.main()
