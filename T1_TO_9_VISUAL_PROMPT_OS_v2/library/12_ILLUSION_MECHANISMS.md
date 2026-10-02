# 12 ILLUSION MECHANISM LIBRARY

An illusion must alter perception, not merely look surreal.

Deep-illusion note: this file keeps operating ratios only. Full technical constants (moiré offset 1–5°, caustics IOR water 1.33 / glass 1.52, droste k≈0.3, per-card failure triggers) live in the archive: Project_Source_Knowledge_Pack/illusion_grammar_module_v1.md — open it for serious illusion work.

Global test:

~~~text
观者的眼睛是否被迫停留、翻转、重读或无法立即分类？如果只是平静欣赏漂亮效果，机制尚未成立。
~~~

Use one principal illusion per shot.

## 1. Anamorphosis — 变形透视

- Ratio: 70-85% believable space, 15-30% resolution zone.
- Proof: distorted form resolves only from one viewpoint or reflection.
- Failure: random stretch readable from every angle.

## 2. Moire — 莫尔干涉

- Ratio: vibrating field balanced by one calm anchor.
- Proof: two regular sharp grids offset about 1-5 degrees.
- Failure: soft edges or hand-drawn waves.

## 3. Op-art vibration — 视网膜震颤

- Ratio: pattern may dominate peripheral field; stable center anchor.
- Proof: high-contrast, repeated, razor-edged geometry.
- Failure: low contrast or anti-aliased blur.

## 4. Caustics — 焦散

- Ratio: light net against larger shadow/matte field.
- Proof: hard point source through uneven water or translucent glass-like form.
- Failure: ordinary soft spots from a broad light.

## 5. Chromatic dispersion — 边缘色差

- Ratio: center remains clean; dispersion increases toward frame edge.
- Proof: red/blue separation only on high-contrast peripheral edges.
- Failure: uniform global filter.

## 6. Double exposure — 双重曝光

- Ratio: about 60% face/body structure and 40% overlay.
- Proof: overlay lives mainly in shadow zones; highlights remain clean.
- Failure: mid-gray soup over the entire face.

## 7. Droste recursion — 递归画中画

- Proof: three or more nested levels with consistent scale and perspective.
- Failure: one shallow repeated frame or abrupt dead end.

## 8. Impossible geometry — 不可能空间

- Proof: each local section is plausible, global assembly contradicts itself.
- Failure: random fantasy architecture with no locally coherent depth cues.

## 9. Pareidolia and bistable figure — 拟像与双稳态

- Proof: two readings emerge naturally without bending real structures.
- Failure: hidden image too obvious or too weak to discover.

## 10. Forced perspective — 强制透视

- Proof: monocular alignment, deep focus, coherent ground and shadow.
- Failure: casual scale joke or mismatched blur.

## 11. Trompe-l'oeil — 错视画

- Ratio: 80-90% coherent surface, 10-20% plane-breaking contradiction.
- Proof: exact edge, occlusion, and shadow logic.
- Failure: impressive realism without perceptual trap.

## 12. Mirror fragmentation — 碎镜错视

- Ratio: fragmented field with at least one intact eye/feature anchor.
- Proof: real glass thickness, edge highlight, angle-specific reflection, cast shadow.
- Failure: flat digital shards.

## 13. Shadow illusion — 投影错觉

- Proof: one hard source, real object, meaningful sharp shadow on a receiving plane.
- Failure: multiple diffuse lights or a second fake person.

## 14. Glitch/datamosh — 像素流

- Ratio: roughly 70% clean, 30% corruption.
- Proof: smear follows motion vectors; eyes/face remain intact.
- Failure: canned horizontal bars over the whole frame.

## 15. Peripheral drift — 边缘漂移

- Proof: asymmetric luminance sequence repeated in the periphery.
- Failure: blurred transitions and insufficient contrast.

## 16. Reverse perspective — 逆透视

- Proof: physical panels or relief geometry that expands toward distance while local surfaces remain coherent.
- Failure: ordinary flat drawing with no spatial evidence.

## Selection table

| Desired experience | Mechanism |
|---|---|
| hidden resolution | anamorphosis |
| vibrating surface | moire or op-art |
| liquid/light inference | caustics |
| dreamlike lens instability | edge dispersion |
| memory/inner landscape | double exposure |
| infinite identity loop | Droste |
| unresolvable architecture | impossible geometry |
| double-take hidden form | pareidolia |
| scale contradiction | forced perspective |
| plane deception | trompe-l'oeil |
| fragmented identity | mirror fragmentation |
| object versus self | shadow |
| digital decay | glitch |
| false peripheral motion | peripheral drift |

## Double exposure — 双重曝光 (scoped)

One stable primary figure (pose, wardrobe, face, light). Hide the second exposure in one primary region plus at most one helper (hair darks, garment, fog/rim, pupil/shadow, defocused prop edge). Do not stack a city, moon, flowers, fire, birds, machines, and text at once. The second layer must not destroy silhouette or facial identity. This is a scoped illusion preset, not a default for every portrait.

## Prompt mechanism schema

~~~yaml
mechanism:
anchor:
base_break_ratio:
privileged_view_or_source:
edge_rule:
thickness_rule:
shadow_rule:
focus_rule:
eye_path:
failure_blocker:
~~~

## Universal illusion negative

~~~text
错觉沦为装饰，效果全画面均匀套用，机制没有光学证据，边缘被柔化，没有厚度，没有投影，随机模糊冒充变形，普通光斑冒充焦散，错误反射，所有元素位于同一焦平面。
~~~


## Clean Impossibility — operating cards (v0.1)

Formation detail: `Knowledge_Mindset/CLEAN_IMPOSSIBILITY_AND_PERCEPTUAL_DESIGN.md`. These cards are an idea library, not new registered families. Prefer one principal relation per shot. Clean = information hierarchy, not high-key gloss.

| Card | Trigger | Owner | Relation | Visible proof | Collapse | Repair |
|---|---|---|---|---|---|---|
| Negative-space world | empty body/prop becomes a place | mechanism or world | void reads as doorway/room | clear rim + structured interior scale | many decorative portals | one doorway; optional one boundary leak |
| Cross-boundary agency | figure inside a picture acts outside | mechanism | source → crossing → destination | occlusion/contact at the rim | floating overlay / blur hides crossing | lock rim + contact; keep action readable |
| Representation reversal | image/shadow/map controls the original | mechanism | representation leads, original follows | paired poses/objects with one intentional mismatch | two unrelated poses | one mismatch only |
| Local gravity / impossible topology | regions locally ok, globally contradict | world | joined paths with conflicting up | footings and load paths readable per region | random fantasy architecture called “Escher” | prove local footing first |
| Optical sovereignty | glass/lens content clearer than outer world | mechanism | carrier owns sharper world | visible rim; locked sharp owner | swirl filter over whole frame | restore carrier + quiet field |
| Dimensional translation | flat ↔ volume mid-action | mechanism | state change at one locus | before/after states intact beside transition | whole-body morph soup | one transition zone |
| Causal / time displacement | effect before cause | mechanism | ordered pair of states | continuous path of the premature effect | explosion clutter / caption dependence | silhouette + path, less FX |
| Recursive scale / return loop | gaze enters and returns to origin | world or mechanism | identifiable repeating cue | one readable loop rule | too many tiny scenes | one loop |

### Prompt compile hint (Clean Impossibility)

~~~text
main event → carrier → relation/boundary → material roles → camera → light/focus → targeted guards
~~~

Declare `first_read_owner: person | mechanism | world`. Do not let face-first defaults silently kill mechanism-first briefs. Negatives must not forbid the intentional impossibility.
