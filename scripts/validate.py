#!/usr/bin/env python3
"""Structural checks for the qstack plugin. Run from anywhere: python3 scripts/validate.py

- every skill has frontmatter with name == directory and a description under 1024 chars
- principle-* skills are model-only (user-invocable: false)
- agents have name and description
- relative links and backticked bundled paths resolve
- every principle-<x> and qstack:<x> mentioned exists
- q-mode's playbook index and playbooks/ match exactly
- every lens has the fixed headings in order, and the lens index and q-mode list match the files
- plugin.json and marketplace.json parse and agree on name and version
- optional: no term from a local, untracked .denylist appears (keeps company names out)
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
errors = []


def err(msg):
    errors.append(msg)


def frontmatter(path):
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        return None, text
    end = text.find("\n---\n", 4)
    if end == -1:
        return None, text
    meta = {}
    for line in text[4:end].splitlines():
        m = re.match(r"^([\w-]+):\s*(.*)$", line)
        if m:
            meta[m.group(1)] = m.group(2).strip().strip('"')
    return meta, text


skills = {p.parent.name: p for p in sorted((ROOT / "skills").glob("*/SKILL.md"))}
agents = {p.stem: p for p in sorted((ROOT / "agents").glob("*.md"))}

for name, path in skills.items():
    meta, _ = frontmatter(path)
    if meta is None:
        err(f"{path}: missing frontmatter")
        continue
    if meta.get("name") != name:
        err(f"{path}: name '{meta.get('name')}' != directory '{name}'")
    desc = meta.get("description", "")
    if not desc:
        err(f"{path}: empty description")
    if len(desc) > 1024:
        err(f"{path}: description is {len(desc)} chars (max 1024)")
    if name.startswith("principle-") and meta.get("user-invocable") != "false":
        err(f"{path}: principles must set user-invocable: false")

for name, path in agents.items():
    meta, _ = frontmatter(path)
    if not meta or meta.get("name") != name or not meta.get("description"):
        err(f"{path}: agent needs name == filename and a description")

LINK = re.compile(r"\]\(([^)#\s]+)(#[^)]*)?\)")
TICKED = re.compile(r"`((?:\.\./[\w-]+/)?(?:playbooks|references|templates|scripts|lenses)/[\w./-]+\.(?:md|py|csv))`")
PRINCIPLE = re.compile(r"(?<!pstack:)\bprinciple-[a-z0-9-]+[a-z0-9]")
NAMESPACED = re.compile(r"`qstack:([a-z0-9-]+)`")

for md in sorted(ROOT.rglob("*.md")):
    if ".git" in md.parts:
        continue
    text = md.read_text(encoding="utf-8")
    base = md.parent
    skill_dir = next((p for p in [md.parent, *md.parents] if (p / "SKILL.md").exists()), None)
    for target, _ in LINK.findall(text):
        if re.match(r"^[a-z]+://", target) or target.startswith("mailto:"):
            continue
        if not (base / target).exists():
            err(f"{md.relative_to(ROOT)}: broken link {target}")
    for target in TICKED.findall(text):
        roots = [base] + ([skill_dir] if skill_dir else [])
        if not any((r / target).exists() for r in roots):
            err(f"{md.relative_to(ROOT)}: missing bundled path {target}")
    for ref in set(PRINCIPLE.findall(text)):
        if ref not in skills:
            err(f"{md.relative_to(ROOT)}: unknown principle {ref}")
    for ref in set(NAMESPACED.findall(text)):
        if ref not in skills and ref not in agents:
            err(f"{md.relative_to(ROOT)}: unknown qstack:{ref}")

qmode = (ROOT / "skills/q-mode/SKILL.md").read_text(encoding="utf-8")
indexed = set(re.findall(r"^- \*\*[^*]+\*\* \(`([a-z0-9-]+)`\)", qmode, re.MULTILINE))
files = {p.stem for p in (ROOT / "skills/q-mode/playbooks").glob("*.md")}
for missing in sorted(files - indexed):
    err(f"q-mode: playbook file {missing}.md is not in the index")
for missing in sorted(indexed - files):
    err(f"q-mode: index names {missing} but playbooks/{missing}.md does not exist")
for name in skills:
    if name.startswith("principle-") and name not in qmode:
        title_words = name[len("principle-"):].split("-")
        if not re.search(r"\*\*" + r"[\s,]+".join(title_words), qmode, re.IGNORECASE):
            err(f"q-mode: principle {name} is not in the principles index")

LENS_HEADINGS = ["Artifact identity", "Stimulus and observation", "Instruments and trust",
                 "Variation and sampling", "Cost and reversibility", "Oracle sources",
                 "Gates and standards", "Layer ladder", "Typical risks", "Failure classes",
                 "Playbook notes"]
lens_dir = ROOT / "skills/q-mode/lenses"
lens_files = {p.stem for p in lens_dir.glob("*.md") if p.name != "README.md"}
for name in sorted(lens_files):
    found = re.findall(r"^## (.+)$", (lens_dir / f"{name}.md").read_text(encoding="utf-8"), re.MULTILINE)
    if found != LENS_HEADINGS:
        missing = [h for h in LENS_HEADINGS if h not in found]
        err(f"lens {name}: headings must be exactly {LENS_HEADINGS} in order"
            + (f"; missing {missing}" if missing else f"; found {found}"))
lens_index = set(re.findall(r"^\| \[([a-z0-9-]+)\]\(\1\.md\) \|", (lens_dir / "README.md").read_text(encoding="utf-8"), re.MULTILINE))
for missing in sorted(lens_files - lens_index):
    err(f"lenses/README.md: lens {missing}.md is not in the index")
for missing in sorted(lens_index - lens_files):
    err(f"lenses/README.md: index names {missing} but lenses/{missing}.md does not exist")
for name in sorted(lens_files):
    if f"`{name}`" not in qmode:
        err(f"q-mode: lens {name} is not listed in the Lenses section")

try:
    plugin = json.loads((ROOT / ".claude-plugin/plugin.json").read_text())
    market = json.loads((ROOT / ".claude-plugin/marketplace.json").read_text())
    entry = next(p for p in market["plugins"] if p["name"] == plugin["name"])
    if entry.get("version") and entry["version"] != plugin["version"]:
        err("marketplace.json version differs from plugin.json")
except Exception as e:
    err(f"plugin manifests: {e}")

deny = ROOT / ".denylist"
if deny.exists():
    terms = [t.strip() for t in deny.read_text().splitlines() if t.strip() and not t.startswith("#")]
    for f in sorted(ROOT.rglob("*")):
        if f.is_file() and ".git" not in f.parts and f.name != ".denylist" and f.suffix in {".md", ".py", ".json", ".sh", ".csv", ".txt"}:
            low = f.read_text(encoding="utf-8", errors="ignore").lower()
            for t in terms:
                if t.lower() in low:
                    err(f"{f.relative_to(ROOT)}: contains denylisted term '{t}'")

if errors:
    print(f"FAIL: {len(errors)} problem(s)")
    for e in errors:
        print("  - " + e)
    sys.exit(1)
print(f"OK: {len(skills)} skills, {len(agents)} agents, {len(files)} playbooks, {len(lens_files)} lenses")
