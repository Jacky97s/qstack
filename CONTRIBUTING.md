# Contributing

## Checks

```sh
python3 scripts/validate.py          # structure, links, indexes, manifests
python3 -m unittest discover -s tests  # guard hook and shift-left lint
```

Both must pass before a change lands. Keep a local `.denylist` (one term per line, untracked) with any company, customer, or product names that must never appear in qstack. `validate.py` fails when one does.

## Writing skills and playbooks

- Keep only prose that changes a decision. Tell the agent what to do. Explain the reason only when the rule is confusing without it.
- A principle is a short, model-only leaf skill (`user-invocable: false`) whose description says when it applies.
- A playbook is a numbered list of steps an agent copies into its todolist verbatim, an owner line, and a **Reply** line naming what is unique to its report. Changing a step's wording can break project playbooks that quote it, so note reworded steps in the changelog.
- Nothing project-specific in the core. Projects put their slots in `.qstack/profile.md` and their extensions in `.qstack/playbooks/`.
- Domain coverage belongs in the shared vocabulary (`skills/q-mode/references/domains.md`) and in domain playbooks, not in special cases scattered through principles.
- When a rule keeps being restated, encode it in structure: a guard rule, a lint, a validator check.

## Versioning

Bump `version` in `.claude-plugin/plugin.json` and `.claude-plugin/marketplace.json` together.
