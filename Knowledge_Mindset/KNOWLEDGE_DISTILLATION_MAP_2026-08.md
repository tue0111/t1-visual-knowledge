# KNOWLEDGE DISTILLATION MAP — 2026-08

Bản đồ chưng cất toàn bộ nguyên liệu thô của workspace sang tri thức có thẩm quyền. Đây là research note thuộc formation layer: nó ghi trạng thái bằng chứng và hàng đợi thăng cấp, không phải luật delivery. Quyết định vận hành vẫn thuộc `AGENTS.md`; thăng cấp family tuân theo `../../T1_TO_9_VISUAL_PROMPT_OS_v2/core/07_FUSION_AND_GROWTH_ENGINE.md`.

## 1. Phương pháp

Mỗi nguồn thô được xếp một trong bốn trạng thái:

| Trạng thái | Nghĩa |
|---|---|
| PROMOTED | đã sống trong canonical với đường dẫn cụ thể |
| CASEBOOK | kết quả thật nhưng chưa đủ bằng chứng lặp lại/falsifier để thành luật |
| CALIBRATION | hành vi riêng của một generator; lưu ở field notes, không vào canonical |
| SUPERSEDED | nội dung đã được V2 thay thế; chỉ còn giá trị lịch sử |

## 2. Kho archive thô (Project_Source_Knowledge_Pack, frozen)

| Nguồn thô | Trạng thái | Đích đến |
|---|---|---|
| Unified Pack v1.2 (00_CORE_MIND, 01_COMPILER, 02_VALIDATOR, 03_GROWTH, 04_FUSION_ENGINE) | SUPERSEDED | Laws 1–13, compiler, validator, growth, fusion → `core/01`–`core/03`, `core/07` (theo CHANGELOG legacy baseline) |
| FAMILY_SEMIREAL_COUTURE_CREATURE_v2 | SUPERSEDED | tổng quát hóa thành `families/FAMILY_COUTURE_ENTITY.md` + kernels |
| FAMILY_EMERALD_INK_SOVEREIGN_v1 | PROMOTED | `families/FAMILY_EMERALD_INK_SOVEREIGN.md` |
| acg_* master v3 + ACG_Universal_Workflow_v2 | SUPERSEDED | chuẩn hóa thành `families/FAMILY_ACG_REALISTIC_COSPLAY.md` |
| Claude_Knowledge_Pictorial_Reality + pictorial_v1_1 | PROMOTED | `families/FAMILY_PICTORIAL_REALITY.md` |
| illusion_grammar_module_v1 | PROMOTED | `library/12_ILLUSION_MECHANISMS.md` |
| Ancient_Jewelry_Boudoir_Phone_Flash_Module | PROMOTED | `families/FAMILY_PHONE_FLASH_BOUDOIR.md` |
| Prompt Ví dụ.txt + Project_Prompt_Master_Knowledge_Pack_20260704 | CASEBOOK | ví dụ đã tuyển chọn vào `examples/`; phần còn lại là lịch sử quyết định (SOURCE_AUDIT_AND_CHAT_DECISIONS.md) |
| raw_keyword_creative_direction_mindset_v1 | CASEBOOK | tư duy chung đã hấp thụ vào Knowledge_Mindset; giữ làm provenance |

Kho archive tiếp tục frozen; không nạp trong tác vụ thường ngày.

## 3. Outputs — kết quả sáng tạo

### 3a. cinematic_deco_xianwuxia — PROMOTED (release 2.5.0)

Charter hoàn chỉnh sinh ra đúng core/07 §8 trước khi generate; bằng chứng: ba album 剑影浮世， 仙土幻境， 夜人行 + dòng sửa lỗi DarkDeco v1 → root variant → v2 (single-axis repair). Đã đăng ký `families/FAMILY_CINEMATIC_DECO_XIANWUXIA.md`. Các album gốc ở Outputs giữ vai trò casebook, không thăng cấp thành examples cho đến khi được định dạng lại đúng contract ba phần và tuyển chọn có chủ đích.

### 3b. SERIES01_SiXiang (A–D) — CASEBOOK, hàng đợi thăng cấp

Bốn album hoàn chỉnh tiếng Trung ở bốn medium dẫn dắt: A 羽翼编年 (digital thick-paint, đã validate trên GPT Image), B 山海问道 (xieyi thủy mặc), C 百鬼夜行 (ukiyoe mộc bản), D 六天乐舞 (敦煌壁画 khoáng sắc). Mỗi cái có anchor/read-order/material logic riêng → ứng viên family kiểu medium-led, nhưng **chưa** có falsifier dự ký trước hay baseline đa seed nên chưa đủ chuẩn core/07.

Falsifier dự ký đề xuất (phải chạy trước khi thăng cấp):

1. Với mỗi style: sinh 3 ảnh fresh-seed từ 母版锁 không chỉnh sửa.
2. Falsifier chung: nếu ≥2/3 ảnh viền medium (ảnh A ra 3D render, ảnh B mất 留白, ảnh C xuất hiện gradient mềm, ảnh D mất龟裂) thì cơ chế medium-lock cần viết lại, không phải thăng cấp.
3. Nếu qua: viết charter theo mẫu §8 core/07 → đăng ký lần lượt, mỗi lần một family, kèm generation log.

### 3c. Khoản mục còn lại

| Nhóm | Trạng thái | Ghi chú |
|---|---|---|
| ALBUM_QINGHUA_LIEJIN_12_FULL_CN_PROMPTS | CASEBOOK | công việc instance dưới kernel khóa 青花裂金； kernel mới chỉ append khi được duyệt |
| DC_XIANXIA_GPT_IMAGE_2_PROMPT_PACK + DarkDeco lineage | CALIBRATION | hành vi GPT Image 2 (anatomy, refusal, megastructure) → `Portable_Agent_OS/FIELD_NOTES.md`; môi trường xianxia quy mô lớn chưa có calibration cục bộ nên chưa vào canonical |
| Khue_Cac_Studio (4 album + prompts index) | CASEBOOK | deliverable hoàn tất; bài học chung (album classification, GPT Image behavior) đã hấp thụ; giữ làm tham chiếu identity-lock |
| silk-water-free-shoal-v2 (prompt text) | CASEBOOK | thử nghiệm T1–T9; render binary đã tách khỏi repo theo luật lưu trữ |

## 4. Hàng đợi làm việc kế tiếp

1. Chạy falsifier 3b cho từng style SiXiang, mỗi style một generation log riêng.
2. Định dạng 1–2 album cinematic_deco_xianwuxia tốt nhất thành canonical examples (đúng ba phần, đúng fence) rồi đăng ký manifest.
3. Bổ sung calibration cục bộ cho xianxia environmental-megastructure trước khi cân nhắc mở rộng family.
4. Một knowledge wave Visual_Resource_Library ưu tiên gap trong reports/RESEARCH_BACKLOG.md.
5. Tiếp nhận nguồn thực hành bên ngoài (4 pháp sư X Articles + vibeshot.club) — **HOÀN TẤT đợt 1+2 (2026-08-25)**: 105 bài captured, 22 bài đọc kỹ, cơ chế craft-general đã vào `library/11` §11 (release 2.6.0), phần generator-scoped vào FIELD_NOTES; chi tiết trong `EXTERNAL_PRACTITIONER_INTAKE.md`. Còn lại: hàng đợi 🔴 đã xử lý xong, các bài 🟡 đọc dần khi relevant.
6. **Làn sóng làm giàu từ kho tri thức nền của agent (2026-08-25):** hai KB formation mới — `PHOTOGRAPHIC_MEDIA_AND_IMAGING_PROCESSES_KB.md` (film stock/process/lens character/CCD-phone signature + bảng brief→media recipe) và `CHINESE_AESTHETICS_AND_MATERIAL_CULTURE_KB.md` (ngũ sắc, palette theo triều đại, hệ vải 绫罗绸缎纱锦缂丝, tiến hóa silhouette trang phục, kiến trúc-viên lâm, hoa văn, mode thẩm mỹ, ranh giới văn hóa). Đều ở formation layer, không đụng delivery contract; các câu zh-CN là khởi điểm heuristic.
