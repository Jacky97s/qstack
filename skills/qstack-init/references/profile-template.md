# qstack profile — <project>

> Every qstack playbook reads this file. Fill every slot, or mark it `n/a: <reason>` or `unknown: <open question>`.
> Do not put secret values here. Point to the place where they are.

## Lenses

- **Active lenses:** <one or more of: software, firmware, hardware, manufacturing, performance, genai, ml-training, data, security, regulated>
- **Product and users:** <one line>
- **Standards and levels:** <e.g. none, WCAG 2.2 AA, ISO 26262 ASIL B, IEC 62304 class B>
- **Report language:** <language for prose; machine tokens stay English>

## Artifact identity

- **How a tested artifact is identified:** <commit SHA, image digest, firmware hash, hardware revision, serial, lot>
- **Where to read it at test time:** <command or location>

## Layers and commands

| Layer | Command | Typical runtime | Notes |
|-------|---------|-----------------|-------|
| unit | `<cmd>` | <time> | |
| integration / API | `<cmd>` | <time> | |
| end-to-end | `<cmd>` | <time> | <parallel mode used in CI> |
| simulation / HIL / rig | `<cmd>` | <time> | <doctor check command> |

- **CI:** <where it runs, which jobs must pass before a merge>
- **Repeat or stress option:** <e.g. `--repeat-each`, `pytest --count`, rig loop command>

## Environments and rigs

| Name | Kind | How to reach | Shared? | Protected? |
|------|------|--------------|---------|------------|
| local | disposable | `<cmd>` | no | no |
| staging | shared | <url> | yes | yes |
| production | production | <url> | yes | read-only only |
| <rig or station> | lab | <how> | <yes/no> | <yes/no> |

- **Protected hosts file:** `.qstack/protected-hosts`
- **Protected commands file:** `.qstack/protected-commands`
- **Destructive or irreversible operations needing per-run approval:** <list>
- **Lab safety rules:** <pointer>

## Test data

- **Provisioning:** <factories, seed scripts, API setup, fixtures>
- **Cleanup:** <how>
- **Accounts and roles:** <pointer to where test accounts are defined, never passwords>
- **Personal data policy:** synthetic only

## Conventions

- **Layout:** <folders>
- **Naming:** <test and case naming convention>
- **Fixtures and helpers:** <page objects, factories, helper inventory>
- **Tags or markers:** <smoke, regression, ...>
- **Assertion style:** <library and idioms>

## Harness

- **Harness:** `.qstack/harness.md` <or `n/a: <reason>`>

## Evidence

- **Reports, traces, screenshots, logs:** <paths>
- **Measurement and calibration records:** <where, for physical work>

## Requirements and traceability

- **Spec sources:** <where requirements live>
- **Requirement ID format:** <e.g. AC-123, REQ-4.2>

## Tracker and people

- **Tracker:** <tool and project>
- **qstack can file tickets:** <yes | draft only>
- **Test reviewers:** <who reviews tests and plans>
- **Release decision owner:** <role>
