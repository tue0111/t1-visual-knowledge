# NOTES 2026-10 — Ánh sáng · Poster · Cinema · Attractor

status: CANDIDATE · authority: thấp nhất (dưới examples) · author: Claude (thảo luận với Tuệ) · date: 2026-10-02
Đây là giả thuyết có lý do, chưa qua `core/11_EVIDENCE_AND_PROMOTION_ENGINE.md`. Mỗi luật ứng viên có phản ví dụ và cách test.
Ảnh dùng để thảo luận là ảnh của người khác (voxcat, ảnh mạng) hoặc ảnh GPT của người dùng; **không lưu ảnh**, chỉ lưu phân tích.

---

## §1. Poster / key visual — "Nhìn tao đi"

Bối cảnh: bộ 3 ảnh "nhân vật + Pokémon" giả lập thật (nhân vật chủ đề rắn + rắn biển; nhân vật cầm quạt + cáo chín đuôi; vu nữ tóc trắng + cáo chín đuôi băng).

**OBSERVATION** — cả bộ dùng một công thức: máy sát đất ngửa lên, ống rộng; đầu sinh vật sát ống kính; người cao vút ở trung cảnh; trời xanh ngọc phẳng; nắng cao mềm (high-key).

**MECHANISM — 5 nguồn bắt mắt, không nguồn nào là ánh sáng:**
1. Tương phản tỷ lệ do góc máy (đầu sinh vật khổng lồ + chân người dài ra).
2. Hai ánh nhìn cùng hướng về người xem (người + mắt sinh vật).
3. Hình nền thành hào quang (thân cuộn làm vòm, đuôi xoè nan quạt sau lưng).
4. Màu "họ hàng": trang phục dịch từ bảng màu sinh vật; đặt trên nền màu bổ túc (hồng/san hô ↔ xanh ngọc).
5. Logic ghép cặp có "à ra thế": chung motif (rắn ↔ rắn biển, hồ ly ↔ cửu vĩ hồ); đạo cụ làm cầu nối (trang sức rắn, quạt, màu tóc).

**Giả lập thật:** giữ nguyên silhouette và mảng màu gốc của sinh vật, chỉ thêm chất liệu vi mô (vảy bóng, sợi lông, mắt ướt). Hiện thực hoá cả hình khối → mất nhận diện.

**DECISION_RULE (candidate):**
- R1.1 Ghép nhân vật + sinh vật: chọn cặp theo **motif chung**, rồi cho một đạo cụ/màu mang motif đó lên người.
- R1.2 Trang phục lấy bảng màu sinh vật; nền lấy màu bổ túc.
- R1.3 Quan hệ phải có tiếp xúc / chức năng / ánh nhìn (khớp casebook C05). Đứng cạnh nhau = yếu nhất.

**FAILURE_MODE:** high-key không bóng đổ → sinh vật trông như ghép; lông trắng chìm vào trời; cả series lặp cùng góc máy → thành công thức (attractor).

**TEST_NEEDED:** cùng cặp, A = nắng phẳng, B = ngược sáng + bóng đổ sinh vật phủ lên người; so độ tin tỷ lệ và độ nhận diện.

---

## §2. Cinema — "Mày đang chứng kiến"

**Khác poster:** poster hướng mọi thứ vào người xem; cinema để người xem là kẻ đứng ngoài một khoảnh khắc nằm giữa chuỗi sự kiện.

**Bộ xương (thiếu là không phải cinema dù màu đẹp):**
1. **Khung là khoảnh khắc trong chuỗi** — ảnh phải gợi "vừa xảy ra gì / sắp xảy ra gì" (đi xa, quay lưng, khăn bay, khói, vật đang rơi).
2. **Ánh nhìn & bức tường thứ tư** — nhân vật nhìn ra ngoài khung tạo không gian ngoài màn hình; nhìn thẳng ống kính → thành chân dung tạp chí.
3. **Ánh sáng có nguồn** — mỗi luồng sáng có lý do trong thế giới (cửa sổ, đèn lồng, khói cho tia sáng). Đèn có trong khung mà không thắp = bỏ phí nguồn sáng.
4. **Máy ở trong không gian** — chụp xuyên vật tiền cảnh (lá, xà, cột). Mẹo cinema phổ biến nhất trong ảnh AI.
5. **Cỡ cảnh theo chức năng kể** — cảnh rộng xác lập (người nhỏ, thế giới lớn); góc cao = góc nhìn của ai đó.

**Lớp da (dễ chép, không phải cốt lõi):** tỷ lệ rộng, grade hạn chế màu, hạt film, halation, bokeh. Khung dọc vẫn có thể cinema nếu đủ xương.

**FAILURE_MODE:** chi tiết dày đều và nét căng khắp khung → ra chất phim cắt cảnh game, không ra phim. Phim chọn chỗ nét / chỗ chìm vào tối.

**DECISION_RULE (candidate):**
- R2.1 Test khung 46/48: "nếu đây là khung 47 của một cảnh, khung 46 và 48 là gì?" Không trả lời được → poster.
- R2.2 Brief cinema mặc định cấm nhìn ống kính trừ khi brief nói khác.
- R2.3 Mỗi nguồn sáng trong prompt phải tồn tại vật lý trong cảnh.

---

## §3. Ánh sáng có bằng chứng

Nguồn ngoài: bài "我把摄影里的布光，写成了 AI 能用的短提示词模板" của 南鸢 nuyoah (X, 2026-09-28). Dưới đây là tóm tắt và mở rộng, không chép nguyên bài. Thử nghiệm của tác giả: chân dung studio, 1 người, 1 đèn, mẫu nhỏ — tác giả tự ghi phần chưa kiểm chứng.

**Công thức gốc:** tên kiểu đèn + hướng + **một kết quả nhìn thấy được trên ảnh** (+ nền nếu cần).
Ví dụ: 晴天直射硬光，太阳从左上方照来，鼻影与下巴影边缘清晰。

**Ba ý chính:**
1. Chỉ ghi tên đèn (分割光, 伦勃朗光…) = rút thăm. Thêm hướng + nửa mặt nào tối thì model mới theo.
2. Kết quả mong muốn đi kèm **mức sàn**: 发丝肩缘镀金 + 面部保留细节; 眼窝加深 + 保留五官可辨.
3. Sửa bằng đối chiếu: ra ảnh → tìm đúng kết quả đã ghi → thiếu thì chỉ sửa câu đó.

**Mở rộng cho cảnh rộng (candidate):**
nguồn sáng có thật trong thế giới + hướng + bằng chứng trên chủ thể + **bằng chứng trên môi trường** + mức sàn.
- Poster sinh vật: 午后太阳从人物右后方照来，九尾毛尖透光发亮，巨狐在人物腿部与地面投下清晰阴影，面部保留细节。
- Cinema nội thất: 灯笼点亮，作为画面内唯一暖光源，在栏杆和她的侧脸留下暖色溢光，远处庭院保持冷蓝阴影。

**R3.1 (candidate):** mỗi nguồn sáng một bằng chứng, chọn bằng chứng **khó làm giả nhất**: bóng đổ > hướng highlight > viền sáng > màu. Model hay vẽ viền sáng mà quên bóng đổ, nên ưu tiên ghi bóng.

**OPEN:** tỷ lệ giữa sáng chính và sáng phản (trời, nền, bounce) — bài gốc bỏ trống; đây là thứ quyết định "thật" hay "dựng". Cần nghiên cứu riêng.

---

## §4. Attractor bố cục (model tự kéo về)

| Attractor | Bằng chứng | Chặn thử |
|---|---|---|
| Đĩa đỏ / mặt trời đỏ sau nhân vật | 10/60 ảnh người dùng (casebook) | ghi rõ nền và nguồn sáng; cấm đĩa tròn đỏ trong negative khi không cần |
| Có cầu → máy đứng **trên mặt cầu**, đường dẫn giữa khung | prompt ông lão xe bánh mì (2026-09) ghi "相机站在桥头岸边" nhưng ảnh đặt máy trên cầu, tiền cảnh lan can sai phía | thêm câu cấm vị trí: 相机不在桥面上 |
| Series cùng một góc sát đất ngửa lên | bộ 3 ảnh Pokémon | đổi ≥2/4 trục mỗi ảnh (casebook C01) |
| Nhân vật nhìn thẳng ống kính dù brief cinema | ảnh lầu tuyết (2026-10) | R2.2 |

**R4.1 (candidate):** khi brief có vật thể mạnh về hình học (cầu, cầu thang, đường ray, hành lang), ghi cả vị trí máy **và** câu phủ định vị trí mà model hay chọn.
