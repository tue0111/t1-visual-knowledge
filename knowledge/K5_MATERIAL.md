# K5 — CHẤT LIỆU & BỀ MẶT

status: v0.1 CANDIDATE · author: Claude · date: 2026-10-02
Nhãn: [VẬT LÝ/TRI GIÁC] có nghiên cứu · [THỰC HÀNH] quy ước nghề (CG, texturing) · [GIẢ THUYẾT-AI] cần test.
Liên quan: `K1_LIGHT.md` §2.6 (SSS), `T1_TO_9_VISUAL_PROMPT_OS_v2/core/06_MATERIAL_SYSTEM_ENGINE.md`, `P/families/KERNELS_COUTURE_ENTITY.md`.

---

## 0. Câu lõi

**Người xem không nhìn thấy "chất liệu"; họ suy ra nó từ cách bề mặt trả ánh sáng: điểm sáng to/nhỏ, sắc/mờ, phản chiếu gì, ánh sáng có đi xuyên vào không, và dấu vết thời gian nằm ở đâu.** Viết chất liệu = viết những dấu hiệu đó, không viết tính từ "chân thực, cao cấp".

## 1. Thẻ chất liệu 5 câu (cho mỗi vật quan trọng)

1. **Kim loại hay không kim loại?** (quyết định màu nằm ở phản chiếu hay ở thân)
2. **Nhám hay láng?** → điểm sáng to-mờ hay nhỏ-sắc.
3. **Ánh sáng có xuyên vào không?** (da, ngọc, sáp, lá, lông, vải mỏng)
4. **Nặng hay nhẹ, cứng hay mềm?** (nếp vải, độ võng)
5. **Đã dùng bao lâu?** Dấu mòn, bụi, ướt nằm ở đâu?

## 2. Cơ chế

### 2.1 Phản xạ gương và khuếch tán [VẬT LÝ]
- Phản xạ gương: góc phản xạ = góc tới. Khuếch tán: ánh sáng vào trong vật liệu không kim loại, tán xạ, rồi thoát ra theo mọi hướng (Adobe PBR Guide).
- **Nhám → điểm sáng to, mờ, tối hơn; láng → điểm sáng nhỏ, sáng, sắc, phản chiếu rõ.**
- **Fresnel:** độ phản xạ tăng mạnh ở góc sượt. Vật không kim loại phản xạ ~2–5% khi nhìn thẳng (shader thường dùng 4%); vì vậy mặt bàn, mặt nước, da phản chiếu mạnh ở rìa / khi nhìn xiên.
- **Kim loại:** phản xạ 50–100%, **không có màu khuếch tán**; màu kim loại nằm trong phản chiếu (vàng = phản chiếu vàng). Không kim loại giữ màu thân của nó.

### 2.2 Tri giác chất liệu [TRI GIÁC]
- Tri giác chất liệu là bài toán suy luận: não phải tách chất liệu khỏi hình dạng và ánh sáng; điểm sáng và phản chiếu là manh mối chính của độ bóng (Fleming 2017).
- **Điểm sáng phải khớp hình khối.** Điểm sáng xoay lệch so với bóng đổ của khối, hoặc nằm trong vùng tối → đọc thành "vết sơn trắng" trên bề mặt mờ, mất cảm giác bóng (Marlow, Kim & Anderson, JoV).
- Người ta đánh giá nhất quán độ bóng, độ trong, độ nhám, độ cứng; mỗi loại chất liệu có "hồ sơ" riêng, nhìn và lời mô tả khớp nhau (Fleming, Wiebel & Gegenfurtner 2013) → mô tả bằng chữ là khả thi.

### 2.3 Trong mờ / tán xạ dưới bề mặt (SSS) [TRI GIÁC]
Dấu hiệu trong mờ (Gigilashvili et al. 2021): mép sáng và mềm; **chỗ mỏng phát sáng** (vành tai, nếp gấp); tương phản thấp, bóng nhạt hơn; **ngược sáng làm tăng mạnh**; có thể in vệt sáng lên bề mặt gần (caustics).
Da, cẩm thạch, ngọc cần SSS mới đúng (Adobe PBR). Lá, sáp, lông theo cùng logic (suy luận, chưa có nguồn riêng).

### 2.4 Ba thang chi tiết [THỰC HÀNH]
- **Macro:** hình khối (nếp áo lớn, đường cong vỏ).
- **Meso:** hoạ tiết thấy được (sợi dệt, vảy, lỗ chân lông, vân gỗ).
- **Micro:** độ nhám — không thấy như hoạ tiết, chỉ thấy qua độ to/mờ của điểm sáng.
Cách chia này là quy ước CG; chưa có bài tri giác dùng đúng ba thang. Hữu ích để kiểm prompt có đủ cả ba không.

### 2.5 Vải [VẬT LÝ + suy luận]
- Độ võng (drape): vải cứng võng ít, vải nặng võng nhiều; còn phụ thuộc độ cứng trượt và chiều dài uốn. → lụa: nhiều nếp nhỏ, chảy; denim: ít nếp, to, cứng; len: ở giữa (phần ánh xạ từng loại là suy luận).
- Người đánh giá cảm giác vải **chính xác hơn khi vải treo/rủ** so với vải trải phẳng; màu và chuyển động giúp đoán độ cứng và khối lượng (Bei Xiao lab).
- Nhung có "sheen": sáng lên ở góc sượt và viền (mô hình velvet/Charlie trong CG). Satin có điểm sáng kéo dài theo hướng sợi (kiến thức CG, chưa có nguồn đã đọc).

### 2.6 Mòn, bụi, tuổi [THỰC HÀNH]
Công cụ texturing đặt bẩn vào **mép và chỗ lõm** (theo bản đồ độ cong), rồi phá đều bằng biến thiên lớn (Adobe Substance "Edge Dirt"). Lý do nó đọc "thật" (suy luận): dấu mòn **khớp hình khối và lịch sử dùng** — giống luật điểm sáng phải khớp khối.
Viết theo cách dùng: tay nắm mòn sáng, góc bàn sứt, bụi đọng trong rãnh, đáy cửa ố nước.

### 2.7 Ướt [TRI GIÁC + VẬT LÝ]
- Bề mặt ướt **tối hơn và bão hoà hơn**; tăng bão hoà kèm đổi độ sáng làm bề mặt trông ướt (Sawayama, Adelson & Nishida 2017).
- Cơ chế: màng nước giữ ánh sáng bằng phản xạ toàn phần → hấp thụ nhiều hơn; nước lấp lỗ rỗng → giảm tán xạ (Lekner & Dorf 1988, trích từ trí nhớ).
- Màng nước làm mặt láng → phản chiếu sắc hơn.

### 2.8 Hoạ tiết cho biết khoảng cách và kích thước [TRI GIÁC + suy luận]
Hoạ tiết càng xa càng nhỏ và dày (gradient hoạ tiết, Gibson). Suy luận: mật độ lỗ chân lông, sợi vải, vảy cho biết cỡ vật — vảy sinh vật to bằng bàn tay nghĩa là sinh vật khổng lồ; vảy li ti đều nghĩa là nhỏ. Dùng để giữ tỷ lệ trong ảnh sinh vật + người.

## 3. Theo chế độ ảnh
- **Poster / giả lập thật:** giữ silhouette và mảng màu gốc, thêm chất liệu vi mô (vảy bóng, sợi lông, mắt ướt) — notes §1. Chất liệu là bằng chứng "có thật", không phải trang trí.
- **Cinema:** chất liệu chỉ nét ở vùng nét; vùng chìm mất chi tiết meso. Bề mặt có dấu vết thời gian.
- **Candid:** chất liệu bình thường, không đánh bóng, có lỗi (nhăn, xơ, bụi).

## 4. Attractor
| # | Attractor | Bằng chứng | Chặn thử |
|---|---|---|---|
| T-A1 | Da sáp, bóng, "nhựa" | **Có nghiên cứu**: Kamali et al. CHI 2025 liệt kê "waxy, glossy, shiny, plastic-like skin" là artifact phong cách | ghi da có lỗ chân lông, điểm sáng nhỏ chỉ ở trán/mũi, phần còn lại mờ; mức sàn 不磨皮 |
| T-A2 | Mọi thứ bóng như nhau | blog (yếu) | chỉ định vật nào láng, vật nào nhám |
| T-A3 | Nét đều mọi thang, mọi khoảng cách | blog (yếu) | chi tiết meso chỉ ở chủ thể / vùng nét |
| T-A4 | Vải không trọng lượng, nếp ngẫu nhiên | blog (yếu), khớp vật lý §2.5 | ghi loại vải + nếp do trọng lực/động tác |
| T-A5 | Phản chiếu lệch, bóng không khớp nguồn | **Có nghiên cứu**: Kamali et al. (vi phạm vật lý) | ghi phản chiếu thấy gì và ở đâu |

## 5. Cách viết (tiếng Trung, có mức sàn)
Công thức: **vật + loại (kim loại/không) + nhám/láng qua điểm sáng + trong mờ nếu có + nặng/nhẹ + dấu vết dùng + mức sàn**.

- 黄铜门把手被手摸得发亮，边缘有细小划痕，凹槽内积着暗色污垢；高光小而锐利，反射出窗户的形状。
- 皮肤保留毛孔与细小纹理，额头和鼻梁有小面积柔和高光，其余区域为哑光；逆光下耳廓透出暖红色；不磨皮，不呈蜡质。
- 厚羊毛斗篷因重量垂坠，只形成几道宽大的褶皱，下摆沾着泥点；海蛇鳞片每片约掌心大小，湿润有光泽，鳞缘反射天空的青色。

Quy tắc:
1. Mỗi chất liệu viết **dấu hiệu ánh sáng** (高光大小/锐利, 透光, 反射什么), không viết "质感高级".
2. Dấu vết tuổi đặt **theo cách dùng** (chỗ tay chạm, chỗ đọng nước).
3. Chỉ định **vật nào láng, vật nào mờ** để chặn T-A2.
4. Ghi cỡ hoạ tiết khi cần giữ tỷ lệ (掌心大小的鳞片).
5. Da luôn có mức sàn chống T-A1.

## 6. Kiểm sau khi ra ảnh
1. Điểm sáng khớp hướng nguồn và khớp khối?
2. Kim loại có màu trong phản chiếu, không có màu thân "sơn"?
3. Da: có lỗ chân lông? có chỗ mờ? vành tai/ngón tay ngược sáng có ửng?
4. Vải: nếp hợp trọng lượng và động tác?
5. Dấu mòn ở mép, chỗ tay chạm, chỗ lõm — hay rải đều?
6. Ướt: tối hơn, bão hoà hơn, phản chiếu sắc?

## 7. OPEN
- **O1** "不磨皮 + 毛孔" có giảm T-A1 trên GPT Image không, hay làm da thô quá?
- **O2** Ghi cỡ vảy/lông (掌心大小) có giúp giữ tỷ lệ sinh vật khổng lồ?
- **O3** Ghi "哑光" cho vật phụ có làm ảnh bớt bóng loáng tổng thể?
- **O4** Dấu mòn theo cách dùng vs "旧的, 有使用痕迹" — khác nhau rõ không?

## Nguồn
- Adobe, The PBR Guide part 1: https://www.adobe.com/learn/substance-3d-designer/web/the-pbr-guide-part-1
- Wikipedia: Schlick's approximation; Texture gradient.
- Fleming (2017), Annual Review of Vision Science: https://www.annualreviews.org/content/journals/10.1146/annurev-vision-102016-061429
- Marlow, Kim & Anderson, JoV: https://jov.arvojournals.org/article.aspx?articleid=2121157
- Fleming, Wiebel & Gegenfurtner (2013), JoV: https://jov.arvojournals.org/article.aspx?articleid=2194004
- Gigilashvili et al. (2021) translucency review: https://pdfs.semanticscholar.org/0150/00e641bc4d7bfe20b4dc8d64aa1b606c0c0b.pdf
- Drapability (ScienceDirect topics): https://www.sciencedirect.com/topics/engineering/drapability · Bei Xiao lab: https://sites.google.com/site/beixiao/perception-of-material-properties
- Narkowicz, Cloth Shading: https://knarkowicz.wordpress.com/2018/01/04/cloth-shading/
- Adobe Substance Edge Dirt node docs.
- Sawayama, Adelson & Nishida (2017), JoV: https://jov.arvojournals.org/article.aspx?articleid=2627514
- Lekner & Dorf (1988) "Why some things are darker when wet" (trang bị chặn; trích từ trí nhớ).
- Kamali et al. (CHI 2025): https://arxiv.org/html/2502.11989v1
