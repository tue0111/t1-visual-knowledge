# T1 Visual Knowledge

Hệ agent viết prompt ảnh cho dự án **T1 to 9**: tiếng Trung, 3 phần 【母版锁】【分镜】【通用负面提示词】, ra ảnh đúng ý ngay lần đầu và sửa đúng chỗ khi hỏng.

Ba tầng, mỗi tầng một file:

| Tầng | File | Nội dung |
|---|---|---|
| Mindset | `system/01_MINDSET.md` | 10 nguyên lý, 4 chế độ ảnh, chọn trục chính |
| Knowledge | `system/02_KNOWLEDGE.md` | 8 trục (ánh sáng, máy, bố cục, màu, chất liệu, không khí, khoảnh khắc, thế giới): hỏi gì, viết gì, model hỏng ở đâu |
| Workflow | `system/03_WORKFLOW.md` | 5 bước từ brief đến prompt, vòng sửa ảnh lỗi |
| Craft | `system/05_CRAFT.md` | phong cách, tham chiếu, câu chuyện, nhiều người, độ thật, series, vệ sinh prompt, sửa lỗi |
| Film grounding | `system/06_FILM_GROUNDING.md` | 14 cơ chế hành động, đường nhìn, màu theo vật mang, điểm đứng máy và tách thân khi chồng lấp; nhãn sách, chưa thử ảnh |
| Khuôn | `system/04_TEMPLATES.md`, `examples/` | khuôn 3 phần, brand, 3 ví dụ đầy đủ |
| Thực chiến | `system/LEARNINGS.md` | lỗi đã thấy trên ảnh thật; lớn dần theo thời gian |

## Dùng

- **Codex:** mở repo, `AGENTS.md` tự nạp. Đưa ý tưởng ảnh.
- **Claude Code:** `CLAUDE.md` trỏ về `AGENTS.md`; skill `.claude/skills/t1-visual-prompt` tự kích hoạt khi xin prompt ảnh.
- **Chat khác (ChatGPT, Claude.ai):** dán `AGENTS.md` + `system/01`, `03`, `LEARNINGS` làm ngữ cảnh; tra `02` khi cần.

Kiểm luật cứng của một prompt (chỉ cần Python 3.9+, không thư viện ngoài):

```bash
python tools/t1lint.py my_prompt.txt          # thêm --strict để cảnh báo cũng fail
python -m unittest discover -s tests          # chạy test của linter
```

## Vòng học
Sinh ảnh → thấy lỗi → sửa 1–2 câu → ghi một dòng vào `system/LEARNINGS.md`. Bài học lặp ≥ 3 lần ở các brief khác nhau thì chuyển vào `02_KNOWLEDGE.md`.

## Lịch sử
Bản trước (OS v2, Knowledge_Mindset, K1–K8/M/W, notes, ~1.3MB) được giữ nguyên ở tag [`legacy-v1`](../../tree/legacy-v1). Bản này chưng cất từ đó cùng với bài học test W2 (2026-10-03).
