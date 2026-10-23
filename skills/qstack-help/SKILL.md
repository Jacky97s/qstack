---
name: qstack-help
description: "Help with qstack: how to set it up, how to start a testing task, which playbook, lens, or skill fits a situation, how to fix a run that went wrong, and how to extend qstack. Answers the question and gives one request the tester can send. Use for /qstack-help, 'how do I use qstack', 'what can qstack do', or 'which playbook fits'."
---

# qstack help

Answer the tester's question about qstack. Give one request that the tester can send, and name the file that the answer came from.

A help question does not start the work. The tester asked how, and a qstack run uses real tokens and can touch real systems. Give the request, and let the tester send it.

A message that asks for work, for example "use qstack to triage this failing test", is not a help question. Read `../q-mode/SKILL.md` and do the work under it.

Read the source file before you answer. The installed files are the authority. This map only points to them.

## Find what the tester needs

Find the need from the message and the conversation. If the need is not clear, ask one multiple-choice question with these options. Then answer only the section that the tester picks.

- Set up qstack
- Start a testing task
- Pick a playbook, lens, or skill for a situation
- Fix a run that went wrong
- Extend qstack

Examine the state that changes the answer, and mention it only when it changes the answer:

- The installed version. Compare the plugin cache version with the `version` in the repository's `.claude-plugin/plugin.json` when both are available. An old cache means the tester does not have recent changes.
- The user settings file `<config>/qstack.md` and its `session hook` line.
- The project files in `.qstack/`. None of them is required.

## Set up qstack

1. Give the install commands from the README: `claude plugin marketplace add <owner>/qstack`, then `claude plugin install qstack@qstack`. To update, run `/plugin update qstack@qstack` and then `/reload-plugins`.
2. Tell the tester that qstack works with no setup. `/qstack:qstack-setup` writes the optional files and the `session hook` setting. Read `../qstack-setup/SKILL.md` before you explain them.
3. Give a first request with a goal and a check that can pass or fail. Use `references/prompting.md`.

## Start a testing task

Describe the task in plain words. The session hook routes it to `qstack:q-mode`. Without the hook, type `/qstack:q-mode` and the task. q-mode picks the lenses and the playbook, copies the playbook steps into the todo list, and reads the principles that it applies.

A good request states the claim, the system, and how to tell the result is right. Do not list skills or steps. A written sequence often drops steps that the playbook keeps. Read `references/prompting.md` before you help the tester write one.

## Pick a playbook, lens, or skill

The default answer is to describe the task and let q-mode route it. Name a playbook, lens, or skill directly when the tester wants it. Read it before you recommend it, and give one example request.

| The tester wants to | Use |
|---|---|
| Know how something is tested now, or how sure we are | Investigation playbook |
| Find how a design, feature, or process can fail | Risk analysis playbook (FMEA) |
| Find defects in a story or spec before work starts | Requirements review playbook |
| Plan the testing for a feature, release, build phase, or model | Test plan playbook |
| Turn a full spec set into traceable cases | Shift-left playbook |
| Get test cases for a requirement or risk | Test design playbook, `qstack:test-design-techniques` |
| Write automated tests, evals, rig scripts, or station programs | Automate playbook |
| Run load, stress, soak, environmental, or eval runs | Test campaign playbook |
| Explore a running system for defects | Exploratory session playbook |
| Know what a change can break and what to run again | Change impact playbook |
| Understand failing checks | Failure triage playbook |
| Fix a check that passes and fails on the same artifact | Flaky triage playbook |
| Report a defect | Bug report playbook |
| Decide go or no-go at a release or gate | Gate review playbook |
| Know how much to trust a suite, eval set, or station | Suite audit playbook |
| Find why a defect reached users, with 8D | Escaped defect playbook |
| Verify something that no playbook fits | Design the verification playbook |
| Prove that tests can catch a defect | `qstack:mutation-check` |
| Get a fresh review of tests | `qstack:test-review`, `qstack:test-reviewer` agent |
| Attack a feature on an approved environment | `qstack:adversarial-tester` agent |
| Get a repeatable way to drive the system | `qstack:create-harness` |
| Stress-test a plan or process with questions | `qstack:grill-the-plan` |
| Set up qstack | `qstack:qstack-setup` |

The lenses are in `../q-mode/lenses/README.md`. Lenses stack.

Close calls:

- Failure triage classifies every failing check. Flaky triage starts when a check passes and fails on the same artifact.
- Test plan covers a feature or release. Shift-left starts from a full spec set and keeps traceability to each requirement.
- Requirements review covers one story or change. Shift-left Stage 0 audits a full spec set with coverage verification.
- The genai lens covers a model that you use in a product. The ml-training lens covers a model whose weights you change.
- Test campaign is for many trials, units, or conditions. Automate is for checks that run as part of a suite.

Playbooks have no slash command. Describe the task, or name the playbook in the request, for example "run the flaky triage playbook on `checkout.spec.ts`". Principles are model-only rules that q-mode reads. You can steer with their names, for example "apply trust the instrument. Show me the known-bad run."

## Fix a run that went wrong

| Symptom | Fix |
|---|---|
| qstack did not start for a testing task | Examine the `session hook` line in `<config>/qstack.md` and `QSTACK_SESSION_HOOK`. Or type `/qstack:q-mode` and the task. |
| A new skill or change is missing | The installed version is old. Run `/plugin update qstack@qstack`, then `/reload-plugins`. To test local source, start with `claude --plugin-dir <path-to-qstack>`. |
| The guard blocked a legitimate line | Add `qstack: allow-sleep <reason>` or a skip reason with a ticket on the same line. Report a false positive as a qstack defect. |
| The verdict has no evidence | Ask for the command, the artifact identity, and the trimmed output. That is **principle-evidence-not-claims**. |
| It changed a test to make it pass | Ask for the failure class and the oracle source. That is **principle-classify-before-you-fix**. |
| It made files that you did not ask for | Tell it where you want the output. q-mode must not make tracking files or process documents. |
| It touched a shared environment | Add the hosts to `.qstack/protected-hosts`. Tell it the environment is protected. |
| The run took too many tokens | Ask for one playbook and one lens. Use a cheaper model for the session. Do not ask for a full matrix or multi-model review unless you need it. |

## Extend qstack

- A new field is a new lens in `../q-mode/lenses/`, with the eleven headings that `../q-mode/lenses/README.md` lists.
- A project step is a project playbook in `.qstack/playbooks/`. Read the Project playbooks paragraph in `../q-mode/SKILL.md`.
- A recurring correction becomes structure: a guard rule, a lint, or a validator check. Read `CONTRIBUTING.md` in the qstack repository.

## Reply

Give the answer first. Give at most one example request in a code block, from `references/prompting.md` when one fits. Then name the source file. Keep the reply short, unless the tester asks for the full map.
