# 09 — SHOT VOCAB: kho từ vựng khung

**Đây là kho để tra, không phải ma trận phải điền kín.** Quy trình dựng album nằm ở `10_CREATIVE_ALBUM.md`: giao việc cho từng khung trước, rồi mới sang đây lấy máy và bố cục phục vụ việc đó.

Lớp mỏng như `06`, `07`. Mở khi người dùng xin **album sáng tạo** (nhiều khung, cùng một người hoặc một thế giới) và cần danh sách khung không lặp nhau. Không nạp mọi lần.

**Nguồn và nhãn.** [quan sát, chưa thử ảnh] Rút từ 5 clip "khẩu quyết" ngắn dạy chụp chân dung (lời Việt, phiên âm máy nên từng chữ có thể lệch), viết lại bằng lời T1 và đổi sang keyword tiếng Trung. Đây là **bộ từ khoá cho mắt người**, chưa ai kiểm model ảnh có phản ứng đúng. Khi thử, ghi `LEARNINGS.md` rồi sửa nhãn ở đây. `LEARNINGS` và `05 §6.2` (ép đa dạng) cao hơn file này.

## Cách dùng: lập bảng khung trước khi viết prompt

1. Chọn số khung n. Mỗi khung điền **một giá trị cho mỗi trục** dưới đây.
2. Với album **hình dạng khám phá** (`10` §4): hai khung bất kỳ khác nhau ở **ít nhất 3 trục**, trong đó có trục A (cỡ cảnh) hoặc B (máy). Các hình dạng khác có luật riêng: biến tấu chỉ đổi một biến, loại hình giữ máy giống hệt, chuỗi kể chuyện giữ hướng và mốc.
3. Mỗi khung chọn **một lệnh chính** ở trục C (đầu/ánh nhìn) khớp với B (xem bảng ghép). Đừng chọn ngẫu nhiên: máy và đầu phải đi cùng nhau.
4. Chỉ 母版锁 giữ người, ánh sáng, nền. Mọi trục dưới đây thuộc 分镜 (xem `05 §6.1`). Với keyword thì lặp khối khoá ở đầu mỗi dòng (`08`).
5. Tối đa 1 giá trị mỗi trục mỗi khung, và tối đa 2 trục "kể chuyện" (E, F) mỗi khung. Nhiều hơn thì giành nhau.

## Trục A. Cỡ cảnh và khoảng trống
| Giá trị | Keyword | Dùng khi |
|---|---|---|
| Toàn cảnh, người nhỏ, chừa trống | 远景+人物占画面很小+大面积留白 | khung mở album, tạo hơi thở |
| Cảnh rộng, chủ thể lệch một phía | 全景+人物位于画面三分之一处+另一侧留出呼吸空间 | khung thở, có hướng nhìn vào chỗ trống |
| Trung cảnh | 中景+腰部以上 | khung nối |
| Cận, đặt giữa, nền gọn | 近景+人物居中+背景简洁 | khung nhấn, cần mặt |
| Đặc tả | 特写+从头顶到锁骨 | khung cảm xúc, cần khoá `五官可辨` |

## Trục B. Điểm đứng máy
[quan sát, chưa thử ảnh] cho các giá trị từ "Thẳng trên xuống" trở xuống, và cho trục D, H mở rộng bên dưới.

| Giá trị | Keyword | Cảm giác |
|---|---|---|
| Ngang mắt | 平视机位 | gần, đời thường |
| Máy thấp | 低机位仰拍 | khí chất, uy, cao |
| Máy cao | 高机位俯拍 | yên tĩnh, cô độc, nhỏ bé |
| Sát đất | xem `07 AD-10` | |
| Sau lưng | 背面拍摄 | bí ẩn, đang đi |
| Nghiêng ba phần tư | 侧前方四分之三 | tự nhiên |
| Thẳng trên xuống | 正上方垂直俯拍+地面布局清楚 | đọc bố cục mặt đất (bàn cờ, ruộng bậc thang, sàn xưởng) |
| Cao ~45° | 约45度高角度俯拍+人物被环境包围 | bị không gian đè, nhỏ bé |
| Thấp ~30° | 约30度低角度仰拍 | khí chất, uy, nhẹ hơn máy thấp hẳn |
| Tele xa | 135毫米远机位+纵深被压缩 | nền dồn sát người (đổi **chỗ đứng**, không chỉ tiêu cự) |
| Rộng thấp | 20毫米广角+低机位约半米+透视夸张 | vật gần phình, không gian vút |
| Rất gần | 极近距离+只容纳头面部 | đặc tả mặt, nền tan hẳn |
| Một điểm tụ đối xứng | 一点透视+严格对称+广角低机位 | trang nghiêm, lạnh (hành lang, cổng, sân ga) |

Tiêu cự (`35毫米`, `85毫米`) chỉ là **góc thu**. Phối cảnh (vật gần phình hay nền dồn sát) đổi theo **chỗ máy đứng**: muốn nền dồn sát thì ghi máy ở xa cộng tiêu cự dài, muốn không gian vút sâu thì ghi máy sát người cộng tiêu cự ngắn, và giữ cỡ người trong khung làm mốc. Góc thấp kèm nền cao (toà nhà, cổng, cây) cho phối cảnh vút lên; có thể thêm `广角` để vật gần phóng đại.

## Trục C. Đầu, vai và ánh nhìn theo máy (bảng ghép)
Mỗi mẫu là một cặp "máy → tư thế đầu". Dùng đúng cặp để tránh cứng.

| Máy | Đầu | Keyword mẫu |
|---|---|---|
| Chính diện | hơi cúi, mắt ngước | 正面+微低头+眼神上抬看向镜头 |
| Nghiêng ba phần tư | hơi ngẩng | 侧前方+下巴微抬+目光越过镜头 |
| Sau lưng | quay đầu nhìn lại | 背对镜头+回眸+侧脸半露 |
| Máy cao | nghiêng đầu | 俯拍+头微侧+目光向上 |
| Máy thấp | vươn cổ, cằm nâng | 仰拍+下巴抬起+目光平视远处 |

Ánh nhìn (chọn một): nhìn vào ống kính 看向镜头 · nhìn ra ngoài khung 目光落在画外 · mắt nửa rủ 双眼半垂 · nhìn vật trong khung 看着手中的物件. Hướng nhìn là cách rẻ nhất để tạo chiều sâu cảm xúc: ghi thành câu riêng, không gộp vào danh sách tính từ.

## Trục D. Bố cục và chiều sâu
| Giá trị | Keyword |
|---|---|
| Tiền cảnh mờ có hướng | 前景失焦的……从一侧斜伸入画面，斜线指向人物 (xem `07 AD-06`) |
| Khung trong khung | 透过门洞/窗框/拱门看向人物，框内是主体 |
| Đường dẫn | 地面/墙线/廊道向人物汇聚 |
| Đường chéo | 构图沿对角线，人物位于对角线一端 |
| Đối xứng | 对称构图，人物居中 |
| Nằm, thấp | 人物侧卧/半坐在地面 (hợp với máy cao hoặc sát đất) |
| Deep focus | 小光圈+前景与主体同时清晰 (ngược thói quen nền mờ; khi tiền cảnh cũng kể chuyện) |
| Nhìn xuyên khung cửa | 镜头位于门框之外+透过开口看见人物 |
| Dọc hành lang cột | 沿两列柱子之间的中轴纵深+人物在尽头 |
| Vật che gần, người lộ sau | 近景柱子/货架遮挡一侧+人物从遮挡后显露 |
| Nhìn qua vai | 从人物肩后看向另一侧对象+前景肩部与主体分层 |
| Hai người, vai che gần | 近处保留一人肩部轮廓+远处完整呈现另一人 |
Mỗi khung chọn một. Khung có đường dẫn cần nền sạch, không thì đường dẫn thành nhiễu.
Ảnh vẫn phẳng sau khi chọn: soát lớp theo `14_DEPTH_AND_PARALLAX.md` §2 và §9. Ảo giác (gương, bóng, tỷ lệ, tranh thành vật, khúc xạ): `14` §6. Album cứ ra cùng một kiểu khung: bảng xoay `14` §7.

## Trục E. Kể chuyện nhỏ (chọn tối đa một)
Tóc bay vài sợi 风吹起几缕发丝 · tà áo hoặc lụa bay 衣袖与纱向一侧飞扬 · đang bước đi 正走向…… · quay đầu 回眸 · tay chạm vật 指尖轻触…… · dừng lại giữa việc 动作停在半途. Chọn cái hợp thế giới, và khoá chiều của gió trong 母版锁 nếu album có gió.

## Trục F. Không khí
Dùng `07 ATMOSPHERE_DEVICES` (viền sáng, sương, khoảng tối, nguồn ấm). Trục này thường là luật cả album nên nằm ở 母版锁; nếu đổi theo khung thì chỉ đổi **hướng** nguồn sáng, không đổi loại.

## Trục G. Chất ảnh (nhẹ, mô phỏng hậu kỳ)
| Muốn | Keyword | Ghi chú |
|---|---|---|
| Mềm hơn | 柔焦/边缘柔和，对比度偏低 | đừng cộng với viền sáng gắt |
| Hoài cổ | 整体褪色+黑位抬起 (đã thấy, `LEARNINGS 2026-11-06`) | |
| Có chất | 胶片颗粒 | một mức cho cả album |
| Da vàng, ảm | 白平衡偏冷一点 | chỉ khi mặt ám vàng |
| Ảnh tối | 画面整体偏暗但主体可辨 | nâng sáng nhẹ ở hậu kỳ (`LEARNINGS 2026-11-11`) |
Chất ảnh là luật album: đặt trong 母版锁, không đổi theo khung.

## Trục H. Khung nối (cho hình dạng chuỗi kể chuyện, `10` §4)
[quan sát, chưa thử ảnh] Mỗi dòng là một cặp hoặc bộ ba khung, không phải một khung. Viết **sổ trạng thái** trước, rồi dán nó vào mọi khung của chuỗi.

| Mẫu | Cách viết hai khung | Kiểm bằng |
|---|---|---|
| Sổ trạng thái | ghi trục hành động, hướng màn hình, hướng nhìn, vị trí đạo cụ, mốc nền: 人物始终向画面右侧走，工具箱始终在其右手边 | đặt hai khung cạnh nhau: trái–phải, tay cầm, phía cửa không đảo |
| Mở rộng → vào gần | khung 1 `远景交代环境，人物很小`; khung 2 cùng nơi `中景` | mốc nền chung còn thấy |
| Insert | giữa hai khung người, một khung `只拍手与道具细节` | cùng vật, cùng tay, cùng ánh sáng |
| Hướng nhìn nối | khung 1 `她望向画面右侧画外`; khung 2 vật ở **phía tương ứng** (右侧窗台上的煤油灯) | hướng nhìn khớp phía |
| Phản ứng | khung người nghe, không cắt ngang hành động | nét mặt theo sự kiện khung trước |
| Qua vai và ngược lại | khung 1 qua vai A thấy B; khung 2 qua vai B thấy A | **cùng một phía trục 180°** |
| Vượt trục | máy vòng ra sau người | chỉ sau khi đã có mốc tái định hướng |
| Khớp hình | hai khung khác nơi nhưng cùng vị trí và hình khối chủ thể | hình khối chủ thể trùng vị trí |
| Khung cuối cho chồng mờ | ít chuyển động, nhiều khoảng trống | dùng cho khung kết |

Bẫy: model lật gương làm người đổi tay cầm hoặc đảo lối đi. Có sổ trạng thái thì ghi lại từng dòng của nó ở mỗi khung.

## Theo tỷ lệ khung [giả thuyết, chưa thử ảnh]
Cùng chiều cao H: 2.39 rộng 2.39H, 1.85 rộng 1.85H, 4:3 rộng 1.33H, 9:16 rộng 0.56H. Tỷ lệ là vùng chứa, không mang cảm xúc.
- **2.39**: hơn 1.85 khoảng 0.54H bề ngang. Dành phần thừa cho quan hệ, đường đi, điểm đến (人物在左侧向右走，右侧留出将要抵达的门和空地). Nếu phần thừa chỉ là nền rỗng thì 1.85 đủ.
- **4:3**: người và vật đứng sát nhau.
- **9:16**: ưu tiên chiều cao. Xếp vật trước, sau, trên, dưới người thay vì cạnh người (站在下半部，抬手触到上方的铃).
- **Cổng crop**: cắt giữa từ 2.39 sang 9:16 chỉ giữ 0.5625/2.39 ≈ 23,5% bề ngang. Hai việc xa nhau theo ngang không vào cùng ô được, nên **dàn lại** (đổi chỗ người, vật hoặc máy), không trượt ô crop. Mặt, tay, điểm chạm, đích nhìn, mốc nền phải nằm trong vùng giao.
- Ghi tỷ lệ đích và vùng có nội dung. Đừng lấy tên kiểu khung làm nội dung: `电影宽银幕` hay sinh hai dải đen và cắt chân tay. Mỗi tỷ lệ một prompt riêng, giữ danh tính và thế giới. Xem `06 FG-14`.

## Mẫu bảng khung (8 khung)
Một **ví dụ của hình dạng khám phá**. Cột VIỆC lên đầu (`10` §5): giao việc trước, rồi mới chọn các trục.

| # | VIỆC | A | B | C | D | E |
|---|---|---|---|---|---|---|
| 1 | Mở | toàn cảnh, người nhỏ | máy cao | nhìn ra ngoài khung | đường dẫn | đang bước |
| 2 | Lộ | cận | ngang mắt | chính diện, cúi, ngước mắt | khung trong khung | tóc bay |
| 3 | Rẽ | trung cảnh | sau lưng | quay đầu | tiền cảnh có hướng | tà áo bay |
| 4 | Thở | cảnh rộng lệch | máy thấp | nhìn vật trong khung | đường chéo | tay chạm vật |
| 5 | Đỉnh | đặc tả | ba phần tư | mắt nửa rủ | đối xứng | — |
| 6… | | | | | | |
Đủ khác nhau thì trộn khung ngang và dọc cũng được (`LEARNINGS 2026-11-11`).

## Bẫy
- **Sinh đôi:** chỉ đổi A hoặc C. Chữa: đổi thêm B và D.
- **Đầu không khớp máy:** máy thấp mà ghi cúi đầu thì cổ và cằm lạ. Dùng bảng ghép C.
- **Quá nhiều trục E, F cùng một khung:** các hướng giành nhau.
- **Toàn cảnh mà vẫn đòi mặt rõ:** người nhỏ không còn mặt. Chọn một.
- **Chữ chuyển động máy trong prompt ảnh** (推镜, 摇镜, 甩镜): dễ sinh nhoè hoặc góc tuỳ tiện. Tả **trạng thái tĩnh**: máy đứng đâu, vật che ở đâu, lớp gần–xa nào.
