---
name: create-harness
description: "Generate, prove, and maintain a project's verification harness: the scripted way an agent sets up the system under test, checks it is fit to test, drives it, captures evidence, and cleans up. Works for web apps, APIs, CLIs, firmware rigs, lab benches, production stations, data pipelines, and eval runners. Use for /create-harness, when a project has no repeatable way to prove behavior, or to refresh a harness that drifted."
---

# Create harness

Every playbook ends in "verify on the real artifact". The harness makes that repeatable for this project: one place that says how to bring the system up, prove it is worth testing, act on it, observe it, and tear it down. You write it for the next agent, who will read it cold in the middle of a task.

The harness lives in `.qstack/harness.md`, with any scripts it ships under `.qstack/harness/`. Record its path in `.qstack/profile.md`.

## 1. Interview the repository and the setup

Answer from the codebase, CI configuration, documents, and lab notes first. Ask the operator only what you cannot observe.

- **Surface:** what the user or the next system actually touches (a UI, an API, a CLI, device pins and buses, a physical product, a station, a dataset, a model endpoint). Pick the primary one, note the rest.
- **Setup:** how to bring it to a usable state from nothing: start commands, migrations, seed data, flashing a known image, powering a rig, loading a station program, staging an eval set. Ready means usable, not just that a process answers.
- **Doctor:** one read-only check that answers "is this instance worth testing right now?" (process up, right version or image hash, port owned by us, auth valid, rig connections and power state, instrument calibration in date, station passes its golden unit).
- **Drive:** the real commands, selectors, bus commands, or procedures, taken from this project, not examples. Prefer stable handles (roles, labels, test ids, command names, register maps).
- **Observe:** what evidence exists and where it goes (screenshots, traces, responses, logs, bus captures, measurements, station records, transcripts).
- **Known-bad case:** a way to make the harness see a failure on purpose (a broken build, a planted mutant, a limit sample, a corrupted fixture, a deliberately wrong answer for a grader). A harness that cannot show a failure is not proven (**principle-trust-the-instrument**).
- **Isolation and safety:** can two runs share the system? What must never be touched (protected hosts, irreversible commands, shared units)? Say so in the harness.

If the setup does not work as documented, fix it or report precisely what fails before writing the harness. A harness written against a broken base teaches wrong steps.

## 2. Write `.qstack/harness.md`

Start from `references/harness-template.md`. Every section is grounded in what the interview found, with no placeholders left: Setup, Doctor, Drive, Observe, Known-bad, Cleanup, Safety, and a capability map (the top three to five user-facing capabilities, each with how to reach it, how to drive it, and the observable end state that proves it works). Any script it ships is executable and its invocation is shown in the harness.

Cleanup removes what the run created and never the evidence. Never kill by process name and never power-cycle shared equipment: stop what you started.

## 3. Prove it

Run the harness once end to end: setup, doctor, drive one capability, capture evidence, run the known-bad case and see it fail, clean up, and confirm the evidence still exists. Fix what fails and clean up after every failed attempt. A harness that was never executed is a draft. If you proved it on a stand-in (a local stack instead of staging, a dev board instead of the product), list what the stand-in did that the real target will not. Those steps stay unverified.

## 4. Maintain it

Run a refresh pass when the product changes or when a playbook reports harness drift:

1. Re-read the capability map against the source and the current product. Flag drift with citations.
2. Run doctor, then drive every capability once, serially on one instance for servers and rigs, or in fresh sessions for short-lived tools.
3. Triage: a wrong description is harness drift (fix the harness), behavior the harness cannot drive is a harness gap (extend it), and behavior that is broken is a product defect (report it through the **Bug report** playbook, and never paper over it in the harness).
4. Re-prove every fix live before it lands. Report the outcome as clean, changed, or blocked, with coverage.
