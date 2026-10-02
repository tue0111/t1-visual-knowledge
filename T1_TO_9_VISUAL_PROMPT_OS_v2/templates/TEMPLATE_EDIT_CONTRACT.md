# TEMPLATE — EDIT CONTROL CONTRACT

Contract home: `schemas/control_contract.schema.json`. There is no `contract_id` field.

```yaml
schema_version: "1.0.0"
objective: ""
controlled_axes: []
constraints: []
ownership_by_dimension: {}
preservation_contract:
  level: SEMANTIC
  regions:
    - region: ""
      level: SEMANTIC
      acceptance: ""
allowed_dependent_changes: []
hard_gates: []
acceptance_checks:
  - id: "A-1"
    method: ""
    pass_condition: ""
```

Filled example: `templates/examples/control_contract.filled.json`.
