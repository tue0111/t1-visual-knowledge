# 15 PHOTOGRAPHY RESHOOT WORKFLOW

Status: COMMUNITY_HEURISTIC, distilled 2026-09-13 from Vibe Shot Club / nuyoah photography-scheme reshoot and APSAL authoring language. Not a second compiler, not a measured model capability, not a mandatory startup module.

Load only when the user wants to keep a photographic scheme and restage new shots — typically with a different person, a new camera position, or the same identity in a new scene. Do not load for ordinary portraits, unrelated briefs, or every reference upload.

## Purpose

Separate “who this person is” from “how this set was photographed,” then compile new shots that still belong to the same photographic scheme.

## Trigger

- explicit reshoot / 复拍 / “same studio, new person, new shots”;
- a set of photographic references plus an identity reference, with a request to keep the scheme;
- APSAL-like language about world, event, camera, and light that should map onto existing task-packet / mother-lock / reference-role structures.

## Non-trigger

- ordinary “write a prompt from this photo”;
- explicit edit of a just-generated image (use core/12 edit routing);
- cinematic discussion or structural rebuild of relation/action/space/camera from a still (`library/20`) — reshoot keeps the photographic scheme; cinematic rebuild may translate the scheme;
- style-family birth (use core/07);
- album-only variation of one locked mother without a photographic scheme;
- installing APSAL Studio, Codex plugins, or DNA registries.

## Inputs required

- photographic scheme references (one or more stills);
- optional identity reference, with an explicit role;
- output count, language/brand overrides, and whether the user asked for prompt text, analysis, or generation.

## Reference roles

Assign roles before compiling. Do not let one image own every dimension.

| Role | Owns | Must not silently own |
|---|---|---|
| Identity | stable adult facial structure, age impression, distinctive marks | makeup, hair, wardrobe, pose, expression, scene, light |
| Photographic scheme | light world, exposure relationship, color response, imaging medium, information hierarchy | the scheme-reference person’s face |
| Event / expression | the current beat that causes brows, breath, mouth, gaze, and hands | identity anchors |
| World / set | space, props, weather, occupancy | identity |
| Camera | station, height, lens consequence, crop | moving the sun with the camera |

Write the assignment in the task packet / reference-role schema. If the user asked to keep the same person, identity stays locked. If they asked for a new original adult, do not copy the scheme-reference face.

Identity anchors may include jaw, cheekbone, eye shape, nose, mouth thickness, hairline, and age register. Expression is not an identity anchor. A restrained smile or frown belongs to the current event.

## Information hierarchy

From the scheme references, record:

- subject-clear zone;
- dominant large shapes;
- secondary detail;
- low-detail rest / negative space;
- sharpness and micro-contrast by plane.

Do not write “rich scene” as “every background layer is sharp.” A dark background can still compete if it is high-frequency. Preserve the scheme’s hierarchy; do not auto-upgrade to commercial clarity.

## Lighting topology (descriptive, not a new physics engine)

When camera station changes, keep world-space light: source, occlusion, fall, bounce, and person-versus-background exposure. The camera changes viewpoint; it does not rotate the sun.

If the original depends on underexposure, missed focus, blocked shadows, or grab-shot accident, do not add rim light, continuous warm hair light, leather-fold hero lighting, or a locked sharp face. If the original is clean editorial, do not dirty it.

Subject-bright / background-dark / rim-separation is a scoped lighting preset (see also library/11). It is not a universal repair.

## APSAL mapping — no second authority

APSAL’s thirteen elements, seven DNA types, and nine-shot default are source structure, not OS quotas.

| APSAL language | Canonical home |
|---|---|
| Content / Emotion | current brief + album attractor |
| Subject / World / Look | identity lock, mother lock, wardrobe/world contract |
| Event / Sequence | album axes or this workflow’s event chain |
| Camera / Light / Style / Color-Post | library/11, family, imaging medium |
| Job / QA | core/12 control contract and validator |
| Nine shots | only when the brief asks for a nine-image set |

Do not install APSAL Studio, DNA registries, or `.apsal/` as runtime. Do not require 13 confirmations or 9 images.

## Process

1. Classify each supplied still: identity, scheme, world, pose, or unused.
2. Extract the shared photographic scheme (medium, white balance, contrast, black, highlight roll-off, grain/compression, hierarchy).
3. Cluster lighting sub-schemes; do not average incompatible lights into one prompt.
4. Plan new shots. Reuse scheme and lens grammar; recombine station, action, gaze, and props. Approximate copies of a signature frame are a scarce exception, not the default.
5. For each shot, name one scene-supported event, then let body, eyes, breath, mouth, gaze, and hands answer that event. Do not write only “natural / lively.”
6. Rebuild lighting topology for the new station.
7. Compile through the current prompt contract (three zh-CN sections unless the request overrides format).
8. On a later reshoot round, return to original references. Previous generated images are diagnosis only unless the user explicitly asked to edit that generated image.

## Conflict with edit routing

Reshoot default: original references are the visual truth.

Explicit “sửa ảnh / edit this generated image”: core/12 wins. Use that image as the edit target. Do not force a reshoot.

## Output

- analysis: Vietnamese, observation vs inference vs decision; Analyst remains NON_FINAL_ADVICE;
- prompt-authoring: complete current-contract prompt, no image tool;
- generate/render: compile, then call a session generate tool if present; otherwise `GENERATION_BLOCKED_TOOL_UNAVAILABLE`;
- never claim pixel-identical restaging or same-face across models.

## Failure / stop

- missing scheme or identity when the brief requires it: ask only for that item;
- identity and scheme mixed in one reference with no role: ask once;
- no generate tool on a generate request: blocked token + prompt;
- rights/provenance unknown: do not treat the still as licensed identity.

## Acceptance

- roles do not leak (scheme face does not replace requested identity; identity expression does not freeze all shots);
- new station still belongs to the same light world, or the break is authored;
- hierarchy matches the scheme;
- brand/language/no-logo overrides survive;
- T1 to 9 remains the default rendered-text exception unless overridden;
- no third-party signature (nuyoah, Azhu, APSAL) is rendered into the image.

## Source provenance

Distilled from the local VSC knowledge-base snapshot (inventory hash recorded in the integration-run baseline, not a runtime path). Upstream pins, when used for wording:

- nuyoah-xiezhen-prompt, public GitHub `nuyoah-ai-works/nuyoah-xiezhen-prompt`, MIT declared on the skill page; this module republishes method, not the full SKILL.md.
- APSAL Open, `henyjone/apsal-open`, Apache-2.0 code / CC BY 4.0 starter content; this module maps language only.

No original articles, prompts, or plugin code are copied as higher authority than this OS.
