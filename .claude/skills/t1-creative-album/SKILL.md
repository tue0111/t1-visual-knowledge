---
name: t1-creative-album
description: Dựng album hoặc bộ ảnh sáng tạo T1 to 9 khi người dùng đưa chủ đề mở, nói "sáng tạo đi", "tự do", "làm gì đó mới", hoặc muốn được đề xuất ý tưởng. Tự tìm ý niệm, tra thêm dữ liệu (web, VSC, sách điện ảnh), chọn hình dạng album, giao việc cho từng khung rồi mới viết prompt. Không dùng cho ảnh đơn đã rõ ý đồ, tái dựng ảnh mẫu hay sửa ảnh lỗi (dùng t1-visual-prompt).
---

1. Đọc `AGENTS.md`, `system/01_MINDSET.md`, `system/LEARNINGS.md`, rồi `system/10_CREATIVE_ALBUM.md`. Làm đúng thứ tự §0 → §8 của file 10.
2. §0–§1: tách cái đã khoá / còn mở; viết ra "album trước là gì" từ LEARNINGS và chỗ album mới phải khác.
3. §2: sinh 5–7 hướng ý niệm từ ít nhất bốn động cơ khác nhau, mỗi hướng một câu có động từ.
4. §3: tra cứu trong ngân sách 3–8 lượt (web cho sự thật đời thực; `vsc_*` cho phong cách, khung máy, cách người khác viết; `film-library` cho dàn cảnh và ánh sáng). Gom thành bảng vật liệu. Không có công cụ thì nói một dòng và làm tiếp.
5. §4: đưa người dùng 3 hướng để chọn (bỏ qua nếu họ nói "cứ làm"), viết phiếu ý niệm, chọn hình dạng album.
6. §5: lập bảng khung, mỗi khung một việc; tra `system/09_SHOT_VOCAB.md`, `07_ATMOSPHERE_DEVICES.md`, `02_KNOWLEDGE.md` để lấy từ, không điền ma trận.
7. §6: chọn khuôn theo generator (3 phần `04`, keyword `08`, hoặc văn xuôi ngắn). Khuôn 3 phần và keyword thì ghi ra file tạm và chạy `python tools/t1lint.py <file>` đến khi PASS.
8. §7: tự soát cấp album. §8: giao phiếu ý niệm, bảng khung, prompt, tối đa 3 dòng rủi ro.
9. Có ảnh rồi: ghi một dòng vào `system/LEARNINGS.md` và cập nhật đoạn "lối mòn hiện tại" ở `10` §1 nếu album vừa xong đã thành khuôn mới.
