# K1 — ÁNH SÁNG

status: KNOWLEDGE v0.1 · 2026-10-02 · author: Claude (nghiên cứu web + tổng hợp repo)
Tầng 1 của lộ trình Kiến thức → Tư duy → Viết prompt trục chính/phụ.

**Nhãn độ tin cậy** gắn ở từng mục:
- **[VẬT LÝ]**: định luật hoặc hiện tượng quang học có nguồn.
- **[THỰC HÀNH]**: heuristic của nhiếp ảnh và điện ảnh, đúng trong đa số trường hợp, không phải luật.
- **[GIẢ THUYẾT-AI]**: quan sát về hành vi của model ảnh, cần test.

**Liên kết repo** (không chép lại ở đây):
- `T1_TO_9_VISUAL_PROMPT_OS_v2/library/11_CAMERA_LIGHT_OPTICS.md`:
  - §3 các trường của quan hệ sáng;
  - §4 công thức studio;
  - mục Eye-life guard và Skin reflection guard (không đánh số);
  - §5 ánh sáng môi trường;
  - §6 không khí;
  - §7 độ nét;
  - §11 heuristic thực hành: dải sáng cứng, ngược sáng "thở", tách chủ thể.
- `core/02_DECISION_WORKFLOW.md` §12 (thứ tự quyết định ánh sáng)
- `notes/2026-10_LIGHT_POSTER_CINEMA.md` §3 (công thức "ánh sáng có bằng chứng")

---

## 0. Một câu cốt lõi

Ánh sáng trong ảnh không phải một "phong cách". Nó là **một hệ vật lý có nguồn**, và hệ đó để lại **dấu vết kiểm được** trên mọi bề mặt: bóng, viền sáng, màu của vùng tối, độ chuyển sáng. Viết prompt ánh sáng là mô tả hệ đó cùng dấu vết của nó, không phải ghi tên hiệu ứng.

---

## 1. Thẻ ánh sáng — 6 câu hỏi

Mọi thiết kế ánh sáng đều trả lời đủ 6 câu dưới đây. Thiếu câu nào thì model tự điền mặc định, mà mặc định thường là ánh sáng đều và phẳng, hoặc "golden hour" (xem §8).

| # | Câu hỏi | Quyết định cái gì | Dấu hiệu kiểm trên ảnh |
|---|---|---|---|
| 1 | **Nguồn là gì, có thật trong thế giới không?** | mặt trời, trời, cửa sổ, đèn, lửa, màn hình, flash | nguồn hiện trong khung, hoặc hướng và màu khớp với một nguồn hợp lý |
| 2 | **Đến từ hướng nào?** | trước, bên, sau, trên, dưới; độ cao | hướng bóng đổ, phía nào sáng, phía nào tối |
| 3 | **Nguồn to hay nhỏ so với chủ thể (cứng/mềm)?** | độ cứng | mép bóng sắc hay loang |
| 4 | **Vùng tối được nâng bao nhiêu (tỷ lệ chính:phụ)?** | độ tương phản, mood | vùng tối còn chi tiết, chỉ còn khối, hay đen |
| 5 | **Màu của nguồn chính và nguồn phụ?** | nhiệt màu, quan hệ ấm/lạnh | màu vùng sáng khác màu vùng tối thế nào |
| 6 | **Môi trường đáp lại ra sao?** | ánh hắt, không khí, phản xạ, độ suy giảm | ánh màu hắt từ bề mặt, sương, tia sáng, vùng sáng tắt nhanh hay chậm |

---

## 2. Vật lý nền

### 2.1 Cứng/mềm do kích thước biểu kiến quyết định [VẬT LÝ]

Độ cứng/mềm phụ thuộc ba thứ: **kích thước bề mặt nguồn, khoảng cách tới vật, độ dày lớp khuếch tán**. Nguồn càng to và gần, khuếch tán càng dày, thì sáng càng mềm. Nguồn nhỏ hoặc xa thì sáng cứng.

- Mặt trời rất to nhưng rất xa, nên **nhỏ về biểu kiến** và cho sáng cứng. Trời mây phủ kín là một hộp sáng khổng lồ, cho sáng rất mềm.
- Hệ quả hay bị quên: **cùng một softbox, đưa ra xa thì cứng hơn**.
- Dấu hiệu kiểm: **vùng chuyển của mép bóng** (bán dạ, penumbra). Mép sắc như dao là nguồn nhỏ. Mép loang vài cm là nguồn to.

Cách viết: 硬光，阴影边缘清晰锐利 / 大面积柔光，阴影边缘柔和渐变、包裹面部

### 2.2 Suy giảm theo bình phương khoảng cách [VẬT LÝ]

Độ sáng giảm theo bình phương khoảng cách tới nguồn. Hệ quả cho ảnh:

- **Nguồn gần** (nến, đèn bàn, màn hình) tạo **vũng sáng tắt nhanh**: mặt sáng, vai đã tối, tường sau tối hẳn.
- **Mặt trời** không suy giảm trong phạm vi một cảnh: tiền cảnh và hậu cảnh sáng như nhau.
- **Ánh sáng trời** (skylight) đến từ mọi hướng và suy giảm rất chậm, nên nó là "nguồn phụ" tự nhiên của mọi cảnh ngoài trời.
- Mẹo nền tối [THỰC HÀNH]: đèn gần chủ thể, chủ thể xa tường, thì nền tự tối mà không cần cấm.

Cách viết: 烛光只照亮面部与双手，光线在肩部迅速衰减，身后墙面沉入黑暗 / 阳光均匀照亮从前景到远景的整个场景

### 2.3 Tỷ lệ sáng chính:phụ — phần repo còn thiếu [VẬT LÝ + THỰC HÀNH]

Định nghĩa (công thức ASC): tỷ lệ = (chính + phụ) : phụ. Mỗi stop chênh lệch là gấp đôi lượng sáng:

| Chênh lệch | Tỷ lệ | Trông như thế nào [THỰC HÀNH] | Dùng cho |
|---|---|---|---|
| 0 stop | 1:1 | gần như không có khối, phẳng | high-key, sản phẩm, beauty sáng |
| 1 stop | 2:1 | vùng tối rõ nhưng mở, nhiều chi tiết | chân dung sáng, thương mại, mềm |
| ~1,5 stop | 3:1 | khối mặt rõ, vẫn tự nhiên | chân dung tự nhiên, editorial |
| 2 stop | 4:1 | vùng tối đậm, chi tiết còn nhưng chìm | tạp chí có chiều sâu, cinema ban ngày |
| 3 stop | 8:1 | vùng tối gần như mất chi tiết | low-key, noir, kịch tính |
| >3 stop | 16:1+ | nửa mặt đen, chỉ còn đường viền | chiaroscuro, split light |

**Model không đọc được con số.** Phải dịch tỷ lệ thành **trạng thái vùng tối nhìn thấy được**:

| Ý định | Viết |
|---|---|
| ~2:1 | 暗部明亮通透，阴影轻浅，细节完整 |
| ~3–4:1 | 面部有清晰明暗体积，暗部保留细节但明显较暗 |
| ~8:1 | 暗部深沉，只保留轮廓与少量细节，不补光 |
| >8:1 | 半张脸沉入黑暗，仅剩边缘轮廓，无补光 |

Luôn kèm mức sàn: 暗部不死黑 hoặc 保留五官可辨, trừ khi chủ ý muốn đen hẳn.

### 2.4 Ánh sáng phụ trong tự nhiên đến từ đâu [VẬT LÝ]

Trong thế giới thật, "đèn phụ" là môi trường:

- **Trời**: phủ mọi hướng, mềm, **lạnh** (màu xanh). Vì vậy bóng nắng ngày quang luôn hơi xanh.
- **Ánh hắt** (spill/bounce): mọi bề mặt bị chiếu sáng thành nguồn phụ **mang màu của nó**. Cỏ hắt xanh lá lên cằm, tường đỏ hắt đỏ lên má, cát hắt ấm, tuyết hắt trắng mạnh từ dưới lên.
- **Phụ âm** (negative fill): bề mặt tối gần chủ thể (tường tối, rèm đen) **hút** ánh hắt, làm một bên mặt tối sâu hơn.

Dấu hiệu kiểm: **màu và độ sáng của vùng tối cho biết nguồn phụ.** Đây là bằng chứng mà model hay làm sai: vùng tối trung tính trong khi môi trường có màu.

Cách viết: 晴天阴影带天空的冷蓝色调 / 草地的绿色反光轻微映在下巴与颈部 / 右侧深色墙面形成负补光，使右脸更深

### 2.5 Nhiệt màu [VẬT LÝ + THỰC HÀNH]

| Nguồn | ~Kelvin | Đọc thành |
|---|---|---|
| Nến, lửa | ~1800 K | cam đỏ, thân mật |
| Bóng đèn sợi đốt | ~3200 K | vàng ấm, trong nhà |
| Mặt trời thấp (golden hour) | ~2500–3500 K | vàng cam |
| Nắng trưa | ~5500–5600 K | trắng trung tính |
| Trời âm u | ~6500 K | trắng hơi lạnh |
| Bóng râm dưới trời xanh | 7500–10000 K+ | xanh lạnh |

Quy tắc dùng:

1. **Vùng tối mang màu của nguồn phụ, vùng sáng mang màu của nguồn chính.** Nắng chiều ấm + trời lạnh cho ra mặt ấm, bóng xanh. Đây là cấu trúc ấm/lạnh tự nhiên nhất.
2. **Pha nhiệt màu là một lựa chọn, không được là tình cờ.** Có ba cách: để một nguồn thống trị, cân bằng các nguồn, hoặc cố ý để chúng đối nghịch. Cảnh trong nhà ban ngày có cửa sổ (lạnh) và đèn bàn (ấm) là cặp kinh điển.
3. Không tả "màu ấm" chung chung. Phải gán màu **cho nguồn cụ thể**.

Cách viết: 窗外冷白天光从左侧进入，室内台灯在右后方投下暖黄色光池，两种色温在人物脸上交汇

### 2.6 Bề mặt nhận ánh sáng [VẬT LÝ]

- **Khuếch tán và phản chiếu:** bề mặt nhám rải sáng mềm đều. Bề mặt bóng phản chiếu **hình dạng của nguồn**: catchlight trong mắt có hình cửa sổ, vệt sáng trên kim loại hay da ướt có hình softbox. Hình dạng điểm sáng phản chiếu là **dấu vân tay của nguồn**.
- **Góc tới:** nhìn mặt nước hay sàn bóng ở góc thấp thì phản chiếu mạnh hơn hẳn so với nhìn thẳng xuống (hiệu ứng Fresnel, kiến thức quang học chuẩn). Mặt sông lúc chiều thấp gần như soi gương bầu trời.
- **Tán xạ dưới bề mặt (SSS):** ánh sáng chui vào vật rồi thoát ra ở chỗ khác. Có ở **da, sáp, cẩm thạch, lá, sữa**. Khoảng 94% độ phản xạ của da người đến từ tán xạ dưới bề mặt. Ánh đỏ lan xa nhất, nên khi bị ngược sáng thì **vành tai, ngón tay, cánh hoa, lá, đầu lông** phát sáng ấm. Thiếu hiệu ứng này, vật liệu trông như nhựa hoặc kim loại.

Cách viết: 逆光下耳廓与指缘透出温暖的红色透光 / 花瓣与叶片被背光照透，边缘发亮 / 眼中高光呈窗户形状，与主光方向一致

### 2.7 Không khí [VẬT LÝ]

Phối cảnh khí quyển: vật càng xa thì **giảm tương phản, giảm bão hoà, ngả về màu của không khí**. Ban ngày ngả xanh, bình minh và hoàng hôn ngả đỏ. Nguyên nhân là ánh sáng bị tán xạ vào đường nhìn, tạo một lớp sáng phủ lên vật.

- Đây là **bằng chứng khoảng cách** mạnh nhất cho cảnh rộng, và là bằng chứng tỷ lệ cho vật khổng lồ (xem notes §1).
- Tia sáng (god rays) chỉ thấy được khi có đủ ba thứ: **nguồn cứng có hướng + hạt trong không khí (sương, khói, bụi) + nền tối hơn phía sau tia**. Thiếu một thứ là tia sáng vô lý.

Cách viết: 远山随距离逐层降低对比与饱和，染上空气的淡蓝 / 香炉的烟雾使斜射阳光形成可见光束，光束后方为较暗的殿内

### 2.8 Nhất quán hình học — lỗi model dễ bị lộ nhất [VẬT LÝ + GIẢ THUYẾT-AI]

- **Mặt trời cho tia gần như song song**, nên mọi bóng trong cảnh **cùng hướng**, độ dài tỷ lệ với chiều cao vật.
- **Nguồn điểm gần** (đèn, nến) cho bóng **toả ra từ nguồn**.
- Phản chiếu phải tuân theo cùng hình học với vật thật.
- Nghiên cứu pháp y ảnh (nhóm Hany Farid) dùng chính các ràng buộc này (bóng, phản chiếu, điểm tụ) để phát hiện ảnh AI. Tức là đây đúng là chỗ model ảnh **hay sai**.

Cách viết: 所有投影方向一致，长度随物体高度成比例 / 人物与巨兽的投影来自同一太阳方向

---

## 3. Ánh sáng tự nhiên theo thời điểm và thời tiết

| Điều kiện | Định nghĩa | Hướng / độ cứng | Bóng | Màu | Dùng |
|---|---|---|---|---|---|
| Trưa nắng | mặt trời cao | từ trên, cứng | ngắn, đậm; hốc mắt tối | trung tính | sáng gắt, mùa hè, đồ hoạ |
| Golden hour | độ cao mặt trời **+6° đến −4°** | ngang thấp, mềm hơn | **dài**, mềm hơn | vàng cam | ấm áp, hoài niệm, ngược sáng viền tóc |
| Blue hour | **−4° đến −6°** | trời phủ, không hướng | gần như không | xanh lạnh, bão hoà | đèn đường và cửa sổ phát sáng nổi bật |
| Âm u | mây kín | hộp sáng khổng lồ, rất mềm | gần như không, tối ở chỗ tiếp xúc | hơi lạnh | da đẹp, buồn, phim tài liệu |
| Bóng râm | khuất nắng, nhìn ra trời | mềm, đến từ phía trời mở | nhẹ | lạnh | chân dung mềm |
| Đêm có đèn | đèn đường, cửa hàng, đèn lồng | nhiều nguồn điểm | toả từ nguồn, tắt nhanh | lẫn nhiều nhiệt màu | đô thị, cinema |
| Sương | hạt lơ lửng | sáng toả, mất hướng | yếu | nhuốm màu nguồn | khoảng cách, tia sáng |

Số liệu golden/blue hour theo PhotoPills. Ngoài các mốc độ cao mặt trời, phần còn lại là [THỰC HÀNH].

[GIẢ THUYẾT-AI] Model mặc định kéo cảnh ngoài trời về "golden hour". Muốn trưa, âm u hay blue hour thì phải ghi **dấu hiệu** (bóng ngắn, không bóng, đèn đã bật), không chỉ ghi tên thời điểm.

---

## 4. Ánh sáng có nguồn (motivated) và đèn trong khung (practical) [THỰC HÀNH — điện ảnh]

- **Motivated lighting:** ánh sáng phải giải thích được trong thế giới của ảnh: cửa sổ, đèn, màn hình, lửa, nến.
- **Practical:** nguồn sáng nằm ngay trong khung, nói cho người xem ánh sáng từ đâu tới.
- Nguồn ngoài khung vẫn được, nhưng **hướng, nhiệt màu, độ cứng** phải khớp với một nguồn hợp lý.
- Ba nguyên tắc nghề:
  1. dựa vào nguồn sáng sẵn có của bối cảnh;
  2. đưa practical vào khung;
  3. khớp nhiệt màu với nguồn được biện minh.
- Ứng dụng prompt: nếu ảnh có đèn lồng, nến hay màn hình mà **không thắp**, đó là lãng phí nguồn. Nếu đã thắp, nó phải để lại vũng sáng hoặc hắt lên chủ thể.

---

## 5. Bậc thang bằng chứng ánh sáng

Mỗi nguồn sáng chỉ cần một bằng chứng, nhưng phải chọn **bằng chứng khó làm giả nhất** có trong cảnh:

1. **Bóng đổ**: hướng, độ dài, độ cứng mép. Gồm cả **bóng tiếp xúc** (vùng tối ngay chỗ vật chạm đất hay chạm nhau). Thiếu bóng tiếp xúc thì vật trông như lơ lửng hoặc bị ghép.
2. **Điểm sáng phản chiếu**: vị trí và hình dạng khớp với nguồn (catchlight, vệt trên kim loại, kính, da).
3. **Màu và độ sáng của vùng tối**: cho biết nguồn phụ (§2.4).
4. **Độ suy giảm**: vũng sáng tắt nhanh cho nguồn gần, sáng đều cho mặt trời.
5. **Viền sáng / tán xạ dưới bề mặt**: đúng phía của nguồn sau lưng.
6. **Tông màu tổng**: yếu nhất, vì model tự áp được.

Model thường cho ra 5 và 6 mà bỏ 1 và 3, nên khi viết hãy ưu tiên ghi rõ 1 và 3.

---

## 6. Thẻ viết tiếng Trung — ráp 6 câu hỏi thành một câu ánh sáng

```
[nguồn có thật] 从 [hướng] [照来/进入]，[cứng/mềm + dấu hiệu mép bóng]；
[tỷ lệ → trạng thái vùng tối]；[nguồn phụ/màu vùng tối]；
[bằng chứng khó giả: bóng đổ / hình phản chiếu]；[mức sàn]。
```

Ví dụ: chân dung cửa sổ, tự nhiên, khoảng 3:1:

> 左侧大窗的阴天柔光从约四十五度方向进入，阴影边缘柔和；面部有清晰明暗体积，暗部保留细节；右侧白墙的反光轻轻提亮暗部；眼中高光呈窗户形状，与光源方向一致；肤色自然，不过曝。

Ví dụ: cảnh rộng, ngược sáng chiều, sinh vật khổng lồ:

> 午后低角度太阳从人物右后方照来，硬光；巨狐在人物腿部与石地上投下清晰长影，方向一致；九尾毛尖与人物发丝被背光照透发亮；暗部带天空冷蓝；面部保留细节，不剪影化。

Ví dụ: nội thất đêm có nguồn trong khung, tỷ lệ cao:

> 桌上烛台是画面内唯一光源，暖橙色光池只照亮面部与双手，在肩部迅速衰减；暗部深沉，仅留轮廓，不补光；墙面沉入黑暗；眼中有微小烛火高光。

---

## 7. Danh sách kiểm sau khi ra ảnh

1. Chỉ được nguồn sáng chính không? Nó có lý do tồn tại trong cảnh không?
2. Mọi bóng có cùng hệ không (song song nếu là mặt trời, toả ra nếu là nguồn điểm)?
3. Có bóng tiếp xúc ở chỗ chân chạm đất, vật chạm vật không?
4. Vùng tối đúng mức của tỷ lệ đã ghi chưa? Màu của nó có khớp với nguồn phụ và môi trường không?
5. Catchlight và điểm sáng phản chiếu có cùng hướng và hình dạng với nguồn không?
6. Vật càng xa có giảm tương phản và bão hoà không? Tia sáng có đủ ba điều kiện không?

Câu nào sai thì sửa đúng câu ánh sáng tương ứng trong prompt, rồi chạy lại. Mỗi lần chỉ sửa một biến (xem `core/09`).

---

## 8. Attractor ánh sáng của model ảnh [GIẢ THUYẾT-AI — cần test]

| Attractor | Nhận ra | Chặn thử |
|---|---|---|
| Golden hour mặc định | cảnh ngoài trời nào cũng vàng cam, bóng dài | ghi thời điểm **và** dấu hiệu: 正午顶光，影子短 / 阴天无明显投影 |
| Viền sáng khắp nơi | rim light quanh người dù không có nguồn sau lưng | chỉ ghi rim khi có nguồn sau; negative: 无来源的轮廓光 |
| Sáng đều kiểu HDR | mọi vùng đủ sáng, không vùng nào chìm | ghi tỷ lệ bằng trạng thái vùng tối (§2.3) + 不使用HDR |
| Glow/bloom toàn ảnh | quầng sáng mờ trên mọi điểm sáng | chỉ cho bloom ở điểm sáng nhất; 不要全局柔光雾化 |
| Tia sáng thiếu điều kiện | god rays không có khói hay bụi, nền sau tia sáng | ghi đủ ba điều kiện (§2.7) hoặc cấm 夸张丁达尔光柱 |
| Không bóng / vật lơ lửng | sinh vật hay người không có bóng tiếp xúc | ghi bóng đổ + bóng tiếp xúc (§5) |
| Vùng tối trung tính | bóng xám trong môi trường đầy màu | ghi màu vùng tối theo nguồn phụ (§2.4) |
| Bóng lệch hướng | hai vật bóng ngả hai hướng dưới cùng mặt trời | 所有投影方向一致 |
| Catchlight dán cố định | chấm trắng tròn trong mắt không khớp nguồn | dùng eye-life guard của `library/11` |

---

## 9. OPEN — cần test hoặc nghiên cứu tiếp

- Model có phản ứng khác nhau với "4:1" và với mô tả trạng thái vùng tối không? Giả thuyết: chỉ mô tả mới có tác dụng.
- Viết màu vùng tối có làm ảnh thật hơn rõ rệt không? Test A/B: cùng prompt, có và không có câu về màu vùng tối.
- Ghi nhiệt màu bằng số Kelvin (3200K) hay bằng tên nguồn (钨丝灯) thì hiệu quả hơn?
- Giới hạn số nguồn: viết 3 nguồn trở lên thì model có bắt đầu bỏ nguồn không?

---

## Nguồn

- Lighting ratio, Wikipedia: https://en.wikipedia.org/wiki/Lighting_ratio
- Fill light, Wikipedia: https://en.wikipedia.org/wiki/Fill_light
- Hard and soft light, Wikipedia: https://en.wikipedia.org/wiki/Hard_and_soft_light
- Aerial perspective, Wikipedia: https://en.wikipedia.org/wiki/Aerial_perspective
- Subsurface scattering, Wikipedia: https://en.wikipedia.org/wiki/Subsurface_scattering
- PhotoPills, Golden hour guide: https://www.photopills.com/articles/golden-hour-photography-guide
- GVM, Color temperature for video: https://gvmled.com/color-temperature-video-filmmaking-guide/
- StudioBinder, Motivated lighting: https://www.studiobinder.com/blog/what-is-motivated-lighting-in-film/
- ICO, Physics-based clues reveal AI-generated images (Farid và cộng sự): https://www.ico-optics.org/physics-based-clues-reveal-ai-generated-images-despite-realism/
- 南鸢 nuyoah (X, 2026-09-28): công thức tên đèn + hướng + kết quả nhìn thấy, xem `notes/2026-10_LIGHT_POSTER_CINEMA.md` §3
