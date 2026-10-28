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
        tracked = subprocess.run(["git", "ls-files", "-z"], cwd=ROOT, capture_output=True, text=True,
                                 check=True).stdout.split("\0")
        for rel in filter(None, tracked):
            (self.repo / rel).parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(ROOT / rel, self.repo / rel)

    def tearDown(self):
        self.tmp.cleanup()

    def git(self, *args):
        subprocess.run(["git", "-c", "user.name=t", "-c", "user.email=t@t", *args], cwd=self.repo,
                       capture_output=True, check=True)

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

    def test_ignores_pstack_principle(self):
        self.append("skills/q-mode/playbooks/automate.md", "\nSee `pstack:principle-does-not-exist`.\n")
        code, out = self.run_validate()
        self.assertEqual(code, 0, out)

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

    def test_catches_lens_missing_a_slot(self):
        p = self.repo / "skills/q-mode/lenses/performance.md"
        p.write_text(p.read_text().replace("## Oracle sources", "## Oracles"))
        self.assertIn("lens performance: headings must be", self.run_validate()[1])

    def test_catches_unindexed_lens(self):
        src = (self.repo / "skills/q-mode/lenses/data.md").read_text()
        (self.repo / "skills/q-mode/lenses/robotics.md").write_text(src)
        out = self.run_validate()[1]
        self.assertIn("lens robotics.md is not in the index", out)
        self.assertIn("lens robotics is not listed", out)

    def test_catches_denylisted_term(self):
        (self.repo / ".denylist").write_text("acme-internal\n")
        self.append("README.md", "\nBuilt for acme-internal.\n")
        self.assertIn("denylisted term 'acme-internal'", self.run_validate()[1])

    def test_ignores_untracked_files_in_git_checkout(self):
        self.git("init", "-q")
        self.git("add", "-A")
        (self.repo / "scratch").mkdir()
        (self.repo / "scratch/notes.md").write_text("See **principle-does-not-exist** and [x](missing.md).\n")
        code, out = self.run_validate()
        self.assertEqual(code, 0, out)

    def test_checks_staged_files_in_git_checkout(self):
        self.git("init", "-q")
        (self.repo / "scratch").mkdir()
        (self.repo / "scratch/notes.md").write_text("See **principle-does-not-exist**.\n")
        self.git("add", "-A")
        self.assertIn("unknown principle principle-does-not-exist", self.run_validate()[1])


if __name__ == "__main__":
    unittest.main()
