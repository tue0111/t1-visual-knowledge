# 04 — TEMPLATES: khuôn và ví dụ

## Khối brand — một nguồn duy nhất
- Đặt trong 母版锁: `system/brand_block.txt`
- Dòng cuối của negative: `system/brand_negative.txt`

Chép **nguyên văn** cả hai, không gõ lại tay. `tools/t1lint.py` sẽ báo lỗi nếu lệch một ký tự.
Nếu brief yêu cầu "không chữ": bỏ cả hai, rồi chạy `t1lint.py --no-brand`.

## Khuôn một ảnh
```text
【母版锁 · 项目名】

[画面性质与观看关系：海报主视觉 / 电影剧照旁观 / 纪实抓拍 / 单一超现实。]
[主体身份与造型DNA；材质与配色角色。]
[世界规则；全片光线语言（如：所有光线都有合理来源）。]
<system/brand_block.txt>
每次只生成一张指定画面，不生成拼图、九宫格或多个备选。

【分镜 · 镜头名】

[（可选）第一眼撞上来的是：……（一句，把主轴的第一读点直接告诉模型）]
[比例。相机位置（世界参照物）、高度、距离、取景到身体哪里。]
[主轴：2–4句，主体证据 + 环境证据 + 底线。（可选）用一句点名张力：……就是这张画面的……]
[副轴：每轴一句。]
[一句反吸引子（需要时）。]
[（可选）阅读顺序：先读到……，再读到……，最后才发现……]

【通用负面提示词】

[主轴的真实失败 + 解剖 + 材质，有目标，不堆砌。]
<system/brand_negative.txt>
```
Album: giữ một 母版锁 và một negative, thêm nhiều khối `【分镜 · …】` ở giữa.

**Ba câu tuỳ chọn trong 分镜** (v2.9.0, [giả thuyết], xem LEARNINGS 2026-11-04):
- **第一眼:** dòng "ĐỌC: đầu tiên" của bảng quyết định thường chỉ nằm ngoài prompt. Câu này gửi nó thẳng cho model, đặt ở đầu 分镜.
- **Câu gọi tên chỗ căng:** một câu nói phần nào là lý do tồn tại của ảnh (đoạn chuyển, vệt sáng, khoảng cách). Model biết chỗ nào phải đẹp nhất. Mỗi 分镜 tối đa một câu.
- **Thứ tự đọc 3 tầng:** đặt cuối 分镜, khớp dòng ĐỌC của bảng quyết định. Dùng cho poster và ảnh có chữ, nơi tầng thông tin dễ tranh nhau.

Cả ba đều phải là bằng chứng nhìn thấy, không phải tính từ. Nếu viết thành "第一眼很震撼" thì thà bỏ.

## Khuôn series có tham số (nền + gia vị)
Dùng khi cùng một quy cách phải chạy cho nhiều chủ đề (bộ poster theo mùa, mỗi địa danh một tấm, mỗi khách một bản). [giả thuyết]

```text
【母版锁 · 系列名】

[画面性质与观看关系。]
[不变的骨架：构图几何、主体与留白的位置、阅读顺序、文字层级。]
[随主题变化的部分写成规则：主题决定……（颜色/场景/主物）；主题换了，……整体换成……，只保留……之间的关系。]
[主题没给文字时，文字由什么生成；中文一律简体。]
<system/brand_block.txt>
每次只生成一张指定画面，不生成拼图、九宫格或多个备选。

【分镜 · 本期】

[本期主题与用途一句；本期例外（换色、换幅、换文字位置）各一句。]

【通用负面提示词】

[这个风格最容易滑向的失败，一两句。]
<system/brand_negative.txt>
```
- 母版锁 là "nền": viết **quan hệ**, không viết giá trị ("màu chủ lấy từ vật liệu đặc trưng của chủ đề", không viết "màu đỏ").
- 分镜 là "gia vị": ngắn, chỉ chứa phần của kỳ này.
- Kiểm bằng cách chạy ít nhất 2 chủ đề thật khác nhau. Nếu ra hai ảnh như một thì nền đang khoá giá trị, chưa khoá quan hệ.

## Ví dụ đầy đủ (đều qua `t1lint --strict`)

| File | Chế độ | Trục chính | Phụ | Chặn | Ý đồ vùng tối |
|---|---|---|---|---|---|
| `examples/A_cinema_lantern.txt` | cinema, xem lâu | K1 (đèn lồng là nguồn ấm duy nhất) | K7, K6 | nhìn ống kính, tia sáng vô cớ | mặt và sân xa đọc được, góc lầu được chìm |
| `examples/B_poster_icefox.txt` | poster, vài giây | K2 + K3 (tỷ lệ cộng hai ánh nhìn, cùng một hiệu ứng) | K4, K5 | cảm giác ghép, cần bóng tiếp xúc | high-key, mặt là vùng sáng nhất của chủ thể |
| `examples/C_candid_bridge.txt` | candid | K7 (ông lão đẩy xe lên dốc) | K8, K1 | máy đứng trên cầu | ánh sáng sớm, không chìm |

**Ghi chú:**
- **A:** so với bản thử W2, bản này ghi thêm ý đồ vùng tối. Bản cũ chỉ đặt mức sàn cho mặt, nên toàn bộ môi trường đen 6/6 ảnh.
- **B:** mặt trời ở sau-phải và cáo ở gần máy, nên bóng phải đổ **về phía máy**. Trời màu mơ ấm nghĩa là mặt trời thấp.
- **C:** câu phủ định 相机不在桥面上 đã thất bại 3/3, nên bản này đổi sang hình học khẳng định (chụp ngang, vuông góc với cầu). **Cách sửa này chưa kiểm.** Nếu máy vẫn lên cầu, thử thêm: máy ở bờ đối diện, cầu nằm ở nửa trên khung.

## Phản ví dụ — viết đều tay (đừng làm)
```text
电影感，美丽的少女站在雪中的古楼上，手提灯笼，暖色调，柔和光线，景深，细节丰富，高品质，8K，大师作品，氛围感。
```
Vì sao hỏng:
- Không có trục chính.
- "暖色调, 柔和光线" không có nguồn.
- Ánh nhìn không có đích: thử W2 cho 6/6 ảnh nhìn ống kính.
- "细节丰富" kéo độ nét đều khắp khung.
- Tính từ đánh giá không mang quyết định nào.
