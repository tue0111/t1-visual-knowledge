# TEMPLATE — ITERATION RECORD

Contract home: `schemas/iteration_record.schema.json`.
Successful layers are named in `held_controls`, not a separate `preserve` field. Changed axes go in `changed_controls`; coupled consequences go in `dependent_changes`.

```yaml
schema_version: "1.0.0"
run_id: ""
attempt_id: ""
parent_attempt: null
baseline_artifacts: []
hypothesis:
  symptom: ""
  cause: ""
  falsifier: ""
changed_controls: []
held_controls: []
dependent_changes: []
outcomes:
  - criterion: ""
    result: NOT_RUN
    evidence: ""
evidence_links: []
next_action: ""
```

Filled example: `templates/examples/iteration_record.filled.json`.
