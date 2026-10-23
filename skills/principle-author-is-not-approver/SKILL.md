---
name: principle-author-is-not-approver
description: "Apply to every test, test case, plan, or verdict you produced. A draft becomes done only after a fresh-context reviewer checks it and after each new test is seen to fail against a broken version. Your own review, passing tests, and CI never count as the independent check."
user-invocable: false
---

# Author Is Not Approver

Generated tests run, pass, and raise coverage while asserting almost nothing. Studies of LLM-generated tests keep finding the same thing: coverage high, fault detection weak, expected values copied from current behavior. The author, human or model, is the worst judge of its own blind spots.

Two gates stand between a draft and done:

1. **Seen to fail.** Every new or changed test must fail against a deliberately broken version of the behavior it claims to protect: the original bug, or a planted mutant (the **mutation-check** skill). A test you never saw fail is `NOT VERIFIED` as a detector, whatever its pass count.
2. **Fresh review.** A reviewer that did not write the work checks oracle sources, assertion strength, determinism, isolation, and layer. Use the `qstack:test-reviewer` agent, on a different model family when the runtime offers one, or a human. Give it the files and the claim, not your conclusion.

Rules:

- Batches do not get batch approval. Every test in an AI-generated batch passes both gates, or the batch is reported with the ones that did not.
- A reviewer that wrote any part of the change counts as an author.
- When no independent reviewer can run, record `BLOCKED: independent review` and keep the work out of done. Do not substitute your own read.
- The human owns acceptance. The agent's job is to make that acceptance cheap and well-founded.
