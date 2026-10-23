### Exploratory session

**You own discovery. Chartered, time-boxed, noted, debriefed.**

1. Write the charter: "Explore <target> with <resources or technique> to discover <information or risk>." Set a time box or step budget. Seed it from recent changes, the risk map, and the defect history.
2. Pick heuristics from `references/heuristics.md`: SFDIPOT for what to vary, tours for how to move, and HICCUPPS-F for oracles.
3. Confirm the environment is disposable or approved (**principle-protect-shared-environments**).
4. Drive the running system: a browser automation skill for UI, an API client for services, the CLI for tools. Keep session notes as you go: what you tried, what you saw, questions, and bugs, with screenshots and timestamps.
5. For each anomaly, name the oracle it violates. It becomes a bug (run the **Bug report** playbook), a question (an open question), or noted as not a bug with the reason.
6. Debrief: what was covered, what was not, the bugs and questions, obstacles, and how confident you are in the area now.
7. Graduate: list paths that were stable and valuable as candidates for the **Automate** playbook, each with the oracle the session used.

Partition a large charter across parallel workers only when the partitions share no mutable state.

**Reply:** the charter, coverage notes, findings ranked by severity, open questions, the graduation list, and remaining risk.
