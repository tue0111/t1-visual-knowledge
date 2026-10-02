# 19 STORYBOARD AND VIDEO HANDOFF

Status: COMMUNITY_HEURISTIC, distilled 2026-09-13 from VSC character-card, virtual-couple vlog, contact-sheet, and Blender-blockout notes. This module prepares still assets and prompts. It does not render video.

Load when the user wants multi-frame memory sheets, identity cards for motion, storyboards, or a video-generation handoff. Do not load for a single selected frame.

## Purpose

Separate three layers that source posts often mix:

1. **Asset readiness** — identity card, three-view, 4×4/2×2 memory sheets, storyboard page;
2. **Generation provider** — whatever image/video tool is actually in session (often absent);
3. **Editing provider** — FFmpeg / NLE / other local tools, never assumed installed.

## Trigger

- character card / 角色设定卡 / turnaround for video;
- virtual couple travel vlog workflow;
- 4×4 contact sheet, 4×5 storyboard, 8-cut anime storyboard;
- white-box / Blender blockout as camera-path rehearsal;
- “prepare clips but I have no video model.”

## Non-trigger

- one photograph;
- album of independent stills with no motion handoff (core/08);
- installing Topview, Seedance, Remotion, HyperFrames, Blender, or FFmpeg.

## Layout vs single-frame law

The OS rule “one selected frame is not a grid” still holds for a single hero request.

Explicit storyboard/contact-sheet/character-card layouts are allowed when the user asked for that workflow. Record separately:

- `subject_count`
- `image_count`
- `layout` (`single` | `sheet` | `grid`)
- `video_clip_count`

Three adults in one summer photo remain `layout=single`. A requested 4×4 iPhone wall is `layout=grid`.

## Character card for motion

Goal: identity anchor for later frames, not eight pretty pictures.

Recommended information, not a mandatory template:

- large full-body front and 90° side for proportion/gait;
- head set: front, back, L45, R45, restrained smile, restrained frown;
- bone-structure lock in prose (jaw, zygoma, chin, eye, brow, nose, mouth, age);
- no readable in-image labels (`FRONT`/`SIDE` can be learned as texture);
- unified exposure/color across panes;
- original adult identity from prompt, not a real-person photo, when platform/legal risk is in scope.

Do not treat photoreal as “is a real person.” Do not write “looks like [living celebrity].”

A single beauty still is a weak motion reference: unseen angles will be invented.

## Virtual-couple / travel-memory path

Default asset order:

1. one 4×4 memory wall in a single generation (identity continuity);
2. split to four 2×2 sheets only if a local splitter exists; otherwise report the crop step as missing automation;
3. male/female studio cards;
4. four clip prompts (handheld, ordinary framing, not a luxury ad unless asked);
5. music prompt as text only;
6. assembly instructions.

If no video provider: deliver assets/prompts/handoff. `video_rendered = NOT_RUN`.

If no local 4×4 splitter: do not pretend four 2×2 files were cropped.

Do not use unauthorized real-couple photos for public demos.

## White-box / blockout

A grey blocking pass is a rehearsal of space, path, and camera. It does not guarantee the video model will copy it.

- build only structures that change occlusion, path, or camera;
- character mesh precision follows action need (stand-in / posed humanoid / keyed contact);
- prompts must add performance, force, and contact the blockout cannot show;
- this OS does not run Blender or local agents.

## Process

1. Name the handoff: still sheet, identity card, storyboard, or video clips.
2. Lock identity and wardrobe.
3. Choose layout explicitly.
4. Compile still prompts through the current contract.
5. For video: write clip prompts with time beats; list required reference images.
6. State provider status: available / missing / NOT_RUN.

## Failure / stop

- generate-video requested without a video tool: `GENERATION_BLOCKED_TOOL_UNAVAILABLE` plus prompts;
- missing identity stills: ask;
- do not claim Seedance/Topview/FFmpeg ran.

## Acceptance

- layout matches the request;
- identity instructions are bone-level, not “keep consistent”;
- no fake rendered clips;
- brand/language overrides survive;
- no third-party watermark.

## Source provenance

Voxcat character-card articles, VSC virtual-couple skill (`vibeshotclub/vsc-skills/virtual-couple-travel-vlog`), contact-sheet prompt, Foyege white-box tutorial (X + community transcript). Methods only. Locked forum prompts remain unrestored.
