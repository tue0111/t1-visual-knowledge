# 11 CAMERA, LIGHT, AND OPTICS LIBRARY

Operational choices for the compiler. Principles remain in core/01_CORE_LAWS.md.

## 1. Field of view, camera distance, and shot scale

Focal-length numbers below are full-frame-equivalent starting language. Sensor/film format and crop determine field of view; camera position and subject distance determine perspective. A short lens does not distort a face by itself—moving the camera close to fill the frame creates the perspective exaggeration. State distance/position and keep faces away from stretched frame edges when fidelity matters.

| Goal | Starting full-frame-equivalent language |
|---|---|
| face fidelity and beauty close-up | 70-100 millimeter |
| face plus upper wardrobe | 50-70 millimeter |
| natural environmental portrait | 35-50 millimeter |
| dynamic foreground pressure | 24-35 millimeter |
| architecture and environmental scale | 16-28 millimeter |
| phone snapshot | small-sensor 24-28 millimeter equivalent |
| compressed landscape layers | 70-135 millimeter |
| material macro | 85-120 millimeter macro |

Chinese execution phrases:

~~~text
85毫米人像镜头，脸部比例自然，浅景深，眼睛与微表情为最清晰焦平面。
35毫米环境人像镜头，略宽但透视受控，前景制造纵深，脸部不得位于画面边缘。
24毫米等效广角，人物脸部保持足够拍摄距离并避开画面拉伸边缘，透视压力由更近的前景承担，禁止放大鼻子、拉长下巴或扭曲脸型。
~~~

## 2. Camera pressure devices

- low-angle pressure (authority or monument only when acting, scale, and the brief support it — height is not a psychology law);
- high-angle overview (does not by itself prove weakness, power, or surveillance);
- foreground prop attack;
- frame-through-object aperture;
- strict profile alignment;
- over-shoulder look-back;
- top-down spiral;
- floorline/waterline/tableline;
- mirror/reflection;
- negative-space landscape;
- rear-view closure;
- long-exposure motion;
- forced perspective.

Use one dominant device per shot by default. Multiple devices are valid when they share hierarchy and do not create competing perspective or attention instructions.

Camera height, distance, and FOV are visual consequences. Do not infer exact focal length, aperture, or camera height from a still without metadata. Wide shot is a crop/scale choice; wide-angle is a FOV/perspective effect. A look into the lens is gaze direction, not proof of a second observer or a POV shot. Cinematic discussion/rebuild: `library/20_CINEMATIC_DISCUSSION_AND_REBUILD_WORKFLOW.md`.

## 3. Light relationship

Specify the fields needed to disambiguate the selected light system:

- source;
- direction;
- softness or hardness;
- subject receiver;
- fill policy;
- edge separation;
- background exposure;
- atmosphere response.

Base block for a lit subject against a retreating field; do not use for high-key, silhouette, luminous-background, or scene-first directions:

~~~text
主体接受主要光线，背景降低曝光与对比，边缘以克制轮廓光或明暗交界分离。高光清晰但不过曝，暗部保留层次，光源方向与投影完全一致。
~~~

## 4. Portrait studio recipes

### Soft sculpting

~~~text
大型柔光箱从左前上方约四十五度照亮脸、眼睛、鼻梁、嘴唇与肩颈；右侧使用负补光雕刻颧骨和下颌；极窄轮廓光分离发丝、肩线与关键材质边缘。
~~~

### High-key minimal

~~~text
冷白色大面积柔光从正面偏上方进入，阴影开放柔和，背景略亮但不吞没白色服装；材质依靠折叠、微弱方向性高光和边缘分离保持体积。
~~~

### Hard-flash cinematic

~~~text
机顶直闪冻结人物与前景材质，主体亮度明显高于环境；环境光压暗一至二档但保持可读，闪光高光清晰、真实、有力度，不形成影楼大平光。
~~~

### Phone-flash snapshot

~~~text
高端智能手机后置镜头直闪，微型传感器成像感，柔和白色正面闪光主要落在人物，背景更暗、低对比、低饱和但可读；禁止长焦压缩、浅景深和强散景。
~~~

## Eye-life guard / 眼神守则 (use when the brief requires a living photoreal gaze)

~~~text
【眼神锁 · photoreal 人脸通用】眼神必须有内在生命：不空洞、不呆滞、不玻璃娃娃眼、不死眼。
虹膜、瞳孔、眼白、上眼睑遮挡与角膜反射保持真实比例；catchlight 的方向、数量、大小与软硬必须服从实际光源，
不得为了“眼神亮”而制造与布光矛盾的固定白点。视线有明确目标或有意的游离状态，焦平面服从镜头意图。
闭目、半睁、侧视、无 catchlight、背光或角色需要空洞目光时，以当前叙事和光源为准，不强加通用表情。
~~~

## Skin texture versus skin reflection / 皮肤反射守则

Texture and reflection are separate controls. 真实皮肤微纹理 governs pores, fine hair, and small tonal variation; it does not govern how the surface reflects light. Every face-bearing shot must also assign a reflection behavior appropriate to its shot scale:

- default when no dewy-skin brief and no sweat evidence: natural semi-matte or restrained satin; T-zone highlight narrow and controlled; cheeks read as soft diffuse reflection;
- 水润唇 / 玻璃唇 / 湿润眼妆 bind only to those features and never spread into a continuous wet shine across forehead, nose, and cheeks;
- sweat or wet shine requires a causal event (heat, exercise, rain, pool) and named zones (hairline, nose tip), never a uniform full-face oil film;
- the high-risk stack — direct flash + hard light + slight overexposure + dewy makeup + facial close-up — requires explicit positive reflection control, not a trailing "no oil" negative.

Chinese execution block:

~~~text
自然半哑光底妆，额头与双颊保持柔和漫反射，T区只保留克制的窄高光，水润质感仅留在唇部；直闪提亮眼神、鼻梁窄线、发丝与服装边缘，不在脸部形成连续油膜。
~~~

Flash obeys shot scale. A series may lock the imaging mechanism (CCD/direct-flash response, contrast, grain), but each shot's flash direction, strength, placement, and highlight width must be redesigned for its own scale and action: close-ups reduce flash strength or shrink the highlight zone, while full-body environmental shots may keep stronger subject separation. If a finished frame reads oily, first reduce flash coverage and overexposure on the face, then patch zoned reflection; adding more "real pores" alone yields porous oily skin.

## 5. Motivated environmental light

- window light: direction and window geometry visible;
- sun: shadow length and sky fill coherent;
- moonlit exterior: reflected sunlight filtered by sky, atmosphere, exposure, adaptation, and local practicals; do not assume it must be weak blue;
- candle/lamp: local warm pool, fast falloff;
- water/glass caustic: hard point source and refractive surface;
- overcast: broad soft sky source, low directional contrast;
- sunset: warm rim plus cool sky fill.

## 6. Atmosphere

Default recipe when atmosphere is a depth/light carrier rather than the subject:

- thin;
- continuous;
- low detail;
- reveals distance or light;
- preserves, reveals, or deliberately conceals the anchor according to the brief.

Chinese block for that default recipe:

~~~text
当薄雾只作为距离与光线载体时：连续、干净、低细节，避免无意形成白雾墙、脏颗粒、烟雾纹理或遮脸效果；若雾、烟或遮蔽本身是主体或叙事机制，则按其材料行为与意图另行设计。
~~~

## 7. Depth of field as hierarchy

Allocate:

~~~text
最清晰：第一视觉锚点。
清楚可读：身份道具、关键材质或第二主体。
逐渐柔化：前景框景、远端结构、次要装饰。
压低细节：背景纹理与空气。
~~~

Phone snapshots may use deeper focus and weaker bokeh. Forced-perspective scenes often benefit from enough depth of field to prove scale, but selective focus may be part of the illusion when the critical size cues remain visible. Macro material shots may deliberately move the face out of first read.

## 8. Edge behavior starting bank

- real face: natural but decisive feature edges;
- glass: bright edge and thickness;
- porcelain: hard curved reflection and fracture edge;
- paper: visible cut/torn edge and shadow;
- smoke: soft volume boundary;
- op-art/moire: razor edges;
- absolute flat graphics: clean zero-thickness edge;
- chromatic aberration: natural lateral CA is usually stronger toward frame edges; longitudinal CA may appear before/behind focus. Intentional creative dispersion may be broader when declared—avoid an unexplained global RGB split.

## 9. Material quick bank

~~~text
皮肤：真实毛孔、细微绒毛、自然油脂高光与柔和次表面反应。
丝绸：方向性高光、真实垂坠、柔软褶皱堆叠与克制边缘反光。
薄纱：半透明叠层、交叠处密度增加、边缘受光。
金属：受控镜面高光、少量边缘亮点，禁止满面噪声。
瓷器：釉面硬反射、曲面高光、边缘厚度、脆性裂纹与真实落影。
纸张：纸纤维、剪裁或撕裂边、轻微翘起、实体投影与印刷网点。
玻璃与树脂：透明深度、折射、边缘高光、内部层次。
水面：宽阔连续反射、克制波纹、正确折射与可能的焦散。
~~~

## 10. Palette discipline

Three to six named colors can be a useful production constraint, not a universal requirement. Define roles and protect identity only from unintended drift; colored bounce and stylized illumination may legitimately affect skin/surfaces.

~~~text
色彩角色为：主场色[ ]、结构辅助色[ ]、锚点色[ ]、强调色[ ]、中性桥接[ ]。人物肤色与身份色在当前光源下保持可信，不被非动机化的全图偏色吞没；允许有来源的环境反射与风格化照明。仅禁止本 brief 已识别的[黄橙/绿色/霓虹/单色]漂移。
~~~

## 11. Attributed practitioner doctrine (2026-08-25 intake)

Recorded from high-volume external practitioners (@nanyuan0412 via vibeshot_club, @VoxcatAI via X Articles) under the 2.4.0 integration precedent: studio heuristics with named sources and stated exception boundaries, not universal constants.

### Series camera-position formula

Series rhythm comes from moving the camera, not swapping backgrounds. Rotate across shots:

~~~text
机位位置 × 相机高度 × 拍摄距离 × 拍摄方向 × 景别 × 前景关系 × 人物占画面比例
~~~

Write each variable as a spatial-relationship sentence, not a label — 「摄影机站在楼梯最上方，向下俯拍，人物只占画面15%，楼梯和栏杆形成纵深」 carries more instruction than 「俯拍」. Corroborates the axis-rotation rule in core/08_ALBUM_ENGINE.md; reach for it when an album reads flat even though scenes differ.

### Hard light-band structural edit

Converting flat light into a hard directional band is specified through six decisions; omit one and the model reverts to uniform soft light:

- 光源: off-frame physical flag cutting unsoftened hard light;
- 形状: narrow diagonal band and its travel direction;
- 落点: named receivers only — one eye, half the nose bridge, cheekbone, lip edge, one hand;
- 边界: sudden cutoff, gradients forbidden;
- 高光: lit planes pushed near white, minor highlight detail loss allowed;
- 阴影: clearly deepened, no fill, darks not recovered.

### Air-breath backlight pairing

Perceived airiness comes from light structure, not resolution words: a strong rear rim outlines hair and contour (骨架) while large soft frontal fill opens the shadows (呼吸); allow the brightest points — petal edges, nose-tip highlight, jewelry — a slight bloom instead of pushing global sharpness. Pair with a restrained palette: a cold quiet background makes warm-white skin read luminous; busy background colors collapse the effect. Heuristic for airy portrait briefs; do not apply when the brief demands flat, noir, or hard-flash systems.

### Skin realism beyond texture

Extends the skin-reflection guard earlier in this file: treat skin as five separated controls — 纹理（毛孔、绒毛、细微凹凸）、高光位置（T区克制皮脂光、脸颊保持哑）、质感基调（半哑光或缎光）、轻微不完美（泛红、小痣、浅纹、不对称）、光线（方向与明暗层次）。A single 真实皮肤 token collapses all five into beauty-filter defaults; name per-zone states instead.

### Subject-eats-light, background-avoids-light (scoped)

A VSC heuristic for separation: light the subject, keep the environment darker, and use a rear/side rim only when the subject would otherwise merge into the ground. Write who is lit, who recedes, and how the edge is separated — not “bright and dark, high-end.”

Do not apply when the reference depends on underexposure, missed focus, or blocked shadows, or when the brief is flat, high-key, or evenly lit documentary. Rim light is not a universal repair. See `library/15_PHOTOGRAPHY_RESHOOT_WORKFLOW.md` for scheme-faithful lighting topology.
