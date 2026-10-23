# Exploration and oracle heuristics

Heuristics are prompts for thinking, not checklists to complete. Use them to generate test ideas and to decide whether what you saw is a problem.

## SFDIPOT: what to vary

From James Bach's Heuristic Test Strategy Model.

- **Structure:** what the product is made of. Components, files, modules, dependencies, versions.
- **Function:** what it does. Features, calculations, error handling, transformations.
- **Data:** what it processes. Inputs, outputs, boundaries, empty, huge, malformed, Unicode, encodings, lifecycle (create, read, update, delete).
- **Interfaces:** how it connects. UI, API, CLI, files, imports and exports, other systems.
- **Platform:** what it depends on. OS, browser, device, network, hardware, third-party services.
- **Operations:** how it is used. Common and rare workflows, roles, concurrent users, misuse, recovery.
- **Time:** when things happen. Timeouts, sequencing, concurrency, scheduling, dates, timezones, long sessions.

## HICCUPPS-F: oracles when there is no spec

A result is suspicious when the product is inconsistent with:

- **History:** its own past behavior.
- **Image:** the image the organization wants to project.
- **Comparable products:** similar products or features.
- **Claims:** what anyone says it does (docs, marketing, tooltips, the spec).
- **User expectations:** what a reasonable user would expect.
- **Product:** itself (the same thing behaving differently elsewhere in the product).
- **Purpose:** the reason it exists.
- **Statutes and standards:** laws, regulations, accessibility and security standards.
- **Familiar problems:** patterns of bugs you have seen before.

Name the inconsistency in the report. "Inconsistent with Claims: the tooltip says X, the result is Y."

## Tours: how to move

From James Whittaker's exploratory testing tours.

- **Feature tour:** touch every control and option once.
- **Money tour:** the flows that make or move money.
- **Landmark tour:** jump between key features in different orders.
- **Bad-data tour:** malformed, extreme, and hostile inputs.
- **Configuration tour:** settings, flags, locales, permissions.
- **Garbage collector's tour:** systematically visit every screen or endpoint in order.
- **Interruption tour:** cancel, go back, refresh, lose connection, time out mid-flow.

## Session notes and debrief

Charter: "Explore <target> with <resources or technique> to discover <information or risk>." Time-box it.

Notes during the session: setup, what was tried, observations, questions, bugs (with evidence), and ideas for later.

Debrief (PROOF): **P**ast (what happened), **R**esults (what was found), **O**utlook (what remains), **O**bstacles (what got in the way), **F**eelings (how confident you are in the area, as a stated level with reasons).
