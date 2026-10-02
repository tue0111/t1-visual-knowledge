# 17 CHARACTER ASSET WORKFLOW

Status: COMMUNITY_HEURISTIC, distilled 2026-09-13 from VSC IP-character-image-system. Not a toy-company imitation, not a claim that assets were rendered.

Load when the user wants a reusable character identity system: master, turnaround, line art, expressions, poses, applications. Do not load for a single hero portrait.

## Purpose

Lock visual invariants, then emit a matrix of asset prompts that stay the same character.

## Trigger

- IP / mascot / character bible / 三视图 / expression sheet / toy-figure plan;
- “from idea to a set of character images.”

## Non-trigger

- one fashion/editorial portrait;
- album of one person in different scenes (use core/08);
- installing Codex skills or claiming Pop Mart as a licensed style.

## Visual invariants

Record and keep across every asset:

- silhouette;
- head/body ratio;
- face structure (eyes, mouth/beak/nose);
- limb logic;
- color zones;
- signature accessories;
- front/side/back structural agreement;
- material language of the chosen presentation.

Allowed to change per asset: expression, pose, scene, packaging layout, merchandise substrate — not identity.

If a base three-view is supplied, it is the character bible. Do not redesign, then expand.

## Asset matrix (default 12, shrink if asked)

1. master render  
2. color three-view  
3. line-art three-view  
4. specification sheet  
5. nine-expression grid  
6. pose sheet  
7. daily scene  
8. commercial/application scene  
9. collectible-figure presentation  
10. packaging  
11. merchandise mockup  
12. social key visual  

Each asset has its own prompt. Do not one-shot the whole matrix in a single image unless the user asked for a sheet layout.

Named commercial toy brands in source texts are visual-trait descriptions only. Translate to “soft vinyl, rounded simplification, clean studio product light.” Do not instruct imitation of a living brand.

## Process

1. Identify input type: idea, text setting, sketch, three-view, or brand brief.
2. Extract character core and must-keep vs optional.
3. Build the invariant list.
4. Choose the matrix subset.
5. Write global style rules, then per-asset prompts through the current contract.
6. Output an acceptance checklist per asset.

Use `templates/TEMPLATE_CHARACTER_ASSET_PLAN.md` for the plan. Analyst may fill invariants and checklist as NON_FINAL_ADVICE; Director owns final prompts.

## Layout rules

- A three-view or expression grid is an explicit sheet layout, not a violation of “one selected frame.”
- A single requested image of three people is one scene, not a grid (see library/14).
- Do not invent that figures were rendered. Prompt/plan delivery is the default unless generation was requested and a tool exists.

## Failure / stop

- missing three-view when the user said the sheet is the bible: ask for it;
- user wants pixel-identical merchandise photos: report untested unless a live tool run exists.

## Acceptance

- invariants match across planned assets;
- no extra accessories unless requested;
- no third-party signature;
- no claim of completed renders without tools.

## Source provenance

GitHub `5fivelogistic-cell/ip-character-image-system` README/SKILL/references as method. This module does not redistribute that repository.
