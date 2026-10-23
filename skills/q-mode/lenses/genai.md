# Lens: genai

## Artifact identity
Model identifier and version, system prompt and prompt template versions, tool definitions, retrieval index version, decoding parameters, and the guardrail configuration. A change to any of them makes a new artifact.

## Stimulus and observation
User inputs, conversation histories, retrieved documents, and tool outputs. Observe the response, the transcript (tool calls, arguments, intermediate results), the final state of the environment, latency, and token cost.

## Instruments and trust
The instruments are code graders, model-graded rubrics, and human review. Calibrate each rubric against human labels on a sample. Read the transcripts, because scores can hide graders that are wrong, unfair, or gamed. For the method, see `../references/ai-evals.md`.

## Variation and sampling
Results vary with sampling randomness, prompt sensitivity, and model updates by the provider. Run k trials for each task. Report pass@k for capability and pass^k for reliability, with the spread (**principle-measure-variation**).

## Cost and reversibility
Each run has a token and compute cost. Agents with tools can take real actions: send messages, change records, and spend money. Run agents against sandboxes. Treat tool side effects like any shared-environment operation.

## Oracle sources
Task success criteria, reference answers where they exist, source documents for faithfulness, policies for safety and refusal, and human judgment through rubrics.

## Gates and standards
Run regression evals in CI on every prompt, model, or retrieval change. Hold a launch review with capability, safety, and reliability results. Transparency obligations under the EU AI Act apply to many generative systems (see the regulated lens).

## Layer ladder
Use these layers in this order:
- deterministic checks with the model mocked (routing, tool wiring, parsing)
- single-step evals with code graders
- multi-step and agent evals
- model-graded rubrics
- human review
- online monitoring and feedback

## Typical risks
These risks are typical:
- hallucination and unfaithfulness to sources
- prompt injection (direct, and indirect through retrieved content and tool outputs)
- data and system-prompt exfiltration
- personal data leakage
- unsafe or harmful output
- over-refusal
- wrong tool or wrong arguments
- runaway loops and cost
- silent regressions from provider model updates

## Failure classes
These failure classes are common:
- grader error
- eval-set contamination (examples that leaked into prompts or fine-tuning)
- provider-side change
- retrieval failure (the system did not retrieve the answer)
- tool failure
- a nondeterministic pass that someone mistakes for success

## Playbook notes
- **Test design:** build the eval set from representative, edge, adversarial, and incident-regression cases. Keep a held-out slice that you never tune against.
- **Automate:** an eval is a test suite. It must pass the same gates: you have seen it fail on a broken prompt or model, and someone reviewed it with fresh eyes.
- **Gate review:** decide on rates over k trials against a baseline. Never decide on one run.
