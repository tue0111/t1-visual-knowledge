# LEARNINGS — bài học thực chiến

File này có quyền cao hơn `02_KNOWLEDGE.md` khi hai bên mâu thuẫn. Chỉ ghi điều **đã thấy trên ảnh thật**. Mỗi dòng ngắn, có ngày và generator.

## Đã thấy

| Ngày | Generator | Lỗi / phát hiện | Cách xử lý | Độ chắc |
|---|---|---|---|---|
| 2026-10-03 | GPT Image | Prompt đều tay (không có đích nhìn) cho 6/6 ảnh nhìn ống kính. Prompt có câu "người xem là kẻ đứng ngoài" cộng câu ánh nhìn có đích cho 0/6. | Luôn ghi đích nhìn dương. Cinema/candid thêm câu quan hệ người xem trong 母版锁. | cao (1 brief) |
| 2026-10-03 | GPT Image | Mức sàn chỉ đặt cho mặt (暗部保留细节) thì môi trường thành mảng đen 6/6. | Ghi ý đồ vùng tối riêng cho môi trường: vùng nào đọc được, vùng nào được chìm. | cao (1 brief) |
| 2026-10-03 | GPT Image | Cảnh cầu: câu vị trí khẳng định 河岸人行道 cộng câu phủ định 相机不在桥面上, mà 3/3 ảnh máy vẫn ở trên dốc cầu. | Phủ định không đủ. Dùng hình học khiến "trên cầu" là bất khả: chụp ngang vuông góc, cầu chạy ngang khung. | cao về lỗi; cách sửa chưa kiểm |
| 2026-10-03 | GPT Image | Tổng thể W2 chưa chứng minh "phân cấp trục" thắng bản đều tay (đo lường còn lỗi). Cái thắng rõ nằm ở từng câu có bằng chứng (ánh nhìn có đích). | Đừng tin công thức ngân sách; tin câu có bằng chứng nhìn thấy. | vừa |

## Từ thực hành của người khác (chưa tự kiểm, dùng như giả thuyết mạnh)
- Da: "真实皮肤" hay "毛孔" một mình cho ra da sáp. Phải tả phân bố điểm sáng (bóng chỉ ở trán và mũi, còn lại mờ).
- Biểu cảm mạnh tả từng bộ phận thì ra mặt kỳ dị. Viết lý do của cảm xúc.
- "低机位" cho ảnh chi tiết (giày) khiến model ngửa cả người. Độ cao máy tính theo tâm vùng chụp.
- Đổi góc máy so với ảnh mẫu thì ánh sáng "đi theo máy". Cố định nguồn sáng trong cảnh.
- Tên phong cách hoặc tên nhân vật không đảm bảo ảnh thật. Phải ghi 真人写实摄影.
- Thêm grain/noise có thể làm ảnh bẩn hơn ở vài generator. Texture da không phải là grain.

## Mẫu ghi mới
```
| YYYY-MM-DD | <generator> | <lỗi thấy được, bao nhiêu/bao nhiêu ảnh> | <câu đã đổi → kết quả> | cao/vừa/thấp |
```
Khi cùng một bài học lặp lại ≥ 3 lần ở các brief khác nhau, chuyển nó vào mục "Chặn" của trục tương ứng trong `02_KNOWLEDGE.md`.
