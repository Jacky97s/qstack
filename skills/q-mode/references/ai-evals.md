# Evaluating LLM and agent features

The terms follow Anthropic's "Demystifying evals for AI agents". A task is one test case. A trial is one attempt at a task. A grader scores a trial. A transcript records everything that the system did in a trial. The outcome is the final state of the environment.

## Design

1. **Tasks per use case.** Write what success means in terms that a person can check. Prefer outcomes (the ticket was created with these fields) over phrasing.
2. **Eval set composition.** Include representative traffic, edge cases, adversarial cases, and regression cases from incidents. Keep a held-out slice. Do not tune against it.
3. **Adversarial coverage.** Cover:
   - direct prompt injection
   - indirect injection through retrieved documents, web pages, and tool outputs
   - jailbreaks
   - system prompt or secret exfiltration
   - personal data leakage
   - harmful requests
   - over-refusal of legitimate requests
4. **Capability vs regression evals.** Capability evals measure progress on hard tasks. Expect them to fail often. Regression evals guard what already works. They must pass almost always.

## Graders

| Grader | Use for | Watch out for |
|--------|---------|---------------|
| Code | Schema, required fields, exact values, tool name and arguments, citations that resolve, latency, token cost | Over-strict string matching that rejects valid alternatives |
| Model-graded rubric | Helpfulness, faithfulness to sources, tone, reasoning quality | Position and length bias, leniency, and drift when the judge model changes. Calibrate against human labels |
| Human | Calibration samples, disputed cases, launch decisions | Cost, and inconsistency between raters. Use written guidelines |

Grade outcomes, not the exact path, when several paths are valid. Read transcripts also, to find graders that are wrong, unfair, or gamed.

## Running and reporting

- Run k trials per task. State k.
- pass@k: at least one success in k. This measures capability.
- pass^k: all k succeed. This measures reliability. Users feel this number.
- Report per-task and overall rates with spread. Compare against a baseline that uses the same task set, k, and graders.
- For agents, also report tool-selection accuracy, argument errors, recovery after a failed step, steps per task, and cost per task.

## Gating in CI

- Use thresholds with tolerance. Set them before you look at the run.
- Fail the gate on a regression that is larger than the noise floor. Measure the noise floor when you run the baseline again.
- Version the eval set, the graders, the prompts, and the model identifier together. Then you can find the cause of a score change.
