---
name: principle-protect-shared-environments
description: "Apply to any action against staging, shared QA, production, third-party sandboxes, shared lab equipment, devices, or real people. Read freely, but mutating calls, bulk data changes, messages to real users, irreversible device operations, destructive physical tests, load tests, and security scans need the operator's explicit approval for that run and a written scope."
user-invocable: false
---

# Protect Shared Environments

Shared environments hold other people's data, demos, and in-flight testing. A test run that deletes accounts, revokes tokens, sends messages, bricks a prototype, or burns a one-time fuse can cost more than the bug it was looking for.

- **Prefer disposable.** Local instances, per-run containers, ephemeral preview environments, and seeded test tenants come first.
- **Know the protected list.** `.qstack/profile.md` names the protected environments and the destructive operations (deletes, payments, refunds, logout or token revocation, bulk updates, notifications to real recipients). The guard hook asks before Bash calls that send mutating requests to listed hosts. Apply the same rule wherever the hook cannot see: browser automation, MCP tools, test runners pointed at a shared base URL.
- **Ask per run, with the list.** Before a run that includes destructive operations against a shared environment, list them and get an explicit yes for this run. Approval for one run does not carry to the next.
- **Production is read-only** unless the operator authorized a specific action. Post-release checks are read-only smoke.
- **No real people.** No real SMS, email, push, or charge from tests. Use sandboxes, mocks, or read-back paths.
- **Load and security testing need written authorization** of target, scope, time window, and rate. Without it, plan the test and stop.
- **Irreversible device operations need a yes per unit.** Burning eFuses or OTP, locking bootloaders or debug ports, mass erase of a unit you cannot reflash, writing calibration or identity data, and anything else that cannot be undone. The guard hook asks before commands matching `.qstack/protected-commands`.
- **Destructive physical tests consume samples.** Drop, crush, HALT to destruction, and teardown use up units the team may need for other tests. Confirm the sample allocation first.
- **People's safety comes before the test.** High voltage, mains power, lithium cells under stress, lasers, RF exposure, moving machinery, and thermal chambers follow the lab's safety rules. An agent never instructs anyone to bypass an interlock.
- **Secrets stay pointers.** Reference where a credential lives. Never print, commit, or paste its value into a report.
