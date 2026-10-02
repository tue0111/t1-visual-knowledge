# ART FUSION & CREATIVE SYNTHESIS
## Hợp — Dịch — Chứng: phối ghép nhiều hệ mỹ thuật mà không hòa bùn, pastiche hay chiếm dụng

> **Vai trò.** File này là sách phương pháp chuyên sâu cho fusion, family birth và creative synthesis. Luật thi hành ngắn nằm ở `T1_TO_9_VISUAL_PROMPT_OS_v2/core/07_FUSION_AND_GROWTH_ENGINE.md`; schema làm việc nằm ở `templates/TEMPLATE_FUSION_BRIEF.md`.
>
> **Luận đề.** Fusion không phải trung bình cộng của hai bề mặt. Nó là một kiến trúc quyền hạn: mỗi nguồn giải một bài toán, các invariant tạo unity, mặc định một tension chính (hoặc nhiều tension có hierarchy/counterpoint) tạo sinh khí, và bridge khiến sự khác biệt thuộc cùng một tác phẩm.

---

# 1. TỪ VỰNG CỐT LÕI

## 1.1 Bốn mức vay mượn

| Mức | Hành động | Giá trị | Rủi ro |
|---|---|---|---|
| Motif quotation | lấy một motif hoặc vật trang trí | nhận diện nhanh | dễ thành costume, cliché hoặc sai context |
| Surface imitation | mô phỏng texture/palette/nét ngoài | mood nhanh | không sống qua subject khác; dễ dính chữ ký nghệ sĩ |
| Formal translation | chuyển quan hệ shape, space, value, rhythm | sâu hơn motif | cần hiểu chức năng và giới hạn nguồn |
| Process/function translation | tái tạo logic chế tác hoặc tác dụng bằng affordance của medium mới | tạo thesis mới | cần nghiên cứu, thử nghiệm và gọi tên trung thực |

Mục tiêu ưu tiên là formal/process/function translation. Motif chỉ được dùng khi quyền, provenance, ý nghĩa và brief cho phép.

## 1.2 Fusion, hybrid, juxtaposition và pastiche

- **Fusion:** các nguồn tạo rule chung hoặc tương tác khiến toàn thể không thể giải thích bằng một nguồn đơn lẻ.
- **Hybrid coexistence:** các miền giữ grammar riêng nhưng cùng một world physics và bridge.
- **Juxtaposition:** đặt cạnh nhau để tạo đối thoại; khác biệt có thể là mục tiêu.
- **Pastiche:** ghép dấu hiệu nhận diện mà không hiểu function/deep grammar.
- **Style-label stacking:** danh sách adjective tranh nhau cùng một dimension; chưa phải design.

## 1.3 Harmony không phải homogenization

~~~text
agreement bed
+ jurisdiction rõ
+ controlled deviation
+ một productive tension
+ bridge có bằng chứng
= coherent synthesis
~~~

Nếu hai nguồn bị xay thành một texture trung bình, novelty và identity đều mất. Nếu không có agreement bed, chúng thành sticker hoặc hai tác phẩm va nhau.

---

# 2. SOURCE GRAMMAR CARD — HIỂU NGUỒN TRƯỚC KHI GHÉP

Không đặt tradition, medium, process, movement, genre, mood, artifact và motif ngang hàng. Mỗi source cần một card:

~~~yaml
source_grammar_card:
  id:
  kind: tradition | medium | process | movement | genre | artifact | artwork

  context:
    community_or_region:
    period:
    original_function:
    original_site_or_support:
    authoritative_source:
    rights_and_provenance:
    sensitivity_flags:
    status: unknown | green | amber | red
    review_state: incomplete | conditional | approved | rejected
    review_basis:
    conditions:

  visual_problem_solved:

  deep_grammar:
    space_and_composition:
    value_structure:
    light_logic:
    shape_and_silhouette:
    line_edge_and_mark:
    color_distribution:
    material_support_and_process:
    rhythm_and_time:
    scale_body_and_gaze:
    symbol_and_semantics:
    simplification_device:

  transferable_mechanisms:
  essential_authorized_motifs:
  restricted_or_non_transferable:
  visible_evidence:
  uncertainties:
  confidence:
~~~

## 2.1 “Visual problem solved” là câu hỏi quan trọng nhất

Ví dụ:

- cloud band có thể giải bài toán chuyển thời gian/không gian trong narrative;
- carved resistance có thể tạo edge cadence và directional rhythm;
- glaze giải bài toán depth màu qua nhiều lớp trong;
- negative space có thể tạo scale, pause hoặc chỗ cho meaning chưa khép;
- calligraphy có thể mang text, transmission, authority và visual rhythm cùng lúc.

Nếu không biết nguồn đang giải vấn đề gì, việc chuyển nó sang medium khác gần như chắc chắn chỉ giữ costume.

## 2.2 Motif diagnostic

Tạm cấm các motif dễ nhận diện nhưng không load-bearing. Hỏi:

- không có motif, spatial/value/mark grammar còn tồn tại không;
- source có còn làm thay đổi cách xây thế giới không;
- người vận hành có mô tả được bằng hành vi thay vì tên không.

Nếu câu trả lời là không, tách hai khả năng: chưa hiểu deep grammar; hoặc motif thật sự mang text, identity, narrative, ritual, heraldic hay iconographic function. Trường hợp sau chỉ giữ motif khi khai báo `essential_authorized_motif` với nguồn, context, permission, giới hạn và honest naming. Reject khi nguồn chỉ còn một motif chưa được hiểu hoặc chưa được phép.

---

# 3. NĂM MODE PHỐI GHÉP

## 3.1 Structural graft

Nguồn A giữ composition/space/hierarchy; nguồn B thay surface, process hoặc local edge behavior. Dùng khi một hệ có cấu trúc mạnh nhưng medium cần đổi.

## 3.2 Surface inoculation

Hệ A gần như nguyên vẹn; B chỉ tạo accent có giới hạn. Tỉ lệ tham khảo 90/10 hoặc 85/15 về **quyền quyết định**, không phải số từ.

## 3.3 Split-domain coexistence

Mỗi ontology giữ 100% grammar trong miền riêng: người photographic, world painterly; vật thể relief, ký hiệu flat. Không dùng global blend ratio. Phải khóa:

- render boundary;
- area/read-order relationship;
- global physics;
- bridge proofs;
- forbidden style bleed.

## 3.4 Process translation

Chuyển thao tác hoặc function của nguồn A sang khả năng riêng của medium B. Không giả vờ output là hiện vật/truyền thống authentic.

## 3.5 Dialectical birth

Hai hệ tạo các emergent rules không có ở cha/mẹ. Đây là mode khó nhất; chỉ được promotion sau baseline, ablation, transfer và stress test.

## 3.6 Ratio regime: controlled dialogue

Đây không phải mode thứ sáu. Nó là một ratio/jurisdiction regime có thể nằm trong structural graft hoặc dialectical birth. Hai nguồn có thể gần 65/35 khi chúng sở hữu các dimension khác nhau. Nếu cùng tranh space, value, edge và material, 65/35 vẫn có thể hòa bùn.

Các con số là starting hypothesis. Calibration quyết định ratio hợp lệ.

---

# 4. JURISDICTION — OWNER MẶC ĐỊNH HOẶC CO-OWNERSHIP CÓ LUẬT

## 4.1 Ma trận quyền tài phán

~~~yaml
jurisdiction:
  - dimension: space_and_composition
    ownership_mode: default_single | explicit_co_owned
    owner:
    co_owners: []
    owner_authority:
    conflict_resolution:
    final_decision_authority:
    support:
    support_may_change:
    invariant:
    forbidden_bleed:
    visible_proof:

  - dimension: value_and_light
    owner:
    owner_authority:
    support:
    support_may_change:
    invariant:
    forbidden_bleed:
    visible_proof:
~~~

Kiểm tra ít nhất các dimension:

1. message/function;
2. hierarchy/read order;
3. space/composition;
4. camera/perspective;
5. value/light;
6. shape/silhouette;
7. line/edge/mark;
8. color distribution;
9. material/support/process;
10. rhythm/motion;
11. identity/body/gaze;
12. ornament/iconography;
13. cultural register;
14. typography/brand nếu có.

## 4.2 Luật owner–support

- Mỗi dimension load-bearing mặc định có một owner; co-ownership chỉ hợp lệ khi authority và conflict resolution được khai báo.
- Support chỉ được thay thuộc tính con đã khai báo.
- `Shared` là quan hệ bridge, không phải cách né chọn owner.
- Một source có thể sở hữu nhiều dimension; không cần ép “mỗi source một trục”.
- Với split-domain, lập jurisdiction theo từng miền rồi thêm global physics contract.
- Global physics — perspective, contact, gravity, light interaction, atmosphere — phải có một authority chung nếu mục tiêu là cùng một thế giới.

Owner không nhất thiết là source A/B. Message thuộc brief; identity có thể thuộc reference; brand thuộc project contract; dialectical birth có thể tạo `emergent_system`. Ghi `owner_authority` và không cho nguồn thấp hơn chiếm dimension đã khóa ở authority cao hơn.

Với split-domain, schema phải biểu diễn từng miền và một global-physics authority:

~~~yaml
domains:
  - domain:
    render_grammar:
    jurisdiction:
    forbidden_bleed:
global_physics:
  authority:
  perspective_and_scale:
  gravity_and_contact:
  light_interaction:
  atmosphere_and_motion:
~~~

## 4.3 Bốn tỉ lệ khác nhau

Không nói “fusion 80/20” nếu chưa rõ đang đo gì:

- **decision ratio:** nguồn nào quyết định nhiều rule hơn;
- **salience ratio:** nguồn nào nổi bật hơn trong cảm nhận;
- **area ratio:** miền nào chiếm nhiều frame hơn;
- **per-axis ratio:** dominance riêng ở space, color, edge, material...

Một minority source có thể chiếm 5% diện tích nhưng 40% salience vì contrast và meaning. Tỉ lệ từ trong prompt không đo được dominance.

---

# 5. INVARIANT, VARIATION VÀ COHERENCE BUDGET

## 5.1 Năm lớp kiểm soát

~~~yaml
fusion_control:
  absolute_invariants:
  relational_invariants:
  bounded_modulation:
  deliberate_open:
  exclusions:
  coupled_axes:
~~~

- **Absolute invariant:** mặt, brand, medium boundary, một shape signature.
- **Relational invariant:** anchor luôn sắc hơn field; accent luôn nhỏ hơn dominant mass; người luôn photographic hơn environment.
- **Bounded modulation:** density, chroma, crop hoặc gesture đổi trong biên.
- **Deliberate open:** micro-gesture, natural accident, incidental life được cố ý nhường cho generator.
- **Exclusion:** style bleed, motif cấm, cultural no-go, collapse.
- **Coupled axes:** light source + cast shadow + material highlight; camera distance + perspective + anatomy.

Relational invariant đặc biệt quan trọng cho album: shot không cần giữ một giá trị cố định, nhưng phải giữ cùng quan hệ.

## 5.2 Coherence và novelty budget

Mỗi frame có ngân sách hữu hạn:

- **coherence budget** dành cho những rule phải được lặp đủ mạnh để người xem tin;
- **novelty budget** dành cho deviation, discovery và surprise.

Nếu mọi dimension đều novel, không còn baseline để đọc. Nếu mọi dimension đều invariant, hình đúng nhưng inert. Chọn 2–4 invariant lớn và 1–2 novelty carriers thay vì làm mọi vùng “đặc biệt”.

---

# 6. PRODUCTIVE TENSION — CĂNG MÀ KHÔNG VỠ

## 6.1 Schema

~~~yaml
productive_tensions:
  - id:
    rank_or_counterpoint_voice:
    pole_A:
    pole_B:
    purpose_for_message:
    agreement_bed:
    disagreement_location:
    first_read:
    delayed_second_read:
    bridge_or_resolution:
    desired_aftertaste:
    collapse_if_too_low: bland_average
    collapse_if_too_high: split_image_or_kitsch
~~~

Các cặp có thể dùng:

- flat/deep;
- precise/gestural;
- sacred/domestic;
- polished/raw;
- historical/contemporary;
- still/kinetic;
- organic/geometric;
- monumental/intimate;
- permanent/ephemeral;
- observed/symbolic.

Một tension chính thường đủ. Có thể giữ nhiều tension khi hierarchy/counterpoint được khai báo và mỗi tension có chức năng khái niệm riêng; bỏ tension lặp hoặc chỉ tăng nhiễu.

## 6.2 Productive và destructive conflict

| Productive | Destructive |
|---|---|
| khác mark nhưng chung perspective/light/contact | khác perspective, scale và contact nên thành sticker |
| flat symbol tồn tại trên một plane zero-thickness rõ | symbol vừa flat vừa có volume/shadow ngẫu nhiên |
| hard graphic form đối thoại với soft atmosphere | mọi edge cùng tranh anchor |
| palette restraint + một accent bất tuân | high chroma khắp nơi nên không còn accent |
| historical process được dịch sang chức năng mới | motif lịch sử bị bê như costume |

---

# 7. BRIDGE — LÝ DO HAI HỆ THUỘC CÙNG MỘT TÁC PHẨM

## 7.1 Hai chiều phân loại

**Type:**

- `shared` — có invariant chung;
- `resonant` — minor behavior của một nguồn vần với major behavior của nguồn kia;
- `engineered` — một carrier/cause thứ ba tạo quan hệ.

**Class:**

- `structural` — geometry, void, grid, symmetry, rhythm;
- `optical` — value map, edge hierarchy, temperature, depth;
- `spatial` — perspective, scale, body–world relation;
- `material` — seam, grain, weave, fracture, shared support;
- `kinetic` — gesture, wind, flow vector, repetition;
- `semantic` — function hoặc metaphor;
- `causal` — hiện tượng khiến hai miền thật sự tương tác.

## 7.2 Bridge card

~~~yaml
bridge:
  type: shared | resonant | engineered
  class: structural | optical | spatial | material | kinetic | semantic | causal
  shared_invariant:
  carrier:
  crossing_zone:
  visible_proofs:
  false_bridge_to_avoid:
~~~

Semantic bridge một mình thường yếu. Nó cần xuất hiện qua structure, material hoặc action. Một third object chỉ là catalyst; nếu nó đòi một grammar đầy đủ khác, fusion đã thành ba hệ tranh quyền.

## 7.3 Boundary, gradient, nesting và counterpoint

Không phải fusion nào cũng cần dissolve:

- **Boundary:** hai miền khác rõ nhưng có contact/occlusion/light chung.
- **Gradient:** một process chuyển dần có các trạng thái trung gian được chứng minh.
- **Nesting:** một grammar sống bên trong container của grammar khác.
- **Counterpoint:** hai grammar luân phiên như hai giọng, giữ nhịp chung.
- **Common constraint:** cùng bị chi phối bởi grid, material limit hoặc narrative rule.

Chọn một topology. Dùng boundary, gradient và nesting cùng lúc mà không phân quyền thường tạo ambiguity xấu.

---

# 8. DỊCH THAY VÌ MÔ PHỎNG

## 8.1 Translation ladder

~~~text
observe visible evidence
→ identify original function
→ extract mechanism
→ identify constraints and context
→ rebuild with the new medium's affordances
→ test equivalent perceptual/semantic effect
→ name the result honestly
~~~

Ví dụ:

- `留白` có thể dịch thành breathing field, fog, exposure, silence hoặc scale contrast; không chỉ là nền giấy trắng.
- Logic khắc gỗ có thể dịch thành edge resistance, cut-direction rhythm và controlled flat planes trong 3D; không cần sao chép wave/cartouche.
- Cấu trúc dệt có thể thành alternating load path hoặc interlaced spatial sequence; không lấy pattern nghi lễ làm wallpaper.
- Glaze có thể thành translucent accumulation trong light/material system; không chỉ thêm chữ “oil painting”.

## 8.2 Anti-imitation test

- Bỏ tên nguồn, instruction còn thi hành được không?
- Bỏ motif không load-bearing, deep grammar còn sống không? Nếu motif thiết yếu, function/context/permission/limits có được chứng minh không?
- Medium mới có dùng khả năng riêng không?
- Có thesis mới hay chỉ mặc costume của nguồn?
- Có sao chép signature composition/motif của một tác phẩm hoặc living artist không?
- Cách gọi có tuyên bố sai “authentic tradition” cho một fusion đương đại không?

Nếu bỏ tên nguồn mà instruction chết, hoặc nguồn chỉ còn một motif không hiểu/không được phép, quay lại source grammar card. Motif thiết yếu đã được ủy quyền không bị loại chỉ vì không thể blackout.

---

# 9. CULTURAL/CONTEXT GATE

Policy đầy đủ thuộc `Visual_Resource_Library/CURATION_POLICY.md`; fusion brief chỉ ghi decision gate:

~~~yaml
context_gate:
  source_id:
  source_named_precisely:
  community_region_period:
  original_function:
  authoritative_source:
  status: unknown | green | amber | red
  sensitivity_flags:
  allowed_extraction:
  essential_authorized_motifs:
  forbidden_extraction:
  attribution_language:
  authenticity_claim:
  review_state: incomplete | conditional | approved | rejected
  review_basis:
  reviewed_by:
  conditions:
  decision_date:
  review_required:
~~~

Gate áp dụng riêng cho từng source. Mặc định `unknown/incomplete`; thiếu authority, rights/provenance, sensitivity decision hoặc review basis thì dừng. Amber chỉ đi tiếp sau khi thỏa điều kiện; red/rejected dừng extraction.

- **Green:** quan hệ formal/process đủ phổ quát, nguồn/quyền rõ.
- **Amber:** living heritage, ceremonial dress, recognizable community motif, colonial/looted provenance; cần contextual review.
- **Red:** sacred/restricted, ancestral/funerary, human remains hoặc quyền không rõ; không tự động chuyển thành motif/family.

Không dùng “Asian”, “African”, “tribal”, “mystic” như style phẳng. Gọi đúng community/region, period, function và mức độ phiên dịch khi có thể.

---

# 10. PHƯƠNG PHÁP TẠO Ý TƯỞNG

## 10.1 Safe / stretch / wild

Sinh ít nhất ba khoảng cách khỏi baseline:

- **Safe:** một mechanism mới, phần còn lại ổn định.
- **Stretch:** hai dimension đổi nhưng jurisdiction rõ.
- **Wild:** đảo ontology hoặc process; vẫn phải trả lời brief.

Không chọn wild chỉ vì lạ, không chọn safe chỉ vì dễ render.

## 10.2 Grammar swap

Giữ message và subject, thay đúng spatial grammar, process hoặc edge system. So sánh effect thay vì vẻ ngoài.

## 10.3 Bridge-first

Chọn một bridge mạnh trước — shared void, interlacing, refraction, wind, scale — rồi tìm hai nguồn có thể thực sự dùng bridge đó.

## 10.4 Tension-first

Chọn một đối cực có ý nghĩa với message, viết agreement bed, sau đó chọn source theo vai trò. Đây thường sâu hơn chọn hai style yêu thích rồi tìm cách dán.

## 10.5 Constraint braid

A đóng góp structural constraint; B đóng góp material/process constraint; catalyst đóng góp bridge. Không thêm nguồn thứ tư nếu chưa chứng minh thiếu.

## 10.6 Morphological matrix

~~~yaml
idea_seed:
  message:
  spatial_engine:
  primary_contrast:
  mark_or_process:
  material_carrier:
  productive_tensions:
  bridge:
  simplification_device:
  cultural_boundary:
~~~

Không random một ô ở mỗi cột. Mọi lựa chọn phải giải cùng một thesis.

## 10.7 Creative operators

- omit;
- invert hierarchy;
- magnify/minify scale;
- compress/expand time;
- substitute material;
- translate medium;
- change viewpoint;
- nest one world inside another;
- reveal cause after effect;
- replace motif with process;
- remove first association/cliché;
- ablate the bridge or minority source.

Mỗi operator tạo hypothesis, không tự tạo concept tốt.

---

# 11. HỢP — DỊCH — CHỨNG WORKFLOW

## G0 — Context

Brief, authority, rights, provenance, sensitivity. Artifact: `context_gate`.

## G1 — Thesis

Message, viewer sequence, one mechanism sentence, success/failure criteria. Artifact: `fusion_thesis`.

## G2 — Decompose

Source grammar cards, motif blackout, uncertainties. Artifact: `source_cards`.

## G3 — Architect

Fusion mode, jurisdiction, ratio semantics, invariants/variables/coupled axes. Artifact: `fusion_architecture`.

## G4 — Harmonize

Agreement bed, productive tension, boundary/topology, bridge and false bridge. Artifact: `coherence_contract`.

## G5 — Study

Theo thứ tự rẻ đến đắt:

1. silhouette/figure-ground;
2. value mass;
3. space/edge;
4. light/material;
5. color in context;
6. full prompt.

## G6 — Compile

Chọn dominant family và mặc định tối đa một support engine. Nhiều support chỉ hợp lệ khi từng source có jurisdiction cần thiết, không trùng và có biện minh cấu trúc. Trong T1:

- `母版锁`: thesis, invariants, jurisdiction quan trọng, boundary/bridge, light/material DNA, cultural no-go;
- `分镜`: bounded variation, camera, gesture, tension và bridge proof cụ thể;
- `通用负面提示词`: style bleed, collapse, false bridge và motif cấm.

## G7 — Calibrate

Close/anchor, wide/environment, hard mechanism, boundary stress. Lặp sample; không phong family từ một lucky image.

## G8 — Critique

Observation → causal hypothesis → minimal controlled test → acceptance criterion. Ghi preserve/change/uncertain.

## G9 — Promote

Chỉ nâng lesson đúng scope và bằng chứng. Nếu chưa thử nhiều generator, ghi generator/version/date.

---

# 12. BỘ THÍ NGHIỆM

Không phải task nào cũng chạy hết. Trước mỗi test, preregister `hypothesis / predicted_result / falsifier / fixed_variables / changed_causal_bundle / planned_samples / acceptance_rule`; sau test giữ `all_result_ids / passed / failed / confounders / conclusion`. Không cherry-pick chỉ output thắng. Family birth/fusion nghiêm túc nên có:

1. Parent A baseline.
2. Parent B baseline.
3. Naive label blend làm control.
4. Jurisdictional fusion.
5. Bridge ablation.
6. Ratio sweep theo decision/salience/area.
7. Jurisdiction swap ở một dimension.
8. Motif diagnostic: blackout motif không load-bearing; audit context/permission nếu motif thiết yếu.
9. Cross-subject hoặc cross-environment transfer.
10. Aspect-ratio transfer.
11. Close/wide/action/low-light stress.
12. Preserve-one/change-one edit.
13. Repeated sampling để tách direction khỏi may mắn.

Mỗi retry kiểm tra **một causal hypothesis**. Có thể đổi nhiều field nếu chúng là coupled axes; đừng giả vờ light source, cast shadow và specular highlight là ba thí nghiệm độc lập.

---

# 13. CRITIQUE RUBRIC VÀ KILL GATES

## 13.1 Rubric định tính

Mỗi mục có thể ghi `absent / named / visible / controlled`, không cộng điểm máy móc trước calibration:

1. Message và time horizon.
2. Anchor/hierarchy.
3. Deep grammar của từng source.
4. Jurisdiction rõ.
5. Dominance không hòa bùn.
6. Nguồn còn phân biệt nhưng thuộc cùng tác phẩm.
7. Authored relationship có visible/formal proof; physical bridge có proof khi shared-world integration là mục tiêu.
8. Tension phục vụ meaning.
9. Space/light/material/edge đồng thuận.
10. Translation tạo thesis mới.
11. Invariant/variation sống qua shot khác.
12. Cultural/context integrity.
13. Có thể debug và tái lập.

## 13.2 Kill gates

Dừng hoặc reframe khi:

- cultural red flag chưa giải quyết;
- source unknown/incomplete hoặc thiếu review basis;
- dimension load-bearing không có owner;
- hai owner tranh cùng dimension mà không có conflict resolution, hoặc owner sai authority;
- split-domain thiếu boundary/authored relationship; nếu tích hợp shared world thì thiếu global physics hoặc physical bridge;
- fusion chỉ là style-label stacking;
- message/hierarchy thất bại ở context sử dụng;
- emergent rule chỉ nhắc lại motif/palette vay mượn;
- essential motif thiếu function/context/permission/honest naming;
- evidence thiếu attempts, failures, denominator, falsifier hoặc acceptance rule;
- output chỉ sống ở một lucky seed;
- source phụ có thể bỏ đi mà effect không đổi.

---

# 14. PROMOTION LADDER

| Mức | Bằng chứng tối thiểu |
|---|---|
| Task note | một output hấp dẫn; chưa có claim ổn định |
| Direction candidate | lặp được nhiều sample trong cùng cấu trúc |
| Project recipe | ít nhất ba cấu trúc khác nhau, không critical collapse |
| Family candidate | ba cấu trúc × tối thiểu hai sample; hai subject/environment; một stress; một ablation; một failure→repair |
| Registered family | charter đầy đủ; signature, collapse, trigger, guard đã chứng minh |
| Universal candidate | sống qua nhiều family/medium; có ablation; không phụ thuộc nguồn văn hóa cụ thể |
| Universal core | tái lập, có biên ngoại lệ và không còn giải thích cạnh tranh hợp lý |

Các ngưỡng trên là governance của project, không phải định luật về sáng tạo.

---

# 15. NGUỒN VÀ BÀI HỌC LỊCH SỬ

- [Design Council — Double Diamond](https://www.designcouncil.org.uk/resources/framework-for-innovation/): divergence/convergence và thử ở quy mô nhỏ.
- [Josef & Anni Albers Foundation — Interaction of Color](https://www.albersfoundation.org/alberses/teaching/interaction-of-color): quan sát và tương tác màu trước công thức cố định.
- [The Met — Japonisme](https://www.metmuseum.org/ja/essays/japonisme): một ví dụ lịch sử về tiếp thu format, asymmetry, viewpoint và emptied space thay vì chỉ dựng props ngoại lai.
- [The Met — Landscape Painting in Chinese Art](https://www.metmuseum.org/de/essays/landscape-painting-in-chinese-art): landscape như biểu hiện cultivated mind, không chỉ scenery motif.
- [The Met — Geometric Patterns in Islamic Art](https://www.metmuseum.org/fr/essays/geometric-patterns-in-islamic-art) và [Calligraphy in Islamic Art](https://www.metmuseum.org/fr/essays/calligraphy-in-islamic-art): pattern, text, order và transmission phải giữ chức năng/context.
- [Smithsonian — Shared Stewardship and Ethical Archiving](https://folklife.si.edu/news-and-events/shared-stewardship-new-guidelines-for-ethical-archiving): community authority và context trong tài liệu văn hóa.

Framework Hợp — Dịch — Chứng là tổng hợp vận hành cho project. Mọi ratio, mode và promotion threshold cần render evidence; không được trình bày như kết quả trực tiếp của các nguồn trên.
