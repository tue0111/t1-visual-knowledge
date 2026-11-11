# 07 — ATMOSPHERE DEVICES: thủ pháp không khí, tra khi cần

Lớp mỏng như `06`. Không nạp mọi lần. Mở khi brief hay ảnh tham chiếu cần: viền sáng ngược, sương, khoảng tối lớn, một nguồn ấm giữa nền lạnh, tiền cảnh lấn khung, che mặt mà vẫn kể chuyện, lụa mỏng, chuyển động, góc máy sát đất. Bỏ mục brief không dính.

## Hai nhãn, đọc riêng

- `source_support`: **[quan sát]** = thấy trên ảnh minh hoạ người khác chia sẻ (cổ trang, tiên hiệp, 12 ảnh) cùng một bài tóm 4 thủ pháp, viết lại bằng lời T1. Ảnh và bài gốc không lưu ở repo.
- `image_evidence`: xem bảng "Trạng thái thử" cuối file. Mục chưa có dòng trong bảng là **UNTESTED** trên ảnh T1. Khi T1 tự sinh và thấy kết quả, ghi `LEARNINGS.md` rồi cập nhật bảng.

Theo người chia sẻ, ảnh của họ ra từ model ảnh gọi thẳng qua API (không qua skill sinh ảnh mặc định của agent). T1 không dùng đường đó, nên mọi câu mẫu dưới đây phải chạy được bằng prompt thường. `LEARNINGS.md` và mắt người dùng ghi đè file này.

## Cách dùng

1. Chọn **một thủ pháp chính** và tối đa **hai phụ**. Nhiều hơn là các thủ pháp giành nhau, ảnh rối.
2. Thủ pháp là luật cả album (sương, bảng màu, nguồn sáng) thì đặt trong 母版锁; thủ pháp riêng một khung (cử chỉ, tiền cảnh, góc máy) đặt trong 分镜.
3. Câu mẫu là khung, sửa vật, hướng, tỷ lệ cho khớp brief. Đừng chép nguyên nếu thế giới khác.
4. Mỗi thủ pháp có cột **Bẫy**: model hay kéo lệch thế nào. Thêm vào negative đúng mục cần, giữ tổng ≤ 14.
5. Kiểm bảng **Cặp xung đột** cuối file trước khi giao.

## Nhóm A. Ánh sáng (K1)

| ID | Nguyên lý | Hỏi | Dấu kiểm thấy được | Bẫy | Câu mẫu 中文 [giả thuyết] |
|---|---|---|---|---|---|
| AD-01 | Nguồn sáng nằm sau người, đi qua sương thành quầng. Tóc và mép áo sáng thành một viền, mặt cố ý để chìm. Viền sáng tách người khỏi nền mà không cần đèn mặt. | Nguồn ở đâu sau người, cao bao nhiêu, sương dày tới đâu? | Viền sáng chạy theo mép tóc, vai, tay áo. Mặt trong bóng nhưng còn đọc được. Quầng sáng có hình (tia, đĩa, chùm) chứ không phủ đều. | Model tự bật đèn mặt, mất viền. Hoặc cháy trắng nửa khung. | 唯一主光源在人物身后画外略高处，光穿过烟雾形成光晕与光柱，发丝与肩袖边缘一圈亮边，面部留在暗部但五官可辨，不补光 |
| AD-02 | Một nguồn ấm nhỏ đặt sát điểm cần nhìn (mắt, tay) trên nền xám xanh. Mắt người xem đi thẳng vào vùng ấm. | Vật phát sáng là gì, đặt cách mắt bao xa? | Vùng ấm nhỏ hơn khoảng 1/6 khung, rơi đúng mắt và đầu ngón tay. Phần còn lại lạnh. | Ánh ấm loang cả khung thành hoàng hôn. Thêm nguồn ấm thứ hai tranh chỗ. | 唯一暖光源是她手中贴近眼睛的灯笼，暖光只照亮眼周与指尖，其余沉入青灰暗部 |
| AD-03 | Vật trong khung tự phát sáng và là nguồn chính trên nền gần như đen. Hướng sáng trên người phải đi ra từ vật. | Vật gì tự sáng mà hợp thế giới (hoa, đèn, nước, đá)? | Mặt hướng về vật sáng hơn, bóng đổ ra xa vật. Ngoài vùng vật chiếu tới là đen. | Model thêm đèn ngoài khung, vật sáng thành miếng dán không chiếu lên ai. | 画面唯一光源是她手中一朵发出冷白微光的莲花，光只照亮手指、下颌与近处衣褶，其余全黑 |

## Nhóm B. Không khí và khoảng trống (K6, K3)

| ID | Nguyên lý | Hỏi | Dấu kiểm thấy được | Bẫy | Câu mẫu 中文 [giả thuyết] |
|---|---|---|---|---|---|
| AD-04 | Sương có tầng: gần đặc, xa loãng, có chỗ sáng chỗ tối, nằm kẹp giữa các lớp cảnh. Sương tạo chiều sâu chứ không phải kính mờ. | Sương nằm giữa những lớp nào? Người có cần nổi khỏi sương không? | Thấy ít nhất hai lớp sương khác nhau. Viền người vẫn rõ. | Sương phủ đều cả khung thành ảnh đục. Sương nuốt mất người. | 烟雾分层，近处浓远处淡，烟雾有明暗起伏，夹在前景、人物与背景之间，人物轮廓清楚不被吞没 |
| AD-05 | Người rất nhỏ, khoảng tối hoặc trời chiếm phần lớn khung, một vật sáng (trăng, đèn) neo khoảng trống. Im lặng nằm ở diện tích trống. | Khoảng trống chiếm bao nhiêu, cái gì neo nó? | Người cao khoảng 1/7 khung hoặc nhỏ hơn. Khoảng trống không bị lấp chi tiết. Vài điểm ấm nhỏ trong nền lạnh. | Model phóng to người hoặc nhét thêm cây, mây, chim cho đầy. | 人物约占画面高度七分之一，上方约四成为纯暗夜空留白，一轮巨大满月偏向一侧，冷月光中点缀两三盏暖灯，水面倒影占画面下半 |

## Nhóm C. Che và dẫn (K3, K5, K7)

| ID | Nguyên lý | Hỏi | Dấu kiểm thấy được | Bẫy | Câu mẫu 中文 [giả thuyết] |
|---|---|---|---|---|---|
| AD-06 | Tiền cảnh mờ (lá, cánh hoa, quạt, lụa) lấn vào từ một mép và có **hướng**: đường chéo của nó chỉ về người. Khác với tiền cảnh làm khung đều bốn phía. | Vật gì trong thế giới này có thể ở sát ống kính? Nó chỉ về đâu? | Tiền cảnh chiếm khoảng 1/4 đến 1/3 khung, từ một hoặc hai mép, đường chéo hướng vào người. Mặt không bị che. | Tiền cảnh rải đều như khung tranh. Che mất mặt. | 失焦的竹叶从画面左下斜伸入画面约三分之一，叶片的斜线指向人物，人物面部不被遮挡 |
| AD-07 | Che mặt nhưng giao việc kể chuyện cho cử chỉ. Mặt nạ trơn có nét cười đi kèm một cử chỉ ngược tông (giơ hai ngón, ngón tay "suỵt"); quạt che nửa mặt; mạng mỏng; vành nón che mắt. | Mặt bị che thì cái gì nói thay: tay, tư thế, vật? | Vật che có cấu trúc thật (nan quạt, vành nón, mép mặt nạ). Cử chỉ rõ, đủ ngón. | Mặt nạ ra mẫu có sẵn của phim hoặc biểu tượng. Tay cử chỉ lỗi ngón. Model lột vật che để khoe mặt. | 脸上戴着一张原创素白面具，只有细弯的笑眼和一道微笑嘴缝，无图案无文字，右手在面具旁比出剪刀手，五指完整 |
| AD-08 | Lụa mỏng làm hai việc: một dải lụa trong suốt uốn chữ S qua khoảng tối để dẫn mắt; một lớp mạng hoặc rèm trước mặt hay trước nguồn sáng làm kính lọc mềm ngay trong cảnh. | Lụa đang dẫn mắt hay đang khuếch tán sáng? | Lụa có lớp xuyên sáng, có mép. Dải chữ S đi từ mép khung tới người. | Lụa thành khối đặc. Dải lụa xuyên qua thân người. | 一条半透明青色薄纱在暗空中绕成蛇形曲线，从画面左上延伸到人物身边，薄纱有透光层次，不遮脸 |

## Nhóm D. Chuyển động và góc máy (K7, K2)

| ID | Nguyên lý | Hỏi | Dấu kiểm thấy được | Bẫy | Câu mẫu 中文 [giả thuyết] |
|---|---|---|---|---|---|
| AD-09 | Ba đường trở lên (vật cầm, tóc bay, tà áo) chạy theo **các hướng khác nhau**. Nhoè chỉ ở phần đang vung, mặt và thân nét. Cảm giác động tác chưa dứt. | Phần nào đang chuyển động, phần nào phải đứng yên? | Các đường chéo không song song. Nhoè giới hạn ở tay và vật cầm. | Nhoè luôn cả mặt. Mọi đường song song thành ảnh gió thổi. | 手中器物、飞起的长发与衣袂形成三个不同方向的斜线，只有挥动的手臂与所持之物带运动模糊，面部与躯干清晰 |
| AD-10 | Máy sát mặt đất ngước lên, người chống một tay xuống đất. Bụi và lá bị hất tung. Mép áo choàng tối rã thành sợi khói mực. | Mặt đất có gì để bắn lên? Phần áo nào được phép tan? | Đường chân trời thấp, mặt đất chiếm phần dưới khung, tay chạm đất rõ. Chỉ mép áo tan, thân còn nguyên. | Khung cắt cụt chân. Khói nuốt cả người. | 相机贴近地面仰拍，她单手撑地半蹲，落叶与尘土被扬起，黑色斗篷边缘碎成丝缕烟墨飘散，面部被斗笠遮住 |

## Cặp xung đột

| Cặp | Vì sao | Cách giữ cả hai |
|---|---|---|
| AD-01 + AD-04 dày | Sương dày phía sau người nuốt viền sáng. | Sương dày ở tiền cảnh và chân, loãng ngay sau người. |
| AD-05 + AD-06 | Tiền cảnh lấn khung ăn mất khoảng trống. | Tiền cảnh chỉ ở góc dưới, khoảng trống giữ ở nửa trên. |
| AD-07 + AD-09 | Nhoè chuyển động làm cử chỉ mất nghĩa. | Tay làm cử chỉ phải nét; nhoè chỉ ở tay còn lại hoặc vạt áo. |
| AD-02 + AD-03 | Hai nguồn trong khung tranh nhau. | Chọn một. |
| AD-10 + khung dọc 9:16 | Sát đất cần bề ngang để thấy bụi và hướng lao. | Ưu tiên 16:9; khung dọc thì cho người chiếm nửa dưới. |

## Ghi chú vận hành

- **Khung nghiêng:** sinh thẳng, nghiêng ở hậu kỳ. Nghiêng 15° mất khoảng 24% cạnh, 30° mất khoảng 35%.
- **Vật cầm là kiếm, dao:** Midjourney từng review tài khoản vì các chữ này, kể cả trong negative. Chạy MJ thì đổi sang quạt xếp, ô gập, dải lụa. GPT Image giữ được.
- **Sương và hậu kỳ:** đã viết sương, viền sáng, rò sáng trong prompt thì hậu kỳ chỉ chỉnh nhẹ, đừng cộng thêm cùng lớp.

## Trạng thái thử (cập nhật 2026-11-11)

Bằng chứng: album khói đỏ và cung điện, GPT Image, 8 khung, mỗi khung 1 ảnh, người dùng duyệt bằng mắt. Chi tiết trong `LEARNINGS.md` và `examples/D_smoke_backlight_hanfu.txt`.

| ID | Trạng thái | Khung đã thử và ghi chú |
|---|---|---|
| AD-01 viền sáng ngược qua sương | **ĐÃ THỬ, đạt** | 6/6 khung dùng (xoay trong khói, cận viền sáng, ô ngược sáng, cổng vòm, bậc đá, lối tường đỏ). Viền sáng bám mép tóc, vai, tay áo; mặt vẫn đọc được khi ghi "不补光" cùng "五官可辨". |
| AD-04 sương nhiều tầng | **ĐÃ THỬ, đạt** | Sương chỉ sáng nơi ánh chạm khi viết "烟雾只在光照到的地方发亮其余隐入黑暗"; sương thành cột sáng ở khung đại điện. |
| AD-06 tiền cảnh lấn khung có hướng | **ĐÃ THỬ, đạt** | Dải lụa đỏ mờ ở góc dưới hoặc một bên, đường chéo chỉ về người; không che mặt. |
| AD-07 che mặt bằng vật | **ĐÃ THỬ một phần** | Ô giấy dầu hạ thấp che gần hết mặt, chừa cằm và môi, ô được rọi sáng từ sau: đạt. Mặt nạ + cử chỉ chưa thử. |
| AD-08 lụa mỏng uốn lượn | **ĐÃ THỬ, đạt** | Đuôi váy trải thành một dải chữ S hoặc một vòng tròn ở khung nhìn từ trên; lụa có lớp xuyên sáng. |
| AD-09 nhoè chuyển động cục bộ | **ĐÃ THỬ một phần** | Khung xoay: tay áo và tóc bay, thân và mặt vẫn nét. Chưa thử vật cầm đang vung. |
| AD-02, AD-03, AD-05, AD-10 | UNTESTED | Chưa có khung nào: nguồn ấm sát mắt, vật tự sáng làm nguồn, người tí hon, sát đất. |
