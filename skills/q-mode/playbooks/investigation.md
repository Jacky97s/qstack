### Investigation

**You own the answer. Read, sample, and cite.**

This work is read-only. The deliverable is a cited answer or a recommendation. It is not a code change.

1. Find the production code of the subject and every test that touches it. Map behaviors to tests, not files to tests. A behavior with no test is a gap, even when line coverage says otherwise.
2. For a confidence question ("are we sure X is covered?"), sample-check the strongest-looking tests with the two imagined edits (**principle-test-behavior-not-implementation**). When the stakes justify it, run a quick **mutation-check** on the riskiest path. Report the survivors.
3. For a flake or health question, get the run history from CI when you can reach it. Report rates with counts, not adjectives.
4. Answer with these items: what is covered, how strongly (the evidence level for each claim), the gaps ranked by risk, and a recommendation.

Do not change tests. Do not file reports. When the answer leads to work, name the playbook that does it.

**Reply:** the answer, a behavior-to-test table when coverage is the question, gaps ranked by risk, and your judgment. Push back when the premise is wrong.
