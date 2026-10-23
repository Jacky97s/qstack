---
name: principle-isolate-test-data
description: "Apply to any test that reads or writes persistent state: databases, queues, files, accounts, caches, third-party sandboxes. Each test creates the data it needs, uses identifiers nobody else uses, and leaves nothing that changes another test's result."
user-invocable: false
---

# Isolate Test Data

Shared data turns independent tests into one fragile test. Most order-dependent and parallel-only failures are data collisions.

- **Create what you need.** Build preconditions through factories, API setup, or seed scripts inside the test or its fixture. Do not depend on records someone else created by hand.
- **Unique by construction.** Suffix names, emails, and keys with a run or worker identifier. Never rely on "the first row" or "the latest order".
- **Clean up, or use disposable state.** Tear down what the test created, or run against a per-run database, schema, tenant, or container. Cleanup failure must not mask the test's own result.
- **No shared mutable fixtures across workers.** Read-only reference data can be shared. Anything a test writes cannot.
- **Synthetic data only.** Never copy real customer or personal data into tests, fixtures, or reports. Mask anything that resembles it.
- **Tie data to the real schema.** Every field a test sets exists in the data model. Invented columns produce tests that pass against a fiction.
- **Know your provisioning method.** Seed script, direct insert, UI setup, or API setup. Name it, so a failure in setup is not mistaken for a product failure.
