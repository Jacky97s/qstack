import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

QA = Path(__file__).resolve().parent.parent / "skills" / "q-mode" / "scripts" / "qa_status.py"
HEADER = "case_id,goal_id,scenario_id,priority,spec_ac,test_type,stage_status\n"


def run(*args):
    r = subprocess.run([sys.executable, str(QA), *map(str, args)], capture_output=True, text=True)
    return r.returncode, r.stdout, r.stderr


class Coverage(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        d = Path(self.tmp.name)
        self.plan = d / "plan.md"
        self.plan.write_text("# Plan\n\n## Goals\n\n### G1 — Checkout\n\n### G2 — Refunds\n")
        self.csv = d / "trace.csv"
        self.csv.write_text(HEADER
                            + "TC-1,G1,G1-S1,P0,AC-1,API,case\n"
                            + ",G1,G1-S2,P0,AC-2,API,scenario\n"
                            + ",G1,G1-S3,P2,AC-3,E2E,scenario\n")

    def tearDown(self):
        self.tmp.cleanup()

    def test_default_reports_gaps_only(self):
        code, out, err = run("rtm", self.csv, "--goals", self.plan)
        self.assertEqual(code, 0, err)
        self.assertIn("P0: 1/2", out)
        self.assertIn("G1-S2", out)
        self.assertIn("Goals without any scenario: G2", out)
        self.assertNotIn("## Traceability matrix", out)

    def test_uncased_p0_fails_the_check(self):
        code, out, _ = run("rtm", self.csv, "--goals", self.plan, "--fail-on-p0")
        self.assertEqual(code, 1)

    def test_full_matrix_on_request(self):
        code, out, _ = run("rtm", self.csv, "--full")
        self.assertIn("## Traceability matrix", out)
        self.assertIn("| AC-1 | G1 | G1-S1 | TC-1 |", out)

    def test_writes_no_files(self):
        before = set(Path(self.tmp.name).iterdir())
        run("rtm", self.csv, "--goals", self.plan, "--full")
        self.assertEqual(before, set(Path(self.tmp.name).iterdir()))

    def test_status_summary(self):
        code, out, _ = run("status", self.csv)
        self.assertEqual(code, 0)
        self.assertIn("2 scenario(s) without a case", out)
        self.assertIn("P0 first: G1-S2", out)


if __name__ == "__main__":
    unittest.main()
