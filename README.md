<div align="center">

# qstack

**Tests are claims. qstack makes the agent prove them.**

A quality-engineering operating mode for AI agents, for software, firmware, hardware, manufacturing, data, and regulated products.

[Why](#why) · [What you get](#what-you-get) · [Install](#install) · [Use](#use) · [How it works](#how-it-works) · [Customize](#customize-without-forking) · [Credits](#credits)

</div>

---

qstack turns a coding agent into a skeptical tester. It names the oracle before it writes a test. It ranks work by risk. It classifies a red test before touching it, proves its own tests can fail, refuses to retry its way to green, keeps its hands off shared environments, and reports every verdict with evidence you can rerun.

The same discipline holds for a REST endpoint, an OTA update path, a sensor board in a thermal chamber, an end-of-line test station, a data pipeline, or an LLM feature. Only the vocabulary, the layers, and the instruments change.

## Why

AI made writing tests cheap. It did not make them trustworthy.

- **Generated tests look better than they are.** They reach high coverage with weak assertions, and often copy current behavior as the expected value, which locks in today's bugs ([AugmenTest](https://arxiv.org/html/2501.17461v1), [mutation-guided generation at Meta](https://arxiv.org/html/2501.12862v1)).
- **Adoption is broad and shallow.** 89% of organizations pilot or deploy generative AI in quality engineering, and 15% have scaled it ([World Quality Report 2025-26](https://www.capgemini.com/resources/world-quality-report-2025)).
- **The bottleneck moved from authoring to judgment.** Deciding what to test, trusting what was generated, triaging failures at scale, measuring nondeterministic AI features, and keeping agents from damaging shared environments.

Most QA skill packs teach an agent how to write a Playwright test. qstack teaches it how to know a result is right, and how to prove that to someone else.

## What you get

| | |
|---|---|
| **`q-mode`** | The entry point: non-negotiables, a principle index, a router to 19 playbooks, autonomy rules, subagent rules, and a reporting format. |
| **19 playbooks** | Step-by-step procedures the agent copies into its todo list. See [the table below](#playbooks). |
| **15 principles** | Short, model-only rules the agent reads in full and cites when they change a decision. |
| **`shift-left`** | An eight-stage pipeline from spec to traceable artifacts, with script-verified spec-audit coverage, a Given/When/Then lint, and a generated traceability matrix. |
| **5 workflow skills** | `test-design-techniques`, `mutation-check`, `test-review`, `grill-the-plan`, `qstack-init`. |
| **2 agents** | `test-reviewer` reviews tests it did not write. `adversarial-tester` tries to break a feature on an approved environment. |
| **Guard hook** | Blocks new fixed sleeps and reasonless skips in test files. Asks before mutating protected hosts or running irreversible device commands such as fuse burning. |
| **References** | Failure taxonomy, flaky causes, exploration and oracle heuristics, the AI eval method, a domain map, reliability statistics, regulated-work pointers, and templates. |

### Principles

| Deciding what to test | Writing tests worth trusting | Reading results honestly | Operating safely |
|---|---|---|---|
| Oracle First | Test Behavior, Not Implementation | Evidence, Not Claims | Protect Shared Environments |
| Risk Before Coverage | Deterministic Tests | Classify Before You Fix | |
| Cheapest Layer That Catches It | Isolate Test Data | Flaky Is a Bug | |
| Label the Unknowns | Author Is Not Approver | Reproduce Before Report | |
| | | Measure Variation | |
| | | Trust the Instrument | |

### Playbooks

| Before the work | Building and running tests | When something fails | Deciding and learning |
|---|---|---|---|
| Investigation | Test design | Failure triage | Release readiness |
| Risk analysis (FMEA) | Automate | Flaky triage | Suite audit |
| Requirements review | Regression scope | Bug report | Escaped defect (8D) |
| Test plan | Exploratory session | | Compliance evidence |
| | AI feature testing | | |
| | Firmware testing | | |
| | Hardware validation | | |
| | Production quality | | |

## Install

**Claude Code**

```sh
claude plugin marketplace add Jacky97s/qstack
claude plugin install qstack@qstack
```

From a local clone:

```sh
git clone git@github.com:Jacky97s/qstack.git
claude plugin marketplace add ./qstack
claude plugin install qstack@qstack
```

**Other agents.** Anything that reads the Agent Skills format can use `skills/` directly. The agents and hooks are Claude Code features. Without them, the principles still carry the rules, without enforcement.

**Requirements.** `python3` for the guard hook and the scripts. No other dependencies.

## Use

Ask in plain words. The session hook sends qualifying tasks to `q-mode`, which picks the playbook.

| You say | qstack runs |
|---------|-------------|
| "Why is `checkout.spec.ts` failing in CI?" | Failure triage |
| "This test fails one run in ten." | Flaky triage |
| "Write API tests for the refund endpoint." | Automate, with a mutation check and a fresh review before it calls them done |
| "Audit this PRD before sprint planning." | Requirements review, or `shift-left` Stage 0 for a full spec set |
| "What should we retest for this diff?" | Regression scope |
| "Run an FMEA on the battery charger." | Risk analysis |
| "Plan DVT for the new sensor board." | Hardware validation |
| "OTA updates brick some devices." | Firmware testing, then Escaped defect |
| "Is the end-of-line station catching bad units?" | Production quality |
| "Is our chatbot good enough to ship?" | AI feature testing |
| "Are we ready to ship 4.2?" | Release readiness |
| "How good is our suite, really?" | Suite audit |

Direct entries: `/qstack:q-mode`, `/qstack:shift-left`, `/qstack:test-review`, `/qstack:mutation-check`, `/qstack:test-design-techniques`, `/qstack:grill-the-plan`, `/qstack:qstack-init`.

Set `QSTACK_SESSION_HOOK=off` to turn off the routing mandate without uninstalling.

## How it works

```
 session start ──▶ routing mandate injected (hooks/session-start.sh)
                         │
 your request ─────▶ q-mode ──▶ reads .qstack/profile.md
                         │
                         ├──▶ picks a playbook, copies its steps into the todo list
                         ├──▶ reads the principles it applies, cites them in the reply
                         ├──▶ does the work: drives the system, writes or runs tests
                         │       │
                         │       └──▶ guard hook: no sleeps, no bare skips,
                         │            ask before protected hosts and irreversible commands
                         │
                         ├──▶ proves it: seen to fail (mutation-check),
                         │    fresh review (test-reviewer), stability over N runs
                         │
                         └──▶ reports VERIFIED / FAILED / INCONCLUSIVE / BLOCKED / NOT RUN
                              with commands to rerun and paths to evidence
```

Three ideas carry most of the weight:

1. **The author is not the approver.** A generated test is a draft until it has been seen to fail against a broken version and reviewed by a context that did not write it.
2. **Classify before you fix.** A red test is product regression, test defect, contract drift, environment, data collision, flaky, rig or instrument, unit defect, build mismatch, or a known issue. Each class has its own action, and "edit the expected value until it passes" is not one of them.
3. **Trust the instrument first.** A harness that never failed, a probe out of calibration, an unverified station, and an uncalibrated LLM judge all print confident numbers.

## Customize without forking

Everything project-specific lives in your repository, not in qstack.

| File | Purpose |
|------|---------|
| `.qstack/profile.md` | Domain, artifact identities, run commands per layer, environments and rigs, conventions, test data, evidence paths, tracker policy, standards, reviewers. Generate it with `/qstack:qstack-init`. |
| `.qstack/protected-hosts` | Hosts the guard protects from mutating calls and test runs. One per line. |
| `.qstack/protected-commands` | Regular expressions for your irreversible commands. One per line. |
| `.qstack/playbooks/*.md` | Project playbooks that extend bundled ones. Changes anchor to quoted step text with `**After**`, `**Before**`, `**Replace**`, or `**In**`. |

After upgrading qstack, run `python3 <plugin>/scripts/check_playbooks.py` from your repository root. It reports any project playbook whose anchor text moved.

## With pstack

qstack runs on its own. With [pstack](https://github.com/cursor/plugins/tree/main/pstack) also installed, product-code changes go through pstack's workflows and qstack owns the test side and the verdict.

## Develop

```sh
python3 scripts/validate.py              # structure, links, indexes, manifests
python3 -m unittest discover -s tests    # guard hook, shift-left scripts, validator
```

See [CONTRIBUTING.md](CONTRIBUTING.md).

## Sources

- Luo et al., "An Empirical Analysis of Flaky Tests" (FSE 2014) and later studies: the flaky cause taxonomy ([multivocal review](https://arxiv.org/pdf/2212.00908)).
- Foster et al., "Mutation-Guided LLM-based Test Generation at Meta" (FSE 2025): targeted mutants as the check on generated tests ([arXiv](https://arxiv.org/html/2501.12862v1)).
- Anthropic, "Demystifying evals for AI agents": tasks, trials, graders, transcripts, pass@k and pass^k ([post](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents)).
- James Bach's Heuristic Test Strategy Model (SFDIPOT, HICCUPPS) and session-based test management. James Whittaker's exploratory tours.
- AIAG-VDA FMEA Handbook (2019), AIAG MSA guidance, ISO 2859-1 attribute sampling, and the 8D discipline.
- The [TestRail Software Testing and Quality Report](https://content.testrail.com/hubfs/Downloadables/Fourth-Edition-Software-Testing-and-Quality-Report.pdf) on where teams struggle.

## Credits

qstack's architecture comes from **[pstack](https://github.com/cursor/plugins/tree/main/pstack) by Lauren Tan**: a routing skill with playbooks copied into a todo list, model-only principle leaf skills, a session-start routing mandate, and project playbooks anchored to quoted step text. The Claude Code port, **[pstack-claude](https://github.com/michael-denyer/pstack-claude) by Michael Denyer**, showed how those pieces map onto plugins, agents, and hooks. One principle, Test Behavior, Not Implementation, is adapted from pstack.

pstack is MIT licensed. Its license texts are in [`licenses/`](licenses/), and [`NOTICE`](NOTICE) lists exactly what qstack takes from it.

## License

[MIT](LICENSE) © 2026 qstack contributors.
