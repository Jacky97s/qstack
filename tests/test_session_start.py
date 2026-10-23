import os
import subprocess
import tempfile
import unittest
from pathlib import Path

HOOK = Path(__file__).resolve().parent.parent / "hooks" / "session-start.sh"


def run(config_dir, env_extra=None):
    env = {k: v for k, v in os.environ.items() if k != "QSTACK_SESSION_HOOK"}
    env["CLAUDE_CONFIG_DIR"] = str(config_dir)
    env.update(env_extra or {})
    return subprocess.run(["sh", str(HOOK)], capture_output=True, text=True, env=env).stdout


class SessionStart(unittest.TestCase):
    def test_injects_by_default(self):
        with tempfile.TemporaryDirectory() as d:
            self.assertIn("<qstack>", run(d))

    def test_settings_file_turns_it_off(self):
        with tempfile.TemporaryDirectory() as d:
            Path(d, "qstack.md").write_text("# qstack settings\n\nsession hook: off\n")
            self.assertEqual(run(d), "")

    def test_settings_file_on_keeps_it(self):
        with tempfile.TemporaryDirectory() as d:
            Path(d, "qstack.md").write_text("session hook: on\n")
            self.assertIn("<qstack>", run(d))

    def test_env_var_still_turns_it_off(self):
        with tempfile.TemporaryDirectory() as d:
            self.assertEqual(run(d, {"QSTACK_SESSION_HOOK": "off"}), "")


if __name__ == "__main__":
    unittest.main()
