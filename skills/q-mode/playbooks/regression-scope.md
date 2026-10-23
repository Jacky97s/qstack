### Regression scope

**You own the safety argument. Find what the change can break beyond its diff.**

1. Read the change: the diff, the symbols added, changed, and removed, configuration, migrations, feature flags, dependency bumps, and what the code now does differently, including what the diff does not spell out.
2. Find the impact beyond the diff: callers, consumers of changed APIs, events, and schemas, shared components, persisted data shapes, other languages or services reading the same bytes, and flag combinations. When pstack is installed, `pstack:blast-radius` covers this step.
3. Find the one fact the change is safe because of, and prove it by running code when you can.
4. Select tests: tests that exercise changed behavior, tests for each consumer, the critical-journey smoke set always, and tests with a history of failing for similar changes.
5. List the risks no test covers. Each becomes a new test, an exploratory charter, or an explicit accepted risk.
6. Produce the run command for the selected set and run it when asked.

**Reply:** the selected tests with a one-line reason each, the safety fact and how far it was proven, uncovered risks with proposed coverage, and the command.
