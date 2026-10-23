import os
import subprocess
import sys
import tempfile
import unittest

LINT = os.path.join(os.path.dirname(__file__), "..", "skills", "q-mode", "scripts", "gwt_lint.py")

CASE = """# G1-S1
## Given
- logged in as role A
## When
```
{when}
```
## Then
```
{then}
```
"""


def lint(when, then, *args):
    with tempfile.NamedTemporaryFile("w", suffix=".md", delete=False) as f:
        f.write(CASE.format(when=when, then=then))
    try:
        r = subprocess.run([sys.executable, LINT, f.name, *args], capture_output=True, text=True)
        return r.returncode, r.stdout
    finally:
        os.unlink(f.name)


class GwtLint(unittest.TestCase):
    def test_clean_case_passes(self):
        code, out = lint('W1: click "Log in" button   [Helper: login]',
                         'T1: "Orders" list shows 1 row → toHaveCount(1)')
        self.assertEqual(code, 0, out)

    def test_verb_inside_quoted_label_is_not_a_second_action(self):
        code, out = lint('W1: click "Select all" button', 'T1: 3 rows checked → toBeChecked')
        self.assertEqual(code, 0, out)

    def test_two_actions_in_one_step_fail(self):
        code, out = lint('W1: input "User" = "a" then click "Log in"', 'T1: x → toBeVisible')
        self.assertEqual(code, 1)
        self.assertIn("[1]", out)

    def test_unapproved_verb_fails(self):
        code, out = lint('W1: login as admin', 'T1: x → toBeVisible')
        self.assertIn("[2]", out)

    def test_vague_then_fails_but_shoulder_does_not(self):
        code, out = lint('W1: click "Save"', 'T1: page works → toBeVisible')
        self.assertIn("[4]", out)
        code, out = lint('W1: click "Save"', 'T1: shoulder icon visible → toBeVisible')
        self.assertEqual(code, 0, out)

    def test_team_language_banned_words(self):
        code, out = lint('W1: click "Save"', 'T1: 畫面正常 → toBeVisible', "--banned", "正常,應該")
        self.assertIn("[4]", out)

    def test_then_without_assertion_fails(self):
        code, out = lint('W1: click "Save"', 'T1: the record is saved')
        self.assertIn("[5]", out)

    def test_unknown_helper_label_fails(self):
        with tempfile.NamedTemporaryFile("w", suffix=".md", delete=False) as inv:
            inv.write("| Helper label | What |\n|---|---|\n| login | x |\n")
        try:
            code, out = lint('W1: click "Save"   [Helper: save-form]',
                             'T1: x → toBeVisible', "--inventory", inv.name)
            self.assertIn("[8]", out)
            code, out = lint('W1: click "Log in"   [Skill: login]',
                             'T1: x → toBeVisible', "--inventory", inv.name)
            self.assertEqual(code, 0, out)
        finally:
            os.unlink(inv.name)


if __name__ == "__main__":
    unittest.main()
