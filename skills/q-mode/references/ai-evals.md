# Evaluating LLM and agent features

Terminology follows Anthropic's "Demystifying evals for AI agents": a task is one test case, a trial is one attempt at it, a grader scores a trial, a transcript records everything the system did in a trial, and the outcome is the final state of the environment.

## Design

1. **Tasks per use case.** Write what success means in checkable terms. Prefer outcomes (the ticket was created with these fields) over phrasing.
2. **Eval set composition.** Representative traffic, edge cases, adversarial cases, and regression cases from incidents. Keep a held-out slice you do not tune against.
3. **Adversarial coverage.** Direct prompt injection, indirect injection through retrieved documents, web pages, and tool outputs, jailbreaks, system prompt or secret exfiltration, personal data leakage, harmful requests, and over-refusal of legitimate requests.
4. **Capability vs regression evals.** Capability evals measure progress on hard tasks and are expected to fail often. Regression evals guard what already works and should pass nearly always.

## Graders

| Grader | Use for | Watch out for |
|--------|---------|---------------|
| Code | Schema, required fields, exact values, tool name and arguments, citations that resolve, latency, token cost | Over-strict string matching on valid alternatives |
| Model-graded rubric | Helpfulness, faithfulness to sources, tone, reasoning quality | Position and length bias, leniency, drift when the judge model changes. Calibrate against human labels |
| Human | Calibration samples, disputed cases, launch decisions | Cost, inconsistency between raters. Use written guidelines |

Grade outcomes rather than the exact path when several paths are valid. Read transcripts anyway, to find graders that are wrong, unfair, or gamed.

## Running and reporting

- k trials per task. State k.
- pass@k: at least one success in k. Capability.
- pass^k: all k succeed. Reliability, the number users feel.
- Report per-task and overall rates with spread. Compare against a baseline on the same task set, k, and graders.
- For agents, also report tool-selection accuracy, argument errors, recovery after a failed step, steps per task, and cost per task.

## Gating in CI

- Thresholds with tolerance, set before looking at the run.
- Fail on a regression beyond the noise floor measured by re-running the baseline.
- Version the eval set, the graders, the prompts, and the model identifier together, so a score change can be attributed.
