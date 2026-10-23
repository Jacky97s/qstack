---
name: principle-isolate-test-data
description: "Apply to any test that reads or writes persistent state: databases, queues, files, accounts, caches, third-party sandboxes. Each test must create the data it needs, use identifiers that nobody else uses, and leave nothing that changes the result of another test."
user-invocable: false
---

# Isolate Test Data

Shared data turns independent tests into one fragile test. Data collisions cause most order-dependent and parallel-only failures.

- **Create what you need.** Build preconditions with factories, API setup, or seed scripts inside the test or its fixture. Do not depend on records that someone else created by hand.
- **Unique by construction.** Add a run or worker identifier as a suffix to names, emails, and keys. Do not rely on "the first row" or "the latest order".
- **Clean up, or use disposable state.** Tear down what the test created. Or run against a per-run database, schema, tenant, or container. A cleanup failure must not hide the result of the test.
- **No shared mutable fixtures across workers.** Workers can share read-only reference data. Workers cannot share anything that a test writes.
- **Synthetic data only.** Do not copy real customer or personal data into tests, fixtures, or reports. Mask anything that looks like such data.
- **Tie data to the real schema.** Every field that a test sets must exist in the data model. Invented columns make tests that pass against a fiction.
- **Know your provisioning method.** It can be a seed script, a direct insert, UI setup, or API setup. Name it. Then nobody mistakes a failure in setup for a product failure.
