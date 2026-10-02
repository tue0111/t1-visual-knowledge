# 02 DECISION WORKFLOW

This is the full design workflow. Select PATCH/STANDARD/DEEP in core/13_RUNTIME_ROUTER.md first. PATCH skips fresh ideation and preserves the available artifact. STANDARD uses only relevant decisions; DEEP follows the full applicable workflow. Compile in the order defined by core/03_PROMPT_COMPILER.md.

## 0. Frame the brief

Before visual prose, answer:

- message — the one thing the image must communicate;
- audience — who reads it and what they already expect;
- context — where and at what size the image will live;
- feeling — one dominant, paired, deliberately ambivalent, or evolving residue as the brief requires;
- action or memory — what should remain after viewing.

Use templates/TEMPLATE_CREATIVE_BRIEF.md when the task is large, ambiguous, reference-heavy, or intended to become a reusable project. Infer harmless missing details and state them as open assumptions. Ask only when a missing answer would materially change identity, deliverable, reference authority, or project direction.

## 1. Classify the task

Choose one primary delivery/task mode and zero or more modifiers that change routing. For example, an album may also be reference-guided, fused, and an existing-family instance:

- single hero image;
- reference-guided image;
- selected-frame refinement;
- album or series;
- failed-output diagnosis;
- existing family instance;
- new domain;
- style fusion;
- narrative page or sequence.

Then classify **chat delivery intent** before writing prose. This is independent of family selection:

- `ANALYSIS_ONLY` / cinematic `DISCUSS` — cùng bàn / thảo luận / 先讨论 / “why cinematic” / chưa viết prompt: observe, extract DNA, optionally offer structural directions; do not compile a renderer prompt and do not call an image tool. Map to `task_packet.mode=analysis_only` plus `extensions.cinematic_rebuild.phase`. Silence is not a delegated choice.
- `PROMPT_AUTHOR` — viết / xem / sửa prompt, including “chọn B, viết prompt” and “tự chọn hướng rồi viết luôn”: record the decision, compile, and show the complete three-section prompt in chat; do not call an image tool; do not ask again.
- `IMAGE_GENERATE` — tạo ảnh / generate / render: compile the prompt, then call a generate tool that is actually present in this session.
- `IMAGE_EDIT` — sửa ảnh: pass the target image to an edit tool if that tool exists. Local color/repair requests stay edits; do not force a cinematic rebuild.
- Ask only for a missing required brief or required input image.
- If the needed generate/edit tool is absent: `GENERATION_BLOCKED_TOOL_UNAVAILABLE`, provide the compiled prompt, and do not claim success.

On-demand cinematic rebuild uses `library/20_CINEMATIC_DISCUSSION_AND_REBUILD_WORKFLOW.md`. It does not replace this workflow and does not autoload. Compile (step 17) only after DISCUSS has a `user_selected` or `delegated` decision, or when the request never asked to discuss.

The chat host (Grok, ChatGPT, Claude, Kimi, Grok Build) is not the image generator. Do not default Grok to GPT Image 2.5. Bind only to tools present in the session. Unregistered generators use the generic-image fallback and only parameters that tool accepts. Details live in core/12.

## 2. Resolve source and context authority before extraction

When a task uses references, cultural/historical sources, living artists, community traditions, sacred/ceremonial material, or provenance-sensitive artifacts, resolve this gate before ideation:

- assign authority per dimension;
- separate facts, relations, inferences, interpretations, and unknowns;
- record source, function, community/region/period, rights, provenance, and sensitivity when relevant;
- default status to `unknown`, not green;
- stop extraction while review is incomplete, amber conditions are unresolved, or red restrictions apply;
- declare permitted mechanisms, essential authorized motifs, prohibited extraction, attribution, and authenticity language.

Use core/04 and the standalone per-source context gate in core/07. In the full workspace, also follow `Visual_Resource_Library/CURATION_POLICY.md`. Ordinary self-authored or context-neutral tasks may mark this step not applicable with a reason.

## 3. Diverge before committing

For a routine, tightly specified production request, one candidate may be enough. For an ambiguous, high-value, novel, or family-building task, create at least three concept territories before naming the final mechanism:

- safe — one controlled departure on a reliable base;
- stretch — two changed dimensions with clear jurisdiction;
- wild — a change of ontology, scale, time, viewpoint, or process that still answers the brief.

Write one sentence, primary contrast, cheapest proof, and predicted collapse for each. Select against the brief's message, audience, context, time horizon, distinctiveness, coherence, feasibility, and responsibility. Score each territory's distinction potential: what does it have that the genre average does not, and what does that difference cost? Prefer the strongest territory that still answers the brief over the safest one, and record why the rejected territories lost. Do not converge on the first association merely because it is easy to render.

## 4. Name the mechanism

Complete one sentence:

~~~text
The image works because the viewer first believes ______, then discovers ______ through ______ physical evidence.
~~~

If the sentence is only a style label, the mechanism is not yet designed.

## 5. Author the viewing sequence

Name:

- first read;
- second read;
- discovery or third read;
- return point or rest;
- background role.

State the intended time horizon: instant, medium, or contemplative. A one-second first read is not mandatory when slow discovery is the brief.

Choose one dominant preset:

- face-first;
- identity-prop-first;
- silhouette-first;
- scene-first;
- illusion-first;
- negative-space-first;
- material-transition-first.

## 6. Audit formal structure

Before surface prose, decide:

- two to five major masses and their figure/ground relationship;
- value architecture: illumination, local value, and accent roles;
- dominant directions, rhythm, interval, pause, and balance/tension;
- depth or deliberate-flatness grammar;
- edge ownership and the cause of decisive hard/soft/lost/found edges;
- agreement bed: perspective, scale, light, contact, atmosphere, and material evidence that must agree;
- invariants, bounded variation, deliberate open, and exclusions;
- notan check: the dark/light mass design composes on its own before any surface detail;
- gesture/force axis for every figure or dynamic form — its energy readable from a single line;
- edge economy: decisive hard edges reserved for the anchor and at most one or two secondary points.

Use thumbnail/blur and value studies for large structure. These are tests, not aesthetic laws; evaluate them at the delivery size and time horizon. In the full workspace, the connoisseur-level versions of these passes (notan discipline, force axis, lost-and-found edge economy, and the L3–L5 distinction tests) are detailed in `Knowledge_Mindset/CONNOISSEURSHIP_AND_AESTHETIC_JUDGMENT.md`.

## 7. Choose anchor and base-to-break ratio when relevant

Define:

- stable anchor;
- believable base;
- precise break;
- ratio;
- evidence that proves the break.

Typical starting hypotheses for representational or hybrid work:

| Domain | Base | Break |
|---|---:|---:|
| Photoreal editorial | 80-90% | 10-20% mood/material departure |
| Couture entity | 60-70% real subject | 20-30% entity flow + 10% graphic |
| Pictorial reality | 60-75% coherent space | 25-40% material/flat intervention |
| Painterly dissolve | 65-70% capture | 20% paint transition + optional 10% illusion |
| Live-action in painted world | 70-80% stylized world | 20-30% real human anchor |
| Optical illusion | mechanism-specific | minority contradiction with strong proof |

Abstract, symbolic, flat, diagrammatic, or non-objective work may define the base through shape, value, rhythm, process, or convention instead of optical belief. Ratios must be calibrated rather than forced.

## 8. Select, birth, or fuse a family

- Select when an existing family matches the structure.
- Birth when no family matches anchor, read order, base/break, and light/material logic.
- Fuse when two styles must create emergent rules rather than decorative borrowing.

For fusion, also choose a mode, assign a default owner or explicit co-ownership/conflict rule per load-bearing dimension, declare ratio semantics, invariant/variation, organized productive tension, the intended physical bridge or non-integration relationship, and a per-source context gate. A split-domain system uses boundary plus global physics, not one global blend ratio.

Use library/13_FAMILY_REGISTRY.md.

## 9. Build a DNA card

~~~yaml
subject:
identity_source:
role_aura:
first_read:
immutable_identity:
face_and_gaze:
silhouette:
wardrobe_architecture:
material_behavior:
palette:
signature_entity_or_symbol:
world_role:
emotional_temperature:
forbidden_drift:
~~~

For concepts without a person:

~~~yaml
anchor_object:
spatial_rule:
material_rule:
light_rule:
scale_anchor:
signature_break:
forbidden_drift:
~~~

## 10. Decide layers and medium boundaries

For every layer specify:

- ontology: real, sculptural, printed, flat, animated, painterly;
- thickness;
- shadow behavior;
- focus level;
- whether it shares physical light;
- where transition occurs.

For mixed media, write the render boundary and authored relationship. Add a physical bridge when shared-world integration is intended; for deliberate collage, symbolic overlay, collision, or counterpoint, state the intended non-integration instead.

## 11. Decide camera and body logic

Specify only what serves the mechanism:

- shot scale;
- lens family;
- camera height and angle;
- perspective pressure;
- crop safety;
- body support points;
- foreground lead;
- gaze target.

Perspective comes from camera position and subject distance; format and focal length determine field of view. For face fidelity, keep sufficient camera distance and let closer foreground objects carry the intended exaggeration.

## 12. Decide light relationship

Name:

- motivated source;
- what receives the key;
- fill policy;
- edge separation;
- background exposure;
- highlight and shadow policy;
- how atmosphere carries light.

## 13. Decide optics and detail budget

Allocate:

- highest detail;
- readable medium detail;
- softened support;
- suppressed texture.

Choose depth planes and atmosphere behavior.

## 14. Design color roles in context

Name field, structural secondary, anchor, accent, neutral bridge, and identity/skin protection when relevant. Three to six named colors can be a useful production constraint, not a universal requirement. Test colors in their actual surround, illumination, material, and area ratio; prevent only the drift relevant to the brief.

## 15. Set certainty

Mark each decision hard, soft, or open. Remove hard commands that do not protect identity, safety, hierarchy, or the mechanism.

## 16. Design targeted negatives

Use core/10_NEGATIVE_ENGINE.md. Block actual risks and contradictions, not every imaginable failure.

## 17. Compile

Use core/03_PROMPT_COMPILER.md and the matching family.

## 18. Validate

Use core/09_VALIDATOR_AND_DEBUGGER.md.

## Mode-specific loops

### Single image

Brief → classify → source/context gate when relevant → concept candidate(s) → mechanism → formal structure → DNA → family → compile → preflight.

### Album

Brief → classify → source/context gate when relevant → concept territory → mother DNA → relational invariants → narrative arc → attractor → axis grid → calibration shots → full series → batch validation.

### Selected frame

Preserve everything that works → name one requested change → generate one frame only → forbid new alternatives.

### Failed output

Observe symptom → compare against intent/time horizon → locate failed layer or failed concept → form one causal hypothesis → choose resample, local patch, system repair, or reframe → preserve successful layers → record the retry in templates/TEMPLATE_GENERATION_LOG.md.

### New family

Complete the grammar, context, jurisdiction, invariant, tension, bridge, and family questions in core/07_FUSION_AND_GROWTH_ENGINE.md → write charter → run baselines, repeated samples, three structurally different shots, transfer, stress, at least one ablation, and one documented failure→repair → register only after stable success.

## U05 interface

At `16. Design targeted negatives`, create the control contract and evidence plan before compilation. At `18. Validate`, record result IDs, denominator, failures, confounders, and the next acceptance criterion.
