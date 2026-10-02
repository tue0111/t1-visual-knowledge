# T1 Visual Knowledge

Kho tri thức thuần cho việc **đọc ảnh, ra quyết định thị giác và viết prompt ảnh** của dự án T1 to 9.
Không gắn với bot, model hay nền tảng nào. Người, Claude, GPT, Grok hay AI khác đều đọc được.

- Nguồn: release `t1gb_r0003` (canonical `t1to9_os_3_2_1_20260925`), ngày 2026-09-25.
- 119 file tri thức được **chép nguyên văn từng byte**. Bằng chứng: `SOURCE_MANIFEST.json` (sha256 từng file), kiểm lại bằng `python tools/verify_manifest.py`.
- Lớp mới (do Claude viết): `README.md`, `INDEX.md`, `AGENTS.md`, `knowledge/`, `notes/`, `tools/`.

## Cấu trúc

```
README.md                      file này
INDEX.md                       mục lục theo chủ đề + danh mục toàn bộ file  ← bắt đầu ở đây
AGENTS.md                      hướng dẫn cho AI khi dùng repo
SOURCE_MANIFEST.json           sha256 của mọi file chép nguyên văn
Knowledge_Mindset/             lớp hình thành tư duy (mỹ thuật, cinema, connoisseurship, fusion, casebook…)
T1_TO_9_VISUAL_PROMPT_OS_v2/   hệ prompt: core (luật, quy trình, compiler, validator), library, families, templates, examples, generators, schemas
knowledge/                     Tầng 1: module kiến thức theo trục (K1 Ánh sáng…) — xem knowledge/README.md
notes/                         tri thức mới, trạng thái CANDIDATE (chưa qua promotion)
tools/verify_manifest.py       kiểm tính nguyên văn
```

Tên thư mục `Knowledge_Mindset/` và `T1_TO_9_VISUAL_PROMPT_OS_v2/` giữ nguyên như bản gốc để mọi đường dẫn tham chiếu chéo bên trong file vẫn đúng.

## Thứ tự thẩm quyền

Khi hai nguồn mâu thuẫn, nguồn đứng trước thắng:

1. yêu cầu / reference / chỉnh sửa mới nhất của người dùng
2. project profile hiện tại (nếu có)
3. `T1_TO_9_VISUAL_PROMPT_OS_v2/core/00_PROJECT_CONTRACT.md`
4. `core/01_CORE_LAWS.md`
5. family khớp (`families/`)
6. engine / library
7. `Knowledge_Mindset/` theo phạm vi bằng chứng
8. examples
9. `notes/` (candidate — chỉ là giả thuyết có lý do)

## Cố ý KHÔNG đưa vào

Hạ tầng riêng của Grok Bot và vận hành: `Runtime_Source/`, `Releases/`, `bot_profiles/`, `tools/*.py|ps1` của bản gốc, `pilot/`, `migration/`, `BOOTSTRAP.md`, `manifest.json`, `VALIDATION_REPORT.md`, `MIGRATION_MAP.md`, `PROJECT_PROFILE.md`, `EGGBOT_LAB_CHANGELOG`. Chúng vẫn nằm nguyên ở repo build `T1_GrokBot_OS_r0003`.

**Không bao giờ đưa lên đây:** đáp án pilot (`pilot_gold`), ảnh của người khác, token/khoá.

Hệ quả: một số file nguyên văn nhắc tới đường dẫn không có trong repo này (ví dụ `BOOTSTRAP.md`, `tools/validate_pack.ps1`, `Portable_Agent_OS/`, `Visual_Resource_Library/`). Đó là tham chiếu lịch sử, không phải file bị thiếu. Danh sách đầy đủ ở cuối `INDEX.md`.

## Cập nhật tri thức

- File nguyên văn: chỉ sửa qua thay đổi có duyệt; sửa xong chạy lại `tools/verify_manifest.py --update` và ghi lý do trong commit.
- Tri thức mới: viết vào `notes/` với trạng thái `CANDIDATE`, kèm bằng chứng và phản ví dụ. Chỉ chuyển sang lớp canonical theo `core/11_EVIDENCE_AND_PROMOTION_ENGINE.md`.
- Không chấm "gu cá nhân" như sự thật; gu hình thành dần qua sử dụng.
