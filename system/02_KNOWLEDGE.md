# 02 — KNOWLEDGE: 8 trục, tra khi cần

Mỗi trục có bốn phần: **Lõi** (một câu), **Hỏi** (các câu phải trả lời, thiếu câu nào model tự điền mặc định), **Viết** (công thức kèm ví dụ tiếng Trung), **Chặn** (attractor: lỗi model hay kéo về, kèm cách chặn).
Mọi câu trục chính kết thúc bằng một **mức sàn**: điều kiện tối thiểu không được hỏng (ví dụ 面部保留细节, 手指自然完整).

---

## K1 — Ánh sáng
**Lõi:** Ánh sáng là một hệ vật lý có nguồn, để lại dấu vết kiểm được (bóng, viền, màu vùng tối, độ chuyển). Mô tả nguồn và dấu vết, không ghi tên hiệu ứng.
**Hỏi:**
1. Nguồn là gì, có thật trong thế giới không?
2. Từ hướng nào, cao hay thấp?
3. To hay nhỏ so với chủ thể, tức mép bóng mềm hay sắc?
4. Vùng tối được nâng bao nhiêu: còn chi tiết, chỉ còn khối, hay đen?
5. Màu của nguồn chính và nguồn phụ?
6. Môi trường đáp lại thế nào: ánh hắt, không khí, độ suy giảm?

**Viết:** `[nguồn có thật]从[hướng]照来，[cứng/mềm + mép bóng]；[trạng thái vùng tối]；[nguồn phụ/màu vùng tối]；[bằng chứng khó giả: bóng đổ/phản chiếu]；[mức sàn]。`
> 桌上烛台是画面内唯一光源，暖橙色光池只照亮面部与双手，在肩部迅速衰减；暗部深沉，仅留轮廓；墙面沉入黑暗；眼中有微小烛火高光。

**Mẹo đã kiểm ngoài thực tế:**
- Ánh sáng xuyên rèm hoặc khe để lại vệt trên mặt, áo **và** tường, mà phía tối vẫn đọc được mắt. Phải có bằng chứng ở môi trường, không chỉ ghi "noir".
- Khi đổi góc máy so với ảnh mẫu, model chép vị trí sáng 2D của mẫu (má trái sáng), làm ánh sáng "đi theo máy". Sửa bằng cách cố định nguồn **trong cảnh**: nguồn ở đâu, bị gì che.
- Số nhiệt màu (3200K) đứng một mình bị bỏ qua hoặc chỉ ra filter vàng. Viết kết quả: "ánh hổ phách ấm trong nhà, ngoài cửa còn chút lạnh hoàng hôn".
- Đèn hắt thì gọi tên **bề mặt hắt** (白色天花板反射的柔光), đừng chỉ ghi tên kỹ thuật "跳闪".
- Gel hai màu thường chỉ bám tóc và mép mặt; giữa mặt vẫn trung tính. Muốn nửa mặt mỗi màu thì phải đặt hai nguồn sát hai bên và nói rõ vùng mặt nhận màu.
- Ánh sáng cực đoan (một mảng nắng nhỏ trên mặt, người đứng đúng ranh sáng–tối, nền sáng hơn người) tạo ảnh có tác giả hơn "ánh sáng đẹp".
- Bloom/泛朦 chỉ ở mép sáng; giữ nét mắt, sống mũi, đường môi.
- **Phân bổ độ sáng thay cho "sáng/tối".** Viết ai nhận sáng, ai lùi vào tối, và hai bên được tách bằng gì:
  - Chủ thể nhận nguồn chính, sáng hơn hẳn môi trường.
  - Nền thiếu sáng. Việc của bóng tối là **lùi**, không phải đen.
  - Mép chủ thể được tách bằng một nguồn sau có thật, hoặc bằng không khí sáng phía sau.
  - Khói và sương là vật mang ánh sáng: tạo chiều sâu, lộ hướng sáng, nhưng không giành chủ thể.
  - Tương phản mạnh là chênh lệch có kiểm soát: highlight không cháy, vùng tối còn một lớp.
- Kiểm A/B nhanh: giữ nguyên độ sáng chủ thể, chỉ đổi độ sáng nền và đèn viền.

**Chặn:**

| Attractor | Cách chặn |
|---|---|
| Golden hour mặc định | ghi thời điểm kèm dấu hiệu: 正午顶光，影子短 / 阴天无明显投影 |
| Viền sáng khắp nơi | chỉ ghi viền khi có nguồn phía sau; negative 无来源的轮廓光 |
| Sáng đều kiểu HDR | ghi trạng thái vùng tối; 不使用HDR |
| Tia sáng thiếu điều kiện | tia cần khe hẹp, hạt trong không khí và nền tối; thiếu thì cấm 体积光光束 |
| Người hoặc vật lơ lửng | bóng đổ + bóng tiếp xúc |
| Bóng lệch hướng | 所有投影方向一致 |

---

## K2 — Máy ảnh
**Lõi:** Máy là một điểm đứng, một hướng nhìn, một khung cắt. Phần lớn lỗi "sai máy" là do thiếu **vị trí** máy, không phải thiếu tên ống kính.
**Hỏi:**
1. Máy đứng ở đâu trong thế giới, có vật gì chắn giữa máy và chủ thể?
2. Cao bao nhiêu so với **tâm vùng cần chụp**?
3. Cách chủ thể bao xa?
4. Khung cắt tới đâu của cơ thể?
5. Lớp nào nét, lớp nào chìm?

**Viết:** `vị trí (điểm tham chiếu thế giới) + độ cao + khoảng cách/cỡ cảnh + kết quả nhìn thấy + mức sàn`
> 相机站在河岸一侧，高度与人物腰部齐平，距离约十米，人物占画面高度约三分之一，桥身只作为斜线出现在右侧。

**Mẹo đã kiểm ngoài thực tế:**
- "Thấp/cao" tính theo tâm vùng chụp, không theo mặt đất. Ảnh giày mà ghi 低机位 thì model ngửa cả người. Ảnh giày thì đặt máy ngang tâm bàn chân.
- "Đổi góc" gồm bốn biến riêng: độ cao, phương vị (trước/sau/ba phần tư), hướng ống (ngang/cúi/ngửa), cỡ cảnh. Ghi từng cái, đừng dùng một nhãn chung.
- Thông số máy (f/1.4, ISO, tên body) không được tính như vật lý. Viết kết quả nhìn thấy trước, số làm phụ.
- Cỡ cảnh ghi bằng chỗ cắt (从腰部以上), model hiểu tốt hơn "中景".
- Cảm xúc mặt không ra thường vì mặt quá nhỏ trong khung. Kéo máy lại gần trước khi tả mắt kỹ hơn.
- 平视 một mình chỉ làm mắt nhìn thẳng. Muốn máy thật sự ngang mặt thì viết 相机与面部中心同高，镜头水平对准鼻梁. Góc máy tính theo **mắt nhân vật**.
- Chồng nhiều thứ khuếch đại méo (flash thẳng + rất gần + máy thấp + ống rộng) làm hỏng tỷ lệ cơ thể. Chỉ chọn một.
- Tỷ lệ khổng lồ cần **thước quen**: người tí hon, mái nhà, cây cầu, lá cờ nhỏ đặt cạnh. Chữ "巨大" không đủ.
- Máy cầm tay, vác vai, chân máy để lại dấu vết khác nhau (nghiêng nhẹ, rung, khung chuẩn). Ghi dấu vết nếu muốn cảm giác đó.
- Nghiêng khung (Dutch) phải có lý do trong cảnh.

**Chặn:**

| Attractor | Cách chặn |
|---|---|
| **Có cầu/đường/hành lang → máy đứng trên chính nó** | câu phủ định 相机不在桥面上 **đã thất bại** (xem LEARNINGS). Dùng hình học khẳng định khiến "trên cầu" là bất khả: chụp ngang vuông góc với cầu từ bờ, cầu chạy ngang khung |
| Series lặp một góc | mỗi ảnh đổi ≥ 2 trong 4 biến: độ cao, khoảng cách, hướng, cỡ cảnh |
| Căn giữa, đối xứng | đặt lệch 1/3 + không gian phía trước hướng nhìn |
| Ống rộng sát mặt gây méo | lùi xa, khung hẹp |
| Nền nhoè đều kiểu chân dung | nói rõ lớp nào nét |

---

## K3 — Bố cục
**Lõi:** Bố cục trả lời câu hỏi mắt đi đâu trước, rồi đi đâu, rồi dừng ở đâu. Nó dựa vào đặc tính nhìn thấy (sáng, tương phản, mặt, hướng nhìn), không phải chữ "构图和谐".
**Hỏi:**
1. Điểm vào ở đâu?
2. Điểm vào có phải chủ thể không?
3. Đường đi của mắt?
4. Chỗ dừng?
5. Chỗ thở?

**Viết:** `điểm vào bằng đặc tính nhìn thấy + đường đi + chỗ dừng + chỗ thở có chức năng + mức sàn`
> 画面第一眼落在人物受光的脸上，视线随她望向画面右侧的灯笼，右侧留出约三分之一的空白，灯笼不抢过人物。

**Mẹo đã kiểm ngoài thực tế:**
- Khoảng trống phải **có chức năng**. Viết "bên trái là căn phòng trống cô đang ngoái nhìn", không viết "trái chừa trắng". Nếu không, khoảng trống chỉ thành bức tường đẹp vô nghĩa.
- Khoảng trống không có nghĩa là trống rỗng: có thể giữ bóng cây hay một cử chỉ, miễn ghi rõ vùng và vật được phép.
- Đừng nói một thông tin bằng nhiều hệ quy chiếu cùng lúc (toạ độ thế giới, trái/phải khung, hướng giữa nhân vật). Chọn **trái/phải theo khung hình**.
- Viết đúng lệch vị trí mà ảnh vẫn bị "chuẩn hoá" về chân dung chính diện giữa khung là do model kéo về khuôn quen. Tăng bằng chứng (vật chắn ở mép, đường chéo có vật mang), đừng chỉ lặp lại lệnh.
- Chống **phân bố đều**: có vùng dày và vùng thở; chi tiết, nhiễu, trang trí phải tập trung ở chỗ chọn.
- **Nền tối ≠ nền yên.** Cành nhỏ, gân lá, đốm sáng dày dù tối vẫn nuốt chủ thể. Ghi cái gì nét (mắt, tay, sự kiện) và cái gì chỉ là mảng.
- Ghi vị trí bằng vùng khung: 头部位于画面右上三分之一. Cắt táo bạo vật tiền cảnh ở mép khung cộng thu nhỏ viễn cảnh là đòn bẩy chống căn giữa.
- Thứ bậc độ rõ: vùng nét chính → mảng lớn chi phối → chi tiết phụ → vùng ít chi tiết. Viết rõ bốn tầng khi cảnh nhiều thứ.
- Mỗi ảnh chỉ một bố cục chính. Hai kiểu bố cục chính (ví dụ hai tấm ghép và một điểm tụ) thì gộp hoặc bỏ một.

**Chặn:**
- Nền chi tiết đều: chỉ định lớp nào chìm.
- Quá nhiều chủ thể phụ: giới hạn số vật mang điểm nhấn.
- Đĩa đỏ hoặc mặt trời đỏ sau nhân vật: 不出现红色圆盘或红日.

---

## K4 — Màu
**Lõi:** Độ sáng (value) dựng khối và đường đọc. Sắc độ dán nghĩa lên trên. Ảnh không đọc được ở đen trắng thì màu nào cũng không cứu được.
**Hỏi:**
1. Bảng giá trị: low-key, high-key hay trung?
2. Màu chủ đạo?
3. Màu nhấn: ≤ 2 điểm, nằm ở chủ thể?
4. Màu do nguồn sáng nào tạo ra?
5. Vùng nào bão hoà nhất?

**Viết:** gắn màu vào **vật mang**, ghi bảng giá trị bằng kết quả.
> 整体为低调画面，大部分处于深暗的靛蓝阴影中，唯一的暖橙色来自人物手中的灯笼；肤色自然，不偏灰不偏绿。

**Mẹo đã kiểm ngoài thực tế:**
- Bảng màu theo vai và tỷ lệ: nền ~45%, vùng sáng phụ ~10%, trọng tâm tối ~10%, da/trung gian ~10%, điểm nhấn ~5%. Cách này cho model biết màu nào chủ đạo, màu nào chỉ điểm xuyết.
- Muốn chủ thể nổi mà giữ chất cảnh: **hạ độ sáng** các vật cạnh tranh, đừng hạ màu cả nền về xám. Nền có thể nhiều cấu trúc nhưng thấp bão hoà.
- Gán màu cho từng vật (vàng cho lá, xanh cho trời, cam cho đèn) thay vì phủ một tông toàn khung.
- Tách bốn lớp khi đọc hoặc viết màu: màu vốn có của vật, ánh sáng hiện trường, phơi sáng, hậu kỳ (mài da, hạt, nén). "Tông xanh" mà không nói lớp nào thì model đoán.
- Giới hạn 3–4 mảng màu chính có tên. Đổi màu cho một ảnh có sẵn thì khoá bố cục, người, máy; chỉ liệt kê đúng các biến màu được đổi.
- Màu phi tự nhiên (rời màu vật) vẫn cần khối sáng tối đúng, nếu không thành phẳng.

**Chặn:**
- Quá bão hoà: ghi bão hoà theo vùng.
- Thiếu cực tối hoặc cực sáng: 画面大部分处于暗部.
- Teal-orange mặc định: ghi bảng màu cụ thể.
- Da lệch màu: 肤色自然.

---

## K5 — Chất liệu
**Lõi:** Người xem suy ra chất liệu từ cách bề mặt trả ánh sáng: điểm sáng to hay nhỏ, sắc hay mờ, phản chiếu gì, ánh sáng có xuyên vào không, mòn ở đâu.
**Hỏi:**
1. Kim loại hay không?
2. Nhám hay láng?
3. Ánh sáng có xuyên vào không?
4. Nặng hay nhẹ?
5. Đã dùng bao lâu, dấu vết nằm đâu?

**Viết:**
> 黄铜门把手被手摸得发亮，边缘有细小划痕，凹槽内积着暗色污垢；高光小而锐利，反射出窗户的形状。

**Da (lỗi số một):**
- "真实皮肤" hay "8K毛孔" khiến model **vừa thêm lỗ chân lông vừa giữ làm mịn**, ra sáp hoặc nhựa.
- Thứ quyết định là **phân bố điểm sáng**: bóng nhỏ chỉ ở trán và sống mũi, phần còn lại mờ; có lông tơ, có vùng hơi hồng.
- Mẫu viết: 皮肤保留毛孔与细小纹理，额头和鼻梁有小面积柔和高光，其余区域为哑光；不磨皮，不呈蜡质。
- Texture da khác grain/noise. Đừng thêm hạt phim để chữa da sáp; có generator còn bẩn hơn khi thêm (chưa kiểm chắc).
- Flash thẳng thì nói flash rơi ở đâu (trán, mũi); flash mạnh không sao, phủ đều mới hỏng.
- Trạng thái vật liệu do **hành vi vừa xảy ra** quyết định: tóc ướt hẳn hay nửa ướt, dính má, nhỏ nước. Mức độ phải hợp vật lý.
- Chất liệu thủ công hoặc phong cách vẽ thì tả **dấu quá trình** (bụi phấn, vệt tay, đường may, nét dao khắc), không ghi nhãn "phong cách phấn".
- Chi tiết cần chỗ đặt và chỗ dừng: mảng lớn nguyên vẹn đọc khối tốt hơn đầy linh kiện nhỏ.

**Chặn:**
- Mọi thứ bóng như nhau: chỉ định vật nào láng, vật nào nhám. Vật matte thì tả dấu chế tác (lỗ rỗng, mép vát, đường nối).
- Vải không trọng lượng: ghi loại vải và nếp do trọng lực hoặc động tác.
- Nét đều ở mọi khoảng cách: chi tiết chỉ ở vùng nét.

---

## K6 — Không khí
**Lõi:** Không khí làm ba việc: tạo chiều sâu (xa thì nhạt), làm ánh sáng hiện hình (tia, quầng), để dấu trên bề mặt (ướt, tuyết, bụi). Thời tiết phải có đủ ba thứ, thiếu một là "dán hiệu ứng".
**Hỏi:**
1. Trong không khí có gì?
2. Thấy xa tới đâu?
3. Ánh sáng lộ ra thế nào?
4. Bề mặt mang dấu gì?
5. Cơ thể phản ứng ra sao?

**Viết:**
> 夜雨，人物身后的霓虹灯逆光照亮斜落的雨丝；湿润的柏油路面变暗，每条倒影都对应画面中的一盏灯。

**Chặn:**
- Sương đều không có chiều sâu: 近处清晰，中景变淡，远景只剩轮廓.
- Mưa mà đất khô: ghi dấu vết bề mặt.
- Trời đục mà bóng sắc: 阴天，无清晰投影.
- Tuyết xám: 积雪洁白保留纹理，阴影呈淡蓝色.
- Bão mà yên ắng: tóc, áo, lá bay cùng một hướng gió.

---

## K7 — Khoảnh khắc, cử chỉ, ánh nhìn
**Lõi:** Ảnh tĩnh mạnh nhất khi là lát cắt của chuyển động: người xem đoán được giây trước và giây sau. Đứng đều hai chân, nhìn ống kính, cười chung chung là đang tạo dáng, không phải đang sống.
**Hỏi:**
1. Giây trước và giây sau là gì?
2. Trọng lượng dồn vào đâu?
3. Tay đang làm gì?
4. Mắt nhìn vào đích nào?
5. Thứ gì đang chuyển động phụ?

**Viết:** `thời điểm + trọng lượng + tay có chức năng + ánh nhìn có đích + chuyển động phụ + mức sàn`
> 她正要推开木门的一瞬间，重心落在前脚，右手按在门板上，左手还提着灯笼，视线落向门缝外的院子；斗篷下摆仍向后飘起；手指自然，五指完整。

**Mẹo đã kiểm ngoài thực tế:**
- **Ánh nhìn luôn có đích**, ghi theo trái/phải của khung: 看着画面左侧的那颗草莓. Đây là cách chặn nhìn ống kính hiệu quả nhất (xem LEARNINGS). Viết câu đích dương trước, câu cấm sau.
- **Biểu cảm phải có lý do:** chuyện vừa xảy ra + cảm xúc + hướng về ai.
  - Cảm xúc kép thì viết: sự kiện + cảm xúc chính/phụ + vì sao che giấu + dấu hiệu lộ ra.
  - Đừng tả từng bộ phận (mày, mắt, miệng) cho cảm xúc mạnh, vì ghép lại sẽ ra mặt kỳ dị.
- Cảnh hai người: dùng câu ngắn khoá số người, ai bên trái, ai bên phải, trang phục đi liền tên, tay nào đưa, tay nào nhận.
- Động tác phản ứng giữa chừng (ngoái lại, khựng, cúi xuống) tốt hơn dáng anh hùng.
- Cầm nắm: ghi điểm cầm và cách đỡ trọng lượng. Vật trao tay thì ghi ai đang giữ phần nào.

**Chặn:**
- Tay dị dạng: ít ngón lộ, cầm vật rõ hình, thêm 手指自然完整.
- Vật xuyên tay: ghi điểm tiếp xúc.
- Người và sinh vật đứng cạnh nhau vô quan hệ: cần ít nhất một trong ba thứ (chạm, chức năng, ánh nhìn chung).

---

## K8 — Thế giới, nền
**Lõi:** Nền là bằng chứng rằng nhân vật sống ở một nơi cụ thể, một thời điểm cụ thể, và đã có chuyện xảy ra ở đó.
**Hỏi:**
1. Loại nơi nào (đọc được trong một liếc)?
2. Ở đâu, thời nào, gọi bằng danh từ có tên?
3. Chuyện gì đã xảy ra, để lại dấu vết gì?
4. Nền làm bối cảnh hay làm hào quang?
5. Có phi lý nào được phép (tối đa một)?

**Viết:**
> 宋代江南书房，直棂窗透入午后光，案上砚台墨迹未干，一卷书摊开压着镇纸；不出现明清家具与现代物品。

**Mẹo đã kiểm ngoài thực tế:**
- Kiểm ba tầng: tiền cảnh có gì, người ở đâu, hậu cảnh có gì. Thiếu tầng nào thì ảnh phẳng.
- **Một vật cốt lõi có người dùng** + 1–2 vết tích hơn mười đạo cụ bày sẵn.
- Thế giới giả tưởng cần logic vận hành: chức năng (lưu trữ, điều phối) phải có hệ vật thể tương ứng, không chỉ logo.
- "中式审美" một mình kéo về khuê phòng cổ. Trung Hoa hiện đại thì ghi danh từ hiện đại cụ thể.
- Đề tài văn hoá dễ lệch (nhân vật thần thoại): ghi cả giải phẫu đúng lẫn các hướng lệch cần tránh.

**Siêu thực:**
- Khoảng 85% thật, 15% phi lý: nơi tin được + chủ thể nhận ra + hành động quen + **một** vật sai cụ thể + người xung quanh bình thản.
- Ghi 唯一的超现实元素, rồi ghi vật mang phi lý tuân vật lý (vết nén, vết nứt, bóng).
- Kiểm cả hai chiều: model **không thêm** phi lý thứ hai, và **không xoá** mất phi lý đích.

**Chặn:**
- Trộn thời đại hoặc vùng: dùng danh từ của đúng một thời và một vùng.
- Chữ hoặc biển hiệu vô nghĩa: tránh biển chữ ở vùng nét. Dấu vết đời thường hay kéo theo chữ (nhãn, giá), nên chọn dấu vết không có chữ.
- Nền kiểu ảnh stock: thêm dấu vết nhân–quả.
- Kiến trúc không đứng được: ghi kết cấu chịu lực.

---

## Hành vi model chung (mọi trục)

- **Tên phong cách hoặc tên nhân vật không thay được lời khai chất liệu.** Muốn ảnh thật phải ghi rõ 真人写实摄影; chỉ ghi tên nhân vật thì model hay trả về anime, CG hoặc minh hoạ.
- **Nói "đúng là A, không phải B"** cho thứ dễ bị hiểu nhầm: "vạch trắng chỉ là đường ngăn hai ảnh, không phải con đường".
- **Thứ tự viết:** ràng buộc cứng trước (số người, trái/phải, ai cầm gì, ai nhìn đâu), rồi sự kiện và bằng chứng, rồi bố cục, cuối cùng phong cách và không khí.
- **Trộn nhiều phong cách:** chia quyền theo kênh (style A giữ màu, style B giữ bố cục), không chồng lên nhau.
- **Token phương tiện kéo cả định dạng:** "contact sheet", "khung máy quay", "REC" có thể sinh ra cả khung UI và chữ. Chỉ dùng khi muốn đúng thứ đó.
- **Ảnh tham chiếu chi tiết có thể kéo theo dáng cứng** của mẫu. Nếu cần dáng sống, giao cho mẫu đúng phần được giữ (giả thuyết).
