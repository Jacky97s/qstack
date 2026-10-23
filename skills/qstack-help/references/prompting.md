# Prompting qstack

A good request has three parts:

- **The claim.** What must be true, for whom, and under which conditions.
- **The system.** The artifact, the environment, and anything that you must not touch.
- **The check.** How to tell that the result is right: a spec clause, an SLO, a threshold, or a known-good comparison.

Do not list skills or steps. q-mode picks the playbook and keeps its steps.

## Steers

Use one line to correct a run:

- "Show me the command and the trimmed output." (evidence)
- "What is the oracle for this assertion?" (oracle)
- "Did you see this test fail on a broken version?" (author is not approver)
- "Classify the failure before you change the test." (classify before you fix)
- "Prove the instrument first." (trust the instrument)
- "How many runs, and what is the spread?" (measure variation)
- "What limits this number?" (explain the number)
- "Put the result in the reply. Do not make files."

## Example requests

| Lens | Request |
|------|---------|
| software | "`checkout.spec.ts` fails in CI on main. Find why. Do not change the expected values." |
| software | "Write API tests for `POST /refunds`. The oracle is the refund rules in `docs/refunds.md`." |
| performance | "Can `GET /search` keep p99 under 300 ms at 2,000 requests per second on the preview environment? Do not load staging." |
| firmware | "Plan tests for the OTA update path on the dev board rig. Include power loss at every phase." |
| hardware | "Plan DVT for revision C of the sensor board against `specs/sensor-board.md`." |
| manufacturing | "Can end-of-line station 3 catch a unit with a cold solder joint? Use the golden unit and the limit sample." |
| genai | "Is the support assistant ready to ship? Use the eval set in `evals/support/` with 5 trials for each task." |
| ml-training | "Did the fine-tuned checkpoint beat the base on every priority slice, by more than the seed spread?" |
| data | "How do we know the nightly orders pipeline does not drop or duplicate rows?" |
| security | "Plan security tests for the login flow. Do not run active scans. I have no written authorization yet." |
| regulated | "Which evidence is missing for the IEC 62304 class B release of 4.2?" |
| any | "We have no idea how to test this. Design the verification first." |
