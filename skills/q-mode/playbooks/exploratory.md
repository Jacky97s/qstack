### Exploratory session

**You own discovery. The session has a charter and a time box. You keep notes and give a debrief.**

1. Write the charter: "Explore <target> with <resources or technique> to discover <information or risk>." Set a time box or step budget. Seed the charter from recent changes, the risk map, and the defect history.
2. Pick heuristics from `references/heuristics.md`: SFDIPOT for what to vary, tours for how to move, and HICCUPPS-F for oracles.
3. Confirm that the environment is disposable or approved (**principle-protect-shared-environments**).
4. Drive the running system. Use a browser automation skill for a UI, an API client for services, and the CLI for tools. Keep session notes as you work: what you tried, what you saw, questions, and bugs, with screenshots and timestamps.
5. For each anomaly, name the oracle that it violates. Then do one of these:
   - Make it a bug (run the **Bug report** playbook).
   - Make it a question (an open question).
   - Note it as not a bug, with the reason.
6. Give a debrief: what you covered, what you did not cover, the bugs and questions, obstacles, and how confident you are now in the area.
7. Graduate: list the paths that were stable and valuable as candidates for the **Automate** playbook. Give each path the oracle that the session used.

Split a large charter across parallel workers only when the parts share no mutable state.

**Reply:** the charter, coverage notes, findings ranked by severity, open questions, the graduation list, and remaining risk.
