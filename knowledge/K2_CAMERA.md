# K2 — MÁY ẢNH (vị trí · độ cao · ống kính · cỡ cảnh · độ nét)

status: v0.1 CANDIDATE · author: Claude · date: 2026-10-02
Nhãn: [VẬT LÝ] đúng với mọi máy · [THỰC HÀNH] quy ước nghề · [GIẢ THUYẾT-AI] cách model ảnh phản ứng, cần test.
Liên quan: `K1_LIGHT.md` (ánh sáng), `notes/2026-10_LIGHT_POSTER_CINEMA.md` §2 (cinema) và §4 (attractor).

---

## 0. Câu lõi

**Máy ảnh = một điểm đứng trong không gian + một hướng nhìn + một khung cắt.** Viết prompt ảnh là chọn ba thứ đó; ống kính chỉ là cái khung cắt (và độ nét), không phải "độ méo".
Model ảnh không có máy thật. Nó đoán ba thứ này từ chữ. Chữ nào mơ hồ → model kéo về vị trí quen (attractor). Vì vậy phần lớn lỗi "sai máy" là lỗi **thiếu vị trí máy**, không phải thiếu tên ống kính.

## 1. Thẻ máy 5 câu (điền trước khi viết cảnh)

1. **Máy đứng ở đâu** trong thế giới (bờ, đầu cầu, sau cột, trong xe)? Có vật nào giữa máy và chủ thể?
2. **Cao bao nhiêu** so với chủ thể (ngang mắt / ngang ngực / sát đất / trên cao nhìn xuống)?
3. **Cách chủ thể bao xa** (gần, trung, xa)? — đây là biến quyết định "méo" và "nén".
4. **Khung cắt thế nào** (cỡ cảnh: thấy tới đâu của người, bao nhiêu thế giới)?
5. **Cái gì nét, cái gì chìm** (một mặt phẳng nét hay cả cảnh nét)?

Câu 1 và 3 là hai câu AI hay bỏ. Câu 1 bỏ → máy trôi lên mặt cầu/giữa đường. Câu 3 bỏ → ra khoảng cách "chụp sản phẩm" trung tính.

## 2. Vật lý [VẬT LÝ]

### 2.1 Khoảng cách quyết định phối cảnh, tiêu cự quyết định khung cắt
- Phối cảnh (vật gần to hơn vật xa bao nhiêu) chỉ phụ thuộc **vị trí máy**. Chụp cùng một chỗ bằng 16mm và 200mm rồi cắt ảnh 16mm cho vừa khung thì được ảnh gần như y hệt ảnh 200mm (PetaPixel, Fstoppers; Wikipedia "Perspective distortion").
- Cái gọi là "ống tele nén cảnh" thực ra là **đứng xa** (nên mới cần tele để lấp khung). "Ống rộng làm méo mặt" thực ra là **đứng sát** (mũi to hơn tai vì mũi gần máy hơn).
- Hệ quả viết prompt: muốn "nền như dựa sát vào người, núi to sau lưng" → ghi **máy xa, khung hẹp**. Muốn "mũi/tay/đầu sinh vật phóng lớn so với phần còn lại" → ghi **máy sát vật gần, nền loãng ra xa**. Chỉ ghi "85mm" hay "14mm" mà không ghi khoảng cách là bỏ ngỏ nửa nghĩa.
- Tỷ lệ gần/xa: vật cách máy 1 m so với vật cách máy 3 m → vật gần to gấp ~3 lần (cùng kích thước thật). Cách 5 m và 7 m → chỉ ~1.4 lần. Càng xa, mọi thứ càng "phẳng" tương đối.

### 2.2 Tiêu cự = góc nhìn (full-frame, tham khảo)
| Tiêu cự | Góc ngang | Cảm giác thường dùng |
|---|---|---|
| 14–24 mm | rất rộng | không gian lớn, đường hội tụ mạnh; sát người thì méo tỷ lệ |
| 28–35 mm | rộng | phóng sự, "máy ở trong cảnh", người + môi trường |
| 50 mm | gần mắt | trung tính |
| 85–135 mm | hẹp | chân dung, tách chủ thể, nền gom lại |
| 200 mm+ | rất hẹp | quan sát từ xa, lớp chồng lên nhau, nền phẳng |

Con số tiêu cự chỉ có nghĩa kèm kích thước cảm biến; model ảnh coi chúng là **nhãn phong cách** hơn là phép đo [GIẢ THUYẾT-AI]. Nên dịch sang **kết quả nhìn thấy** (xem §6).

### 2.3 Độ cao máy → hướng đường chân trời [VẬT LÝ]
- Đường chân trời luôn nằm **ngang tầm mắt máy**. Máy cao 1.6 m thì chân trời cắt người đứng ở khoảng ngang mắt; máy sát đất thì chân trời xuống thấp, trời chiếm phần lớn khung; máy trên cao thì chân trời lên cao, mặt đất chiếm khung.
- Mọi đường song song (đường ray, lan can, mép cầu) hội tụ về điểm tụ **trên đường chân trời**. Máy nghiêng lên/xuống làm đường thẳng đứng nghiêng hội tụ (nhà "đổ").
- Hệ quả: nói "máy thấp" mà ảnh vẫn thấy đường chân trời giữa khung = mâu thuẫn; sửa bằng việc ghi nửa dưới khung là gì (mặt đường, cỏ) và nửa trên (trời).

### 2.4 Độ sâu trường ảnh (DoF) và bokeh
- DoF nông hơn khi: khẩu độ mở lớn (f nhỏ), **máy sát chủ thể**, cảm biến lớn, tiêu cự dài *ở cùng khoảng cách*. Nếu đổi tiêu cự mà lùi/tiến để giữ chủ thể cùng cỡ thì DoF gần như bằng nhau (Photography Life).
- Nền nhoè đẹp cần **khoảng cách giữa chủ thể và nền** lớn. Chủ thể sát tường thì nền khó nhoè dù f/1.4.
- Nền nhoè ≠ chủ thể nét đều: vật ở cùng khoảng cách với mặt phẳng nét cũng nét; vật quá gần máy cũng nhoè (tiền cảnh nhoè là dấu hiệu "máy ở trong không gian").

### 2.4b Cỡ cảnh (shot scale) [THỰC HÀNH]
Chuỗi từ gần đến xa: cận đặc tả (ECU) → cận mặt (CU) → cận ngực (MCU) → nửa người (MS) → từ đùi (cowboy) → từ gối (MWS) → toàn thân (FS) → cảnh rộng (WS) → cực rộng (EWS, người nhỏ như điểm) (StudioBinder).
Chức năng kể chuyện (quy ước nghề, không phải luật):
- EWS/WS: xác lập địa điểm, cô độc, quy mô.
- FS/MWS: hành động và tư thế, người trong không gian.
- MS: hội thoại, quan hệ, đạo cụ trong tay.
- CU/ECU: cảm xúc, chi tiết có ý nghĩa.
Quy tắc dùng: **cỡ cảnh chọn theo "người xem cần biết gì ở khung này"**, không chọn theo "đẹp".

## 3. Góc máy và nghĩa cảm xúc [THỰC HÀNH]
- Thấp (nhìn lên): thế mạnh, uy quyền, to lớn; trời vào khung nhiều.
- Ngang mắt: trung tính, bình đẳng.
- Cao (nhìn xuống): nhỏ bé, bị quan sát, mất ưu thế; thấy mặt đất, bố cục hoạ tiết.
- Từ trên thẳng xuống: sơ đồ, tính toán, quy mô.
- Nghiêng khung (Dutch): bất ổn, mất phương hướng — dùng ít.
- POV / qua vai: nhập vai, quan hệ giữa hai người.
Đây là **ngữ pháp điện ảnh**; mỗi ảnh nên chọn góc theo ý, và series nhiều ảnh phải đổi góc (xem attractor A2).

## 4. Poster và cinema khác nhau ở máy thế nào
| | Poster / key visual | Cinema |
|---|---|---|
| Máy | sát, thường thấp, ống rộng, chủ thể nhìn ống kính | **trong không gian**, có vật tiền cảnh che một phần |
| Khoảng cách | gần để phóng đại tỷ lệ | xa hơn hoặc trung, cỡ cảnh theo chức năng |
| Nét | chủ thể nét, nền nhoè mềm hoặc hào quang | nét có chọn lọc, vùng tối chìm |
| Mục đích | "nhìn tao đi" | "mày đang chứng kiến" |
Chi tiết khung 47/46/48 ở notes §2.

## 5. Attractor của model (hay kéo về) [GIẢ THUYẾT-AI]
| # | Attractor | Bằng chứng | Chặn thử |
|---|---|---|---|
| A1 | Có cầu/đường/hành lang → máy đứng **trên chính vật đó**, đường dẫn thẳng giữa khung | ông lão xe bánh mì (2026-09): ghi "bờ đầu cầu", ra máy trên mặt cầu, lan can sai phía. **W2 (2026-10-03): prompt P3 có cả câu vị trí khẳng định (河岸人行道) lẫn 相机不在桥面上 → cả 3 ảnh máy vẫn ở trên dốc/lòng đường cầu** (`notes/2026-10-03_W2_TEST_RESULT.md`) | câu phủ định **chưa đủ** (bằng chứng chống). Thử tiếp: mô tả hình học khẳng định mạnh hơn — máy ở bờ đối diện / dưới thấp nhìn lên, cầu nằm ở nửa trên khung, người đi trên cầu nhỏ trong khung; hoặc bỏ cây cầu khỏi vùng dưới khung |
| A2 | Series cùng một góc sát đất ngửa lên | bộ 3 ảnh Pokémon | casebook C01: đổi ≥2/4 trục mỗi ảnh (khoảng cách, góc máy, hành động, chủ tiêu điểm); về máy riêng: đổi độ cao, khoảng cách, hướng hoặc cỡ cảnh |
| A3 | Chủ thể luôn căn giữa, đối xứng | quan sát chung, chưa có số liệu | chỉ định chủ thể lệch + hướng nhìn có không gian phía trước |
| A4 | Ống rộng sát mặt → méo tỷ lệ mặt/tay | quan sát chung | tăng khoảng cách và dùng khung hẹp, hoặc nói rõ phần gần máy chỉ là bàn tay/vật |
| A5 | Nền nhoè đều khắp, "ảnh chân dung" dù brief là cảnh | hay gặp | nêu rõ lớp nào nét (tiền/trung/hậu) |
| A6 | Chủ thể nhìn thẳng ống kính | ảnh lầu tuyết (2026-10) | cinema: 视线落向画外 |
Các dòng A2–A6 là quan sát chưa đếm tần suất; chỉ A1 và A2 có case cụ thể.

## 6. Cách viết (tiếng Trung, có mức sàn)
Công thức: **vị trí máy (điểm tham chiếu) + độ cao + khoảng cách/cỡ cảnh + kết quả nhìn thấy + câu phủ định nếu có attractor + mức sàn**.

Ví dụ ngắn:
- 相机站在河岸一侧，高度与人物腰部齐平，距离约十米，全景构图，人物占画面高度约三分之一，桥身只作为斜线出现在右侧，不出现桥面正中的透视通道。
- 相机贴近地面向上仰拍，距离狐狸头部很近，狐狸鼻吻明显大于人物上半身，人物双腿被拉长但五官比例正常，面部保留细节。
- 相机位于门廊内，前景有一根木柱遮住画面左侧约四分之一，人物在庭院中央，中景，画面中心保持清晰，前景柱子轻微虚化。

Quy tắc:
1. Tiêu cự chỉ ghi khi cần "nhãn phong cách"; bên cạnh luôn ghi kết quả nhìn thấy (đầu to hơn người bao nhiêu, nền có nhiều lớp hay phẳng).
2. Vị trí máy dùng **điểm tham chiếu thế giới** (bờ, cột, cửa), không dùng "ngã ba, ở giữa".
3. Nếu có vật hình học mạnh, ghi **câu phủ định vị trí** (R4.1 notes).
4. Cỡ cảnh ghi kèm **cắt ở đâu của cơ thể** (từ thắt lưng lên) — model hiểu "cắt" tốt hơn "medium shot".
5. Series: bảng 4 trục (độ cao / khoảng cách / hướng / cỡ cảnh) trước khi viết.

## 7. Kiểm sau khi ra ảnh
1. Đường chân trời đúng chỗ so với độ cao máy đã ghi?
2. Máy có thật sự đứng ở điểm tham chiếu (bờ, không phải mặt cầu)?
3. Vật tiền cảnh nằm đúng phía và đúng tỷ lệ che?
4. Khoảng cách đúng: tỷ lệ gần/xa giữa chủ thể và vật nền hợp lý?
5. Mặt/tay gần máy có méo bất thường?
6. Nét/nhoè đúng lớp đã nêu?
7. Series: ≥2/4 trục C01 (khoảng cách, góc máy, hành động, chủ tiêu điểm) đã đổi?

## 8. OPEN — cần test, chưa kết luận
- **O1** Ghi số khoảng cách ("十米") vs ghi cảm giác ("人物占画面三分之一") — cái nào model theo chắc hơn? Test cùng cảnh, 6 mẫu mỗi nhánh.
- **O2** Câu phủ định vị trí máy có giảm A1 không, hay làm model vẽ chính vật bị cấm? (có thể tác dụng ngược) — *W2: 0/3 ảnh thoát A1 khi có câu phủ định; chưa có nhánh đối chứng không phủ định → chưa biết phủ định vô tác dụng hay phản tác dụng. Kế hoạch TASK_01 đợt B01.*
- **O3** Tên ống kính (24mm/85mm) có đổi gì không khi đã có khoảng cách và cỡ cảnh?
- **O4** Hiệu ứng tiền cảnh che (cột, lá): model có đặt đúng phía và tỷ lệ không?
- **O5** Với model chỉ nhận prompt rất dài, câu máy đặt đầu hay cuối thì được tuân thủ tốt hơn?

## Nguồn
- PetaPixel, "Lenses Don't Cause Perspective Distortion and 'Lens Compression'" (2021).
- Fstoppers, "How Lens Compression and Perspective Distortion Work".
- Wikipedia, "Perspective distortion".
- Photography Life, "Understanding Depth of Field".
- StudioBinder, "50+ Types of Camera Shots, Angles, and Techniques".
- Trong repo: casebook C01, notes §2, §4.
