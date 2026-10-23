### Failure triage

**You own the classification. A red test is information until proven otherwise.**

For one or more failing tests, locally or in CI.

1. Get the real failure for the exact commit and environment: the log, the assertion diff, the trace, screenshots, and the CI job. Note what changed since the last green run: code, dependencies, environment, data, time.
2. Group failures that share a cause before investigating any one. Forty failures from one expired credential are one finding.
3. Classify each group with evidence (**principle-classify-before-you-fix**, `references/failure-taxonomy.md`). You may rerun once in isolation to classify. Record both results. A rerun is evidence, never a fix.
4. Act by class:
   - **Product regression:** run the **Bug report** playbook. The test stays red, or is quarantined only with the operator's decision, a ticket, and an expiry.
   - **Test defect:** fix the test and cite the oracle source that proves the old expectation was wrong.
   - **Contract or doc drift:** report it to the spec owner with both sides cited. Do not edit the expected value to the system's output.
   - **Environment:** report to its owner with the evidence. Rerun after it is fixed.
   - **Data collision:** isolate the data (**principle-isolate-test-data**).
   - **Flaky:** run the **Flaky triage** playbook.
   - **Known issue:** link the ticket.
5. Verify: rerun the exact failing set on the same environment after each action. `VERIFIED` only when it passes for the reason you fixed.

**Reply:** a table of failure, class, evidence, action, and status. Then the decisive failing and passing output, trimmed to the assertion and counts.
