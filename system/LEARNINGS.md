# LEARNINGS — bài học thực chiến

File này có quyền cao hơn `02_KNOWLEDGE.md` khi hai bên mâu thuẫn. Chỉ ghi điều **đã thấy trên ảnh thật**. Mỗi dòng ngắn, có ngày và generator.

## Đã thấy

| Ngày | Generator | Lỗi / phát hiện | Cách xử lý | Độ chắc |
|---|---|---|---|---|
| 2026-10-03 | GPT Image | Prompt đều tay (không có đích nhìn) cho 6/6 ảnh nhìn ống kính. Prompt có câu "người xem là kẻ đứng ngoài" cộng câu ánh nhìn có đích cho 0/6. | Luôn ghi đích nhìn dương. Cinema/candid thêm câu quan hệ người xem trong 母版锁. | cao (1 brief) |
| 2026-10-03 | GPT Image | Mức sàn chỉ đặt cho mặt (暗部保留细节) thì môi trường thành mảng đen 6/6. | Ghi ý đồ vùng tối riêng cho môi trường: vùng nào đọc được, vùng nào được chìm. | cao (1 brief) |
| 2026-10-03 | GPT Image | Cảnh cầu: câu vị trí khẳng định 河岸人行道 cộng câu phủ định 相机不在桥面上, mà 3/3 ảnh máy vẫn ở trên dốc cầu. | Phủ định không đủ. Dùng hình học khiến "trên cầu" là bất khả: chụp ngang vuông góc, cầu chạy ngang khung. | cao về lỗi; cách sửa chưa kiểm |
| 2026-10-03 | GPT Image | Tổng thể W2 chưa chứng minh "phân cấp trục" thắng bản đều tay (đo lường còn lỗi). Cái thắng rõ nằm ở từng câu có bằng chứng (ánh nhìn có đích). | Đừng tin công thức ngân sách; tin câu có bằng chứng nhìn thấy. | vừa |
| 2026-11-04 | GPT Image (Codex) | Album 7 khung tái dựng từ một bộ snapshot phim. Prompt tả mặt bằng tính từ đẹp, không nói ảnh tham chiếu mặt KHÔNG điều khiển gì, không gọi tên máy chụp → 7/7 ra chân dung người mẫu đã tút, cận, trời và biển đậm. | Gọi tên máy (傻瓜胶片机 + 负片扫描), câu vai tham chiếu "只决定她是谁…不决定…", câu da chưa tút → 21/21 ra snapshot phai. Còn lệch ở khung cận mặt và ở váy: 2/6 ảnh có chân bị xuyên (05 §5.8, §6.6). | vừa (1 series) |
| 2026-11-04 | GPT Image (Codex) | "太阳在画面左侧" hoặc "太阳在她身后偏左" → đĩa mặt trời nằm trong khung 9/9 (3 khung ngày, 6 khung hoàng hôn), khung ngày bị nhuộm thành hoàng hôn. Bản tiếng Anh cùng ý, có thêm "outside the left edge" → 0/3. | Ghi rõ 画外/画内 (05 §7.10). Cách sửa bằng tiếng Trung chưa kiểm. | cao về lỗi |
| 2026-11-04 | GPT Image (Codex) | A/B/C một khung cận người đi tới, 3 ảnh mỗi bản, 6 tiêu chí: A (T1 3 phần, zh) 10/18; B (văn xuôi en, có câu 第一眼 + câu gọi tên chỗ căng) 14/18; C (cấu trúc B viết zh) 14/18. Cấu trúc thắng; ngôn ngữ hoà: en hơn ở vị trí mặt trời và độ thật của da, zh hơn ở số hoa vải và viền sáng. | Giữ luật tiếng Trung. Thêm ba câu tuỳ chọn ở 04 §分镜. Chưa tách được câu nào trong cấu trúc tạo ra khác biệt. | thấp (3 ảnh/bản, 1 khung) |
| 2026-11-06 | GPT Image | 5 khung bỉ ngạn bản phim, prompt keyword "+" (không 3 phần), có khối khoá lặp ở mọi khung và cụm phương tiện 胶片快照+彩色负片扫描+整体褪色+黑位抬起: 5/5 trúng ý đồ lần đầu, chất ảnh như MJ (đen nâng, tiền cảnh hoa mờ, halation). Khung lộ trọn mặt (nằm, góc thẳng trên xuống) bị trẻ hoá. | Khung lộ mặt đẩy 成熟五官与骨相 lên ngay sau cụm cỡ cảnh; bỏ món đồ đọc thành đồng phục (tất cao). | vừa (1 ảnh/khung) |
| 2026-11-09 | GPT Image (prompt do Grok bot viết từ 4 ảnh mẫu) | 4 khung tái dựng (hồ koi chồng ảnh, hiên gỗ xoay 90°, khung cửa đôi, đọc sách bên quạt): bố cục và đạo cụ bám ảnh mẫu 4/4. Khối màu viết thẳng trong prompt (đen nâng xanh olive, highlight hồng đào, sương, rò sáng góc dưới) ra ảnh xong, không cần hậu kỳ. Cá betta đỏ và cobalt trong bể làm hai điểm bão hoà đúng ý. Lệch: prompt 003/004 ghi tóc dài, ảnh mẫu và 001/002 tóc ngang vai, album thành hai người. | Khoá độ dài tóc trong mọi khung của album; ghi tỷ lệ đúng ảnh mẫu (mẫu 2:3, prompt để 3:4). | vừa (1 ảnh/khung) |
| 2026-11-10 | GPT Image | Album cổ trang v1 (hồ, sương, rừng trúc, đình, 7 khung): 母版锁 dài ~80 chữ tả cả một thế giới + cả khung khử bão hoà xanh xám, không có nguồn sáng chính. Người dùng nhận xét: ảnh phẳng, nền quá nhiều gây nhiễu, thiếu chủ thể ánh sáng, khói và bóng tối. | Mỗi khung chỉ một nguồn sáng mạnh sau người; nền ghi "空无一物", tối đa một mảng kiến trúc; bỏ phần tả thế giới khỏi 母版锁. | vừa (nhận xét người dùng) |
| 2026-11-11 | GPT Image | Album khói đỏ và cung điện, 8 khung (xoay trong khói, cận viền sáng, ô ngược sáng, cổng vòm đối xứng, lối tường đỏ nhìn từ trên, đàn tranh giữa đại điện, đàn tranh nhìn thẳng từ trên, sáo trên bậc đá nhìn từ dưới), prompt 270-310 chữ (v1: 455-540), 10-12 mục negative (v1: 14): 8/8 trúng ý đồ lần đầu. Ô gập ở khung nhìn từ trên bị vẽ thành ô mở. Chiều sâu đến từ ba thứ cùng lúc: một nguồn mạnh ngoài khung sau người, khói chỉ sáng nơi ánh chạm, 30-40% diện tích gần đen. Đạo cụ (ô, đàn tranh, sáo) đúng hình 8/8 nhờ nhãn cấu trúc (伞骨清晰, 琴弦平行清晰雁柱整齐). Một người nhất quán nhờ khoá búi tóc nửa đầu, dải lụa đỏ, áo đỏ; trộn khung ngang và dọc trong một album vẫn đều. | Giữ khuôn ngắn "ánh sáng trước": 母版锁 chỉ khoá người, ánh sáng, nền trống, tiền cảnh; mặt ngược sáng thì ghi "不补光+五官可辨" và đặt "面部补光" vào negative; đổi bối cảnh bằng một mảng kiến trúc, không tả cả cung điện; hậu kỳ chỉ nâng sáng nhẹ ảnh tối (gamma 0,78-0,90 trên độ sáng, hue giữ nguyên) và hạ đỉnh đỏ cháy. | vừa (8 khung, 1 ảnh/khung) |

## Từ thực hành của người khác
Đã chưng cất vào `05_CRAFT.md` (nhãn [đã thấy] / [nhiều nguồn] / [giả thuyết]). Khi ảnh thật của T1 xác nhận hoặc bác một mục, ghi một dòng vào bảng trên và sửa nhãn ở 05.

## Mẫu ghi mới
```
| YYYY-MM-DD | <generator> | <lỗi thấy được, bao nhiêu/bao nhiêu ảnh> | <câu đã đổi → kết quả> | cao/vừa/thấp |
```
Khi cùng một bài học lặp lại ≥ 3 lần ở các brief khác nhau, chuyển nó vào mục "Chặn" của trục tương ứng trong `02_KNOWLEDGE.md`.
