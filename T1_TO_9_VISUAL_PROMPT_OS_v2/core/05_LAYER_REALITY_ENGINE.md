# 05 LAYER AND REALITY ENGINE

This engine defines how multiple ontological or rendering layers coexist.

## 1. Layer vocabulary

### Three-dimensional physical layer

- real subject or object;
- full volume;
- receives light;
- casts shadow;
- participates in perspective, occlusion, and depth of field.

### Two-point-five-dimensional material layer

- cut paper, relief, resin, porcelain arc, glass membrane, fabric sculpture, printed fragment;
- has finite thickness;
- receives light;
- casts shadow;
- can lift, bend, overlap, refract, or bridge between layers.

### Absolute two-dimensional plane

- pure graphic circle, band, line, printed plane, symbolic field;
- zero thickness;
- no cast shadow;
- not modeled by scene light;
- remains geometrically flat and edge-clean.

## 2. Layer contract

For each layer answer:

~~~yaml
ontology:
thickness:
surface_behavior:
shadow_behavior:
focus_level:
perspective_relationship:
transition_boundary:
forbidden_drift:
~~~

If these answers are missing, the model defaults to a visually convenient but structurally wrong blend.

## 3. Shared-world requirements

Three-dimensional and two-point-five-dimensional layers usually share:

- camera perspective;
- scale;
- key light;
- cast-shadow direction;
- atmospheric depth;
- depth-of-field falloff.

Absolute two-dimensional layers share composition and visual rhythm but remain physically flat.

## 4. Transition grammar

A cross-layer transition should be visible and directional.

Formula:

~~~text
source form → readable transition zone → destination form
~~~

Examples:

- silk embroidery → gold repair seam on porcelain → flat gold line;
- real skirt hem → visible cut edge → printed paper train;
- animal fin → translucent organza membrane → brush trace;
- photographic motion blur → directional paint stroke;
- physical shadow → flat symbolic line inside the shadow zone.

Do not blur the transition to hide uncertainty. Show the edge, seam, thinning, fracture, refraction, or material behavior that explains it.

## 5. Cross-medium boundary and authored relationship

Law 14 requires a render-boundary contract and a relationship contract.

### Render boundary

Example:

~~~text
人物皮肤、五官、头发与白裙保持真人摄影；人物之外的天空、树木、草地、建筑与昆虫保持手绘动画材质。人物不得动画化，环境不得摄影写实化。
~~~

### Physical bridge when shared-world integration is intended

Example:

~~~text
人物与手绘世界共享同一摄影机透视、太阳方向、地面尺度、接触阴影、前后遮挡、空气纵深和风向。鞋底压住草叶，草叶自然遮挡脚踝，环境反射光进入白裙暗部。
~~~

Boundary preserves difference. A physical bridge creates shared-world belonging. Deliberate collage, symbolic overlay, unresolved collision, or counterpoint may instead use a stated formal/narrative relationship without pretending the domains share physical causality.

## 6. Pictorial reality rules

For real space plus material collage:

- real layer proves architecture and person;
- material cutout has visible edge, thickness, lift, and shadow;
- flat graphic plane has no thickness or shadow;
- the human may be small if space is first read;
- absurd juxtaposition must remain deliberate.

GPT-style semantic correction often removes absurdity. If this happens, strengthen:

~~~text
这是一件刻意的纸片拼贴艺术。剪贴物不是墙上壁画或场景中的真实物体；必须保留明显剪裁边、纸张厚度、拼贴接缝与统一方向的实体投影。绝对平面图形保持零厚度、零投影。
~~~

## 7. Constructed-reality modes

| Mode | Anchor | Bridge | Flat layer |
|---|---|---|---|
| Couture entity | real face/body | entity-material sculpture | halo/disc/line |
| Pictorial reality | real person and architecture | printed/cut material | graphic plane |
| Resin diorama | real face | resin, acetate, glass, bubbles | dark paper field |
| Porcelain gold seam | real model/garment | porcelain crescent | incomplete cobalt circle |
| Live-action painted world | real human | shared physical world, not a 2.5D object | optional graphic only |
| Monumental relief | original 2D composition | sculptural volume | retained line/ink plane |

## 8. Integration proofs

A mixed image should show at least four:

- contact shadow;
- mutual occlusion;
- shared perspective;
- shared scale;
- shared light direction;
- environment bounce light;
- reflection;
- atmosphere crossing boundaries;
- common wind or motion;
- transition seam.

## 9. Failure diagnosis

## U05 interface

Preservation levels for layers and boundaries are declared in the control contract. Use `PIXEL_EXACT` only with a machine-tested region; otherwise use `STRUCTURAL`, `SEMANTIC`, or `UNTESTED` honestly.

| Symptom | Trigger | Repair |
|---|---|---|
| Sticker collage | no thickness/shadow | add cut edge, lift, thickness, cast shadow |
| All layers become illustration | painterly style bleeds inward | hard-lock real anchor; forbid paint on face |
| All layers become photo | stylized/material layer underdefined | lock stylized surface behavior and boundary |
| Unintended green-screen composite in an integrated world | boundary exists but bridge missing | add contact, occlusion, shadow, bounce, atmosphere |
| Deliberate non-integration becomes accidental-looking | relationship is unstated | define the collage, symbolic, collision, or counterpoint logic and preserve its boundary |
| 2D shape becomes object | physical language leaks into flat plane | zero thickness, zero shadow, no scene-light response |
| Transition becomes mush | source/destination listed without bridge | specify one visible transition zone |
| Too many ontologies | all media active at once | reduce to two or three active material families |


## First-read ownership (Clean Impossibility override)

Face-first / person-as-clearest-3D-anchor defaults are portrait defaults, not universal. When the brief declares `first_read_owner: mechanism | world`, guards and negatives must follow that owner: the sharpest/highest-contrast evidence region may be a cutout interior, glass content, paper burn edge, or prop action — not the face. Do not silently reassert face-first against an authored mechanism-first brief. See `Knowledge_Mindset/CLEAN_IMPOSSIBILITY_AND_PERCEPTUAL_DESIGN.md`.
