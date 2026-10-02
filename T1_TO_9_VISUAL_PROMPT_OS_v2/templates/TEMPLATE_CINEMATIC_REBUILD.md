# TEMPLATE — CINEMATIC REBUILD

Internal worksheet. Do not paste this whole card into the renderer. Chat stays in director language. Vocabulary matches `schemas/cinematic_rebuild.schema.json`.

## Input

~~~yaml
reference_id: R01
input_status: IMAGE_OBSERVED # DESCRIPTION_ONLY | PROMPT_ONLY
input_revision: "fingerprint-of-current-refs-and-request"
observations:
  - "Visible fact, no plot"
interpretations:
  - claim: "Suggested feeling"
    confidence: tentative
    visual_basis: "Sign that supports it"
~~~

## DNA

~~~yaml
dna:
  identity: {policy: lock_if_assigned, evidence: []}
  relational_signature: []
  emotional_register: []
  world_material_grammar: []
  render_boundaries: []
  attention_logic: []
  palette_roles: []
  signature_mechanism: []
  decisions:
    carry: []
    lock: []
    translate: []
    repair: []
    drop: []
    open: []
  uncertainties: []
  forbidden_drift: []
~~~

`translate` = keep the function, change the expression. A visible trait is not automatically a lock.

## Directions

Each direction needs treatment, DNA kept or translated, structural change, why it fits, and cost. Recommend one. Do not emit renderer prompts in DISCUSS.

## Shot specification

~~~yaml
shot_id: S01
decision_revision: 1
selection_status: user_selected # or delegated
selected_direction: B
intent: "What the viewer should feel or understand"
moment: "One instant that fits in a still"
invariants: []
changes_from_reference:
  - {dimension: staging, before: "...", after: "...", reason: "..."}
performance:
  action: "..."
  support_and_weight: "..."
  gaze_target: "..."
  gesture_evidence: "..."
viewer_relation:
  viewpoint_type: external_observer
  observer_identity: unspecified
  known_vs_hidden_information: "..."
camera:
  station: "..."
  height_distance_orientation: "..."
  shot_size_crop: "..."
  field_of_view_effect: "..."
space:
  planes: []
  occludes: []
  keep_visible: []
attention:
  first_read: "..."
  focus_plan: "..."
  contrast_plan: "..."
  rest_areas: []
lighting:
  sources_world_space: []
  face_or_mechanism_exposure: "..."
  motivated_exception: "none or intentional departure"
render_domains: []
intentional_impossibility: null
target_generator: "requested or proposed; independent of host"
output_contract: "active contract plus current overrides"
acceptance_cues: []
~~~

## Change ledger

Every structural rebuild lists staging / station / gaze / spatial_relation / first_read (and action when it is the beat). Palette-only rows cannot carry a rebuild.

## Critique

DNA kept or lost; relation vs portrait; occlusion; focus/light; licensed impossibility. Repair the failed layer. A new user correction invalidates derived spec/prompt at that revision; identity locks remain.
