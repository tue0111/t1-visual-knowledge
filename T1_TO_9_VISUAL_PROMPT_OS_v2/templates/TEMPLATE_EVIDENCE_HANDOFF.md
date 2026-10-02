# TEMPLATE — ANALYST EVIDENCE HANDOFF

Contract home: `schemas/analyst_handoff.schema.json`.
`evidence_class` is epistemic (SOURCE_FACT / VISUAL_OBSERVATION / INFERENCE / HEURISTIC / ASSUMPTION).
`evidence_method` is how the observation was collected (DOCUMENTARY / RENDER / PROMPT / HUMAN_REVIEW / MACHINE_CHECK). Do not put a method value in `evidence_class`.

```yaml
schema_version: "1.0.0"
task_id: "task-001"
source_fingerprint: ""
observations:
  - id: "O-1"
    text: ""
    evidence_class: VISUAL_OBSERVATION
    locator: ""
interpretations:
  - id: "I-1"
    text: ""
    uncertainty: []
    evidence_links: []
unknowns:
  - id: "Q-1"
    question: ""
    impact: ""
reference_roles: []
ownership_conflicts: []
control_candidates:
  - id: "C-1"
    mechanism: ""
    acceptance: ""
evidence_links: []
prohibited_inferences: []
```

Filled example: `templates/examples/analyst_handoff.filled.json`.
