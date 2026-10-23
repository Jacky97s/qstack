### Test campaign

**You own the measurement. A campaign is an experiment. You fix the question, the sample plan, and the decision rule before the first run.**

Use for any run that needs many trials, units, conditions, or hours, such as:
- load and stress tests
- soak tests
- characterization across corners
- environmental and reliability tests
- fault-injection campaigns
- eval runs for AI features
- model comparisons
- station correlation studies

1. State the question and the decision it feeds, as a falsifiable predicate. Examples: "p99 stays under 300 ms at 500 requests per second with under 0.1% errors", "no unit fails 500 thermal cycles", "the candidate beats the baseline on every priority slice by more than seed spread".
2. Design the experiment from the active lenses:
   - the factors and their levels (load, temperature, voltage, prompt set, seed)
   - the sample size and its reasoning (**principle-measure-variation**)
   - the run order (randomize where drift is possible)
   - the warm-up and settling data to discard
   - the stop rules (abort conditions, safety limits)
3. Fix the decision rule before you run: thresholds, tolerance, and the baseline that you compare against, measured the same way.
4. Prove the instruments (**principle-trust-the-instrument**):
   - The load generator is not the bottleneck.
   - The instruments are calibrated.
   - The graders are calibrated.
   - The rig passes its doctor check.
   - The metric implementation is right on a known case.
5. Confirm authorization and safety: environments, units consumed, irreversible operations, and the window (**principle-protect-shared-environments**).
6. Run it. Record identities and conditions with every result. Log anomalies when they happen. Do not reconstruct them later.
7. Analyze the results per condition, with sample size and spread, against the decision rule. Explain each number that you report (**principle-explain-the-number**): what limits it, and why it does not measure something else.
8. Investigate every failure to a cause. A failure in a campaign is data, not noise.

**Reply:** the question and decision rule, the design, the results table per condition with sample sizes and spread, the limiter behind each key number, failures with causes, and the decision that the results support.
