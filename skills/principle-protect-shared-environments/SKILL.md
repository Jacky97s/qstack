---
name: principle-protect-shared-environments
description: "Apply to any action against staging, shared QA, production, third-party sandboxes, shared lab equipment, devices, or real people. You can read freely. Mutating calls, bulk data changes, messages to real users, irreversible device operations, destructive physical tests, load tests, and security scans need the explicit approval of the operator for that run and a written scope."
user-invocable: false
---

# Protect Shared Environments

Shared environments hold the data, demos, and in-progress tests of other people. A test run can delete accounts, revoke tokens, send messages, brick a prototype, or burn a one-time fuse. That can cost more than the bug that the run looked for.

- **Prefer disposable.** Use these first: local instances, per-run containers, ephemeral preview environments, and seeded test tenants.
- **Know the protected list.** `.qstack/profile.md` names the protected environments and the destructive operations, such as:
  - deletes
  - payments
  - refunds
  - logout or token revocation
  - bulk updates
  - notifications to real recipients

  The guard hook asks before Bash calls that send mutating requests to listed hosts. Apply the same rule where the hook cannot see: browser automation, MCP tools, and test runners that point at a shared base URL.
- **Ask per run, with the list.** Before a run that includes destructive operations against a shared environment, list the operations. Get an explicit yes for this run. Approval for one run does not apply to the next run.
- **Production is read-only** unless the operator authorized a specific action. Post-release checks are read-only smoke tests.
- **No real people.** Tests must not send real SMS, email, or push messages. Tests must not make real charges. Use sandboxes, mocks, or read-back paths.
- **Load and security testing need written authorization** of target, scope, time window, and rate. Without it, plan the test and stop.
- **Irreversible device operations need a yes for each unit.** These operations include:
  - burning eFuses or OTP
  - locking bootloaders or debug ports
  - mass erase of a unit that you cannot reflash
  - writing calibration or identity data

  They also include anything else that you cannot undo. The guard hook asks before commands that match `.qstack/protected-commands`.
- **Destructive physical tests consume samples.** Drop, crush, HALT to destruction, and teardown use up units that the team can need for other tests. Confirm the sample allocation first.
- **The safety of people comes before the test.** These hazards follow the safety rules of the lab:
  - high voltage
  - mains power
  - lithium cells under stress
  - lasers
  - RF exposure
  - moving machinery
  - thermal chambers

  An agent must never tell anyone to bypass an interlock.
- **Secrets stay pointers.** Say where a credential lives. Do not print, commit, or paste its value into a report.
