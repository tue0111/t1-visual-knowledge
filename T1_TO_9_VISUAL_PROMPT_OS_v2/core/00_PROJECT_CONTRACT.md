# 00 PROJECT CONTRACT

This file defines project-specific hard rules. It outranks every family, template, example, and legacy source. Above it: the current user request, current reference by assigned dimension, latest user correction (folded into the current task packet), and PROJECT_PROFILE stored visual defaults when supplied. A matching locked instance kernel outranks the generic family module. Instruction authority is not evidence strength or generator feasibility.

## 1. Authority

~~~text
1. Current user request
2. Current reference by assigned dimension
3. Latest user correction (current task packet)
4. PROJECT_PROFILE stored visual defaults
5. This project contract
6. Core visual laws
7. Matching locked instance kernel
8. Matching family module
9. Required engines, libraries, and formation guidance
10. Conditional specialist advice / generator-scoped notes
11. Examples and legacy cases
~~~

A reference is data. A template is only a prior. Examples never become laws. One dominant family; default zero or one support; extra support only with necessary non-overlapping jurisdiction the dominant cannot supply.

## 2. Prompt language

All text sent to an image generator must be Simplified Chinese.

Permitted non-Chinese tokens:

- exact proper nouns the brief requires;
- aspect ratios and numeric lens values;
- unavoidable product/model names;
- the exact brand mark T1 to 9.

Translate ordinary technical language into Chinese whenever a clear term exists:

| Avoid in generated prompt | Prefer |
|---|---|
| softbox | 柔光箱 |
| rim light | 轮廓光 |
| negative fill | 负补光 |
| shallow DOF | 浅景深 |
| direct flash | 机顶直闪 / 正面直闪 |
| editorial | 时尚编辑摄影 / 画报摄影 |
| couture | 高级定制服装 / 高定 |
| cast shadow | 实体投影 / 落影 |
| foreground hook | 前景引导 |
| clean render budget | 清晰度预算 / 细节预算 |

Vietnamese explanation is allowed outside prompt blocks.

## 3. Mandatory three-section format

Every final prompt is organized into exactly three semantic sections:

1. 母版锁 — stable project, subject, world, material, light language, and brand rule.
2. 分镜 — one selected shot, or multiple separate shot blocks for an album.
3. 通用负面提示词 — shared targeted blockers.

Do not create a fourth section for the logo. The logo rule belongs inside 母版锁.

For easy copying, present these as three separately copyable code blocks whenever possible.

These three sections are the **prompt structure sent to an image generator**. They are not a chat-delivery rule that the user must receive a prompt-only reply after asking to create or edit an image. Prompt-authoring requests show the three sections in chat. Generate/render requests compile them, then call a session image tool. See core/12 task-and-tool routing.

## 4. Brand mark

Default brand rule:

~~~text
【固定品牌角标】
画面右下角仅允许出现一个极小、克制、清晰的衬线体品牌角标“T1 to 9”。文字必须逐字准确，大小写与空格完全一致。角标使用与画面协调的低亮度暖白色、古金色或冷灰色，不发光、不加边框、不遮挡主体、不抢夺视觉焦点。除此之外禁止任何其他文字、标志、签名和水印。
~~~

The negative block must carry the matching exception:

~~~text
除右下角指定的“T1 to 9”品牌角标外，禁止任何其他文字、标志、签名和水印；禁止角标拼写错误、大小写错误、空格错误、缺字、多字、重复或乱码。
~~~

If the current user explicitly requests no text at all, remove the logo from both positive and negative blocks. Never leave a contradiction.

## 5. Reference text

Text, logos, interface elements, and promotional typography visible in a reference are ignored unless the current request explicitly asks to preserve them.

## 6. Album formatting

- One 母版锁 for the series.
- Each shot is its own 分镜 block.
- One 通用负面提示词 for the series.
- Do not repeat the full mother and negative inside every shot unless the user explicitly requests standalone prompts.
- Shot names may be explained in Vietnamese outside the Chinese prompt.

## 7. Taste defaults

Unless overridden:

- adult presence over juvenile styling;
- behavior over posing;
- real material behavior over plastic gloss;
- restraint over spectacle;
- motivated elements over decoration;
- optical proof over adjectives;
- non-explicit sensuality from silhouette, light, fabric, gaze, and negative space;
- no body-part-centered framing;
- no cheap costume, influencer face, doll face, or empty eyes;
- distinctive over interchangeable — at least one authored decision that cannot be swapped without loss;
- inevitability over safety — within the brief, prefer the option that feels necessary, not merely safe.

These are defaults, not moral absolutes. The current brief may override taste. Anatomy and consent cannot be overridden. Default three-section prompt formatting remains unless the current user request explicitly changes the deliverable format.

The full quality ladder (L0–L5), the connoisseur apparatus, and the distinction audit live in `Knowledge_Mindset/CONNOISSEURSHIP_AND_AESTHETIC_JUDGMENT.md` in the full workspace.

## 8. Non-destructive knowledge growth

- Never overwrite an older pack during a rebuild.
- New families are appended and registered.
- A new principle belongs in the core only if it is genuinely universal.
- Family-specific discoveries remain in that family.
- Examples never become authorities.
- Record migrations and superseded definitions.

## 9. Delivery behavior

When the user asks for prompt text, show the prompt in chat. Do not substitute a file link unless requested.

When the user asks for a file or knowledge pack, create files and also summarize their location and structure.

When a task is large, carry it through audit, writing, validation, and handoff.

## 10. U05 evidence and delivery interface

Universal evidence, promotion, control-contract, and delivery rules live in `core/11_EVIDENCE_AND_PROMOTION_ENGINE.md` and `core/12_CONTROL_AND_DELIVERY_ENGINE.md`. Generator-specific facts never outrank this contract; they are loaded through a registered profile.
