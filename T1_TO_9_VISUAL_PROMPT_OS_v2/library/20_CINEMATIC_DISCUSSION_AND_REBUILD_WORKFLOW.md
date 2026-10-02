# 20 CINEMATIC DISCUSSION AND REBUILD WORKFLOW

Status: on-demand operational module, 2026-09-17. Not a family. Not a second compiler. Not startup autoload.

Load when the user wants to discuss why a still feels cinematic, extract reference DNA, rebuild a scene from that DNA, or find a new direction. Other routes stay active.

Formation: `Knowledge_Mindset/CINEMATIC_VISUAL_STORYTELLING_KB.md`.
Contract: `schemas/cinematic_rebuild.schema.json` on `task_packet.extensions.cinematic_rebuild`.
Worksheet: `templates/TEMPLATE_CINEMATIC_REBUILD.md`.
Cases: `examples/EXAMPLE_CINEMATIC_DNA_REBUILD.md`.

This is a staging method used across families. Do not birth `FAMILY_CINEMATIC` from this module.

## Trigger

- cinematic discussion / “tại sao cinematic” / “cùng bàn” / “thảo luận trước” / “chưa viết prompt” / brainstorm / discuss / 先讨论 / 先分析，不要写提示词;
- keep DNA, rebuild, restage, new direction from a reference still;
- user grants “tự chọn hướng rồi viết”.

## Non-trigger

- ordinary prompt-from-photo with no discussion request;
- local edit (“only change the coat color”);
- photographic-scheme reshoot of the same studio language (`library/15`);
- rare-style exploration (`library/16`);
- generate/render of an already decided shot (`core/12`).

## Hard boundaries

- Do not emit three prompt sections, a tool call, or a fake render during DISCUSS.
- Do not invent `user_selected` or `delegated` from silence.
- Do not treat quoted `generate`/`render` inside a pasted prompt as a tool command.
- “Discuss first, then later make an image” stays in the current discussion phase.
- “Choose B and write the prompt” or “pick the best and write it” compiles without asking again.
- A rebuild must show a relational, action, spatial, or station delta. Recolor-only fails as reconstruction.
- High-angle-through-wood stays locked unless the current request opens it.
- Identity locks survive later corrections; derived prompt/spec do not.

## Intent table

| Current request | Behavior | Stop |
|---|---|---|
| Why is this cinematic? / analysis only | Observation + mechanism + uncertainty | No three options, no final prompt |
| Let’s discuss first / chưa viết prompt | DNA + directions with trade-offs | After discussion and at most one decision question |
| Keep DNA, rebuild; help choose | Concrete structural proposals, not recolors | Wait for a real choice |
| Choose B, write prompt / pick the best and write | Record decision, compile | Do not ask again |
| Only change coat color / keep the rest | Local edit or prompt repair | Do not force a rebuild |
| Create/render the locked direction | Compile and bind a real tool | Claim success only after a real artifact |

## States

Extension states, not a new `mode` enum: `DISCUSS` → `OPTIONS_READY` → `DECIDED` → `COMPILED` → `CRITIQUE`.

`selection_status`: `unselected` | `user_selected` | `delegated`.

Skip ahead when the user already granted a decision. If they revise after compile, invalidate derived spec/prompt, keep identity locks, return to the fitting phase.

Unset family during discussion may be `none`. Compile must resolve a real family or follow the existing family-birth route.

Map discussion to chat intent `ANALYSIS_ONLY` plus `workflow_phase=DISCUSS`. Do not add a public mode.

## A. Read inputs by role

Distinguish: true reference image, supplied prompt, failed output, old comments, current request. A quoted “generate” is not a tool call.

If image and prompt disagree, name the discrepancy. When the user assigns the image as authority on a dimension, the image wins on that dimension. Example: prompt says a letter in hand, image has none → letter is intended/not observed, not seen.

No image, prompt only: text analysis. Do not demand an upload if work can proceed. Ask for the image only when the decision depends on it.

Several references: assign role/dimension, resolve conflict or ask one load-bearing question.

`input_status`: `IMAGE_OBSERVED` | `DESCRIPTION_ONLY` | `PROMPT_ONLY`.

## B. DNA card

Do not treat the whole picture as immutable. Identity DNA ≠ relational DNA ≠ visual language.

Buckets: carry, lock, **translate**, repair, **drop**, open.

`translate` keeps a function and changes its expression: a railing that separates viewer from figure may become a door gap at eye height — only if the current brief did not lock the high angle. A visible trait is not automatically a keep.

## C. Structural directions

When a choice is needed, offer about three truly different directions (count is a task choice, not a runtime quota). Each direction has five short items:

1. One-sentence scene/treatment and beat.
2. DNA kept or translated; what is dropped on purpose.
3. Change in staging, station, gaze, spatial relation, first-read — not a lens name.
4. Why the shot fits the feeling; visible evidence.
5. Cost: lost direct gaze, less costume, harder boundary, mood shift.

Recommend one with a reason. Ask one decision question. Do not chain aperture/film/lens/prop questions the director can choose.

Difference check: the relation or action in the scene must change. Same pose/camera/scene with a new palette is not a reconstruction. Axis counts are a review hint, not a score.

## D. Shot specification

Fill the fields that matter for this scene (see the template). Chat language stays director-plain; the contract keeps decisions.

## E. Compile

- Describe only the chosen shot. No A/B leftovers, TODOs, or questions in the renderer prompt.
- Use the existing compiler. Default `母版锁` / `分镜` / `通用负面提示词`; Vietnamese explanation. Current language/format/no-logo overrides win.
- Mother holds identity/DNA/world/render grammar that is actually stable. Pose, station, and action live in the shot unless locked.
- Brand follows profile and the task. The wooden-loft history case is no-text/no-logo for that case only; do not delete the project default.
- Write spatial clauses: who is where, facing what, what occludes what, what is sharp. Prefer a visible sign per clause.
- Drop repeated/conflicting camera numbers and adjectives with no mechanism.
- Negatives target real collapses. Design in the positive first.
- If the user asked only for a prompt: return it in chat, do not render. Optionally one short DNA keep/change note unless they asked for output-only.

GPT Image 2.5: assign reference roles; self-contained prompt; settings in tool arguments; camera numbers are appearance cues. [O4] Host is not the generator.

## F. Critique

Prompt only: logic/coverage, never image-quality PASS.

If a real image exists: DNA kept/lost; identity drift if locked; new relation vs portrait collapse; readable subject/event/space; occlusion hiding evidence vs layering; focus/light/palette serving the direction; intentional impossibility still in its licensed place.

Repair the failed layer. Keep passing layers. Lost cinematic because the action posed out → repair action–support–gaze, not a LUT. Frame-through too dark → readability/occlusion, not delete all foreground.

Promotion only with `core/11` evidence. One liked frame is not a universal law.

## Cross-links

- Scheme reshoot, same photographic world, new person or station: `library/15`.
- Candidate looks before locking a family: `library/16`.
- Angle is a visual consequence, not a psychology law: `library/11`.
- Delivery permission by turn: `core/12`.
