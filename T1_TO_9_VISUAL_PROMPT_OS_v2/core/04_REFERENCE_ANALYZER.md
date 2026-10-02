# 04 REFERENCE ANALYZER

Use this engine whenever one or more references are supplied.

## 1. Reference authority

Current reference and correction outrank family defaults. Do not fight a strong reference with a generic template.

## 2. Classify each reference

A reference may provide one or more roles:

- identity reference;
- pose reference;
- wardrobe reference;
- composition reference;
- lighting reference;
- material reference;
- environment/style reference;
- selected output frame;
- failure evidence.

Do not assume every visible property should be copied.

## 3. Fast visual diagnosis

Read the reference in this order:

1. What are observable facts, before interpretation?
2. What lands first, what returns, and what is discovered later?
3. What are the major masses, value groups, figure/ground, rhythm, and edge ownership?
4. What is the stable anchor and the background's primary role?
5. What projection, viewpoint, camera distance, or deliberate flatness is implied?
6. Where does light come from, and do form, cast shadow, atmosphere, and material agree?
7. Which materials are proven by highlights, folds, edges, thickness, shadow, or refraction?
8. What formal/material mechanism makes the image work?
9. Which interpretation is evidence-backed, which is uncertain, and which depends on cultural context?
10. What would most likely drift if regenerated?
11. What visible text, logo, or interface should be ignored?

## 4. Carry, lock, translate, repair, drop, and open

Divide observations into buckets. A visible trait is not automatically a lock. Identity DNA is not relational DNA.

### Carry

The reference already shows it clearly. Let the image carry it without over-description.

### Lock

Identity, must-not-change wardrobe, signature material, read order, or a mechanism that must survive because the current brief assigned it.

### Translate

Keep the function, change the expression. A high railing that separates viewer from figure may become a door gap at eye height — only if the current brief did not lock the original station.

### Repair

A flaw in the reference or requested change. Prompt only this layer strongly.

### Drop

Present in the reference but not required for this task. Drop is explicit, not accidental omission. Face-series swaps that discard original makeup/hair/scene belong here when the user asked for a new series.

### Open

Micro-gesture, incidental environmental life, exact wrinkle, tiny camera accident.

## 5. Reference types

### Face reference

Preserve:

- whole facial proportion;
- eye spacing and eyelid shape;
- nose and lip relationships;
- jaw and cheek structure;
- age and skin tone;
- gaze quality and emotional register.

Do not reduce identity to isolated feature adjectives.

When the same face must enter a different target series (new makeup, wardrobe, scene, or light world), keep only the identity anchors from the reference and let the target series take over everything else — the reference's original makeup, hair, wardrobe, and scene are dropped unless the user explicitly asks to keep them:

~~~text
参考图仅用于保持五官辨识度；不保留参考图的原妆容、原发型、原服装与原场景。角色已完成目标系列妆造后，再进入目标拍摄现场。
~~~

When the user wants to keep the photographic scheme and restage shots (new person, new station, or same identity in a new event), also load `library/15_PHOTOGRAPHY_RESHOOT_WORKFLOW.md`. Identity and photographic-scheme references must not share one undifferentiated role. Expression follows the current event, not the identity still. A later reshoot round returns to original references; a generated image is diagnosis-only unless the user explicitly asked to edit it (core/12).

### Pose reference

Preserve:

- support points;
- weight-bearing leg or arm;
- shoulder and pelvis relationship;
- gesture axis;
- camera-to-body angle.

Do not copy anatomy errors.

### Style/environment reference

Decompose into:

- original context, function, support, and process when relevant;
- spatial logic;
- value structure and light logic;
- shape and silhouette grammar;
- mark-making;
- edge hierarchy and material behavior;
- color distribution rather than isolated swatches;
- rhythm, time, scale, body, and gaze;
- iconographic logic;
- emotional/cultural register.

Describe the mechanisms and uncertainty. Do not rely only on a style or studio name.

For cultural, historical, sacred, ceremonial, living-heritage, or provenance-sensitive sources, apply the standalone per-source context gate in core/07. In the full workspace, also follow `Visual_Resource_Library/CURATION_POLICY.md`. Do not detach a motif, calligraphy, garment, or ritual object from function and community context.

### Selected frame

Preserve all successful layers. Change one requested variable. Explicitly forbid grid, alternatives, and redesign.

## 6. Multiple references

Assign one authority per dimension:

~~~yaml
identity: reference_A
pose: reference_B
wardrobe: reference_C
environment: reference_D
lighting: reference_E
current_user_correction: highest
~~~

If two references conflict on the same dimension, the current user correction decides. If none exists, choose one explicitly rather than averaging.

## 7. Text and logo handling

Ignore visible text, titles, interface, subtitles, Steam/store graphics, promotional logos, and watermarks unless the user explicitly requests them.

The project brand T1 to 9 follows core/00_PROJECT_CONTRACT.md and is independent from reference text.

## 8. Cross-medium reference analysis

When a reference combines live action and stylization, identify:

Render boundary:

- what remains photographic;
- what remains animated, painted, graphic, printed, or sculptural;
- where style must not bleed.

If the domains are intended to share one physical world, test a physical bridge:

- shared perspective;
- light;
- ground contact;
- shadow;
- occlusion;
- reflection;
- atmosphere;
- motion direction.

If deliberate collage, symbolic overlay, unresolved collision, or counterpoint is intended, record that authored non-integration and the formal relation that keeps it purposeful; do not add physical cues that erase the distinction.

Example derived from the project:

~~~text
真人女性保持真实摄影皮肤、发丝与白裙；人物之外的环境保持手绘动画三维材质。两者共享摄影机透视、太阳方向、地面尺度、接触阴影、空气深度与风向。
~~~

## 9. Reference-to-prompt workflow

1. State the reference roles.
2. Separate facts, relations, inferences, interpretations, and uncertainties.
3. Extract only structurally important and context-permitted cues.
4. Write `preserve / translate / avoid / uncertain` and decide carry/lock/translate/repair/drop/open.
5. Build a DNA or source-grammar card. For cinematic discussion/rebuild also fill `extensions.cinematic_rebuild` (library/20); do not treat every reference as immutable coordinates.
6. Choose the closest family; for fusion, assign jurisdiction and context gate. Discussion may keep `none` until compile.
7. Add only likely drift controls.
8. Compile in three sections only when the current intent is prompt-author, generate, or edit — not during DISCUSS / analysis-only.
9. Validate that the prompt does not redundantly re-describe the whole image or make a false authenticity claim. If image and prompt disagree, keep observation and intention separate; the current assignment wins.

## 10. Failure patterns

## U05 interface

Emit dimension-specific reference roles and separate documentary evidence from render evidence. A role marked `IGNORE` is not allowed to leak into the compiled prompt; an `OPEN` role must remain an explicit decision, not an accidental default.

| Failure | Cause | Repair |
|---|---|---|
| Model copies unwanted text | reference text not explicitly ignored | forbid all reference typography |
| Face drifts | identity reduced to style adjectives | lock holistic proportions and reference authority |
| Pose mutates | support points omitted | state weight, supports, and camera-body angle |
| Reference becomes generic | only labels copied | decompose mechanisms |
| Prompt fights image | too much redundant description | carry strong evidence; lock only drift |
| Mixed media becomes one style | no render boundary | specify forbidden style bleed |
| Subject looks unintentionally pasted in an integrated world | missing physical bridge | add shared perspective, light, shadow, occlusion, scale |
| Deliberate collage loses its argument | physical integration erases the intended difference | restore the render boundary and state the formal or symbolic relationship |
| Cultural source becomes costume | motif extracted without function/context | pause; research provenance, community, restriction, and transferable mechanism |
| Reference analysis overclaims meaning | observation and interpretation collapsed | split fact/relation/inference/interpretation/uncertain |
