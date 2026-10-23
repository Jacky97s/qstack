### Change impact

**You own the safety argument. Find what a change can break beyond what it touched.**

For any change: a code diff, a firmware release, an engineering change to a board or part, a supplier or material substitution, a process change on a line, a retrained model, or a new data source.

1. Read the change itself: what was added, changed, and removed, including what the description does not spell out. For code, the diff, symbols, configuration, migrations, flags, and dependency bumps. For physical and process changes, the change order, the parts and suppliers, and the affected steps.
2. Find the impact beyond the change: consumers of changed interfaces (APIs, events, schemas, connectors, pinouts, file formats), shared components, persisted data and calibration, other products or lines using the same part or code, and combinations with flags or configurations. When pstack is installed, `pstack:blast-radius` covers this step for code.
3. Find the one fact the change is safe because of, and prove it by running or measuring when you can.
4. Select checks: those exercising the changed behavior, those for each consumer, the critical-path smoke set always, and those with a history of failing for similar changes. For physical changes, name which verification tests must be repeated on new units.
5. List the risks nothing covers. Each becomes a new check, an exploratory charter, or an explicit accepted risk with its owner.
6. Produce the command or test request for the selected set, and run it when asked.

**Reply:** the selected checks with a one-line reason each, the safety fact and how far it was proven, uncovered risks with proposed coverage, and the command or request.
