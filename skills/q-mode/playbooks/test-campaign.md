### Test campaign

**You own the measurement. A campaign is an experiment with a question, a sample plan, and a decision rule fixed before the first run.**

For any run that needs many trials, units, conditions, or hours: load and stress tests, soak tests, characterization across corners, environmental and reliability tests, fault-injection campaigns, eval runs for AI features, model comparisons, and station correlation studies.

1. State the question and the decision it feeds, as a falsifiable predicate: "p99 stays under 300 ms at 500 requests per second with under 0.1% errors", "no unit fails 500 thermal cycles", "the candidate beats the baseline on every priority slice by more than seed spread".
2. Design the experiment from the active lenses: the factors and their levels (load, temperature, voltage, prompt set, seed), the sample size and its reasoning (**principle-measure-variation**), the run order (randomize where drift is possible), warm-up and settling to discard, and the stop rules (abort conditions, safety limits).
3. Fix the decision rule before running: thresholds, tolerance, and the baseline you compare against, measured the same way.
4. Prove the instruments (**principle-trust-the-instrument**): the load generator is not the bottleneck, instruments are calibrated, graders are calibrated, the rig passes its doctor check, the metric implementation is right on a known case.
5. Confirm authorization and safety: environments, units consumed, irreversible operations, and the window (**principle-protect-shared-environments**).
6. Run it. Record identities and conditions with every result. Log anomalies as they happen rather than reconstructing them later.
7. Analyze: results per condition with sample size and spread, against the decision rule. For any number you report, explain it (**principle-explain-the-number**): what limits it, and why it is not measuring something else.
8. Investigate every failure to a cause. A failure in a campaign is data, not noise.

**Reply:** the question and decision rule, the design, the results table per condition with sample sizes and spread, the limiter behind each key number, failures with causes, and the decision the results support.
