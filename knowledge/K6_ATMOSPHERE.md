# K6 — KHÔNG KHÍ & THỜI TIẾT

status: v0.1 CANDIDATE · author: Claude · date: 2026-10-02
Nhãn: [VẬT LÝ] · [THỰC HÀNH] · [GIẢ THUYẾT-AI].
Liên quan: `K1_LIGHT.md` §2.7 (god-ray), §3 (thời điểm/thời tiết); `K4_COLOR.md` §2.4; `K5_MATERIAL.md` §2.7 (ướt).

---

## 0. Câu lõi

**Không khí là lớp vật chất giữa máy và mọi thứ. Nó làm ba việc: tạo chiều sâu (càng xa càng nhạt), làm ánh sáng hiện hình (tia, quầng), và để lại dấu vết trên bề mặt (ướt, tuyết, bụi).** Thời tiết trong prompt phải có cả ba: trong không khí, trên ánh sáng, trên mặt đất. Thiếu một là "dán hiệu ứng".

## 1. Thẻ không khí 5 câu

1. **Trong không khí có gì?** (sạch, hơi nước, sương mù, bụi, khói, mưa, tuyết)
2. **Tầm nhìn bao xa?** Lớp xa nhất còn thấy là gì?
3. **Ánh sáng lộ ra thế nào?** (tia, quầng quanh đèn, toả sáng ngược sáng, phẳng)
4. **Bề mặt mang dấu vết gì?** (ướt, vũng phản chiếu, tuyết bám, bụi phủ)
5. **Cơ thể/vật phản ứng thế nào?** (hơi thở, tóc ướt, áo bám, mắt nheo)

## 2. Vật lý

### 2.1 Phối cảnh không khí [VẬT LÝ]
- Phân tử và hạt trong không khí tán xạ ánh trời vào đường nhìn → với khoảng cách: **tương phản giảm, chi tiết mất, màu nhạt và ngả về màu không khí** (xanh khi nắng, đỏ khi bình minh/hoàng hôn).
- Tương phản giảm **theo hàm mũ** với khoảng cách (Koschmieder / Beer–Lambert); tầm nhìn định nghĩa ở ngưỡng tương phản 2%.
- **Rayleigh** (phân tử ≪ bước sóng): ưu tiên xanh, tán xạ trước-sau như nhau → trời xanh, xa ngả xanh. **Mie** (giọt/hạt ~ bước sóng): gần như mọi màu như nhau, chủ yếu tán xạ **về phía trước** → mây, sương, khói trắng/xám; sáng rực khi ngược sáng.
- Luật viết: lớp xa sáng hơn, tương phản thấp hơn; xanh trong không khí sạch, trắng/xám trong ẩm. Ngoại lệ: lớp được nắng chiếu trên nền tối.

### 2.2 Sương mù, sương mỏng, mù khô [VẬT LÝ]
- Ngưỡng tầm nhìn (Wikipedia, gán cho WMO; các cơ quan khác nhau): **sương mù < 1 km**, sương mỏng 1–2 km, mù khô 2–5 km.
- Sương mù/sương mỏng = giọt nước trong không khí gần bão hoà; mù khô = hạt khô (bụi, khói, ô nhiễm), có thể ngả nâu hoặc xanh tuỳ góc nắng.
- Sương làm **quầng (corona)** quanh đèn và trăng: đĩa trắng-xanh nhạt dần sang nâu đỏ, đôi khi có vòng màu.
- Sương hiện **bóng 3 chiều** khi ánh sáng lọt qua khe cây/kiến trúc — cần sương đủ dày để sáng lên, đủ mỏng để ánh sáng xuyên qua.

### 2.3 Luồng sáng và tia sáng (god rays) [VẬT LÝ]
- Luồng sáng thấy được: nguồn có hướng + hạt trong không khí + nền tối hơn (trùng K1 §2.7). Đèn pha trong sương cho một luồng mà không cần khe.
- **Nhiều tia tách nhau** (crepuscular rays): cần thêm khe/vật che chia luồng (mây, lá, ván gỗ). Tia thực ra song song, trông như toả ra do phối cảnh.
- Thiếu điều kiện tương ứng → tia là "hiệu ứng dán".

### 2.4 Mưa [THỰC HÀNH + VẬT LÝ]
- Hạt mưa **chỉ thấy rõ khi ngược sáng trên nền tối**. Tốc độ màn trập: ~1/60–1/200 s ra vệt ngắn; ≥ 1/250 s đóng băng giọt; ≤ 1/30 s thành "màn trắng".
- Mặt ướt tối hơn (K5 §2.7); vũng nước thêm phản chiếu gương.
- Đường nhựa ướt ban đêm: đèn phản chiếu thành **vệt dọc kéo dài về phía máy**. Mỗi vệt phải có nguồn đèn tương ứng.

### 2.5 Tuyết [VẬT LÝ + THỰC HÀNH]
- Tuyết mới phản xạ ~80–95% ánh sáng (nhựa đường 4–12%, cỏ ~25%) → tuyết là **tấm phản sáng khổng lồ**, mặt người được rọi từ dưới.
- Máy đo sáng kéo tuyết về xám → nhiếp ảnh gia bù +0.7 đến +2 stop. Ảnh tuyết đúng là tuyết trắng có chi tiết.
- Bóng trên tuyết **xanh** dưới trời trong (chỉ ánh trời chiếu); gần như không có bóng khi trời đục.
- Tuyết rơi: vệt ở ~1/40–1/100 s, chấm ở ≥ 1/250 s.

### 2.6 Bụi, khói, hơi nước [VẬT LÝ]
- Tán xạ về trước → **sáng rực khi nhìn về phía nguồn (ngược sáng)**, xỉn khi nguồn ở sau máy.
- Mù làm mặt trời và hoàng hôn dịu, ấm. Ánh "vàng ấm" của bụi ngược sáng chủ yếu do mặt trời thấp ấm, không phải do tán xạ (suy luận).

### 2.7 Bầu trời là nguồn sáng [VẬT LÝ]
- Trời đục hoàn toàn (8/8 oktas): gần như không có nắng trực tiếp, toàn ánh tán xạ; cường độ từ ~1/6 nắng (mây mỏng) đến ~1/1000 (mây bão dày). Mây tán xạ mọi màu như kính mờ → "softbox khổng lồ".
- Suy luận (chưa có nguồn mạnh): mây ti mỏng chỉ làm nắng mềm nhẹ; mây tích rời → ánh sáng loang, đổi nhanh; mây tầng → ánh phẳng.

### 2.8 Luật nhất quán [VẬT LÝ]
- Trời đục → **không có bóng đổ sắc cạnh**.
- Mặt đất ướt tối → đang mưa hoặc vừa mưa.
- Hơi thở thấy được → lạnh và ẩm, thường dưới ~7 °C (tuỳ độ ẩm).
- Tia sáng → đủ điều kiện §2.3 (nhiều tia cần khe).
- Sương → có **gradient theo chiều sâu** (gần rõ, xa mất), đèn trong sương có quầng.
- Tuyết dưới trời trong → bóng xanh; trời đục → gần như không bóng.

## 3. Theo chế độ ảnh
- **Poster:** không khí làm hào quang/tách nền (sương sau lưng, bụi ngược sáng). Thường giữ trời sạch để màu sạch (notes §1) — nhưng khi đó cần bóng đổ để sinh vật không như ghép.
- **Cinema:** không khí là công cụ chiều sâu chính; khói/bụi làm ánh sáng có nguồn hiện hình (notes §2 R2.3).
- **Candid:** thời tiết thật, không đẹp hoá: mưa làm tóc bết, nheo mắt, áo ướt.

## 4. Attractor (đều là quan sát, chưa có nghiên cứu)
| # | Attractor | Chặn thử |
|---|---|---|
| W-A1 | Tia sáng xuất hiện khắp nơi, không có khe/hạt | ghi đủ điều kiện §2.3 hoặc cấm: 无体积光 |
| W-A2 | Sương đều, không gradient sâu | ghi "近处清晰，中景变淡，远景只剩轮廓" |
| W-A3 | Có mưa mà mặt đất khô, hoặc phản chiếu không có nguồn | ghi dấu vết bề mặt + nguồn của từng phản chiếu |
| W-A4 | Bão mà "yên tĩnh lạ thường" (FoxWeather) | ghi hậu quả: lá, tóc, áo bay cùng hướng gió |
| W-A5 | Trời đục nhưng có bóng sắc | ghi "阴天，无清晰投影" |
| W-A6 | Tuyết xám hoặc bóng tuyết trung tính | "积雪洁白保留纹理，阴影呈淡蓝色" |

## 5. Cách viết (tiếng Trung, có mức sàn)
Công thức: **thứ trong không khí + gradient theo chiều sâu + ánh sáng hiện hình (đủ điều kiện) + dấu vết bề mặt + phản ứng cơ thể + mức sàn**.

- 清晨薄雾，近处石桥清晰，中景柳树变淡，远处城楼只剩浅灰轮廓；路灯周围有柔和光晕；人物面部保留细节。
- 夜雨，人物身后的霓虹灯逆光照亮斜落的雨丝；湿润的柏油路面变暗，灯光在地面拉出指向镜头的竖直倒影，每条倒影都对应画面中的一盏灯。
- 晴天雪地，雪面洁白保留纹理，人物脸部被雪地从下方反光照亮，阴影呈淡蓝色，呼出的白气在冷空气中可见。
- 晨光从谷仓木板缝隙射入，空气中漂浮灰尘，背后是深暗的仓内，形成数道清晰光束。

## 6. Kiểm sau khi ra ảnh
1. Có gradient xa-nhạt? Màu xa đúng loại không khí (xanh / trắng xám)?
2. Tia sáng đủ điều kiện §2.3?
3. Thời tiết có dấu vết trên mặt đất và trên người?
4. Trời đục mà có bóng sắc? Phản chiếu không nguồn?
5. Tuyết trắng có chi tiết, bóng xanh?

## 7. OPEN
- **O1** Câu gradient ba lớp (近/中/远) có thắng W-A2 không?
- **O2** "每条倒影都对应一盏灯" có giảm phản chiếu không nguồn?
- **O3** Cấm volumetric (无体积光) có làm model bỏ luôn không khí?
- **O4** Ghi tốc độ màn trập (1/125 秒) vs ghi kết quả (短雨丝) cho mưa/tuyết.

## Nguồn
- Wikipedia: Aerial perspective; Visibility; Mie scattering; Diffuse sky radiation; Mist; Haze; Fog; Corona (optical phenomenon); Crepuscular rays; Albedo; Cloud cover.
- Nature TTL, rain/snow streaks: https://www.naturettl.com/how-to-get-rain-snow-streaks/
- PBS NC, why things look darker when wet: https://www.pbsnc.org/blogs/science/why-do-things-look-darker-when-they-get-wet/
- ePhotozine, blue snow: https://www.ephotozine.com/article/why-s-the-snow-in-my-shot-blue--17912
- Library of Congress, seeing your breath: https://www.loc.gov/everyday-mysteries/browse-all-questions/item/why-do-i-see-my-breath-when-its-cold-outside/
- FoxWeather, AI weather photos (giai thoại): https://www.foxweather.com/learn/real-or-fake-weather-photos-ai
- aiformule, reflections in AI photos (blog, yếu): https://aiformule.com/blog/reflections-ai-photos
