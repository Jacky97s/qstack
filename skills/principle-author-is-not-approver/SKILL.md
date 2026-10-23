---
name: principle-author-is-not-approver
description: "Apply to every test, test case, plan, or verdict you produced. A draft is done only after a fresh-context reviewer checks it and after you see each new test fail against a broken version. Your own review, passing tests, and CI are not the independent check."
user-invocable: false
---

# Author Is Not Approver

Generated tests run, pass, and raise coverage, but they assert almost nothing. Studies of LLM-generated tests find the same result each time. Coverage is high and fault detection is weak. The expected values come from the current behavior. The author, human or model, is the worst judge of its own blind spots.

Two gates stand between a draft and done:

1. **Seen to fail.** Every new or changed test must fail against a deliberately broken version of the behavior it claims to protect. Use the original bug or a planted mutant (the **mutation-check** skill). If you never saw a test fail, it is `NOT VERIFIED` as a detector. The number of passes does not change this.
2. **Fresh review.** A reviewer that did not write the work checks oracle sources, assertion strength, determinism, isolation, and layer. Use the `qstack:test-reviewer` agent or a human. Use a different model family when the runtime offers one. Give the reviewer the files and the claim. Do not give your conclusion.

Rules:

- Batches do not get batch approval. Every test in an AI-generated batch must pass both gates. If a test does not pass, report the batch with the tests that did not pass.
- A reviewer that wrote any part of the change counts as an author.
- When no independent reviewer can run, record `BLOCKED: independent review`. Keep the work out of done. Do not use your own read as a substitute.
- The human owns acceptance. The agent must make that acceptance cheap and well-founded.
