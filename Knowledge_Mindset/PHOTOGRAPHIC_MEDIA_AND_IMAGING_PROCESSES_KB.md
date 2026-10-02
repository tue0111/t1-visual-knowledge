# PHOTOGRAPHIC MEDIA AND IMAGING PROCESSES KNOWLEDGE BASE

Formation-layer reference for locking the *imaging medium* of a shot. Nguồn: kiến thức mỹ thuật nhiếp ảnh tổng hợp (art-history level, công khai, ổn định). Phân biệt rõ ở mỗi mục: **đặc tính vật lý đã được thiết lập** (có thể viết như cơ chế) và **gợi ý phong cách** (heuristic, cần brief xác nhận). File này KHÔNG chứa tuyên bố về hành vi generator cụ thể — phần đó thuộc `Portable_Agent_OS/FIELD_NOTES.md`. Delivery contract vẫn thuộc core; KB này không đổi ngôn ngữ hay cấu trúc giao hàng.

## 1. Nguyên tắc khóa medium

Một medium lock thuyết phục cần ba lớp: (a) **loại bỏ trước** — phủ định các medium dễ fallback (không phải摄影 / 不是三维渲染…); (b) **chữ ký dương tính** — đặc tích quang học/vật liệu đặc trưng của đúng medium chọn; (c) **hậu kỳ nhất quán** — grain, halation, màu, viền khung cùng một hệ. Trộn chữ ký mâu thuẫn (VD: grain phim Tri-X + HDR điện thoại + bokeh anamorphic) tạo "medium soup" — ảnh nhìn giả ngay cả khi từng chi tiết đẹp.

## 2. Film stocks — chữ ký màu và grain

| Stock | Chữ ký thiết lập | Viết prompt thế nào |
|---|---|---|
| Kodak Portra 400 | da ấm dịu, tương phản thấp, grain mịn, dải sáng rộng cho da; chuẩn wedding/portrait | 肤色温润偏奶油，颗粒细腻，整体对比柔和，高光过渡绵长 |
| Kodak Gold | vàng ấm hoài cổ, hơi oversaturated vùng vàng-xanh lá, chất consumer thập niên 90 | 金黄色调偏暖，怀旧家庭相册质感，阴影略带棕 |
| Fujifilm Pro 400H | xanh mint nhẹ trong highlight, da lạnh thanh lịch, pastel | 高光泛薄荷青，肤色清冷透亮，日系淡彩 |
| Kodak Ektar 100 | bão hòa cao, tương phản mạnh, grain cực mịn, đỏ rực | 色彩浓郁饱和，红色鲜明，适合强色块与风光 |
| Fuji Velvia | bão hòa cực đại cho cảnh, da khó看 (thiên magenta-green), chuẩn landscape | 风光色彩浓烈通透，绿色深邃，不适合人像特写 |
| Kodak Tri-X 400 | đen trắng grain thô có kết cấu, tương phản ăn, chuẩn reportage | 黑白粗颗粒，明暗对比强烈，新闻纪实感 |
| Ilford HP5 | đen trắng mềm hơn Tri-X, trung tính dài | 黑白层次绵长，灰阶丰富 |
| Cine Vision3 | dải động lớn, dễ grade, grain điện ảnh mịn | 电影级宽容度，为调色留余地 |

**Heuristic:** chọn stock theo *da hay cảnh* làm anchor. Da → Portra/Gold/400H. Cảnh → Ektar/Velvia. Đen trắng narrative → Tri-X/HP5.

## 3. Process looks (hóa học tạo look)

- **Push processing (C-41 +1/+2 stop):** tăng tương phản, grain thô đi, bóng tối dày — viết: 强迫冲增感两档，颗粒明显，暗部厚重的胶片。
- **Cross-process (rửa E6 trong C-41):** shift xanh-lá-vàng, tương phản cay, highlight cháy xanh — retro fashion thập niên 2000. 写：交叉冲洗，青黄偏色，高光泛蓝，对比生硬的时尚片。
- **Bleach bypass:** giữ bạc → giảm bão hòa, metallic, tương phản cao kiểu war-film. 写：漂银工艺，低饱和金属质感，黑白灰之间带冷。
- **Redscale:** quay mặt sau phim → toàn cảnh cam-đỏ. 写：红标反装，全画面橙红暖调。
- **Day-for-night:** ban ngày thu nhỏ khẩu + filter → trời gần đen, da vẫn đọc được; ánh mắt "ban đêm" nhưng bóng đổ vẫn là nắng. 写：白天模拟夜景，天空压近黑，人物可辨但环境沉暗。

## 4. Instant / Polaroid

- **SX-70:** tương phản thấp, màu phai ấm, da ngả cam-pastel, phát triển chậm. **600:** đậm đà hơn.
- Khung viền trắng đặc trưng (nếu brief muốn khung hiện hình, phải khai báo rõ — nó là một graphic element chiếm layout).
- Lỗi đặc trưng hợp lệ để dùng có chủ đích: ốm hóa học (chemical blotch), emulsion lift (nhũ trượt tạo vân sơn), quầng sáng tấm integral.

## 5. Digital eras và sensor signature

- **CCD digicam 2000s (đang trend "CCD质感"):** chroma noise trong bóng tối, halation cháy nhẹ quanh nguồn sáng, góc ảnh mềm, màu hơi tách kênh, cảm giác scan. Viết: 老式CCD数码相机直出，暗部彩色噪点，高光轻微溢出，边角偏软，2000年代随身机画质。
- **Early DSLR:** sắc nét "sạch" nhưng dải màu hẹp, da hơi vàng-xanh kỹ thuật.
- **Modern full-frame:** sạch, dải động rộng — cần chủ động thêm grain/halation nếu muốn chất film, vì mặc định nó trung tính.
- **Computational phone:** HDR làm phẳng tương phản, night-mode kéo nét dài gây smear chuyển động, portrait-mode sai depth ở tóc/mép kính. Muốn "chụp điện thoại thật", giữ các lỗi này có kiểm soát thay vì ẩn.

## 6. Lens character (ký tự ống kính)

| Lens/hiệu ứng | Chữ ký | Dùng khi |
|---|---|---|
| Anamorphic 2x | bokeh oval ngang, flare kẻ ngang xanh/chấm, mép kéo | cinematic widescreen, hero shot |
| Helios 44-2 | bokeh xoáy (swirl) quanh tâm, glow mềm | portrait dreamy retro |
| Petzval | xoáy mạnh hơn, viền tối cong, tâm sắc nét | vintage dramatic |
| Mirror (catadioptric) | bokeh hình vành khuyên | hiếm, điểm nhấn ánh sáng nhỏ |
| Soft-focus / Pro mist | highlight loang halo, đen vẫn giữ depth | romantic, music video |
| Tilt-shift | mặt phẳng tiêu cực nghiêng; miniaturize khi quay từ trên | kiến trúc, đồ chơi hóa cảnh thật |
| Fisheye | cong trụ cực đại, góc ~180° | skate/punk/energetic; cấm gần mặt |

## 7. Motion & analog video formats

- **Super 8 / 8mm:** grain to, gate weave (khung rung nhẹ), vignette, màu vàng-lục; chuẩn home-movie hoài niệm.
- **16mm documentary:** grain mịn hơn 8mm, cảm giác cinéma vérité.
- **VHS/CCTV:** độ phân giải thấp, color bleed, timestamp overlay, scanline — dùng cho found-footage.
- **90s camcorder:** autofocus hunt, micro-shake, màu video tách kênh.

## 8. Cặp đôi brief → media recipe (heuristic khởi điểm)

| Brief mood | Recipe khởi điểm |
|---|---|
| Hoài niệm gia đình | Gold 400 · snapshot · flash nội bộ · date stamp tùy chọn |
| Fashion editorial lạnh | Pro 400H hoặc digital+bleach bypass · medium format · softbox |
| Noir thành thị | Tri-X · hard key · deep shadow · rain wet-down |
| Cinematic epic | Vision3 · anamorphic · haze nhẹ · rim separation |
| Dreamy thanh xuân | Helios swirl hoặc Pro mist · backlight · pastel |
| Documentary góc nhìn tay | 16mm hoặc phone computational · handheld cues (motion blur nhẹ,构图 lệch) |

## 9. Câu thực thi tiếng Trung (bắt đầu, không phải công thức)

~~~text
柯达Portra 400胶片质感，肤色温润奶油调，颗粒细腻，对比柔和，高光过渡绵长，轻微暗角。
老式CCD数码相机直出：暗部彩色噪点，高光轻溢，边缘偏软，整体2000年代随身机氛围。
变形宽银幕镜头：椭圆形焦外，横向蓝色眩光条，画面比例2.39:1。
黑白Tri-X质感：粗颗粒结构感，明暗对比强烈，纪实摄影气质。
~~~

## 10. Boundary

- Bảng stock/process mô tả **truyền thống nhiếp ảnh đã thiết lập**, không phải luật phổ quát; mỗi generator tái hiện khác nhau — log kết quả vào generation log trước khi khóa làm recipe cố định.
- Không bao giờ trộn chữ ký mâu thuẫn trong một lock (mục 1).
- Media look không được lấn sang nội dung: đổi film stock không cứu một composition yếu (Luật 15 hài hòa trước, chi tiết sau).

