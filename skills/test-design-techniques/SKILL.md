---
name: test-design-techniques
description: "Pick and apply the right test design technique for the shape of the problem: equivalence partitions, boundary values, decision tables, state transitions, pairwise and combinatorial, CRUD and permission matrices, property-based tests, error guessing, design of experiments, corner and stress analysis, and fault injection. Use when deriving cases from a requirement, sizing a test matrix, or asked which technique fits."
---

# Test design techniques

Choose by the shape of the input and state space, not by habit. Each technique tells you which cases are worth running and which are redundant. Every case still needs an oracle (**principle-oracle-first**).

## Pick by shape

| The requirement looks like | Use |
|----------------------------|-----|
| A range, a size, a count, a length, a date window | Equivalence partitions plus boundary values |
| Several conditions combining into outcomes | Decision table |
| An object with a lifecycle (order, account, device, job) | State transition testing |
| Many independent options or configurations | Pairwise or n-wise combinatorial |
| A resource with roles | CRUD by role matrix |
| A rule that holds for all inputs (round trip, ordering, conservation) | Property-based testing |
| A history of defects in the area | Error guessing and fault models from that history |
| Physical parameters interacting (temperature, voltage, load) | Design of experiments, corner analysis |
| Behavior under faults (power loss, open circuit, dropped packets) | Fault injection |
| Margins and limits | Stress and step-stress to failure |

## Equivalence partitions and boundaries

Split each input into classes the system should treat the same: valid classes and each distinct invalid class. Take one value per class, then the boundaries of each class: just below, on, and just above every edge. Boundaries include zero, empty, one, maximum, maximum plus one, negative, and the type's own limits (length in bytes versus characters, integer overflow, timestamp ranges). Multi-byte text, leading and trailing whitespace, and case often hide extra partitions.

## Decision tables

List conditions as rows and every meaningful combination as columns, with the expected action for each. Collapse columns whose outcome does not depend on a condition. Each remaining column is a case. Gaps in the table (combinations the spec does not define) are open questions.

## State transitions

Draw the states and the events. Cover every valid transition at least once, every invalid event in each state (it must be rejected or ignored as specified), and loops and sequences that reach rarely visited states. Dead-end states and missing transitions are spec defects.

## Pairwise and combinatorial

When options interact rarely beyond pairs, a pairwise set covers every pair of values in far fewer cases than the full product. Use a generator (PICT, allpairs, or a library) and add constraints for impossible combinations. Raise to three-wise for high-risk areas. Keep known-dangerous combinations as explicit cases.

## CRUD by role

Rows are resources, columns are roles, cells list create, read, update, delete, and each special action, with allowed or denied. Test every denied cell as well as the allowed ones. Include reading through indirect paths: exports, search, notifications, and APIs.

## Property-based testing

State an invariant, generate many inputs, and let the tool shrink failures to a minimal case. Good properties: round trip, idempotence, commutativity where promised, invariants preserved by every operation, model equivalence against a simple reference, and "never crashes on any input" for parsers.

## Error guessing

Seed cases from what has broken before here and in similar systems: nulls and missing fields, duplicates, concurrency on the same record, retries and timeouts, time zones and daylight saving, rounding and currency, encodings, large payloads, and partial failures.

## Design of experiments

When several factors may interact, vary them together in a planned design (full or fractional factorial, or a response-surface design) instead of one at a time, so interactions become visible with fewer runs. Randomize run order and replicate to separate effect from noise.

## Corners, stress, and fault injection

- Corners: combine the extremes of the parameters that matter (process, voltage, temperature, load, humidity) rather than testing only nominal.
- Step stress: raise one stress in steps until operation fails, then until it is destroyed, to find the operating and destruct margins.
- Fault injection: power loss at random points, brownouts, open and short circuits, bit flips, dropped and reordered messages, dependency timeouts, and disk full. Repeat timing-sensitive faults many times.
