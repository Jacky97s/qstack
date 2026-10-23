---
name: qstack-setup
description: "Set up qstack for a user and a project. Writes the user settings file (session hook on or off) and, when the tester wants them, the project files: the profile with active lenses and run commands, protected hosts, and protected commands. Detects facts from the repository, confirms each choice, validates by running one command, and offers a harness. Use for /qstack-setup, setting up or changing qstack, turning the routing hook on or off, or when a playbook reports a missing profile slot."
---

# qstack setup

qstack works with no setup. This skill writes only the settings the tester chooses. Re-run it to change them. Every write replaces the whole file, so a second run gives the same result.

There are two scopes:

- **User scope:** `<config>/qstack.md`, where `<config>` is `$CLAUDE_CONFIG_DIR` when it is set and `~/.claude` otherwise. It holds the `session hook` line.
- **Project scope:** `.qstack/` in the repository root. It holds `profile.md`, `protected-hosts`, and `protected-commands`. All are optional.

## Steps

### 1. Detect

Find the facts from the repository and its documents. Cite where each fact came from. Do not guess a value.

- The lenses that apply, from `../q-mode/lenses/README.md`. Lenses stack.
- How a tested artifact is identified: commit, image digest, firmware hash, hardware revision, serial, lot, or dataset and checkpoint.
- The run command for each test layer, as CI runs it. Read the CI configuration, package scripts, makefiles, and test configuration.
- The environments and rigs, and how to reach each one.
- The test conventions: layout, naming, fixtures, helpers, tags, and assertion style.
- How test data is made and removed.
- Where evidence goes: reports, traces, screenshots, logs, and measurement records.
- Where requirements live.

### 2. Load the current state

Read `<config>/qstack.md` and every file in `.qstack/` that exists. Use their values as the current choices. Mark each value that the repository now contradicts.

### 3. Confirm

Show the detected and current values in one table. Ask one question at a time, and give a recommended answer with each question. Use `AskUserQuestion` when it is available. Ask only what the repository cannot show:

1. Which project files to keep: none, profile only, or profile with protected hosts and commands.
2. Which lenses apply, when the detection is not clear.
3. Which environments are shared or protected, and which hosts go in `protected-hosts`.
4. Which operations are destructive or irreversible, and which commands go in `protected-commands`.
5. Whether qstack can file tickets, or only write drafts.
6. Which standards and levels apply, when the regulated lens is active.
7. The language for report prose.

### 4. Choose the session hook

The SessionStart hook tells each new session to route testing work to `qstack:q-mode`. It is on by default. Ask whether to keep it on. The answer is the `session hook` line: `on` or `off`. `QSTACK_SESSION_HOOK=off` in the environment also turns it off for one shell.

### 5. Validate

- Run one cheap command from the profile, for example the fastest test layer or a rig doctor check. Record whether it behaved as the profile says.
- Compile each line of `protected-commands` as a regular expression. Fix or remove each line that does not compile.
- Make sure no file contains a secret. A file can point to where a credential lives. It must not contain the credential.

If a check fails, tell the tester and ask again. Do not write a value that failed.

### 6. Write

Write only the files the tester chose.

User settings, `<config>/qstack.md`:

```markdown
# qstack settings

session hook: on
```

Project files:

- `.qstack/profile.md` from `references/profile-template.md`. Fill every slot, or write `n/a: <reason>` or `unknown: <open question>`.
- `.qstack/protected-hosts`: one host for each line. Lines that start with `#` are comments.
- `.qstack/protected-commands`: one regular expression for each line. The guard hook already asks before common fuse, OTP, debug-lock, and mass-erase commands. Add the project's own tools.

### 7. Confirm the result

Tell the tester:

- Which files you wrote, and where.
- Whether the session hook is on or off.
- Which values you verified by a run, which you read from files, and which came from the tester.

### 8. Offer a harness (optional)

When the project has no repeatable way to set up, check, drive, and observe the system under test, offer one time: "Do you want a harness, so agents can drive the system and prove results? I can make one with `qstack:create-harness`." If the tester says yes, use **create-harness**. If the tester says no, continue.
