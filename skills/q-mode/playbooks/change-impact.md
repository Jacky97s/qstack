### Change impact

**You own the safety argument. Find what a change can break beyond what it touched.**

Use for any change, such as:
- a code diff
- a firmware release
- an engineering change to a board or part
- a supplier or material substitution
- a process change on a line
- a retrained model
- a new data source

1. Read the change itself: what it added, changed, and removed, including what the description does not state. For code, read the diff, symbols, configuration, migrations, flags, and dependency bumps. For physical and process changes, read the change order, the parts and suppliers, and the affected steps.
2. Find the impact beyond the change:
   - consumers of changed interfaces (APIs, events, schemas, connectors, pinouts, file formats)
   - shared components
   - persisted data and calibration
   - other products or lines that use the same part or code
   - combinations with flags or configurations

   When pstack is installed, `pstack:blast-radius` covers this step for code.
3. Find the one fact that makes the change safe. Prove it by running or measuring when you can.
4. Select the checks:
   - those that exercise the changed behavior
   - those for each consumer
   - the critical-path smoke set, always
   - those with a history of failure for similar changes

   For physical changes, name which verification tests you must repeat on new units.
5. List the risks that no check covers. Each risk becomes a new check, an exploratory charter, or an explicit accepted risk with its owner.
6. Produce the command or test request for the selected set. Run it when asked.

**Reply:** the selected checks with a one-line reason each, the safety fact and how far you proved it, uncovered risks with proposed coverage, and the command or request.
