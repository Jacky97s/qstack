### AI feature testing

**You own the measurement. A nondeterministic feature is tested by evals, not by a run.**

For LLM, RAG, and agent features in the product under test. Read `references/ai-evals.md` and **principle-measure-variation** first.

1. Define the tasks and what success means for each use case. Separate what code can check (schema, required fields, the tool called with the right arguments, a refusal, a citation that resolves, latency, cost) from what needs a graded rubric (helpfulness, faithfulness to sources, tone).
2. Build the eval set: representative cases, edge cases, adversarial cases (prompt injection, including through retrieved content and tool output, jailbreaks, data exfiltration, personal data leakage, harmful requests), and regression cases from past incidents. Keep a held-out slice.
3. Build graders: code graders first, model-graded rubrics second, each rubric calibrated against human labels on a sample, plus a human spot-check schedule.
4. Run k trials per task. Report pass@k for capability and pass^k for reliability, with spread across trials and across model or prompt versions.
5. For agents, grade the end state of the environment, and read transcripts to check tool selection, arguments, error recovery, and step and cost budgets. Use transcripts to validate the graders too.
6. Gate in CI: thresholds with tolerance against a baseline, on the same task set and k. Never decide from one run.
7. Report the failures by category with example transcripts.

**Reply:** the eval design, results with k and spread, failure categories with examples, grader calibration, and the gate recommendation.
