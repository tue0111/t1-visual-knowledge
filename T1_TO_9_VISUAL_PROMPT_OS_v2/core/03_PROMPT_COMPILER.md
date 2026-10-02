# 03 PROMPT COMPILER

This file converts completed design decisions into the project's exact output format.

Do not compile during cinematic `DISCUSS` or analysis-only turns. The compiler accepts a shot specification that has already resolved direction conflicts (`extensions.cinematic_rebuild.phase` is `DECIDED` or `COMPILED`, `selection_status` is `user_selected` or `delegated`). Keep the current format and language overrides. Pose, station, and action belong in 分镜 unless the brief locked them.

## 1. Non-negotiable output contract

Generated prompt text is Simplified Chinese and uses exactly three semantic sections:

1. 母版锁
2. 分镜
3. 通用负面提示词

The brand rule is inside 母版锁.

For albums, write one mother, multiple separately copyable 分镜 blocks, and one shared negative.

## 2. Default assembly order

Use this order as a human-readable compiler and debugging convention unless a calibrated model/version-specific route has stronger evidence:

~~~text
image purpose and ratio
→ viewing time, dominant read, and hierarchy
→ major masses, figure/ground, and spatial container
→ camera/viewpoint and scale
→ identity and DNA
→ face, gaze, expression
→ pose and body support
→ entity, prop, or mechanism
→ background role
→ value and light architecture
→ color roles in context
→ wardrobe, material, process, and edge behavior
→ depth, atmosphere, rhythm, and detail budget
→ invariant/variation, boundary, bridge, and cultural no-go when relevant
→ brand rule
→ shot-specific variables
→ targeted negatives
~~~

The thinking order lives in core/02_DECISION_WORKFLOW.md. This writing order makes omissions and contradictions easier to inspect; it does not by itself prove a universal generator-order effect. Record any model/version/date-specific order advantage as calibrated evidence before promoting it.

## 3. What belongs in 母版锁

Include only stable cross-shot information:

- family and project identity;
- reference and identity lock;
- world and render boundary;
- viewing sequence, hierarchy, and relational invariants if stable;
- wardrobe/material DNA;
- palette roles;
- signature mechanism or named system;
- fusion jurisdiction, productive tension, and bridge when relevant;
- camera and light language if stable;
- realism or stylization finish;
- T1 to 9 brand rule;
- single-image/no-grid instruction.

Do not put shot-specific pose, scene, or focal length here unless truly immutable.

## 4. What belongs in 分镜

Each shot defines:

- one shot name;
- aspect ratio;
- camera and lens;
- body state and support;
- gaze/energy state;
- one scene;
- one dominant mechanism;
- bounded variation and one visible tension/bridge proof when relevant;
- light motivation;
- foreground/middle/background plan;
- one anti-attractor sentence when needed.

Do not merge multiple shot concepts into one image.

## 5. What belongs in 通用负面提示词

Include:

- Tier 1 format/anatomy/artifact blockers;
- family signature collapses;
- identity and wardrobe drift;
- medium-boundary bleed;
- album attractor blockers;
- exact logo exception.

Keep per-shot risks in that shot when they are not shared.

## 6. Strict mode versus art-direction mode

Use strict mode for:

- identity replication;
- selected-frame correction;
- complex anatomy;
- cross-medium boundaries;
- optical illusion;
- exact character DNA;
- cross-model portability.

Use art-direction mode for:

- strong reference images;
- calm photobooks;
- lifestyle editorial;
- exploratory concepts;
- natural photographic variation.

Strict mode locks mechanism and boundaries. Art-direction mode still hard-locks identity, safety, hierarchy, and family signature, but leaves micro-gesture and incidental life open.

## 7. Prompt length control

A long prompt is justified when it protects:

- cross-medium boundaries;
- multi-layer physics;
- identity continuity;
- a complex album mother;
- an illusion mechanism.

Shorten when the reference already carries:

- exact face;
- outfit;
- pose;
- composition;
- world appearance.

Never duplicate the same instruction in poetic, technical, and negative forms unless an observed model failure requires reinforcement.

### Information density and module jurisdiction

Judge a prompt by independent decisions and role coverage, not character count. A long string of evaluative adjectives can still be thin; a short production-type term can carry dense conventions about capture, layout, purpose, or identity.

Assign every dense module one jurisdiction:

- capture or medium — how the subject is photographed or rendered;
- layout or order — how the frame is organized;
- purpose or concept — why the asset exists and what it communicates;
- subject identity — whose silhouette, palette, symbols, and behavior reorganize the system.

Do not let several labels compete for the same role without an explicit hierarchy. A separator between labels has no special force; compatible jurisdiction does the work.

### Compression modes

- **Discovery:** one dense production type plus a subject; fast and emergent, but high variance.
- **Direction:** one compatible module per role plus the important constraints; balanced authorship and emergence.
- **Production or portability:** expand load-bearing labels into visible camera, layout, identity, light, material, and keep/change rules.

Use a compressed prompt to discover a direction, then decode and lock the decisions that made the winning result work. One attractive sample proves potential, not stability; test repeated samples, distinct subjects, and boundary ratios before promoting a short stack into a reusable route.

## 8. Copy-ready single-image skeleton

~~~text
【母版锁 · [项目名]】

[参考与身份锁。]
[家族、视觉机制与阅读顺序。]
[人物或主体 DNA。]
[服装、材质、色板与世界规则。]
[光线、空间、景深与清晰度预算。]
[跨媒介边界与共同物理；不适用则省略。]
[固定品牌角标规则。]
每次只生成一张指定画面，不生成拼图、九宫格或多个备选。

【分镜 · [镜头名]】

[比例、焦段、机位、构图。]
[动作、支撑点、视线、情绪。]
[前景、中景、远景。]
[本镜头唯一机制与物理证据。]
[光源与景深。]
[反吸引子限制。]

【通用负面提示词】

[格式、解剖、身份、材质、背景与家族崩坏。]
[跨媒介漂移或错觉失效。]
除右下角指定的“T1 to 9”品牌角标外，禁止任何其他文字、标志、签名和水印；禁止角标拼写错误、大小写错误、空格错误、缺字、多字、重复或乱码。
~~~

## 9. Album skeleton

~~~text
【母版锁 · [相册名]】

[系列稳定 DNA。]
[叙事与情绪弧线。]
[统一摄影、材质、世界、修图和品牌规则。]
[明确哪些变量允许变化。]
每次只启用一个分镜，不得混合多个分镜。

【分镜一 · [名称]】
[完整单镜头模块。]

【分镜二 · [名称]】
[完整单镜头模块。]

[继续添加；每个分镜独立可复制。]

【通用负面提示词】

[系列共享负面。]
[吸引子禁令与重复姿态禁令。]
[品牌角标例外。]
~~~

## 10. Final compiler checks

## U05 interface

Compilation consumes a validated task packet, analyst handoff, control contract, and generator profile. The final prompt still has exactly the project-mandated three semantic sections; runtime settings and evidence metadata travel beside it, not as a hidden fourth prompt section.

Before delivery:

- all prompt text is Chinese except permitted exact tokens;
- exactly three semantic sections exist;
- logo is inside the mother;
- no positive/negative contradiction;
- one shot means one image;
- every listed element has a role;
- co-role members with shared function, causal behavior, and compatible ontology form one named system; deliberate distinct systems state their relationship;
- cross-medium work has a render boundary and authored relationship, plus a physical bridge when shared-world integration is intended;
- major masses, value, edge, space, and viewing sequence support the brief at its intended time horizon;
- fusion has a default owner or explicit co-ownership/conflict rule per load-bearing dimension, invariant relations, organized productive tension, and evidence for the chosen physical bridge or deliberate non-integration;
- cultural no-go and authenticity boundaries are respected when relevant;
- the negative is targeted rather than indiscriminate.
