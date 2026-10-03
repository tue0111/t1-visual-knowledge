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

[比例。相机位置（世界参照物）、高度、距离、取景到身体哪里。]
[主轴：2–4句，主体证据 + 环境证据 + 底线。]
[副轴：每轴一句。]
[一句反吸引子（需要时）。]

【通用负面提示词】

[主轴的真实失败 + 解剖 + 材质，有目标，不堆砌。]
<system/brand_negative.txt>
```
Album: giữ một 母版锁 và một negative, thêm nhiều khối `【分镜 · …】` ở giữa.

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
