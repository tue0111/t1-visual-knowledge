# 10 NEGATIVE ENGINE

Negative prompts are targeted drift controls, not a wall of anxiety.

## 1. Three tiers

### Tier 1 — always relevant when applicable

- wrong format or multi-image output;
- anatomy errors;
- unreadable or unintended text;
- hierarchy failure;
- duplicate subjects;
- broken reflection/shadow;
- artifact texture;
- safety violations.

### Tier 2 — photoreal defaults

Use only when the intended anchor is photoreal:

- animated or illustrated face;
- plastic/wax skin;
- over-retouch;
- game-render body;
- false HDR;
- global sharpening;
- impossible lens distortion.

Drop medium-style negatives when painterly, animated, comic, or graphic rendering is intentional.

### Tier 3 — family and shot specific

Examples:

- pet/cartoon drift for couture entity;
- mural/sticker drift for pictorial reality;
- DSLR drift for phone snapshot;
- green-screen drift for live-action painted world;
- attractor pose for album;
- one-shot mechanism failure.

## 2. Build a negative from risk

Ask:

1. What is the nearest wrong family?
2. What identity drift is likely?
3. What material collapse is likely?
4. What camera/anatomy risk exists?
5. What background takeover risk exists?
6. What medium-boundary bleed exists?
7. What format/text conflict exists?

Use only relevant categories.

## 3. Positive-negative consistency

Never ban what the positive prompt requires.

Common contradictions:

- asking painterly dissolve while banning illustration;
- asking stylized environment while banning animation;
- asking phone snapshot while demanding 85-millimeter compression;
- asking absolute flat graphics while banning flatness;
- requiring T1 to 9 while banning all text without exception.

## 4. Logo exception

Canonical ending:

~~~text
除右下角指定的“T1 to 9”品牌角标外，禁止任何其他文字、标志、签名和水印；禁止角标拼写错误、大小写错误、空格错误、缺字、多字、重复或乱码。
~~~

## 5. Shared negative banks

### Universal format and anatomy

~~~text
拼图，九宫格，多格排版，分割画面，边框，多张备选，重复人物，多余肢体，多余手指，畸形手脚，错误关节，扭曲五官，错误比例，错误倒影，错误投影，背景抢主体，纹理碎渣，棋盘噪点，脏颗粒，厚雾墙。
~~~

### Photoreal human

~~~text
动漫脸，插画脸，三维角色脸，玩偶脸，幼态脸，网红脸，塑料皮肤，蜡像皮肤，过度磨皮，空洞眼神，发光瞳孔，脸部透视变形。
~~~

### Mixed medium

~~~text
风格边界消失，人物与环境融成同一画风，人物像贴纸，绿幕合成感，抠图白边，光线不一致，透视不一致，地面尺度错误，没有接触阴影，前后遮挡错误。
~~~

### Pictorial collage

~~~text
剪贴变成墙上壁画，纸边消失，纸张厚度消失，投影消失，拼贴接缝消失，所有碎片无缝融合成连续插画，绝对平面图形长出厚度或投影。
~~~

### Couture entity

~~~text
普通宠物，道具动物，卡通生物，怪物化，实体遮脸，结构断裂，材质流随机装饰，道具堆叠，花墙，纹样像贴纸，普通戏服，廉价角色扮演。
~~~

### Phone snapshot

~~~text
单反棚拍，长焦压缩，浅景深，强散景，专业柔光箱，电影轮廓光，全室均匀照亮，背景过亮，商业画报式超锐。
~~~

### Optical illusion

~~~text
错觉只是装饰，效果全画面均匀套用，边缘被柔化，没有厚度，没有投影，随机模糊冒充变形，普通光斑冒充焦散，错误反射，隐藏图形过于明显。
~~~

### Album

~~~text
所有分镜重复同一姿态、同一脸部角度、同一镜头高度、同一人物比例、同一手势、同一视线与同一光位；只更换背景而不改变身体、镜头与情绪状态。
~~~

## 6. Per-shot anti-attractor

Use a one-line blocker inside the shot when needed:

~~~text
强制[目标状态]，不得回到[默认姿态、视线、道具与构图]。
~~~

## 7. Length rule

## U05 interface

Targeted negatives are linked to the controlled axis and its falsifier. They may block a signature collapse, but may not contradict the preservation contract or quietly introduce an additional creative objective.

If a negative becomes longer than the positive mechanism, prune it. Keep:

- nearest wrong family;
- signature collapse;
- anatomy risk;
- text/logo exception.
