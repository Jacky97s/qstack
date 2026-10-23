# Harness — <project>

> Read cold by the next agent. Every command is real and was run. Record the last proof date.
> Last proven: <YYYY-MM-DD> on <environment or rig>

## Surface

- Primary: <UI / API / CLI / device / station / dataset / model endpoint>
- Others: <...>

## Setup

```sh
<exact commands to reach a usable state from nothing>
```

Ready when: <observable signal that it is usable, not just running>

## Doctor

```sh
<one read-only check>
```

Healthy output: <what it prints when fit to test>

## Drive

<the recipe with real commands, selectors, bus commands, or procedures>

## Observe

| Evidence | How to capture | Where it goes |
|----------|----------------|---------------|
| <screenshot / trace / response / log / measurement / transcript> | <command> | <path> |

## Known-bad

<how to make the harness see a failure on purpose, and what that failure looks like>

## Cleanup

```sh
<stop what this run started; never the evidence; never shared equipment>
```

## Safety

- Protected environments and hosts: <list or pointer to .qstack/protected-hosts>
- Irreversible operations: <list or pointer to .qstack/protected-commands>
- Isolation: <can two runs share the system?>

## Capability map

### <capability>
- How to reach it: <user point of view>
- Drive: <commands>
- Proof: <observable end state>
- Gotchas: <preconditions, flakiness, data needs>
