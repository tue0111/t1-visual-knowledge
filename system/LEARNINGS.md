# LEARNINGS — bài học thực chiến

File này có quyền cao hơn `02_KNOWLEDGE.md` khi hai bên mâu thuẫn. Chỉ ghi điều **đã thấy trên ảnh thật**. Mỗi dòng ngắn, có ngày và generator.

## Đã thấy

| Ngày | Generator | Lỗi / phát hiện | Cách xử lý | Độ chắc |
|---|---|---|---|---|
| 2026-10-03 | GPT Image | Prompt đều tay (không có đích nhìn) cho 6/6 ảnh nhìn ống kính. Prompt có câu "người xem là kẻ đứng ngoài" cộng câu ánh nhìn có đích cho 0/6. | Luôn ghi đích nhìn dương. Cinema/candid thêm câu quan hệ người xem trong 母版锁. | cao (1 brief) |
| 2026-10-03 | GPT Image | Mức sàn chỉ đặt cho mặt (暗部保留细节) thì môi trường thành mảng đen 6/6. | Ghi ý đồ vùng tối riêng cho môi trường: vùng nào đọc được, vùng nào được chìm. | cao (1 brief) |
| 2026-10-03 | GPT Image | Cảnh cầu: câu vị trí khẳng định 河岸人行道 cộng câu phủ định 相机不在桥面上, mà 3/3 ảnh máy vẫn ở trên dốc cầu. | Phủ định không đủ. Dùng hình học khiến "trên cầu" là bất khả: chụp ngang vuông góc, cầu chạy ngang khung. | cao về lỗi; cách sửa chưa kiểm |
| 2026-10-03 | GPT Image | Tổng thể W2 chưa chứng minh "phân cấp trục" thắng bản đều tay (đo lường còn lỗi). Cái thắng rõ nằm ở từng câu có bằng chứng (ánh nhìn có đích). | Đừng tin công thức ngân sách; tin câu có bằng chứng nhìn thấy. | vừa |
| 2026-11-01 | GPT Image | Cảnh cầu ngói Thanh Toàn: câu hình học khẳng định (相机站在对岸，与桥身成直角，桥在画面上半部水平横穿) cho 2/2 ảnh máy ngang đúng bờ đối diện, không lên mặt cầu. | Xác nhận cách sửa ở dòng cầu 2026-10-03: dùng hình học khiến chỗ đứng sai bất khả, không dùng phủ định. | cao (1 brief, 2 ảnh) |
| 2026-11-01 | GPT Image | 母版锁 ghi 低中饱和 + negative chặn 金色滤镜, nhưng mọi cảnh có mặt trời thấp (bình minh, chiều, hoàng hôn) phần lớn ra vàng cam bão hoà, mặt trời lọt khung kèm tia (khoảng 8/10 ảnh ở 5 cảnh). Cảnh âm u, sương, mưa giữ đúng tông 8/8. | Chữ không kìm được màu khi có mặt trời thấp. Hoặc đưa mặt trời ra ngoài khung sau mây mỏng, hoặc chấp nhận và grade hậu kỳ chung một LUT. | vừa |
| 2026-11-01 | GPT Image | Tỷ lệ người ghi 4–6% thì khoảng một nửa số ảnh ra 10–15% (hang Sơn Đoòng 2/2, hồ Ba Bể 1/2). | Con số % chỉ là hướng; muốn người thật nhỏ thì thêm vật so sánh cụ thể (cao bằng một phiến đá, nhỏ hơn con thuyền) hoặc đẩy máy xa bằng mốc thế giới. | vừa |

## Từ thực hành của người khác
Đã chưng cất vào `05_CRAFT.md` (nhãn [đã thấy] / [nhiều nguồn] / [giả thuyết]). Khi ảnh thật của T1 xác nhận hoặc bác một mục, ghi một dòng vào bảng trên và sửa nhãn ở 05.

## Mẫu ghi mới
```
| YYYY-MM-DD | <generator> | <lỗi thấy được, bao nhiêu/bao nhiêu ảnh> | <câu đã đổi → kết quả> | cao/vừa/thấp |
```
Khi cùng một bài học lặp lại ≥ 3 lần ở các brief khác nhau, chuyển nó vào mục "Chặn" của trục tương ứng trong `02_KNOWLEDGE.md`.
