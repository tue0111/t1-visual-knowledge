# 03 — WORKFLOW: từ ý tưởng đến ảnh đúng

## Bước 1 — Hiểu brief (≤ 1 phút)
Đọc yêu cầu và ảnh tham chiếu nếu có. Chỉ hỏi lại khi thiếu thứ làm đổi hẳn bức ảnh: chủ thể là ai, ảnh dùng để làm gì, tỷ lệ khung. Còn lại tự chọn phương án hợp gu T1 và ghi giả định trong bảng quyết định.

Có ảnh tham chiếu thì tách hai phần:
- **Phần giữ:** cái làm ảnh mẫu đáng chép. Thường là quan hệ không gian (mặt lộ ra từ đâu, tiền cảnh che phía nào, chỗ cắt khung), không phải danh từ trang trí.
- **Phần bỏ:** chữ và logo trong mẫu, các chi tiết ngẫu nhiên.

Brief có phong cách, nhiều ảnh tham chiếu, nhiều người hay cần ảnh thật kiểu candid thì đọc mục tương ứng trong `05_CRAFT.md` trước khi viết.

## Bước 2 — Bảng quyết định (luôn viết ra, 6 dòng)
```
CHẾ ĐỘ: poster / cinema / candid / siêu thực  ·  XEM: <1s / vài giây / lâu
ĐỌC: đầu tiên ___ → sau đó ___ → cuối ___
TRỤC CHÍNH: K_ (vì ___)
TRỤC PHỤ: K_, K_ (phục vụ chính bằng ___)
CHẶN: attractor ___ ở trục ___
Ý ĐỒ VÙNG TỐI: ___ phải đọc được / ___ được phép chìm
```

## Bước 2b — Đối chứng VSC (khi có quyền gọi Vibeshot)

Mục đích: lấy kinh nghiệm cộng đồng để soi bản nháp của Tuệ, không thay nó.

1. **Tìm theo brief, không theo kho.** Từ bảng quyết định lấy 2–4 cụm then chốt (trục chính, thiết bị/film, ánh sáng, chất liệu). Gọi `vsc_search` (lexicon, kèm gallery nếu cần cách viết cụ thể), từ khoá Trung + Anh. Mỗi brief tối đa 3 lượt search, chỉ trang 1.
2. **Đưa 3–5 lựa chọn** cho Tuệ: tên style, id, một dòng vì sao hợp brief. Không tự lấy detail hết.
3. **Lấy detail đúng cái được chọn** (thường 1–3, tối đa 5 mỗi brief). Gallery prompt thì ghi tên tác giả.
4. **Bảng đối chứng** (tiếng Việt, ≤ 8 dòng):
   | Hạng mục | Bản Tuệ | VSC | Kết luận |
   |---|---|---|---|
   Hạng mục cố định: thiết bị/quang học · ánh sáng (nguồn, hướng, bóng) · màu và hạt · chất liệu · attractor/negative · cụm dễ kéo chữ.
   Kết luận chỉ có 3 loại: **giữ** (bản Tuệ đã đủ) · **bổ sung** (thêm cụm VSC, ghi nguyên văn cụm) · **bỏ** (cụm VSC trái luật T1 hoặc trái brief, ghi lý do).
5. **Khối bổ sung** dán được: 1 dòng keyword 中文 nối bằng `+`, và 1 dòng `负面` bổ sung. Đây là thứ đưa sang người viết prompt chính (Grok bot hoặc agent).
6. **Không sửa thẳng prompt của Tuệ** trừ khi được yêu cầu. Đưa bảng + khối bổ sung, Tuệ quyết.

Luật lọc khi bổ sung: bỏ mọi cụm kéo chữ (timestamp, logo, signage, UI, label) → chặn bằng `文字、标志`, dấu ngày/OSD làm hậu kỳ · tách thiết bị / quang học / ánh sáng thành cụm riêng · không tên hoạ sĩ, nhiếp ảnh gia còn sống · không tính từ rỗng đứng một mình.

## Bước 3 — Viết 3 phần
1. **母版锁:** những gì ổn định qua mọi shot: chế độ và quan hệ với người xem, danh tính, chất liệu và vai màu, luật thế giới, ngôn ngữ ánh sáng chung, khối brand, câu "chỉ một ảnh".
2. **分镜:**
   - Câu tỷ lệ khung và máy (vị trí, độ cao, khoảng cách, cỡ cảnh).
   - Trục chính: 2–4 câu, có bằng chứng ở chủ thể **và** ở môi trường, có mức sàn.
   - Trục phụ: mỗi trục một câu, có một bằng chứng.
   - Một câu chặn attractor nếu cần.
   - Giữ thứ tự: máy → người, ánh nhìn, động tác → vật → nền → ánh sáng → màu và chất liệu → không khí. Nhấn trục chính bằng **số quyết định**, không bằng vị trí câu.
3. **通用负面提示词:** chỉ chặn có mục tiêu (lỗi thật của trục chính, giải phẫu, chữ), rồi câu ngoại lệ brand nguyên văn. Không xả danh sách 30 thứ cấm.

## Bước 4 — Tự soát (bắt buộc, trước khi giao)
- [ ] Che bảng quyết định đi, chỉ đọc 分镜: đoán ra trục chính không?
- [ ] Trục chính có bằng chứng ở chủ thể **và** môi trường, có mức sàn?
- [ ] Ánh nhìn có đích? Tay có điểm cầm?
- [ ] Máy có điểm tham chiếu thế giới? Nếu cảnh có cầu, đường hay hành lang, hình học có loại trừ được chỗ đứng sai không?
- [ ] [giả thuyết] Điểm đọc đầu tiên có đúng anchor của brief, kể cả khi đó là vật hoặc khoảng trống chứ không phải mặt? Thu về cỡ hiển thị cuối để kiểm; phóng lớn không thay kiểm thumbnail.

- [ ] Ý đồ vùng tối đã ghi rõ?
- [ ] Có cụm tính từ rỗng không? (高品质, 大师作品, 8K, 氛围感, 电影感 đứng một mình) Có thì xoá hoặc thay bằng bằng chứng.
- [ ] Có mâu thuẫn không? (dương và âm; phong cách với phong cách; dấu vết sinh ra chữ trong khi brand cấm chữ)
- [ ] Đủ luật cứng: tiếng Trung, 3 phần, brand nguyên văn, một shot một ảnh.

## Bước 5 — Giao
Bảng quyết định → 3 khối code → tối đa 3 dòng "nhìn gì khi ra ảnh" (các rủi ro attractor).

---

## Vòng sửa — khi ảnh ra lỗi
Xem thêm `05_CRAFT.md` §8 (thang sửa theo tầng, kiểm da nhựa, khuôn quen).

1. **Gọi tên lỗi bằng thứ nhìn thấy**, đừng dùng "chưa đẹp". Ví dụ: "máy đứng trên mặt cầu", "nhân vật nhìn ống kính", "da bóng nhựa".
2. **Xác định trục và loại lỗi:**
   - **Thiếu chữ:** prompt không nói gì về chỗ đó → thêm câu có bằng chứng.
   - **Chữ mơ hồ:** có nói nhưng là nhãn hoặc tính từ → đổi sang kết quả nhìn thấy.
   - **Mâu thuẫn:** hai câu kéo hai hướng → bỏ một câu.
   - **Model kéo về khuôn quen:** đã viết rõ mà vẫn lệch → đổi hình học hoặc bằng chứng khiến khuôn quen trở thành bất khả. Đừng lặp lại lệnh hay chỉ thêm câu phủ định.
3. **Sửa tối thiểu:** đổi 1–2 câu, không viết lại toàn prompt. Lỗi nhận dạng một chi tiết thì sửa đúng dấu nhận dạng đó (màu, viền, cấu trúc).
4. **Sinh lại 2–4 ảnh** rồi nhìn. Một ảnh đẹp chỉ chứng minh là có khả năng, chưa chứng minh ổn định.
5. **Ghi LEARNINGS** nếu bài học dùng lại được (mẫu ở cuối `LEARNINGS.md`).

## Bước 6 — Học sau khi có ảnh

Sau khi gen (2–4 ảnh mỗi bản):
1. So **bản có bổ sung VSC** với **bản gốc của Tuệ** nếu có cả hai. Không có thì chỉ nhìn bản đã gen.
2. Ghi một dòng `LEARNINGS.md`: generator, cụm VSC nào, tác dụng thấy được trên bao nhiêu/bao nhiêu ảnh, giữ hay bỏ.
3. Style đã dùng thật thì ghi vào `07_VSC_LEXICON.md` đúng lineage của nó, theo format F12, đổi nhãn từ [giả thuyết] sang [đã thấy · ngày · generator] cho phần đã kiểm.
4. Bài học lặp ≥ 3 brief khác nhau → chuyển vào `02_KNOWLEDGE.md` như luật cũ.

## Album / series
- Một 母版锁 chung, mỗi shot một 分镜, một negative chung.
- Mỗi ảnh đổi ≥ 2 trong 4 biến: khoảng cách, góc máy, hành động, chủ tiêu điểm. Nếu không, cả series thành một ảnh lặp lại.
- Ghi rõ trong 母版锁 những biến nào được phép đổi.

## Chế độ nhanh
Người dùng chỉ cần thăm dò ý tưởng: viết một prompt nén (vài khái niệm dày nghĩa, mỗi cái một việc + chủ thể + luật cứng; xem `05_CRAFT.md` §1.6a). Muốn tìm hướng mới thì sinh nhiều tổ hợp theo §1.6b. Khi ra ảnh ưng, giải mã cái gì làm nó đẹp rồi khoá lại bằng bảng quyết định.
