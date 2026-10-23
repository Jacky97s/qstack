---
name: qstack-init
description: "Create or refresh this project's qstack profile at .qstack/profile.md by interviewing the repository first and the operator second: domain, artifact identities, run commands per layer, environments and rigs, protected hosts and irreversible commands, data provisioning, conventions, evidence location, tracker, standards, and reviewers. Use for /qstack-init, setting up qstack in a repo, or when a playbook reports a missing profile slot."
---

# qstack-init

The profile is where everything project-specific lives, so the rest of qstack stays generic. Every playbook reads it first. A wrong slot misleads every later run, so a slot is filled only from evidence or from the operator, never from a guess.

## 1. Interview the repository

Answer what you can from the codebase and its documents, citing where each answer came from:

- **Domain:** software, firmware, hardware, manufacturing, data or ML, or a mix (`../q-mode/references/domains.md`).
- **Artifact identity:** how a tested artifact is identified (commit, image digest, firmware hash, hardware revision, serial, lot).
- **Layers and run commands:** the exact command for each layer that exists (unit, integration, end-to-end, simulation, rig), as CI runs them. Read the CI configuration, package scripts, makefiles, and test config.
- **Environments and rigs:** local, disposable, shared, and production, with how each is reached. Rigs, benches, stations, and device farms, with their doctor checks.
- **Conventions:** test layout, naming, fixtures, page or screen objects, factories, markers or tags, and assertion style. Note them as found, not as you would prefer.
- **Data:** how test data is provisioned and cleaned.
- **Evidence:** where reports, traces, screenshots, logs, and measurement records go.
- **Spec sources:** where requirements live, and whether a shift-left project folder exists.

## 2. Ask the operator only what the repository cannot show

Typical questions: which environments are shared or protected, which operations are destructive or irreversible, whether qstack may file tickets or only draft them, which standards and levels apply, the artifact language for reports, who reviews tests, and any safety rules for the lab. Ask them one at a time with a recommended answer.

## 3. Write the files

- `.qstack/profile.md` from `references/profile-template.md`. Every slot is filled, marked `n/a` with a reason, or marked `unknown` with the open question.
- `.qstack/protected-hosts`: one host per line, `#` for comments. The guard hook asks before mutating HTTP calls and test runs aimed at these hosts.
- `.qstack/protected-commands`: one regular expression per line for irreversible commands (fuse burning, OTP writes, debug lock, mass erase, production data scripts). The guard hook asks before matching Bash commands. The hook already covers common fuse, OTP, and lock commands, so add the project's own tools.
- `.qstack/playbooks/` only when the operator wants a project playbook. Follow the extension format in `../q-mode/SKILL.md`.

Never write secrets into these files. Point at where credentials live.

## 4. Prove it

Run one cheap command from the profile (the fastest test layer, or a rig doctor check) and confirm it behaves as the profile says. A profile whose commands were never run is a draft. Report which slots were verified by running, which were read from files, and which came from the operator.
