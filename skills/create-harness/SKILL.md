---
name: create-harness
description: "Generate, prove, and maintain the verification harness of a project. The harness is the scripted way for an agent to set up the system under test, check that it is fit to test, drive it, capture evidence, and clean up. Works for web apps, APIs, CLIs, firmware rigs, lab benches, production stations, data pipelines, and eval runners. Use for /create-harness, when a project has no repeatable way to prove behavior, or to refresh a harness that drifted."
---

# Create harness

Every playbook ends in "verify on the real artifact". The harness makes that repeatable for this project. It is one place that tells how to:
- start the system
- prove that it is worth testing
- act on it
- observe it
- shut it down

You write it for the next agent. That agent reads it with no context in the middle of a task.

The harness is in `.qstack/harness.md`. Any scripts that it includes are under `.qstack/harness/`. Record its path in `.qstack/profile.md`.

## 1. Interview the repository and the setup

Answer from the codebase, CI configuration, documents, and lab notes first. Ask the operator only about what you cannot observe.

- **Surface:** what the user or the next system touches, such as:
  - a UI
  - an API
  - a CLI
  - device pins and buses
  - a physical product
  - a station
  - a dataset
  - a model endpoint

  Pick the primary surface. Write down the others.
- **Setup:** how to bring it to a usable state from nothing. This includes start commands, migrations, seed data, flashing a known image, powering a rig, loading a station program, and staging an eval set. Ready means usable. It does not mean only that a process answers.
- **Doctor:** one read-only check that answers "is this instance worth testing now?" It checks that:
  - the process is up
  - the version or image hash is correct
  - we own the port
  - auth is valid
  - the rig connections and power state are correct
  - the instrument calibration is in date
  - the station passes its golden unit
- **Drive:** the real commands, selectors, bus commands, or procedures from this project. Do not use examples. Use stable handles when you can (roles, labels, test ids, command names, register maps).
- **Observe:** which evidence exists and where it goes (screenshots, traces, responses, logs, bus captures, measurements, station records, transcripts).
- **Known-bad case:** a way to make the harness see a failure on purpose, such as:
  - a broken build
  - a planted mutant
  - a limit sample
  - a corrupted fixture
  - a deliberately wrong answer for a grader

  A harness that cannot show a failure is not proven (**principle-trust-the-instrument**).
- **Isolation and safety:** can two runs share the system? What must you never touch (protected hosts, irreversible commands, shared units)? Write this in the harness.

If the setup does not work as documented, fix it. Or report exactly what fails before you write the harness. A harness that you write against a broken base teaches wrong steps.

## 2. Write `.qstack/harness.md`

Start from `references/harness-template.md`. Base every section on what the interview found. Leave no placeholders. The sections are: Setup, Doctor, Drive, Observe, Known-bad, Cleanup, Safety, and a capability map. The capability map lists the top three to five user-facing capabilities. For each one, give how to reach it, how to drive it, and the observable end state that proves it works. Make each script in the harness executable. Show how to run it in the harness.

Cleanup removes what the run created. It does not remove the evidence. Do not kill a process by its name. Do not power-cycle shared equipment. Stop only what you started.

## 3. Prove it

Run the harness one time from start to end. Do these steps:

1. Run setup and doctor.
2. Drive one capability.
3. Capture evidence.
4. Run the known-bad case and see it fail.
5. Clean up.
6. Make sure the evidence still exists.

Fix what fails. Clean up after every failed attempt. A harness that nobody executed is a draft. If you proved it on a stand-in, list what the stand-in did that the real target does not do. A stand-in is a local stack instead of staging, or a dev board instead of the product. Those steps stay unverified.

## 4. Maintain it

Run a refresh pass when the product changes or when a playbook reports harness drift:

1. Compare the capability map again with the source and the current product. Flag drift and cite the source.
2. Run doctor. Then drive every capability one time. For servers and rigs, do this one after the other on one instance. For short-lived tools, use fresh sessions.
3. Triage each problem. A wrong description is harness drift: fix the harness. Behavior that the harness cannot drive is a harness gap: extend the harness. Broken behavior is a product defect: report it through the **Bug report** playbook. Do not hide it in the harness.
4. Prove every fix again on the live system before you accept it. Report the outcome as clean, changed, or blocked, with coverage.
