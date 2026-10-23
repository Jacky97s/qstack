import json
import os
import subprocess
import sys
import tempfile
import unittest

GUARD = os.path.join(os.path.dirname(__file__), "..", "hooks", "guard.py")


def run(payload):
    out = subprocess.run([sys.executable, GUARD], input=json.dumps(payload),
                         capture_output=True, text=True, check=True).stdout.strip()
    return json.loads(out)["hookSpecificOutput"] if out else None


def edit(path, old, new):
    return {"tool_name": "Edit",
            "tool_input": {"file_path": path, "old_string": old, "new_string": new}}


class SleepAndSkip(unittest.TestCase):
    def test_denies_new_sleep_in_test_file(self):
        d = run(edit("tests/test_login.py", "", "    time.sleep(2)\n"))
        self.assertEqual(d["permissionDecision"], "deny")
        self.assertIn("sleep: time.sleep(2)", d["permissionDecisionReason"])

    def test_denies_wait_for_timeout_in_spec(self):
        d = run(edit("e2e/cart.spec.ts", "", "await page.waitForTimeout(500);"))
        self.assertEqual(d["permissionDecision"], "deny")

    def test_allows_sleep_outside_test_files(self):
        self.assertIsNone(run(edit("src/retry.py", "", "time.sleep(backoff)")))

    def test_allows_marked_sleep(self):
        self.assertIsNone(run(edit("tests/test_rig.py", "",
                                   "time.sleep(1)  # qstack: allow-sleep relay settle per datasheet")))

    def test_ignores_sleep_already_present(self):
        old = "time.sleep(2)\nassert x\n"
        new = "time.sleep(2)\nassert x == 1\n"
        self.assertIsNone(run(edit("tests/test_a.py", old, new)))

    def test_asyncio_sleep_zero_is_a_yield(self):
        self.assertIsNone(run(edit("tests/test_a.py", "", "await asyncio.sleep(0)")))

    def test_denies_bare_skip(self):
        d = run(edit("tests/test_a.py", "", "@pytest.mark.skip\ndef test_x(): pass"))
        self.assertEqual(d["permissionDecision"], "deny")
        self.assertIn("skip:", d["permissionDecisionReason"])

    def test_allows_skip_with_reason(self):
        self.assertIsNone(run(edit("tests/test_a.py", "",
                                   '@pytest.mark.skip(reason="PROJ-12 upstream outage")')))

    def test_js_skip_needs_ticket_or_reason(self):
        self.assertEqual(run(edit("src/a.test.ts", "", "it.skip('adds', () => {})"))
                         ["permissionDecision"], "deny")
        self.assertIsNone(run(edit("src/a.test.ts", "", "it.skip('adds', () => {}) // QA-77")))
        self.assertIsNone(run(edit("src/a.spec.ts", "",
                                   "test.skip(browserName === 'webkit', 'no webkit support')")))

    def test_write_compares_with_file_on_disk(self):
        with tempfile.TemporaryDirectory() as d:
            p = os.path.join(d, "tests", "test_w.py")
            os.makedirs(os.path.dirname(p))
            with open(p, "w") as f:
                f.write("time.sleep(1)\n")
            payload = {"tool_name": "Write",
                       "tool_input": {"file_path": p, "content": "time.sleep(1)\nx = 1\n"}}
            self.assertIsNone(run(payload))


class FalsePositives(unittest.TestCase):
    """Regressions from the independent review: legitimate code must pass."""

    def test_playwright_conditional_skip_with_callback_and_reason(self):
        self.assertIsNone(run(edit("e2e/a.spec.ts", "",
            "test.skip(({ browserName }) => browserName !== 'chromium', 'Chromium only');")))

    def test_comment_mentioning_sleep_is_not_code(self):
        self.assertIsNone(run(edit("tests/test_a.py", "",
            "# do not use time.sleep() here; poll with a deadline")))

    def test_zero_delay_promise_flush_is_not_a_wait(self):
        self.assertIsNone(run(edit("src/a.test.ts", "",
            "const flushPromises = () => new Promise(r => setTimeout(r, 0));")))

    def test_nonzero_promise_timeout_is_still_a_wait(self):
        self.assertEqual(run(edit("src/a.test.ts", "",
            "await new Promise(r => setTimeout(r, 500));"))["permissionDecision"], "deny")

    def test_markdown_under_specs_is_not_a_test_file(self):
        self.assertIsNone(run(edit("docs/specs/retry.md", "",
            "The client calls sleep(2) between retries.")))
        self.assertIsNone(run(edit("tests/README.md", "", "Never add time.sleep(1) to a test.")))

    def test_asyncio_sleep_zero_float_is_a_yield(self):
        self.assertIsNone(run(edit("tests/test_a.py", "", "await asyncio.sleep(0.0)")))

    def test_encoding_name_is_not_a_ticket(self):
        self.assertEqual(run(edit("tests/test_a.py", "", "@pytest.mark.skip  # UTF-8"))
                         ["permissionDecision"], "deny")

    def test_hash_number_inside_test_title_is_not_a_ticket(self):
        self.assertEqual(run(edit("src/a.test.ts", "", "it.skip('handles #1 item', () => {})"))
                         ["permissionDecision"], "deny")


class Bash(unittest.TestCase):
    def setUp(self):
        self.dir = tempfile.TemporaryDirectory()
        os.makedirs(os.path.join(self.dir.name, ".qstack"))
        with open(os.path.join(self.dir.name, ".qstack", "protected-hosts"), "w") as f:
            f.write("# shared\nstaging.example.com\n")
        with open(os.path.join(self.dir.name, ".qstack", "protected-commands"), "w") as f:
            f.write(r"\bfactory-reset-prod\b" + "\n")

    def tearDown(self):
        self.dir.cleanup()

    def bash(self, cmd):
        return run({"tool_name": "Bash", "tool_input": {"command": cmd}, "cwd": self.dir.name})

    def test_asks_before_mutating_protected_host(self):
        d = self.bash("curl -X DELETE https://staging.example.com/api/users/9")
        self.assertEqual(d["permissionDecision"], "ask")
        self.assertIn("staging.example.com", d["permissionDecisionReason"])

    def test_asks_before_suite_against_protected_host(self):
        self.assertEqual(self.bash("BASE_URL=https://staging.example.com pytest -m smoke")
                         ["permissionDecision"], "ask")

    def test_allows_read_of_protected_host(self):
        self.assertIsNone(self.bash("curl -s https://staging.example.com/health"))

    def test_allows_mutation_of_unlisted_host(self):
        self.assertIsNone(self.bash("curl -X POST http://localhost:8080/api/users -d '{}'"))

    def test_asks_before_builtin_irreversible(self):
        self.assertEqual(self.bash("espefuse.py --port /dev/ttyUSB0 burn_efuse JTAG_DISABLE")
                         ["permissionDecision"], "ask")

    def test_asks_before_project_protected_command(self):
        self.assertEqual(self.bash("./tools/factory-reset-prod --all")["permissionDecision"], "ask")

    def test_invalid_project_regex_does_not_disable_builtins(self):
        with open(os.path.join(self.dir.name, ".qstack", "protected-commands"), "a") as f:
            f.write("flash(\n")
        self.assertEqual(self.bash("espefuse.py --port /dev/ttyUSB0 burn_efuse JTAG_DISABLE")
                         ["permissionDecision"], "ask")
        self.assertEqual(self.bash("tool flash( now")["permissionDecision"], "ask")

    def test_ignores_other_tools(self):
        self.assertIsNone(run({"tool_name": "Read", "tool_input": {"file_path": "x"}}))

    def test_fails_open_on_bad_input(self):
        out = subprocess.run([sys.executable, GUARD], input="not json",
                             capture_output=True, text=True)
        self.assertEqual(out.returncode, 0)
        self.assertEqual(out.stdout, "")


if __name__ == "__main__":
    unittest.main()
