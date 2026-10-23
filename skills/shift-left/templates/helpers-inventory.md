# [Helper] inventory

> Maps `[Helper: name]` labels used in test cases to the real executable helper
> (a page-object method, API client call, fixture, or CLI wrapper). A label exists
> here only if the helper exists. Steps without a helper stay natural language,
> which is honest partial automation, not a defect.

| Helper label | What it does | Backed by | Notes |
|--------------|--------------|-----------|-------|
| login | log in as a given role | `helpers/login.ts` | param: role |
| form-input | type into a labeled field | `helpers/form.ts` | |

## Proposed (not yet implemented)

> Collected from the "Proposed helpers" section of test cases. The inventory
> owner implements them and promotes them to the table above.

| Proposed label | Needed by | What it should do |
|----------------|-----------|-------------------|
| | | |
