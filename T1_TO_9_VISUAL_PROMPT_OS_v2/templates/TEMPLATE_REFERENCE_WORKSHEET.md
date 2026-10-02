# TEMPLATE — REFERENCE WORKSHEET

Fill before prompting from references.

~~~yaml
request_summary:

references:
  - id:
    source_context:
      source_named_precisely:
      maker_artist_or_community:
      community_region_period:
      original_function:
      authoritative_source:
      rights_and_provenance:
      status: unknown | green | amber | red
      sensitivity_flags: []
      allowed_extraction: []
      essential_authorized_motifs: []
      forbidden_extraction: []
      authenticity_claim:
      review_state: incomplete | conditional | approved | rejected
      review_basis:
      reviewed_by:
      conditions: []
      decision_date:
      review_required:
    role:
      identity:
      pose:
      wardrobe:
      composition:
      light:
      material:
      environment:
      selected_frame:
    ignore:
      - text
      - logo
      - interface

    analysis_layers:
      observed_facts: []
      observed_relations: []
      inferences: []
      cultural_or_historical_interpretations: []
      uncertainties: []

authority_by_dimension:
  identity:
  pose:
  wardrobe:
  environment:
  lighting:
  current_correction:

fast_read:
  first_read:
  anchor:
  background_role:
  camera:
  light_source:
  depth_planes:
  material_proof:
  success_mechanism:
  likely_drift:

carry:
lock:
repair:
open:

render_boundary:
authored_relationship:
physical_bridge_if_shared_world:

closest_family:
support_systems:
  - id:
    jurisdiction:
    necessity:
target_output:
~~~

Prompt only what belongs in lock and repair. Let carry remain carried by the reference.
