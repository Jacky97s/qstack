---
name: test-design-techniques
description: "Pick and apply the correct test design technique for the shape of the problem. Techniques: equivalence partitions, boundary values, decision tables, state transitions, pairwise and combinatorial, CRUD and permission matrices, property-based tests, error guessing, design of experiments, corner and stress analysis, and fault injection. Use when you derive cases from a requirement, size a test matrix, or when someone asks which technique fits."
---

# Test design techniques

Choose a technique by the shape of the input and state space. Do not choose by habit. Each technique shows which cases are worth a run and which are redundant. Every case still needs an oracle (**principle-oracle-first**).

## Pick by shape

| The requirement looks like | Use |
|----------------------------|-----|
| A range, a size, a count, a length, a date window | Equivalence partitions plus boundary values |
| Several conditions combining into outcomes | Decision table |
| An object with a lifecycle (order, account, device, job) | State transition testing |
| Many independent options or configurations | Pairwise or n-wise combinatorial |
| A resource with roles | CRUD by role matrix |
| A rule that is true for all inputs (round trip, ordering, conservation) | Property-based testing |
| A history of defects in the area | Error guessing and fault models from that history |
| Physical parameters interacting (temperature, voltage, load) | Design of experiments, corner analysis |
| Behavior under faults (power loss, open circuit, dropped packets) | Fault injection |
| Margins and limits | Stress and step-stress to failure |

## Equivalence partitions and boundaries

Split each input into classes that the system must treat in the same way: valid classes and each distinct invalid class. Take one value for each class. Then take the boundaries of each class: just below, on, and just above every edge. Boundaries include:
- zero
- empty
- one
- maximum
- maximum plus one
- negative
- the own limits of the type (length in bytes versus characters, integer overflow, timestamp ranges)

Multi-byte text, leading and trailing whitespace, and case often hide extra partitions.

## Decision tables

List conditions as rows and every meaningful combination as columns. Give the expected action for each column. Merge the columns where the outcome does not depend on a condition. Each remaining column is a case. Gaps in the table (combinations that the spec does not define) are open questions.

## State transitions

Draw the states and the events. Cover these items:

- Every valid transition at least one time.
- Every invalid event in each state. The system must reject or ignore it, as the spec says.
- Loops and sequences that reach states that few people visit.

Dead-end states and missing transitions are spec defects.

## Pairwise and combinatorial

When options seldom interact in groups larger than pairs, a pairwise set covers every pair of values in far fewer cases than the full product. Use a generator (PICT, allpairs, or a library). Add constraints for impossible combinations. Use three-wise for high-risk areas. Keep known-dangerous combinations as explicit cases.

## CRUD by role

Rows are resources and columns are roles. Each cell lists create, read, update, delete, and each special action, with allowed or denied. Test every denied cell and every allowed cell. Include reads through indirect paths: exports, search, notifications, and APIs.

## Property-based testing

State an invariant and generate many inputs. The tool shrinks each failure to a minimal case. Good properties are:
- round trip
- idempotence
- commutativity where the spec promises it
- invariants that every operation keeps
- model equivalence against a simple reference
- "never crashes on any input" for parsers

## Error guessing

Seed cases from what broke before, here and in similar systems. Examples: nulls and missing fields, duplicates, concurrency on the same record, retries and timeouts, time zones and daylight saving, rounding and currency, encodings, large payloads, and partial failures.

## Design of experiments

When several factors can interact, change them together in a planned design (full or fractional factorial, or a response-surface design). Do not change them one at a time. Then you can see the interactions with fewer runs. Randomize the run order and replicate the runs to separate the effect from noise.

## Corners, stress, and fault injection

- Corners: combine the extremes of the parameters that matter (process, voltage, temperature, load, humidity). Do not test only the nominal values.
- Step stress: increase one stress in steps until operation fails, then until the unit is destroyed. This shows the operating and destruct margins.
- Fault injection: power loss at random points, brownouts, open and short circuits, bit flips, dropped and reordered messages, dependency timeouts, and full disks. Repeat timing-sensitive faults many times.
