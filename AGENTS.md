# AGENTS.md — dành cho AI dùng repo này

Repo này là **tri thức**, không phải bot hay chương trình. Dùng nó để suy nghĩ và viết prompt ảnh tốt hơn.

## Cách dùng
1. Đọc `INDEX.md` mục 1, chọn đúng lộ trình cho việc đang làm. Chỉ nạp các file trong lộ trình đó.
2. Khi viết prompt cho dự án T1 to 9: tuân theo `T1_TO_9_VISUAL_PROMPT_OS_v2/core/00_PROJECT_CONTRACT.md` — tiếng Trung giản thể, đúng 3 phần 【母版锁】【分镜】【通用负面提示词】, chữ "T1 to 9" nằm trong 母版锁 trừ khi brief nói khác.
3. Thứ tự thẩm quyền: xem `README.md`. Yêu cầu hiện tại của người dùng luôn thắng.
4. Viết prompt mới theo 3 tầng: `mindset/M1` (chọn trục chính/phụ) → `knowledge/K1–K8` (chỉ trục được chọn) → `writing/W1` (ngân sách + map vào 3 phần). Các file 3 tầng là v0.1 CANDIDATE: dưới `core/` về thẩm quyền.

## Kỷ luật phân tích ảnh
- Tách NHÌN THẤY / SUY LUẬN / KHÔNG THỂ BIẾT. Không khẳng định loại máy, film, tiêu cự, địa danh, danh tính.
- Nói cơ chế (vì sao ảnh hiệu quả / hỏng), không chỉ liệt kê nội dung.
- Không chấm gu cá nhân như sự thật.

## Kỷ luật sửa repo
- File có trong `SOURCE_MANIFEST.json` là nguyên văn: không sửa trừ khi người dùng duyệt thay đổi. Sửa xong: `python tools/verify_manifest.py --update`.
- Tri thức mới → `notes/` với `status: CANDIDATE`, có bằng chứng, phản ví dụ, cách test.
- Không commit: đáp án pilot, ảnh của người khác, token/khoá, file chạy riêng cho bot.
- Đường dẫn trong file nguyên văn trỏ tới hạ tầng cũ (xem `INDEX.md` mục 4) là tham chiếu lịch sử — bỏ qua.
