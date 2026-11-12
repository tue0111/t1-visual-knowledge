---
name: t1-visual-prompt
description: Viết hoặc sửa prompt ảnh T1 to 9 (tiếng Trung, 3 phần 母版锁/分镜/通用负面提示词). Dùng khi người dùng đưa một ý đồ ảnh đã rõ, ảnh tham chiếu, hoặc ảnh lỗi cần sửa prompt. Album mở hay yêu cầu sáng tạo thì dùng t1-creative-album.
---

1. Đọc `AGENTS.md`, `system/01_MINDSET.md`, `system/03_WORKFLOW.md`, `system/LEARNINGS.md`.
2. Viết bảng quyết định 6 dòng; tra `system/02_KNOWLEDGE.md` đúng trục chính và trục phụ; có phong cách, ảnh tham chiếu, nhiều người, candid, gợi cảm người lớn hay series thì tra thêm `system/05_CRAFT.md`; cần viền sáng ngược, sương, khoảng tối, che mặt bằng vật, tiền cảnh lấn khung hay chuyển động thì tra `system/07_ATMOSPHERE_DEVICES.md` (skill `t1-atmosphere-devices`); ảnh phẳng, cần chiều sâu ở bất kỳ tông sáng nào, hoặc ảo giác thị giác (gương, bóng, tỷ lệ, tranh thành vật, khúc xạ) thì tra `system/14_DEPTH_AND_PARALLAX.md` (skill `t1-depth-layers`).
3. Soạn 3 phần theo `system/04_TEMPLATES.md` (nếu người dùng chọn keyword một dòng thì theo `system/08_KEYWORD_FORMAT.md`, không brand trong prompt); brand chép từ `system/brand_block.txt` và `system/brand_negative.txt`.
4. Ghi prompt ra file tạm, chạy `python tools/t1lint.py <file>`; sửa đến khi PASS.
5. Giao: bảng quyết định, 3 khối code, tối đa 3 dòng rủi ro.
6. Ảnh lỗi: chạy "Vòng sửa" trong `system/03_WORKFLOW.md`, rồi thêm một dòng vào `system/LEARNINGS.md`.
