# Exploration and oracle heuristics

Heuristics are prompts for thinking. They are not checklists to complete. Use them to generate test ideas and to decide if what you saw is a problem.

## SFDIPOT: what to vary

This list comes from the Heuristic Test Strategy Model of James Bach.

- **Structure:** what the product is made of: components, files, modules, dependencies, versions.
- **Function:** what it does: features, calculations, error handling, transformations.
- **Data:** what it processes: inputs, outputs, boundaries, empty, huge, malformed, Unicode, encodings, lifecycle (create, read, update, delete).
- **Interfaces:** how it connects: UI, API, CLI, files, imports and exports, other systems.
- **Platform:** what it depends on: OS, browser, device, network, hardware, third-party services.
- **Operations:** how people use it: common and rare workflows, roles, concurrent users, misuse, recovery.
- **Time:** when things happen: timeouts, sequencing, concurrency, scheduling, dates, timezones, long sessions.

## HICCUPPS-F: oracles when there is no spec

A result is suspect when the product does not agree with:

- **History:** its own past behavior.
- **Image:** the image that the organization wants to show.
- **Comparable products:** similar products or features.
- **Claims:** what anyone says that it does (docs, marketing, tooltips, the spec).
- **User expectations:** what a reasonable user expects.
- **Product:** itself (the same thing behaves differently in another part of the product).
- **Purpose:** the reason it exists.
- **Statutes and standards:** laws, regulations, accessibility and security standards.
- **Familiar problems:** patterns of bugs that you saw before.

Name the inconsistency in the report. For example: "Inconsistent with Claims: the tooltip says X, the result is Y."

## Tours: how to move

These tours come from the exploratory testing tours of James Whittaker.

- **Feature tour:** touch every control and option one time.
- **Money tour:** the flows that make or move money.
- **Landmark tour:** go between key features in different orders.
- **Bad-data tour:** malformed, extreme, and hostile inputs.
- **Configuration tour:** settings, flags, locales, permissions.
- **Garbage collector's tour:** visit every screen or endpoint in order, one by one.
- **Interruption tour:** cancel, go back, refresh, lose connection, or time out in the middle of a flow.

## Session notes and debrief

Charter: "Explore <target> with <resources or technique> to discover <information or risk>." Set a time limit for it.

Write these notes during the session: setup, what you tried, observations, questions, bugs (with evidence), and ideas for later.

Debrief (PROOF):
- **P**ast (what happened)
- **R**esults (what you found)
- **O**utlook (what remains)
- **O**bstacles (what blocked you)
- **F**eelings (how confident you are in the area, as a stated level with reasons)
