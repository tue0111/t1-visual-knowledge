---
name: t1-atmosphere-devices
description: Chọn và ghép thủ pháp không khí vào prompt ảnh T1 to 9 — viền sáng ngược qua sương, sương nhiều lớp, khoảng tối lớn với người nhỏ, một nguồn ấm trên nền lạnh, vật tự phát sáng trong khung, tiền cảnh lấn khung có hướng, che mặt bằng mặt nạ/quạt/mạng/nón kèm cử chỉ, lụa mỏng, nhoè chuyển động cục bộ, góc máy sát đất. Dùng khi brief hoặc ảnh tham chiếu cần không khí, che mặt, chuyển động, hoặc mang chất cổ trang/tiên hiệp.
---

Skill này đi kèm `t1-visual-prompt`, không thay nó. Khuôn 3 phần, luật cứng và brand vẫn theo skill đó.

1. Chạy `t1-visual-prompt` tới bước bảng quyết định.
2. Mở `system/07_ATMOSPHERE_DEVICES.md`. Dùng cột "Hỏi" để chọn **một thủ pháp chính, tối đa hai phụ**. Ghi ID (AD-xx) vào dòng trục của bảng quyết định.
3. Chép câu mẫu rồi sửa vật, hướng, tỷ lệ cho khớp brief. Luật cả album đặt trong 母版锁, chi tiết riêng khung đặt trong 分镜.
4. Lấy cột "Bẫy" của từng thủ pháp đã chọn, thêm đúng mục cần vào negative, giữ tổng ≤ 14.
5. Đối chiếu bảng "Cặp xung đột". Có cặp trùng thì sửa theo cột "Cách giữ cả hai" hoặc bỏ một thủ pháp.
6. Khung nghiêng: viết khung thẳng, ghi trong phần rủi ro là nghiêng ở hậu kỳ. Chạy Midjourney thì đổi kiếm, dao sang đạo cụ khác.
7. Ghi prompt ra file tạm, chạy `python tools/t1lint.py <file>` đến khi PASS.
8. Giao như `t1-visual-prompt`; dòng rủi ro lấy từ cột "Bẫy".
9. Có ảnh ra: ghi một dòng `system/LEARNINGS.md` có ID thủ pháp; thủ pháp đã thấy chạy thì đổi nhãn UNTESTED trong `07`.
