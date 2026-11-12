# T1 Visual Knowledge

Hệ agent viết prompt ảnh cho dự án **T1 to 9**, tiếng Trung. Hai làn:
- **Chính xác:** ý đồ đã rõ thì viết cho ra ảnh đúng ngay lần đầu, hỏng thì sửa đúng chỗ (`system/03_WORKFLOW.md`).
- **Sáng tạo:** chủ đề mở thì tự tìm ý niệm, tra thêm dữ liệu, chọn hình dạng album rồi mới viết (`system/10_CREATIVE_ALBUM.md`).

Khuôn prompt (3 phần 【母版锁】【分镜】【通用负面提示词】, keyword một dòng, văn xuôi ngắn) là bước đóng gói cuối, chọn theo generator.

Ba tầng (mindset, knowledge, workflow) và các lớp mỏng tra khi cần:

| Tầng | File | Nội dung |
|---|---|---|
| Mindset | `system/01_MINDSET.md` | 12 nguyên lý, 4 chế độ ảnh, chọn trục chính |
| Knowledge | `system/02_KNOWLEDGE.md` | 8 trục (ánh sáng, máy, bố cục, màu, chất liệu, không khí, khoảnh khắc, thế giới): hỏi gì, viết gì, model hỏng ở đâu |
| Workflow | `system/03_WORKFLOW.md` | làn chính xác: 5 bước từ brief đến prompt, vòng sửa ảnh lỗi |
| Workflow sáng tạo | `system/10_CREATIVE_ALBUM.md` | làn sáng tạo: chống lối mòn, 10 động cơ sinh ý niệm, tra cứu mở rộng có ngân sách, 8 hình dạng album, việc của từng khung, nhịp album, chọn khuôn sau cùng |
| Craft | `system/05_CRAFT.md` | phong cách, tham chiếu, câu chuyện, nhiều người, độ thật, series, vệ sinh prompt, sửa lỗi |
| Film grounding | `system/06_FILM_GROUNDING.md` | 14 cơ chế hành động, đường nhìn, màu theo vật mang, điểm đứng máy và tách thân khi chồng lấp (có giới hạn khung dọc); nhãn sách, chưa thử ảnh |
| Atmosphere devices | `system/07_ATMOSPHERE_DEVICES.md` | 10 thủ pháp không khí: viền sáng ngược, sương nhiều lớp, khoảng tối, nguồn ấm cục bộ, vật tự sáng, tiền cảnh có hướng, che mặt kể bằng cử chỉ, lụa mỏng, nhoè cục bộ, sát đất; nhãn quan sát, chưa thử ảnh |
| Keyword | `system/08_KEYWORD_FORMAT.md`, `examples/keyword/` | khuôn bổ sung một dòng nối bằng `+`: hình dạng, 9 luật linter bắt, khối khoá nhân vật, cách tách ví dụ để lint không xung đột |
| Shot vocab | `system/09_SHOT_VOCAB.md` | kho từ vựng khung để tra (không phải ma trận phải điền): 7 trục, bảng ghép máy–đầu, mẫu bảng 8 khung; nhãn quan sát, chưa thử ảnh |
| Đèn và ống kính | `system/11_LIGHT_AND_OPTICS.md` | đèn trên mặt người đọc bằng bóng mũi, phía chiếu, cỡ nguồn và độ suy giảm, đốm sáng mắt, vùng nét, tiêu cự và chỗ máy đứng; chưa thử ảnh |
| Không gian và dàn cảnh | `system/12_SPACE_AND_STAGING.md` | 8 thiết bị không gian (trục lùi, khung cửa, mượn cảnh, hành lang cột, hiên sâu, giếng trời, lớp bán trong, mặt phản chiếu), nơi chốn và trang phục Việt, hai người đối nhau, cảnh thật hay cảnh dựng, người trong nơi của họ; chưa thử ảnh |
| Thế giới và lối kể | `system/13_WORLD_AND_TELLING.md` | ba câu hỏi của bối cảnh, giữ một nơi chốn qua nhiều khung, vật mang chuyện ba trạng thái, vết mòn có nguyên nhân, màu để dành, mốc thời kỳ, bảy lối kể cho album, cảm xúc bằng thân; chưng từ kho phim `film-craft`, chưa thử ảnh |
| Ví dụ sáng tạo | `examples/creative/` | hai phiếu album mẫu: G biến tấu (nhuộm chàm, keyword), H loại hình vắng người (ghế nhựa vỉa hè, văn xuôi ngắn); chưa sinh ảnh |
| Khuôn | `system/04_TEMPLATES.md`, `examples/` | khuôn 3 phần, brand, 4 ví dụ đầy đủ (D: ánh sáng ngược xuyên khói) |
| Thực chiến | `system/LEARNINGS.md` | lỗi đã thấy trên ảnh thật; lớn dần theo thời gian |

## Dùng

- **Codex:** mở repo, `AGENTS.md` tự nạp. Đưa ý tưởng ảnh.
- **Claude Code:** `CLAUDE.md` trỏ về `AGENTS.md`; skill `.claude/skills/t1-visual-prompt` tự kích hoạt khi xin prompt ảnh; skill `.claude/skills/t1-creative-album` kích hoạt khi xin album mở hoặc yêu cầu sáng tạo; skill `.claude/skills/t1-atmosphere-devices` thêm vào khi cần không khí, che mặt, chuyển động.
- **Chat khác (ChatGPT, Claude.ai):** dán `AGENTS.md` + `system/01`, `03`, `LEARNINGS` làm ngữ cảnh; tra `02` khi cần.

Kiểm luật cứng của một prompt (chỉ cần Python 3.9+, không thư viện ngoài):

```bash
python tools/t1lint.py my_prompt.txt          # tự nhận 3 phần hoặc keyword; thêm --strict để cảnh báo cũng fail
python tools/t1lint.py --strict examples/*.txt examples/keyword/*.txt
python -m unittest discover -s tests          # chạy test của linter
```

## Vòng học
Sinh ảnh → thấy lỗi → sửa 1–2 câu → ghi một dòng vào `system/LEARNINGS.md`. Bài học lặp ≥ 3 lần ở các brief khác nhau thì chuyển vào `02_KNOWLEDGE.md`.

## Lịch sử
Bản trước (OS v2, Knowledge_Mindset, K1–K8/M/W, notes, ~1.3MB) được giữ nguyên ở tag [`legacy-v1`](../../tree/legacy-v1). Bản này chưng cất từ đó cùng với bài học test W2 (2026-10-03).
