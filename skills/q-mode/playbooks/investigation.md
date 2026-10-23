### Investigation

**You own the answer. Read, sample, cite.**

Read-only. The deliverable is a cited answer or a recommendation, not a code change.

1. Locate the subject's production code and every test that touches it. Map behaviors to tests, not files to tests. A behavior with no test is a gap even when line coverage says otherwise.
2. For a confidence question ("are we sure X is covered?"), sample-check the strongest-looking tests with the two imagined edits (**principle-test-behavior-not-implementation**). When the stakes justify it, run a quick **mutation-check** on the riskiest path and report survivors.
3. For a flake or health question, pull run history from CI when you can reach it. Report rates with counts, not adjectives.
4. Answer with what is covered, how strongly (the evidence level for each claim), the gaps ranked by risk, and a recommendation.

No test changes, no reports filed. When the answer leads to work, name the playbook that would do it.

**Reply:** the answer, a behavior-to-test table when coverage is the question, gaps ranked by risk, and your judgment. Push back when the premise is wrong.
