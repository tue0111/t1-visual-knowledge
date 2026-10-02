# 18 PEN-AND-WASH PRESET

Status: COMMUNITY_HEURISTIC, distilled 2026-09-13 from Azhu Pen & Wash Travel Sketch v0.23 method. Scoped preset, not a new family, not a change to OS delivery format.

Load only when the user asks to turn a travel/street/portrait/food/pet/object/nature still into a spacious pen-and-wash sketch. Do not load for ordinary photographic work.

## Purpose

Keep identity, pose, main objects, environment anchors, and light logic, then shrink the scene into a compact island on quiet paper.

## Trigger

- 钢笔淡彩 / pen and wash / travel sketch / PaperMemory-like paper memory when the user wants ink+wash, not a generic illustration.

## Non-trigger

- analysis-only of a photo with no conversion request;
- “make it artistic” without this medium;
- forcing image-only delivery on a prompt/analysis request.

## Visible mechanism

- near-black waterproof-ink contours, light continuous line;
- transparent watercolor, limited palette from the source (about four or five colors);
- paper: quiet ivory/off-white, not yellowed souvenir paper unless requested;
- subject cluster near center, large quiet paper around it (source used ~15% subject / ~80% paper as a heuristic, not a hard gate);
- edge context as support only;
- ignore source typography by default. Preserve readable source signage only when the current user explicitly requests it and the reference is legible; do not invent lettering.

Aspect: follow the source orientation; honor an explicit user ratio.

## Delivery

This source skill defaults to image-only inside its own tool. In this OS:

- prompt/analysis request: return analysis and/or the three-section prompt; do not call an image tool;
- generate/render request: compile, then use a session generate tool if present; otherwise `GENERATION_BLOCKED_TOOL_UNAVAILABLE`;
- do not add the Azhu signature, `nuyoah`, or any third-party mark;
- default brand rule remains `T1 to 9`; an explicit user brand, no-logo or no-text request overrides that default.

## Process

1. Read the source still (or described scene).
2. Choose ink/wash/paper/negative-space decisions.
3. Compile through the current contract.
4. Multi-image inputs stay one result per source, in order, unless a collage was requested.

## Acceptance

- identity and main spatial relations survive;
- paper stays quiet; no filled decoration;
- no third-party signature;
- prompt-only tasks do not generate.

## Source provenance

GitHub `azhu032/azhu-pen-wash-travel-sketch-v0-23` (MIT declared). Method only; full SKILL.md is not the OS authority. PaperMemory (VSC open-source page) is a related paper-memory idea; its public page was login-gated in the snapshot and is not copied here.
