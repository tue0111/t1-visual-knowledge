# K4 — MÀU

status: v0.1 CANDIDATE · author: Claude · date: 2026-10-02
Nhãn: [VẬT LÝ/TRI GIÁC] có nghiên cứu · [THỰC HÀNH] quy ước nghề · [GIẢ THUYẾT-AI] cách model phản ứng, cần test.
Liên quan: `K1_LIGHT.md` §2.5 (nhiệt màu), `K3_COMPOSITION.md` (điểm vào), `K6_ATMOSPHERE.md` (màu theo khoảng cách).

---

## 0. Câu lõi

**Độ sáng (value) dựng hình khối và đường đọc; sắc độ (hue) dán nghĩa và cảm xúc lên trên.** Ảnh đọc được ở bản đen trắng thì màu chỉ cần chọn đúng; ảnh không đọc được ở đen trắng thì màu nào cũng không cứu được.

## 1. Thẻ màu 5 câu

1. **Bảng giá trị:** chủ thể sáng trên nền tối, tối trên nền sáng, hay cùng tông (low-key / high-key / trung)?
2. **Màu chủ đạo:** 1 họ màu chiếm phần lớn khung là gì?
3. **Màu nhấn:** có 1 màu nhỏ, khác họ, nằm ở chủ thể không? (≤ 1–2 điểm)
4. **Màu do ánh sáng:** nguồn sáng ấm/lạnh nào, bóng nhận màu gì (trời, phản xạ)?
5. **Độ bão hoà theo vùng:** chỗ nào đậm nhất, chỗ nào nhạt (bóng, xa, sương)?

## 2. Cơ chế

### 2.1 Độ sáng gánh cấu trúc [TRI GIÁC]
- Đường thần kinh xử lý độ sáng "mù màu" và gánh chiều sâu, khối 3D, vị trí, chuyển động. Hai màu khác sắc nhưng cùng độ sáng (equiluminant) thì hình "rung", vị trí mơ hồ, khối phẳng — ví dụ mặt trời trong *Impression, Sunrise* của Monet (Livingstone).
- Trong tìm kiếm thị giác ở vùng ngoại vi, tương phản độ sáng dẫn mắt hiệu quả hơn tương phản màu; màu giúp chủ yếu khi đi kèm chênh sáng (Cajar & Laubrock 2026).
- **Test đen trắng:** chuyển ảnh sang xám; chủ thể còn nổi, khối còn tròn → cấu trúc ổn.

### 2.2 Bão hoà làm "sáng giả" [TRI GIÁC]
Hiệu ứng Helmholtz–Kohlrausch: ở cùng độ sáng đo được, màu bão hoà trông sáng hơn màu xám/trắng; mạnh nhất với đỏ, hồng, xanh dương, yếu với vàng/xanh lá, mạnh hơn trong cảnh tối. Hệ quả: tăng bão hoà một vùng = tăng độ "kéo mắt" của nó, có thể phá bảng giá trị và cướp điểm vào (K3).

### 2.3 Màu đổi theo hàng xóm [TRI GIÁC]
Tương phản đồng thời (Chevreul): một màu đổi sắc và độ sáng biểu kiến theo màu bên cạnh. Cùng một màu da trông hồng hơn trên nền xanh, vàng hơn trên nền tím. Màu trong prompt không phải tuyệt đối; nó luôn được đọc trong quan hệ.

### 2.4 Ánh sáng quyết định màu bóng [VẬT LÝ]
- Nhiệt màu (Wikipedia): nến ~1850K, đèn sợi đốt ~2400–2550K (đèn phim chuẩn 3200K), ban ngày 5500–6000K, trời đục ~6500K, trời xanh trong 15000K+.
- Vùng bóng ngoài trời nắng được trời xanh chiếu → bóng **lạnh** so với vùng nắng ấm. Đây là cơ sở vật lý của "sáng ấm / bóng lạnh"; không phải phong cách tuỳ ý.
- Càng xa, màu càng nhạt, kém tương phản và ngả về màu trời (xem K6).
- Nhiều nguồn khác nhiệt màu cùng lúc → chênh màu nhìn thấy; cân bằng trắng chọn nguồn nào trông "trung tính".

### 2.5 Hoà sắc: phần lớn là quy ước [THỰC HÀNH, bằng chứng yếu]
- Nghiên cứu thích cặp màu (Schloss & Palmer): người ta thích cặp **cùng họ sắc** hơn; nhưng hai màu gần như trùng thì "chỏi", cần chênh sáng/bão hoà rõ. Thích **nền lớn tối hơn, xanh hơn + hình nhỏ sáng hơn, vàng hơn**. Sở thích màu đơn lẻ giải thích tốt bởi đồ vật gắn với màu đó (mô hình "ecological valence", ~80% phương sai theo các nguồn — cần kiểm lại số chính xác trong bài gốc PNAS 2010).
- Teal/orange: da nằm vùng cam, teal là bổ túc → người nổi khỏi nền; lan rộng khi grade số (DI) phổ biến — DI phổ biến từ *O Brother, Where Art Thou?* (2000, grade ngả sepia, không phải teal/orange) — và bị chê lạm dụng.
- **Không tìm thấy** nghiên cứu có kiểm soát chứng minh bảng bổ túc / tương đồng / đơn sắc trong phim làm người xem hiểu hay cảm tốt hơn. Coi là công cụ nghề.

### 2.6 Màu nhấn và chú ý [TRI GIÁC, phụ thuộc cảnh]
Màu làm thay đổi chỗ người xem nhìn vượt ngoài dự đoán theo độ sáng, nhưng mức độ phụ thuộc loại ảnh: tương phản đỏ-xanh lá kéo mắt mạnh trong cảnh rừng, không tác dụng trong ảnh fractal (Frey, Honey & König 2008). Màu nhấn hiệu quả nhất khi **đi kèm chênh sáng**.

### 2.7 Da [THỰC HÀNH]
Da có sắc độ khá ổn định (dải cam hẹp trên vectorscope, dung sai ~10°). Grade cảnh nhưng giữ da khỏi lệch cam/xanh lá/xám. "Bóng trên da giữ ấm, không xám/xanh" là quy ước colorist, chưa có nguồn nghiên cứu.

## 3. Theo chế độ ảnh
| | Poster | Cinema | Candid |
|---|---|---|---|
| Bảng giá trị | rõ, chủ thể tách nền | có vùng chìm thật sự | theo ánh sáng thật |
| Chủ đạo | trang phục dịch từ bảng màu sinh vật/chủ đề; nền màu bổ túc (notes §1) | giới hạn 2–3 họ, grade có chủ ý | màu đời thường, không đồng bộ |
| Nhấn | 1 màu mạnh ở chủ thể | màu nhấn có lý do trong thế giới (đèn lồng, áo) | ngẫu nhiên |
| Bão hoà | cao nhưng có cấp | thấp/vừa, cao chỉ ở điểm nhấn | tự nhiên |

## 4. Attractor [GIẢ THUYẾT-AI + bằng chứng]
| # | Attractor | Bằng chứng | Chặn thử |
|---|---|---|---|
| M-A1 | Quá bão hoà, màu "không tự nhiên" | **Có nghiên cứu**: guidance (CFG) cao làm ảnh bão hoà, phi tự nhiên (Imagen, Saharia 2022; arxiv 2410.02416) | ghi bão hoà theo vùng; với generator có tham số, hạ guidance |
| M-A2 | Độ sáng trung bình, thiếu ảnh rất tối / rất sáng | **Có nghiên cứu**: lịch nhiễu của SD giới hạn ở độ sáng trung bình (Lin et al. WACV 2024) | low-key/high-key phải ghi rõ bằng kết quả: 画面大部分处于暗部 |
| M-A3 | Da sáp, bóng nhựa, "bóng loáng" | **Có nghiên cứu** (phân loại Kamali et al. CHI 2025) + hướng dẫn Kellogg (heuristic) | xem K5 |
| M-A4 | Teal-orange mặc định, HDR phẳng | **chưa có nguồn**, chỉ quan sát | ghi bảng màu cụ thể + "阴影保持深暗" |
| M-A5 | Đĩa đỏ / mặt trời đỏ | casebook 10/60 | notes §4 |

## 5. Cách viết (tiếng Trung, có mức sàn)
Công thức: **bảng giá trị + màu chủ đạo (vật mang) + màu nhấn (vị trí) + màu do ánh sáng + bão hoà theo vùng + mức sàn**.

- 整体为低调画面，大部分处于深暗的靛蓝阴影中，唯一的暖橙色来自人物手中的灯笼，照亮她的脸和袖口；肤色保持自然暖调，不偏灰不偏绿。
- 人物服装取自海蛇的配色：珊瑚粉与象牙白，背景为大片平整的青绿色天空，饱和度低于服装，人物面部为画面最亮处。
- 午后阳光为暖色，阴影受天空照射呈冷蓝色，远山颜色变浅、偏蓝、对比降低。

Quy tắc:
1. Gắn màu vào **vật mang** (áo, đèn, trời), không ghi màu trôi nổi ("色调温暖").
2. Màu nhấn ≤ 2, ghi vị trí và ghi nó nằm ở chủ thể.
3. Ghi bảng giá trị bằng kết quả ("大部分处于暗部", "面部为最亮处") — sửa M-A2.
4. Màu bóng ghi theo nguồn chiếu bóng (天空 → 冷蓝), không ghi tuỳ ý.
5. Bảo vệ da bằng mức sàn: 肤色自然，不偏橙不偏灰.

## 6. Kiểm sau khi ra ảnh
1. Chuyển xám: chủ thể còn nổi? còn khối?
2. Vùng bão hoà cao nhất có trùng chủ thể?
3. Màu bóng khớp nguồn (trời lạnh, phản xạ ấm từ đất/tường)?
4. Xa có nhạt và ngả màu trời?
5. Da: lệch cam/xám/xanh?
6. Số màu nhấn ≤ 2?

## 7. OPEN
- **O1** Ghi bảng giá trị bằng chữ ("低调", "暗部占七成") có thoát được M-A2 trên GPT Image không? Test 6 mẫu.
- **O2** Gắn màu vào vật mang vs ghi tông chung — model nào ổn định hơn?
- **O3** Ghi "饱和度低于服装" có thật sự hạ bão hoà nền?
- **O4** Ghi Kelvin vs ghi tên nguồn sáng (trùng K1 O3).

## Nguồn
- Livingstone, qua Harvard Magazine "The Neurobiology of Art" (2003): https://www.harvardmagazine.com/2003/07/the-neurobiology-of-art-html
- Cajar & Laubrock (2026), Attention, Perception & Psychophysics: https://link.springer.com/article/10.3758/s13414-026-03226-7
- Wikipedia: Helmholtz–Kohlrausch effect; Contrast effect; Color temperature; Aerial perspective; Bleach bypass; Human skin color.
- Palmer Lab (Schloss & Palmer) color preference: https://palmerlab.berkeley.edu/color1.html
- Frey, Honey & König (2008), Journal of Vision: https://jov.arvojournals.org/article.aspx?articleid=2193355
- Saharia et al. (2022) Imagen: https://arxiv.org/html/2205.11487 · arxiv 2410.02416 · Lin et al. (2024) https://arxiv.org/abs/2305.08891
- Kellogg Insight, AI photos identification (heuristic): https://insight.kellogg.northwestern.edu/article/ai-photos-identification
- Vectorscope/skin line: https://bramstout.nl/en/webbooks/vectorscopes/
- Teal/orange critique (blog, 2010): http://theabyssgazes.blogspot.com/2010/03/teal-and-orange-hollywood-please-stop.html
