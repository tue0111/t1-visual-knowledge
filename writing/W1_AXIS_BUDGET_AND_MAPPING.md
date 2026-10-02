# W1 — NGÂN SÁCH TRỤC & BẢN ĐỒ VÀO 3 PHẦN

status: v0.1 CANDIDATE · author: Claude · date: 2026-10-02
Nền: `mindset/M1`, `core/03_PROMPT_COMPILER.md` §2–§7, `core/10_NEGATIVE_ENGINE.md`.

---

## 0. Câu lõi

**Chữ là sự chú ý của model. Trục chính nhận nhiều quyết định nhất, có bằng chứng nhìn thấy được, có mức sàn và được bảo vệ bằng negative. Trục phụ nhận một câu phục vụ. Trục để ngỏ không nhận gì, hoặc chỉ một mức sàn.**
Đo bằng **số quyết định độc lập**, không đếm ký tự (`core/03` §7).

## 1. Ngân sách theo cấp (giả thuyết, cần test)

| Cấp | Số trục | Quyết định trong 分镜 | Bằng chứng nhìn thấy | Mức sàn | Negative riêng |
|---|---|---|---|---|---|
| **Chính** | 1 (tối đa 2 nếu cùng hiệu ứng) | ~40–50% tổng quyết định của shot | ≥ 2 (một ở chủ thể, một ở môi trường) | bắt buộc | 1–2 câu chặn attractor của trục |
| **Phụ** | 2–3 | 1 câu mỗi trục | 1 | khi có rủi ro | chỉ khi có attractor đã biết |
| **Để ngỏ** | còn lại | 0 (art-direction) hoặc 1 mức sàn | — | tuỳ | chỉ attractor nguy hiểm (B6 của M1) |
| **Khoá cứng** | DNA, khung, brand | ở 母版锁 | — | — | Tier 1 trong 通用负面 |

Ví dụ "40–50%" không phải công thức; nó nói rằng nếu đọc prompt mà không biết trục chính là gì thì ngân sách đã sai.

## 2. Cấu trúc câu trục chính

Mở rộng công thức nuyoah (notes §3) cho mọi trục:

> **[tên/khái niệm] + [vị trí/hướng/thời điểm] + [bằng chứng trên chủ thể] + [bằng chứng trên môi trường] + [mức sàn]**

| Trục | Tên | Vị trí/hướng | Bằng chứng chủ thể | Bằng chứng môi trường | Mức sàn |
|---|---|---|---|---|---|
| K1 | 灯笼暖光 | 从人物左下方 | 侧脸与袖口暖色溢光 | 栏杆投下长影，远处保持冷蓝 | 面部保留细节 |
| K2 | 低机位仰拍 | 相机贴地，距狐头很近 | 狐鼻吻大于人物上半身 | 地平线压到画面下五分之一 | 人物五官比例正常 |
| K3 | 视线引导 | 人物位于左三分之一 | 视线望向右侧灯笼 | 右侧留出安静空白 | 人物仍为第一眼焦点 |
| K4 | 低调配色 | 大部分处于靛蓝暗部 | 唯一暖橙在手中灯笼 | 远景偏蓝、对比降低 | 肤色自然不偏灰 |
| K5 | 湿润鳞片 | 鳞片掌心大小 | 鳞缘小而锐利的高光 | 鳞片反射天空青色 | 不呈塑料感 |
| K6 | 清晨薄雾 | 由近到远渐浓 | 人物轮廓清晰 | 远处城楼只剩浅灰轮廓 | 路灯有柔和光晕而不过曝 |
| K7 | 推门的一瞬间 | 重心落在前脚 | 右手按门、左手提灯 | 斗篷下摆向后飘 | 手指自然完整 |
| K8 | 宋代书房 | 午后直棂窗 | 案上墨迹未干 | 书卷压着镇纸 | 不出现明清家具与现代物品 |

Câu trục phụ: chỉ **tên + một bằng chứng** (ví dụ: 远处城楼在薄雾中变淡。).

## 3. Bản đồ 8 trục → 3 phần

Nguyên tắc từ `core/03`: **ổn định qua các shot → 母版锁; riêng shot → 分镜; chặn sụp đổ → 通用负面** (riêng shot thì negative nằm trong shot).

| Trục | 母版锁 (khi ổn định / series) | 分镜 (mặc định) | 通用负面 / câu chặn trong shot |
|---|---|---|---|
| K1 Ánh sáng | ngôn ngữ ánh sáng chung của series (ví dụ "chỉ dùng nguồn có thật") | nguồn, hướng, bằng chứng bóng, tỷ lệ | rim light khắp nơi, không bóng tiếp xúc, tia sáng vô cớ |
| K2 Máy | chỉ khi cả series một ngôn ngữ máy | vị trí (điểm tham chiếu), độ cao, khoảng cách, cỡ cảnh, tiêu cự | 相机不在桥面上 (trong shot); series: cùng một góc lặp (A2) |
| K3 Bố cục | thứ tự đọc chung, quan hệ bất biến | điểm vào, đường đi, khoảng trống | chủ thể căn giữa vô cớ; vùng cạnh tranh |
| K4 Màu | **vai màu** (chủ đạo, nhấn, da) — thường ổn định | màu do ánh sáng của shot | quá bão hoà, đĩa đỏ, da lệch màu |
| K5 Chất liệu | DNA trang phục/vật liệu | trạng thái riêng (ướt, bụi) | da sáp/nhựa, mọi thứ bóng |
| K6 Không khí | chỉ khi series một thời tiết | thứ trong không khí, gradient, dấu vết bề mặt | tia sáng khắp nơi; mưa mà đất khô |
| K7 Khoảnh khắc | — (hầu như luôn riêng shot) | thời điểm, trọng lượng, tay, ánh nhìn có đích | tay dị dạng; nhìn ống kính (cinema); dáng lặp (series) |
| K8 Thế giới | luật thế giới, thời đại/vùng, phi lý được cấp phép | nơi cụ thể của shot, dấu vết | đồ sai thời đại; phi lý thứ hai |

## 4. Thứ tự câu trong 分镜 khi có trục chính

`core/03` §2 cho thứ tự lắp ráp chuẩn (để dễ kiểm). Trong khuôn đó, **câu trục chính đứng sớm nhất có thể trong khối của nó** và không bị câu trục phụ chen ngang. Nếu trục chính là K1, câu ánh sáng có bằng chứng đi trước câu màu; nếu trục chính là K7, câu khoảnh khắc đi trước câu ánh sáng.
Ngoại lệ có chủ ý so với `core/03` §2: khi trục chính thuộc một khối đứng sau (ví dụ K1 đứng sau tư thế), câu trục chính được kéo lên ngay sau câu khung/máy. Ngoại lệ này chỉ áp dụng cho trục chính; trục phụ giữ thứ tự chuẩn.
Hiệu ứng thứ tự trên generator **chưa được chứng minh** (`core/03` §2 nói rõ); đây là quy ước để người đọc thấy ngay trục chính.

## 5. Negative bảo vệ trục chính

- Negative **có mục tiêu**: chặn đúng attractor của trục chính (K1 §8, K2 §5, K3 §4, K4 §4, K5 §4, K6 §4, K7 §4, K8 §4).
- Không lặp cùng một chỉ dẫn ở dạng thơ, kỹ thuật và phủ định, trừ khi đã thấy model lỗi (`core/03` §7).
- Câu phủ định vị trí (K2) và câu phủ định thời đại (K8) có rủi ro **gợi ra chính thứ bị cấm** — OPEN K2 O2, K8 O2. Ưu tiên câu khẳng định đủ mạnh; chỉ thêm phủ định khi đã thấy attractor xảy ra.

## 6. Checklist trước khi giao

1. Đọc 分镜 không có bảng quyết định: đoán được trục chính không?
2. Trục chính có ≥ 2 bằng chứng (chủ thể + môi trường) và mức sàn?
3. Mỗi trục phụ ≤ 1 câu, có bằng chứng, không tạo điểm vào cạnh tranh?
4. Trục để ngỏ có bị viết "cho đủ"? Xoá.
5. Negative có chặn đúng attractor của trục chính? Có câu nào không phục vụ trục nào?
6. Luật cứng `core/03` §10: tiếng Trung, 3 phần, brand trong 母版锁, một shot một ảnh, không mâu thuẫn dương–âm.

## 7. OPEN
- **O1** Ngân sách 40–50% có tạo khác biệt đo được so với viết đều tay? Test: cùng brief, A = đều tay, B = phân cấp; người chấm mù đọc "thứ đầu tiên thấy".
- **O2** Bằng chứng môi trường có quan trọng ngang bằng chứng chủ thể không, hay chỉ với K1/K6?
- **O3** Negative riêng cho trục chính vs negative chung dài — cái nào ít tác dụng phụ hơn?
