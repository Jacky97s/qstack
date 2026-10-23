import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


class Validate(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.repo = Path(self.tmp.name) / "qstack"
        shutil.copytree(ROOT, self.repo, ignore=shutil.ignore_patterns(".git", "__pycache__"))

    def tearDown(self):
        self.tmp.cleanup()

    def run_validate(self):
        r = subprocess.run([sys.executable, str(self.repo / "scripts" / "validate.py")],
                           capture_output=True, text=True)
        return r.returncode, r.stdout

    def append(self, rel, text):
        p = self.repo / rel
        p.write_text(p.read_text() + text)

    def test_clean_tree_passes(self):
        code, out = self.run_validate()
        self.assertEqual(code, 0, out)

    def test_catches_unknown_principle(self):
        self.append("skills/q-mode/playbooks/automate.md", "\nSee **principle-does-not-exist**.\n")
        code, out = self.run_validate()
        self.assertEqual(code, 1)
        self.assertIn("unknown principle principle-does-not-exist", out)

    def test_catches_broken_link(self):
        self.append("skills/q-mode/SKILL.md", "\n[x](references/missing.md)\n")
        self.assertIn("broken link references/missing.md", self.run_validate()[1])

    def test_catches_unindexed_playbook(self):
        (self.repo / "skills/q-mode/playbooks/orphan.md").write_text("### Orphan\n")
        self.assertIn("orphan.md is not in the index", self.run_validate()[1])

    def test_catches_name_mismatch(self):
        p = self.repo / "skills/mutation-check/SKILL.md"
        p.write_text(p.read_text().replace("name: mutation-check", "name: mutation"))
        self.assertIn("!= directory 'mutation-check'", self.run_validate()[1])

    def test_catches_denylisted_term(self):
        (self.repo / ".denylist").write_text("acme-internal\n")
        self.append("README.md", "\nBuilt for acme-internal.\n")
        self.assertIn("denylisted term 'acme-internal'", self.run_validate()[1])


if __name__ == "__main__":
    unittest.main()
