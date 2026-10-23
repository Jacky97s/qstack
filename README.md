<div align="center">

# qstack

**Tests are claims. qstack makes the agent prove them.**

*Inspired by [Lauren Tan's pstack](https://github.com/cursor/plugins/tree/main/pstack), and by [Michael Denyer's Claude Code port](https://github.com/michael-denyer/pstack-claude). MIT licensed.*

A quality-engineering operating mode for AI agents, for any field: software, firmware, hardware, manufacturing, performance, GenAI, model training, data, security, and regulated products.

[Why](#why) · [The idea](#the-idea) · [What you get](#what-you-get) · [Install](#install) · [Use](#use) · [Optional project files](#optional-project-files) · [Credits](#credits)

</div>

---

qstack turns a coding agent into a skeptical tester. It names the oracle before it writes a check. It ranks work by risk. It classifies a red result before touching it, proves its own checks can fail, refuses to retry its way to green, keeps its hands off shared environments and irreplaceable units, and reports every verdict with evidence you can rerun.

pstack showed that an agent gets better at *all* development work when you encode how to work rather than what each technology looks like. qstack applies the same idea to verification.

## Why

AI made writing tests cheap. It did not make them trustworthy.

- **Generated tests look better than they are.** They reach high coverage with weak assertions, and often copy current behavior as the expected value, which locks in today's bugs ([AugmenTest](https://arxiv.org/html/2501.17461v1), [mutation-guided generation at Meta](https://arxiv.org/html/2501.12862v1)).
- **Adoption is broad and shallow.** 89% of organizations pilot or deploy generative AI in quality engineering, and 15% have scaled it ([World Quality Report 2025-26](https://www.capgemini.com/resources/world-quality-report-2025)).
- **The bottleneck moved from authoring to judgment.** Deciding what to test, trusting what was generated, triaging failures at scale, measuring nondeterministic systems, and keeping agents from damaging shared environments.

Most QA skill packs teach an agent how to write a Playwright test. qstack teaches it how to know a result is right, in any field, and how to prove that to someone else.

## The idea

Testing a REST endpoint, an OTA update, a sensor board in a thermal chamber, an end-of-line station, a fine-tuned model, and a service under load looks like six different jobs. It is one job with different parameters.

**One core loop, the same in every field:**

```
claim → risk → oracle → design → prove the instrument → run → read → verdict → decide → learn
```

**Eight slots that differ between fields,** supplied by a lens:

| Slot | API under load | Circuit board DVT | Fine-tuned model |
|------|----------------|-------------------|------------------|
| Artifact identity | Image digest | Hardware revision, serials, lot | Dataset hashes, checkpoint |
| Stimulus and observation | Arrival rate, latency histograms | Supply, temperature, signals | Eval sets, predictions by slice |
| Instruments and trust | Generator not the bottleneck | Calibration, gauge R&R | Metric checked on a known case |
| Variation and sampling | Warm-up, repetitions | Unit-to-unit, corners | Seeds, confidence intervals |
| Cost and reversibility | Shared environment at risk | Destructive tests consume units | Compute cost |
| Oracle sources | SLOs | Specification, standards | Held-out labels |
| Gates and standards | Release gate | EVT, DVT, PVT, EMC | Launch review, EU AI Act |
| Layer ladder | Micro-benchmark → system → shadow traffic | Simulation → board → chamber | Sanity run → small run → full run → A/B |

**Playbooks by kind of work, never by field.** A triage is a triage whether the failing check is a unit test or an end-of-line station. Adding a new field means adding one lens file, not a new process. Anything no playbook fits goes to **Design the verification**, which runs the core loop explicitly.

## What you get

| | |
|---|---|
| **`q-mode`** | The entry point: the core loop, non-negotiables, the principle index, lenses, the playbook router, autonomy and subagent rules, and the reporting format. |
| **17 playbooks** | By kind of work. See [the table below](#playbooks). |
| **10 lenses** | `software`, `firmware`, `hardware`, `manufacturing`, `performance`, `genai`, `ml-training`, `data`, `security`, and the `regulated` overlay. They stack. |
| **16 principles** | Short, model-only rules the agent reads in full and cites when they change a decision. |
| **6 workflow skills** | `create-harness`, `test-design-techniques`, `mutation-check`, `test-review`, `grill-the-plan`, `qstack-init`. |
| **2 agents** | `test-reviewer` reviews checks it did not write. `adversarial-tester` tries to break a feature on an approved environment. |
| **Guard hook** | Blocks new fixed sleeps and reasonless skips in test code. Asks before mutating protected hosts or running irreversible device commands such as fuse burning. |
| **References and scripts** | Spec-audit method, Given/When/Then rules, failure taxonomy, flaky causes, exploration and oracle heuristics, the AI eval method, and reliability statistics. Scripts for spec-audit coverage, case linting, and coverage checks. |

### Principles

| Deciding what to test | Building checks worth trusting | Reading results honestly | Operating safely |
|---|---|---|---|
| Oracle First | Test Behavior, Not Implementation | Evidence, Not Claims | Protect Shared Environments |
| Risk Before Coverage | Deterministic Tests | Classify Before You Fix | |
| Cheapest Layer That Catches It | Isolate Test Data | Flaky Is a Bug | |
| Label the Unknowns | Author Is Not Approver | Reproduce Before Report | |
| | | Measure Variation | |
| | | Trust the Instrument | |
| | | Explain the Number | |

### Playbooks

| Before the work | Building and running checks | When something fails | Deciding and learning |
|---|---|---|---|
| Investigation | Test design | Failure triage | Gate review |
| Risk analysis (FMEA) | Automate | Flaky triage | Suite audit |
| Requirements review | Test campaign | Bug report | Escaped defect (8D) |
| Test plan | Exploratory session | | Design the verification |
| Shift-left | Change impact | | |

## Install

**Claude Code**

```sh
claude plugin marketplace add Jacky97s/qstack
claude plugin install qstack@qstack
```

From a local clone:

```sh
git clone https://github.com/Jacky97s/qstack.git
claude plugin marketplace add ./qstack
claude plugin install qstack@qstack
```

**Other agents.** Anything that reads the Agent Skills format can use `skills/` directly. The agents and hooks are Claude Code features. Without them, the principles still carry the rules, without enforcement.

**Requirements.** `python3` for the guard hook and the scripts. No other dependencies.

## Use

Ask in plain words. The session hook sends qualifying tasks to `q-mode`, which picks the lenses and the playbook.

| You say | Lenses | Playbook |
|---------|--------|----------|
| "Why is `checkout.spec.ts` failing in CI?" | software | Failure triage |
| "This test fails one run in ten." | software | Flaky triage |
| "Write API tests for the refund endpoint." | software | Automate, with a mutation check and a fresh review |
| "Audit this PRD before sprint planning." | software | Requirements review |
| "Turn this spec set into traceable test cases." | software | Shift-left |
| "Can the API hold 2,000 requests per second?" | performance | Test campaign |
| "Run an FMEA on the battery charger." | hardware | Risk analysis |
| "Plan DVT for the new sensor board." | hardware | Test plan, then Test campaign |
| "OTA updates brick some devices." | firmware | Bug report, then Escaped defect |
| "Is the end-of-line station catching bad units?" | manufacturing | Suite audit |
| "Is our chatbot good enough to ship?" | genai | Test campaign, then Gate review |
| "Did fine-tuning actually help?" | ml-training | Test campaign |
| "What does this supplier change put at risk?" | hardware, manufacturing | Change impact |
| "Prepare the IEC 62304 evidence for release." | software, regulated | Gate review |
| "How would we even test this?" | any | Design the verification |

Direct entries: `/qstack:q-mode`, `/qstack:create-harness`, `/qstack:test-review`, `/qstack:mutation-check`, `/qstack:test-design-techniques`, `/qstack:grill-the-plan`, `/qstack:qstack-init`.

Set `QSTACK_SESSION_HOOK=off` to turn off the routing mandate without uninstalling.

## How it works

```
 session start ──▶ routing mandate injected
                         │
 your request ─────▶ q-mode ──▶ project profile and harness, when the team keeps them
                         │
                         ├──▶ active lenses fill the eight slots
                         ├──▶ playbook steps copied into the todo list
                         ├──▶ principles read and cited where they change a decision
                         ├──▶ the work runs on the real artifact
                         │       └──▶ guard hook: no sleeps, no bare skips,
                         │            ask before protected hosts and irreversible commands
                         ├──▶ proof: seen to fail (mutation-check), fresh review
                         │    (test-reviewer), samples with spread, instruments proven
                         └──▶ VERIFIED / FAILED / INCONCLUSIVE / BLOCKED / NOT RUN,
                              with commands to rerun and paths to evidence
```

## Optional project files

qstack helps the tester. It does not decide how the team stores or uses its outputs, and it creates no tracking files or process documents unless asked. Results go in the reply or wherever the tester says.

A team that wants qstack to remember project facts can keep any of these. All are optional.

| File | Purpose |
|------|---------|
| `.qstack/profile.md` | Active lenses, artifact identity, run commands per layer, environments and rigs, conventions, test data, evidence paths, tracker policy, standards, reviewers. Generate it with `/qstack:qstack-init`. |
| `.qstack/harness.md` | How to set up, check, drive, observe, and clean up the system under test, proven by running it. Generate it with `/qstack:create-harness`. |
| `.qstack/protected-hosts` | Hosts the guard protects from mutating calls and test runs. One per line. |
| `.qstack/protected-commands` | Regular expressions for your irreversible commands. One per line. |
| `.qstack/playbooks/*.md` | Project playbooks that extend bundled ones, anchored to quoted step text with `**After**`, `**Before**`, `**Replace**`, or `**In**`. |

A new field is a new lens in `skills/q-mode/lenses/`, with eight slots and the domain's risks, failure classes, and playbook notes. `scripts/validate.py` checks its shape.

After upgrading qstack, run `python3 <plugin>/scripts/check_playbooks.py` from your repository root to see whether any project playbook's anchor text moved.

## With pstack

qstack works alone. You do not need pstack.

If you install the two plugins, they do different tasks:

- pstack changes the product code. It fixes defects, adds features, and changes the structure of the code.
- qstack does the verification. It finds the risks, makes and runs the tests, and gives the verdict.

Example: a test fails in CI.

1. qstack finds the type of the failure.
2. If the product has a defect, qstack writes the defect report and the steps to reproduce it.
3. pstack fixes the code.
4. qstack does the same steps again in the same environment. Then it gives the verdict.

If you do not install pstack, change the code with your usual method. qstack does the verification in the same way.

## Develop

```sh
python3 scripts/validate.py              # structure, links, indexes, lens shape, manifests
python3 -m unittest discover -s tests    # guard hook, scripts, validator
```

See [CONTRIBUTING.md](CONTRIBUTING.md).

## Sources

- Luo et al., "An Empirical Analysis of Flaky Tests" (FSE 2014) and later studies: the flaky cause taxonomy ([multivocal review](https://arxiv.org/pdf/2212.00908)).
- Foster et al., "Mutation-Guided LLM-based Test Generation at Meta" (FSE 2025): targeted mutants as the check on generated tests ([arXiv](https://arxiv.org/html/2501.12862v1)).
- Anthropic, "Demystifying evals for AI agents": tasks, trials, graders, transcripts, pass@k and pass^k ([post](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents)).
- Google's ML Test Score rubric, and the REFORMS reporting standards on leakage ([arXiv](https://arxiv.org/pdf/2308.07832)).
- Gil Tene on coordinated omission, and the [k6 notes on open and closed workload models](https://grafana.com/docs/k6/next/using-k6/scenarios/concepts/open-vs-closed/).
- James Bach's Heuristic Test Strategy Model (SFDIPOT, HICCUPPS) and session-based test management. James Whittaker's exploratory tours.
- AIAG-VDA FMEA Handbook (2019), AIAG MSA guidance, ISO 2859-1 attribute sampling, the 8D discipline, and OWASP ASVS and WSTG.
- The [TestRail Software Testing and Quality Report](https://content.testrail.com/hubfs/Downloadables/Fourth-Edition-Software-Testing-and-Quality-Report.pdf) on where teams struggle.

## Credits

qstack is inspired by **[pstack](https://github.com/cursor/plugins/tree/main/pstack) by Lauren Tan**, and by **[pstack for Claude Code](https://github.com/michael-denyer/pstack-claude) by Michael Denyer**. From pstack come the architecture (a routing skill whose playbooks are copied into a todo list, model-only principle leaf skills, a session-start routing mandate, and project playbooks anchored to quoted step text), the two principles Test Behavior, Not Implementation and Explain the Number, and the shape of `create-harness`, which generalizes pstack's verification-skill generator.

pstack is MIT licensed. Its license texts are in [`licenses/`](licenses/), and [`NOTICE`](NOTICE) lists exactly what qstack takes from it.

## License

[MIT](LICENSE). Copyright (c) 2026 Jacky Tan, Lauren Tan, and Michael Denyer.
