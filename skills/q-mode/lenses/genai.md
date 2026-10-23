# Lens: genai

## Artifact identity
Model identifier and version, system prompt and prompt template versions, tool definitions, retrieval index version, decoding parameters, and the guardrail configuration. A change to any of them is a new artifact.

## Stimulus and observation
User inputs, conversation histories, retrieved documents, tool outputs. Observe the response, the transcript (tool calls, arguments, intermediate results), the final state of the environment, latency, and token cost.

## Instruments and trust
Code graders, model-graded rubrics, and human review. Calibrate each rubric against human labels on a sample. Read transcripts, because scores can hide graders that are wrong, unfair, or gamed. Method in `../references/ai-evals.md`.

## Variation and sampling
Sampling randomness, prompt sensitivity, and model updates by the provider. Run k trials per task. Report pass@k for capability and pass^k for reliability, with spread (**principle-measure-variation**).

## Cost and reversibility
Token and compute cost per run. Agents with tools can take real actions: sending messages, changing records, spending money. Run agents against sandboxes, and treat tool side effects like any shared-environment operation.

## Oracle sources
Task success criteria, reference answers where they exist, source documents for faithfulness, policies for safety and refusal, and human judgment through rubrics.

## Gates and standards
Regression evals in CI on every prompt, model, or retrieval change. A launch review with capability, safety, and reliability results. Transparency obligations under the EU AI Act apply to many generative systems (see the regulated lens).

## Layer ladder
Deterministic checks with the model mocked (routing, tool wiring, parsing) → single-step evals with code graders → multi-step and agent evals → model-graded rubrics → human review → online monitoring and feedback.

## Typical risks
Hallucination and unfaithfulness to sources, prompt injection (direct, and indirect through retrieved content and tool outputs), data and system-prompt exfiltration, personal data leakage, unsafe or harmful output, over-refusal, wrong tool or wrong arguments, runaway loops and cost, and silent regressions from provider model updates.

## Failure classes
Grader error, eval-set contamination (examples leaked into prompts or fine-tuning), provider-side change, retrieval failure (the answer was not retrieved), tool failure, and nondeterministic pass mistaken for success.

## Playbook notes
- **Test design:** build the eval set from representative, edge, adversarial, and incident-regression cases. Keep a held-out slice you never tune against.
- **Automate:** an eval is a test suite. It passes the same gates: seen to fail on a broken prompt or model, and reviewed fresh.
- **Gate review:** decide on rates over k trials against a baseline, never on one run.
