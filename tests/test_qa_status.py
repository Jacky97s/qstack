import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

QA = Path(__file__).resolve().parent.parent / "skills" / "shift-left" / "scripts" / "qa_status.py"
HEADER = "case_id,goal_id,scenario_id,priority,spec_ac,test_type,helpers,automatable,stage_status,owner,ticket,notes\n"


class Rtm(unittest.TestCase):
    def test_goal_without_scenario_is_a_gap(self):
        with tempfile.TemporaryDirectory() as d:
            proj = Path(d)
            (proj / "02-test-goals").mkdir()
            (proj / "02-test-goals" / "test-goals.md").write_text(
                "# Test Goals\n\n## G1 — Checkout\n\n- **Priority:** P0\n\n## G2 — Refunds\n\n- **Priority:** P1\n")
            (proj / "test-index.csv").write_text(
                HEADER + "TC-1,G1,G1-S1,P0,AC-1,API,,T,case,,,\n")
            r = subprocess.run([sys.executable, str(QA), "rtm", str(proj)], capture_output=True, text=True)
            self.assertEqual(r.returncode, 0, r.stderr)
            rtm = (proj / "07-rtm" / "rtm.md").read_text()
            self.assertIn("Goals without any scenario", rtm)
            self.assertIn("G2", rtm.split("Goals without any scenario")[1])
            self.assertIn("goals: 2", rtm.lower())
            self.assertIn("gap", r.stdout.lower())


if __name__ == "__main__":
    unittest.main()
