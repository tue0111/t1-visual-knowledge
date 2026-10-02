# FORMATION ROUTER
## Nạp đúng tri thức cho đúng bài toán

`Knowledge_Mindset/` là lớp đào tạo tư duy, không phải nguồn delivery contract. Nếu formation knowledge mâu thuẫn với yêu cầu hiện tại, `PROJECT_PROFILE`, core hoặc matching family, nguồn có thẩm quyền cao hơn thắng.

## Load map

| Nhu cầu | File chính | Vai trò |
|---|---|---|
| Nền mỹ thuật, perception, form, composition, color, medium, cultural reading | `FINE_ARTS_PERCEPTION_AND_FORM_KNOWLEDGE_BASE.md` | nền chuyên sâu; phân biệt evidence/heuristic/context |
| Phối ghép, family birth, source grammar, jurisdiction, tension, translation | `ART_FUSION_AND_CREATIVE_SYNTHESIS.md` | phương pháp Hợp — Dịch — Chứng |
| Brief, ideation, study, art direction, critique, experiment và learning | `ART_DIRECTION_WORKFLOW_AND_CRITIQUE_OS.md` | workflow end-to-end |
| Phán đoán chất lượng, taste, connoisseurship, chuẩn master, competent mediocrity | `CONNOISSEURSHIP_AND_AESTHETIC_JUDGMENT.md` | tầng L3–L5; không ghi đè brief/message |
| Primer thiết kế và nhiếp ảnh | `VISUAL_DESIGN_KNOWLEDGE_BASE.md` | vocabulary nhanh; các recipe là heuristic |
| Hệ prompt, world-building và master-file lịch sử | `ART_PROMPTING_KNOWLEDGE_BASE.md` | compatibility/case-derived prompting knowledge |
| Rule routing, visual learning và prompt compression nghiên cứu 2026-08 | `PROMPT_SYSTEMS_AND_VISUAL_LEARNING_RESEARCH_2026-08.md` | research note; không tự động là canonical |
| Bản đồ chưng cất tri thức thô & hàng đợi thăng cấp family | `KNOWLEDGE_DISTILLATION_MAP_2026-08.md` | trạng thái bằng chứng; quyết định thăng cấp vẫn theo core/07 |
| Ngữ pháp môi trường ghi hình: film stock, process, lens character, CCD/phone | `PHOTOGRAPHIC_MEDIA_AND_IMAGING_PROCESSES_KB.md` | khóa medium có cơ chế; recipe là heuristic khởi điểm |
| Văn hóa thẩm mỹ & vật chất Trung Hoa: màu, vải, trang phục, kiến trúc, hoa văn | `CHINESE_AESTHETICS_AND_MATERIAL_CULTURE_KB.md` | nền văn hóa cho family xianxia/guofeng; giữ ranh giới tôn trọng |
| Family Y/style-bible case knowledge | `family_y_STYLE_BIBLE_knowledge.md` | casebook; không phải universal law |
| Cinematic still: staging, station, moment, light, space, attention, DNA rebuild | `CINEMATIC_VISUAL_STORYTELLING_KB.md` | on-demand; operational via `library/20`; không phải family |
| Clean Impossibility / phi thực tế có cấu trúc / first-read owner / crossing proofs | `CLEAN_IMPOSSIBILITY_AND_PERCEPTUAL_DESIGN.md` | formation; không phải family đã đăng ký; current request thắng |
| Reverse-match User Reference / đoán prompt / REPAIR toward ref (EggOS slim) | `REVERSE_IMAGE_PROMPT_LOOP_SLIM.md` (+ `VOXCAT_CREATIVE_CHAIN.md`) | lab process; REVERSE_LOOP-only; không thay normal Final path |
| So sánh A/B, đọc reference, "đúng mà vô danh", vùng phụ (casebook phân tích 2026-09) | `VISUAL_ANALYSIS_CASEBOOK_2026-09.md` | candidate casebook; luật ứng viên, không phải canonical; current request thắng |

## Epistemic order

Khi hai mệnh đề trong formation layer xung đột:

1. yêu cầu/reference/authority hiện tại và điều kiện sử dụng;
2. scoped calibrated evidence có model/version/date, controls, denominator và exception boundary trong đúng phạm vi;
3. sourced fine-arts/perception foundation;
4. studio heuristic;
5. family preference;
6. case history hoặc ví dụ.

Không dùng một câu mạnh trong file cũ để vượt qua boundary ghi trong file mới.

## Minimal recipes

### Single image cần art direction

~~~text
VISUAL_DESIGN_KNOWLEDGE_BASE
→ ART_DIRECTION_WORKFLOW_AND_CRITIQUE_OS
→ matching canonical family
~~~

### Reference hoặc nghiên cứu mỹ thuật

~~~text
FINE_ARTS_PERCEPTION_AND_FORM_KNOWLEDGE_BASE
→ core/04_REFERENCE_ANALYZER
→ Visual_Resource_Library/CURATION_POLICY khi có văn hóa/quyền
~~~

### Fusion hoặc family mới

~~~text
FINE_ARTS_PERCEPTION_AND_FORM_KNOWLEDGE_BASE
→ ART_FUSION_AND_CREATIVE_SYNTHESIS
→ ART_DIRECTION_WORKFLOW_AND_CRITIQUE_OS
→ core/07 + TEMPLATE_FUSION_BRIEF
~~~

### Failed output

~~~text
ART_DIRECTION_WORKFLOW_AND_CRITIQUE_OS phần Critique OS
→ core/09
→ TEMPLATE_GENERATION_LOG
~~~

### Cinematic discussion hoặc dựng lại từ reference

~~~text
CINEMATIC_VISUAL_STORYTELLING_KB
→ core/04 (carry/lock/translate/repair/drop/open)
→ library/20_CINEMATIC_DISCUSSION_AND_REBUILD_WORKFLOW
→ core/02 (không compile khi DISCUSS)
→ core/03 chỉ khi đã DECIDED/delegated
~~~

### Nâng cấp thẩm mỹ / greatness audit

~~~text
CONNOISSEURSHIP_AND_AESTHETIC_JUDGMENT
→ FINE_ARTS_PERCEPTION_AND_FORM_KNOWLEDGE_BASE
→ core/02 step 3 và step 6
→ core/09 pass 16 + image pass 11
~~~


### Clean Impossibility / structured surreal

~~~text
CLEAN_IMPOSSIBILITY_AND_PERCEPTUAL_DESIGN
→ library/12_ILLUSION_MECHANISMS (Clean Impossibility cards)
→ layer-occlusion-preflight khi có stack/crossing
→ matching canonical family (không force Dark Deco / face-first nếu first_read_owner = mechanism|world)
~~~


### Reverse-match / recreate User Reference (EggOS)

~~~text
REVERSE_IMAGE_PROMPT_LOOP_SLIM
→ VOXCAT_CREATIVE_CHAIN (Base vs Revision)
→ Director Final (1/turn) + Analyst REVERSE_LOOP DM
~~~

## Boundary

## U07 active field-note and resource routing

Use `Portable_Agent_OS/field_notes_active.json` as the machine-readable selector and `Portable_Agent_OS/FIELD_NOTES.md` as the append-only source. Load only notes whose scope matches the current family, generator, method, or brief. Superseded notes remain historical evidence.

For visual references, use `Visual_Resource_Library/` metadata and curation policy first; fetch or load binary resources only when the task packet assigns a reference role that needs them. `Visual_Calibration_Corpus/` is a compatibility/calibration input, not a universal prompt authority. Evidence, rights/provenance, and render observations stay in separate records.

- Recipe trong file cũ không phải universal law chỉ vì được viết ở giọng khẳng định.
- `rule of thirds`, palette ratio, lens recipe, eye/catchlight setup và prompt-order claim đều là hypothesis/heuristic trừ khi nguồn hoặc calibration chứng minh phạm vi.
- `deliberate open` là quyết định, không phải omission.
- Mixed media có một grammar chủ đạo cho mỗi ontology/layer, không bắt toàn ảnh dùng một medium/line language.
- Cultural source phải giữ community/region, period, function, provenance và restriction khi relevant.
- Thang L0–L5 và các distinction test trong `CONNOISSEURSHIP_AND_AESTHETIC_JUDGMENT.md` là dụng cụ phán đoán, không phải công thức sản xuất; chúng không bao giờ ghi đè message/brief.
