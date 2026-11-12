---
name: t1-depth-layers
description: Dựng chiều sâu và ảo giác thị giác cho prompt ảnh T1 to 9 ở mọi tông sáng (tối ngược sáng, sáng trắng, nắng gắt, sáng đều bằng màu, đêm nhiều màu đèn, phẳng có chủ đích) - bản đồ lớp từ sát máy ra xa, mười dấu sâu, không khí làm thước đo khoảng cách (mù, khói, sương, mưa tuyết, bụi nắng, kính đọng hơi, dưới nước), một đỉnh tương phản, và mười lăm phép thị sai đóng băng (mảnh gương, bóng phản chiếu lệch, gương đối gương, kính vừa soi vừa xuyên, cảnh trong khe, ép phối cảnh, đảo tỷ lệ, tranh tràn ra phòng, bước ra khỏi khung, sân khấu giấy, hoa văn hút mắt, kiến trúc bất khả, bóng làm việc khác, khúc xạ, khoảng trống thành hình). Dùng khi ảnh phẳng dù đủ chi tiết, người dính vào nền, sương khói làm đục ảnh, album cứ ra nền tối giống nhau, brief nhắc thị sai, parallax, ảo giác thị giác, chiều sâu, nhiều lớp, hoặc ảnh sẽ đem làm clip có máy chuyển động.
---

Skill này đi kèm `t1-visual-prompt` (ảnh đơn) hoặc `t1-creative-album` (album), không thay chúng. Khuôn, luật cứng và brand vẫn theo hai skill đó.

**Không có mặc định.** Nền tối, khói, ngược sáng, phụ nữ đứng nghiêng là lối đã thử nhiều nhất, không phải lối đúng nhất. Mọi bước dưới đây phải chạy được ở trưa nắng, sương trắng, màu rực, ảnh không người.

1. Chạy skill chính tới bảng quyết định (ảnh đơn) hoặc bảng khung (album).
2. Mở `system/14_DEPTH_AND_PARALLAX.md`. **Chọn chìa sáng trước mọi thứ** (§3, sáu chìa A đến F), theo ý niệm chứ không theo thói quen.
3. Đi qua bảng xoay §7: chọn một giá trị ở từng trục (chìa, bảng màu, vật liệu của mép và lớp sát máy, máy, chủ thể, thân, nơi), đổi ít nhất ba trục so với lần dùng trước. Album: không hai khung nào trùng cả chìa, vật liệu lớp sát máy và độ cao máy.
4. Viết bảng năm dòng ở §9. Điền lớp rồi soát theo §2: có khe, hai lớp kề nhau khác ít nhất hai trong sáu thứ, so le theo một thuộc tính. **Thiếu gì mới viết thêm cái đó**; cảnh đã đủ lớp thì không chép luật lớp vào prompt.
5. Chọn ít nhất ba dấu sâu hợp với chìa (§1). Cần câu đèn hay viền sáng thì lấy ở `system/07_ATMOSPHERE_DEVICES.md` và `system/11_LIGHT_AND_OPTICS.md`, không viết lại.
6. Không khí: có hay không. Có thì **một** dạng ở §4, và ánh sáng phải đi qua nó về phía máy hoặc xiên ngang.
7. Chốt một đỉnh tương phản (§5), ghi nó là cái gì trên cái gì. Đỉnh có thể là tối trên sáng, màu trên xám, nét giữa mờ.
8. Brief cần ảo giác thì chọn **một** phép P1 đến P15 (§6). Viết cái mép trước, rồi viết **từng phần riêng**: góc của từng mảnh, hướng nhìn của từng bên, tư thế của người và của bóng, đường đi của vật từng đoạn.
9. Ảnh sẽ thành clip thì soát §8 và ghi trong phần rủi ro: máy trượt hướng nào, hay phải đứng yên.
10. Đối chiếu bảng cặp xung đột §10. Negative lấy từ cột "hay hỏng" của đúng thứ đã dùng, tổng ≤ 14.
11. Ghi prompt ra file tạm, chạy `python tools/t1lint.py <file>` đến khi PASS. Giao như skill chính, kèm bảng năm dòng.
12. Có ảnh ra: ghi một dòng `system/LEARNINGS.md` nêu chìa và phép đã dùng, rồi sửa bảng trạng thái ở `14` §11.
