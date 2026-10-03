---
name: t1-visual-prompt
description: Viết hoặc sửa prompt ảnh T1 to 9 (tiếng Trung, 3 phần 母版锁/分镜/通用负面提示词). Dùng khi người dùng đưa ý tưởng ảnh, ảnh tham chiếu, hoặc ảnh lỗi cần sửa prompt.
---

1. Đọc `AGENTS.md`, `system/01_MINDSET.md`, `system/03_WORKFLOW.md`, `system/LEARNINGS.md`.
2. Viết bảng quyết định 6 dòng; tra `system/02_KNOWLEDGE.md` đúng trục chính và trục phụ; có phong cách, ảnh tham chiếu, nhiều người, candid, gợi cảm người lớn hay series thì tra thêm `system/05_CRAFT.md`.
3. Soạn 3 phần theo `system/04_TEMPLATES.md`; brand chép từ `system/brand_block.txt` và `system/brand_negative.txt`.
4. Ghi prompt ra file tạm, chạy `python tools/t1lint.py <file>`; sửa đến khi PASS.
5. Giao: bảng quyết định, 3 khối code, tối đa 3 dòng rủi ro.
6. Ảnh lỗi: chạy "Vòng sửa" trong `system/03_WORKFLOW.md`, rồi thêm một dòng vào `system/LEARNINGS.md`.
