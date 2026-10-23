---
name: qstack-init
description: "Create or refresh the qstack profile of this project at .qstack/profile.md. Interview the repository first and the operator second. The profile covers: active lenses, artifact identities, run commands per layer, environments and rigs, protected hosts and irreversible commands, data provisioning, conventions, evidence location, tracker, standards, and reviewers. Use for /qstack-init, to set up qstack in a repo, or when a playbook reports a missing profile slot."
---

# qstack-init

The profile holds everything that is specific to the project. This keeps the rest of qstack generic. Every playbook reads the profile first. A wrong slot misleads every later run. Fill a slot only from evidence or from the operator. Do not guess.

## 1. Interview the repository

Answer what you can from the codebase and its documents. Cite the source of each answer:

- **Lenses:** which of the lenses in `../q-mode/lenses/README.md` apply (software, firmware, hardware, manufacturing, performance, genai, ml-training, data, security, and the regulated overlay). Lenses combine.
- **Artifact identity:** how to identify a tested artifact (commit, image digest, firmware hash, hardware revision, serial, lot).
- **Layers and run commands:** the exact command for each layer that exists (unit, integration, end-to-end, simulation, rig), as CI runs them. Read the CI configuration, package scripts, makefiles, and test configuration.
- **Environments and rigs:** local, disposable, shared, and production, with the way to reach each one. Also rigs, benches, stations, and device farms, with their doctor checks.
- **Conventions:** test layout, naming, fixtures, page or screen objects, factories, markers or tags, and assertion style. Write them as you find them. Do not write your own preference.
- **Data:** how the team provisions and cleans test data.
- **Evidence:** where reports, traces, screenshots, logs, and measurement records go.
- **Spec sources:** where requirements live.

## 2. Ask the operator only what the repository cannot show

Typical questions are:
- Which environments are shared or protected?
- Which operations are destructive or irreversible?
- Can qstack file tickets, or can it only draft them?
- Which standards and levels apply?
- What is the artifact language for reports?
- Who reviews tests?
- Which safety rules apply to the lab?

Ask the questions one at a time. Give a recommended answer with each question.

## 3. Write the files

- `.qstack/profile.md` from `references/profile-template.md`. Fill every slot, or mark it `n/a` with a reason, or mark it `unknown` with the open question.
- `.qstack/protected-hosts`: one host per line, `#` for comments. The guard hook asks for approval before it allows mutating HTTP calls and test runs that target these hosts.
- `.qstack/protected-commands`: one regular expression per line for irreversible commands (fuse burning, OTP writes, debug lock, mass erase, production data scripts). The guard hook asks for approval before it allows a Bash command that matches. The hook already covers common fuse, OTP, and lock commands. Add the tools of the project.
- `.qstack/playbooks/` only when the operator wants a project playbook. Use the extension format in `../q-mode/SKILL.md`.

Do not write secrets into these files. Point to the place where the credentials are.

## 4. Prove it

Run one cheap command from the profile (the fastest test layer, or a rig doctor check). Make sure that it behaves as the profile says. A profile with commands that nobody ran is a draft. Report which slots you verified by a run, which slots you read from files, and which slots came from the operator.

If the project has no repeatable way to set up, check, drive, and observe the system under test, offer the **create-harness** skill next.
