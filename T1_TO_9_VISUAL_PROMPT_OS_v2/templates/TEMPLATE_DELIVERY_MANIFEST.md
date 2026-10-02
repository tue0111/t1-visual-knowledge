# TEMPLATE — DELIVERY MANIFEST

Contract home: `schemas/delivery_manifest.schema.json`.
Do not convert `NOT_RUN`, `UNKNOWN`, or `UNTESTED` into a success claim.

```yaml
schema_version: "1.0.0"
task_id: ""
artifacts:
  - path: ""
    sha256: "0000000000000000000000000000000000000000000000000000000000000000"
    kind: prompt
provenance:
  source: ""
acceptance_results:
  - check_id: "A-1"
    status: NOT_RUN
    evidence: ""
preservation_results:
  - region: ""
    level: SEMANTIC
    status: NOT_RUN
source_fingerprints: {}
limitations: []
actual_execution_status: NOT_RUN
```

Filled example: `templates/examples/delivery_manifest.filled.json`.
