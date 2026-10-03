# 05 — CRAFT: tay nghề xuyên trục

`02_KNOWLEDGE` trả lời "trục này viết thế nào". File này trả lời các vấn đề **không nằm gọn trong một trục**: phong cách, ảnh tham chiếu, câu chuyện, nhiều người, độ thật, series, vệ sinh prompt, sửa lỗi.

Nguồn: chưng cất từ khoảng 400 kinh nghiệm thực hành đọc được (2026), viết lại thành nguyên tắc của T1.
Mỗi mục có nhãn độ tin:
- **[đã thấy]** — có ví dụ đối chứng.
- **[nhiều nguồn]** — nhiều người độc lập cùng nói.
- **[giả thuyết]** — một nguồn, chưa kiểm.

Gặp ảnh thật trái với nhãn thì ghi vào `LEARNINGS.md`.

---

## 1. Phong cách

**1.1 Phong cách = cách ảnh được làm ra, không phải tính từ.** [nhiều nguồn]
- Viết thiết bị, quy trình, điều kiện xem: máy film du lịch, flash thẳng CCD, in riso, khắc gỗ. Đừng viết "cao cấp, có không khí".
- Mỗi cách làm kéo theo cả chuỗi logic hình: hạt, màu, độ cứng flash, lỗi cắt khung.
- **Mỗi ảnh chỉ một phương tiện chụp.** Trộn film với 8K sắc nét là tự mâu thuẫn.

**1.2 Tên phong cách đã mòn kéo về khuôn sáo.** [nhiều nguồn]
- Cyberpunk ra đêm mưa neon tím; editorial tự thêm tên tạp chí và khối chữ; Y2K ra tim, bướm, điện thoại nắp gập; neo-noir ra đêm mưa và người quay lưng.
- Cách tránh: chốt **một mỏ neo cụ thể** (một thời kỳ, một đời máy, một loại lỗi in) hoặc nhãn phụ hiếm về chất liệu/thời đại/phương tiện.
- Thử ngược cũng đúng: phong cách nào chỉ thêm dấu hiệu bề mặt (filter, viền vàng, đèn tím) mà thiếu quan hệ cấu trúc sẽ thành hoá trang.

**1.3 Tên hoạ sĩ → cơ chế.** [nhiều nguồn] Đừng ghi "kiểu Rembrandt". Ghi: số nguồn, vị trí nguồn, nền chìm vào màu gì, vùng tối giữ chi tiết đến đâu.

**1.4 Trộn nhiều phong cách thì chia quyền theo kênh.** [nhiều nguồn] Một phong cách giữ màu, một giữ bố cục, một giữ chất liệu. Xung đột giải bằng thứ hạng, không chồng lên nhau. Mỗi khái niệm dày nghĩa chỉ được trả lời một câu hỏi: ai / chụp thế nào / bố cục / thành phẩm loại gì / để làm gì.

**1.5 Phong cách "thô cố ý" phải tách ba tầng:** phong cách nét, biến dạng hình, nội dung. [giả thuyết] Lệnh "thô một chút" thì model vẽ bẩn; "biến dạng cơ thể" thì mọc thêm tay.

**1.6 Ghi rõ "ảnh thật" khi cần ảnh thật.** [đã thấy] Tên phong cách hay tên nhân vật không đổi được chất liệu ảnh. Thiếu câu 真人写实摄影 thì model hay trả về anime, CG hoặc minh hoạ.

## 2. Ảnh tham chiếu

**2.1 Mỗi ảnh tham chiếu một vai, và nói rõ nó KHÔNG được điều khiển gì.** [nhiều nguồn]
- Ảnh danh tính chỉ trả lời "người này là ai". Nếu không nói, tóc, áo, biểu cảm của ảnh gốc sẽ quay về.
- Ảnh bố cục chỉ cho khoảng cách và độ cao máy.
- Ảnh màu chỉ cho LUT.
- Nhiều ảnh thì xếp thứ hạng ưu tiên.

**2.2 Tách "người là ai" khỏi "bộ ảnh chụp thế nào".** [nhiều nguồn] Hai tham chiếu, hai thẩm quyền: danh tính khác, kế hoạch chụp (cảnh, ánh sáng, tông, trang điểm) khác.

**2.3 Mượn một chiều của ảnh A cho ảnh B:** "chuyển [ánh sáng/màu/…] của ảnh 1 sang ảnh 2, giữ danh tính và nội dung ảnh 2". [đã thấy]

**2.4 Đọc ngược ảnh mẫu: quan hệ không gian trước, danh từ sau.** [nhiều nguồn]
- Khí chất ảnh nằm ở chỗ mặt lộ ra từ đâu, tiền cảnh che phía nào, chỗ cắt khung, ánh sáng tràn tới đâu.
- Chỉ ghi điều thấy được. Không bịa tên ống kính, thương hiệu. Phần tự thêm thì đánh dấu là bổ sung.

**2.5 Không dùng ảnh vừa sinh làm tham chiếu mới.** [nhiều nguồn] Mỗi vòng sửa quay về tham chiếu gốc và biên dịch lại prompt đầy đủ; ảnh vòng trước chỉ để chẩn đoán. Nếu không, sai lệch sẽ khuếch đại qua từng vòng.

**2.6 Ảnh tham chiếu quá chi tiết có thể làm dáng cứng.** [giả thuyết] Muốn dáng sống thì giao cho tham chiếu đúng phần cần giữ.

## 3. Câu chuyện và cảm xúc

**3.1 Phần tử không phải câu chuyện.** [nhiều nguồn]
- Năm đạo cụ đặt chung khung mà không ai dùng thì chỉ là năm danh từ.
- Câu chuyện là **một vật cốt lõi có người tương tác** cộng 1–2 vết tích môi trường. Thêm đạo cụ không thêm chuyện.

**3.2 Bố cục và bằng chứng không được chọi nhau.** [nhiều nguồn]
- Muốn đọc rõ tấm vé thì đừng chọn toàn cảnh xa. Muốn vết trên tường xa rõ thì đừng chọn DoF nông.
- Chọn bằng chứng quan trọng nhất trước, rồi mới chọn cỡ cảnh.

**3.3 Hai tầng của ảnh.** [nhiều nguồn]
- **Ngữ pháp** (bố cục, sáng tối, màu, khoảng trống) quyết định nhìn đâu trước.
- **Ngữ nghĩa** (hành động, biểu cảm, quan hệ với nơi chốn, khoảng cách người chụp) quyết định thấy gì.
- Hỏng một tầng thì tầng kia không cứu được.

**3.4 Công thức biểu cảm:**
- Cảm xúc đơn: chuyện vừa xảy ra + cảm xúc + hướng về ai. [nhiều nguồn]
- Cảm xúc kép: sự kiện + cảm xúc chính/phụ + vì sao che giấu + dấu hiệu lộ ra.
- Khi chỉ muốn đổi nét mặt, thêm câu: "sự kiện chỉ để giải thích biểu cảm, giữ nguyên cảnh và trang phục". Nếu không, model vẽ luôn cả sự kiện. [đã thấy]
- Không dùng emoji để điều khiển biểu cảm. [giả thuyết]

**3.5 Từ trạng thái mơ hồ cần từ chặn đi kèm.** [giả thuyết] Chồng "mơ màng, chếnh choáng, ngập ngừng" làm mặt nhờn và trượt. Viết dấu hiệu: ánh mắt khựng lại, miệng mở rồi dừng.

**3.6 Một sự kiện tách thành ba shot:** xa = hoàn cảnh, trung = quyết định, đặc tả = bằng chứng. [nhiều nguồn] Dùng cho album hoặc chọn shot đắt nhất cho ảnh đơn.

**3.7 Dịch trừu tượng thành hình thái.** [giả thuyết] Kiệt sức, trì hoãn, buông xuôi phải thành ép dẹt, kéo dài, thắt nút, gập xuống. Mắt, miệng, lực thân phải đổi cùng lúc.

## 4. Người và cơ thể

**4.1 Bốn chữ cho dáng: xoay – cong – nối – lộ.** [nhiều nguồn]
- **Xoay:** đầu, ngực, chân là ba mặt. Cả ba cùng hướng ống kính là "mặt phẳng", tức đang tạo dáng.
- **Cong:** một chỗ cong, còn lại thả lỏng.
- **Nối:** cổ tay, mũi chân nối mạch với tay, chân.
- **Lộ:** tay có điểm đặt rõ (搭在大腿外侧) và ngón thấy được.

**4.2 "Tự nhiên, thư giãn" là từ hỏng.** [nhiều nguồn] Model hiểu thành giá trị trung bình: quay đầu nhìn ống kính. Viết thao tác cụ thể.

**4.3 Dáng và điểm nhìn là một cấu hình**, không phải hai danh sách. [giả thuyết] Thân chéo đi với máy hơi cao, gần; silhouette kéo dài đi với máy thấp ngửa lên.

**4.4 Viết dáng theo cỡ cảnh.** [giả thuyết] Cận mặt thì viết vi biểu cảm, hơi thở. Toàn thân thì để model tự do hơn, dáng phục vụ phom và vải bay. Dáng hiếm (đứng một chân) thì liệt kê từng điểm chịu lực.

**4.5 Nhiều người: một sự kiện, một chuỗi phản ứng.** [nhiều nguồn]
- A té nước, B né, C cười. Đừng để mỗi người làm một việc riêng.
- Model coi mọi người là nhân vật chính, nên phải nói ai là môi trường: người phụ chỉ lộ mặt nghiêng, lưng, hoặc một bàn tay ở mép khung.
- Nhóm thì tránh xếp hàng ngang, cùng cỡ, cách đều. Cho một người gần, một người xa, một người bị che, một người đang ra khỏi khung.

**4.6 Hai người: ánh nhìn là quan hệ.** [đã thấy]
- Cùng nhìn ống kính thì ra ảnh nhân viên chụp chung.
- Ba quan hệ khác nhau: nhìn nhau, nhìn vật chung, cố ý tránh nhau.
- Cảnh qua vai (shot/reverse) phải ghi vai người kia ở góc nào, mờ ra sao.

**4.7 Cận mặt cực gần** dễ mất ngũ quan và sinh "bóng ma" ở nửa mặt kia. Thêm mức sàn: 面部结构自然，眼睛位置准确. [giả thuyết]

**4.8 Trang điểm chỉ cần neo nhận dạng nhỏ nhất:** một câu tổng + 2–3 chi tiết. [nhiều nguồn] Liệt kê mắt, mi, môi, má, sống mũi sẽ ra ảnh quảng cáo mỹ phẩm.

**4.9 Động vật:** phản ứng phải do một sự kiện thấy được, đọc qua tai, mắt, đầu, dáng thân cùng lúc. [giả thuyết]

**4.10 Hành động mạnh:** viết chuỗi nhân quả (chuẩn bị → tiếp xúc → phản ứng): ai ra lực, hướng nào, chạm ở đâu, thân kia phản ứng ra sao. [nhiều nguồn] Hiệu ứng chỉ bám vào chi thể thật; chạm trước, rung sau.

## 5. Độ thật và candid

**5.1 Quan hệ người chụp quyết định ánh nhìn.** [nhiều nguồn] Chọn trước một trong các vai:
- Người lạ qua đường: không biết có máy.
- Bạn bè chụp: quen máy, có thể che ống, té nước, quay lại chờ.
- Chân máy tự hẹn giờ: ánh nhìn cố ý đi nơi khác.
- Gương, tự chụp: máy hiện trong ảnh, tay giơ.

Gọi tên thiết bị ("chụp bằng camera gốc điện thoại, tự chụp gần") là công tắc chế độ mạnh hơn liệt kê hiệu ứng.

**5.2 Lỗi có kiểm soát là bằng chứng thật:** "lỗi của người chụp, không phải lỗi của model". [nhiều nguồn]
- Lệch tâm, tóc ra ngoài khung, tiền cảnh che, giọt nước trên ống, nét hụt nhẹ, ánh sáng không đẹp có chủ ý (huỳnh quang phẳng).
- Mỗi ảnh chọn 1–2 lỗi, không rải đủ.

**5.3 Candid lén quan sát:** máy sau vật chắn (cửa, cột, kệ, lá), vật chắn chiếm khoảng 15–40% khung, mép mờ. [giả thuyết]

**5.4 Cụm chặn candid giả:** không dáng người mẫu, không ai nhìn ống kính, không chân dung giữa khung, không nền rối, không mịn da. [nhiều nguồn]

**5.5 Token phương tiện vẽ ra UI.** [nhiều nguồn] CCD/DV/film chỉ để mang nghĩa chất hình. Cấm rõ REC, pin, khung lấy nét, ngày giờ. Brand T1 đã cấm chữ khác, nhưng nên ghi thêm "无相机界面".

**5.6 Model tự "thương mại hoá".** [nhiều nguồn] Nó làm mặt sáng hơn, mắt nét hơn, thêm viền sáng ấm, và giết mất sức mạnh của ảnh dựa vào thiếu sáng, lệch nét, đen đặc. Ảnh kiểu đó phải ghi rõ ý đồ "chủ ý thiếu sáng/lệch nét", kèm mức sàn tối thiểu.

**5.7 Ít hơn thì thật hơn.** [giả thuyết] Không chất đầy cảnh, giữ tạo hình người và ánh sáng tự nhiên thì giống ảnh phố thật hơn bản "điện ảnh tinh xảo". Hai chế độ khác nhau; chọn một.

## 6. Series, biến thể, album

**6.1 Cặp cố định / tự do.** [nhiều nguồn] Khớp đúng 母版锁 / 分镜:
- **Cố định:** danh tính, chất liệu, hệ màu, phong cách, một ảnh đơn.
- **Tự do:** máy, bố cục, động tác, biểu cảm, ánh nhìn.

**6.2 Ép đa dạng.** [nhiều nguồn]
- n biến thể cùng chủ đề sẽ tự sao chép (cùng phòng, cùng ánh sáng, cùng đồ).
- Mỗi bản phải khác nhiều chiều: vị trí máy, tiêu cự, vật che, động tác, hướng người, khoảng cách, cảnh, ánh sáng, có phát hiện máy hay không.
- Cấm chỉ đổi một chiều.

**6.3 Neo nhận dạng bắt mắt giữ tốt; chi tiết nhỏ và trạng thái thì trôi.** [nhiều nguồn] Dây buộc tóc đỏ, áo len đỏ giữ ổn qua nhiều ảnh. Giày cũ bạc màu thì không. Muốn giữ cái gì thì làm nó to và tương phản.

**6.4 Ảnh model tự sinh không phải tài sản tham chiếu tốt.** [nhiều nguồn] Từng tấm đẹp nhưng tỷ lệ, mặt, áo, ngôn ngữ máy khác nhau; đưa vào vòng sau chỉ khuếch đại bất nhất.

## 7. Vệ sinh prompt

**7.1 Prompt dài không hỏng vì dài, mà vì bốn lý do.** [nhiều nguồn]
1. Nhiều giọng chủ đạo trong cùng một chiều (ánh dịu + kịch tính + fill đều + tương phản cao).
2. Tham số giả (ISO, tốc độ) không được tính như vật lý.
3. Không có tuyến chính.
4. Mâu thuẫn chéo (chụp lén + quảng cáo xa xỉ; hạt phim + 8K).

**7.2 Ba tầng ràng buộc.** [nhiều nguồn]
- **Không nhượng:** danh tính, chữ chính xác, cấu trúc sản phẩm, tỷ lệ, số lượng.
- **Ưu tiên:** bố cục, màu, ánh sáng, chất liệu.
- **Tự do:** đạo cụ phụ, chi tiết nhỏ.

Khoá quá sớm tầng tự do làm model cứng.

**7.3 Hai chế độ làm việc.** [nhiều nguồn]
- **Khám phá:** prompt ngắn, cấp cao rõ (thành phẩm, chủ thể, thế giới, mục đích), cấp thấp tự do, chạy nhiều mẫu.
- **Khoá:** giải mã cái làm ảnh đẹp, tách thành quyết định, viết lại đầy đủ.
- Đừng khoá khi chưa biết mình muốn gì.

**7.4 Số đếm phải ghi tường minh:** "đúng chín cái đuôi tách rời", "một sinh vật duy nhất", "không có chân thừa". [nhiều nguồn] Nhiều chi tiết nhỏ không đảm bảo đúng số lượng: bàn cờ vẫn sai số quân, sơ đồ vẫn sai nhãn.

**7.5 Một thông tin, một hệ quy chiếu.** [nhiều nguồn] Chọn trái/phải theo khung hình. Đừng trộn với toạ độ thế giới và hướng giữa nhân vật trong cùng đoạn.

**7.6 Nói "đúng là A, không phải B"** cho vật dễ hiểu nhầm. [nhiều nguồn] Ví dụ: "khung trắng mảnh là ô lấy nét của giao diện, không phải kính mắt".

**7.7 Nhãn danh mục (风格/主体/构图…) khoá vai của từ.** [giả thuyết] Có nhãn thì từ ít lan sang vai khác (ổn định hơn); bỏ nhãn thì từ ảnh hưởng chéo (bất ngờ hơn). Dùng nhãn khi cần kiểm soát, bỏ khi khám phá.

**7.8 Ngân sách diện tích ≠ ngân sách chú ý.** [giả thuyết] Nền chiếm khoảng 60%, trung gian 30%, điểm nhấn 10% diện tích; nhưng thứ hút mắt có thể là 10% đó. Tỷ lệ chỉ là điểm khởi đầu.

## 8. Sửa lỗi

**8.1 Xác định sai ở tầng nào, chỉ sửa tầng đó.** [nhiều nguồn]
- Nhận nhầm danh tính → sửa phân vai tham chiếu.
- Không nhìn nhau → thêm hướng thân và đích nhìn.
- Máy sai chỗ → sửa hình học máy.

Đừng thêm từ chất lượng.

**8.2 Ba câu kiểm nhanh khi ảnh chưa đạt:**
1. Vị trí – nghiêng – cắt khung.
2. Ánh nhìn – cử chỉ – tiếp xúc.
3. Quan hệ ánh sáng – vật liệu.

[nhiều nguồn]

**8.3 Da vẫn nhựa thì kiểm theo thứ tự:** highlight có phủ cả vùng không → ánh sáng có hướng và chuyển bóng không → lúc đó mới xem texture. [nhiều nguồn]

**8.4 Một chi tiết cứ rớt:** rút prompt nền về tối thiểu trước, rồi mới đẩy chi tiết đó lên sớm hơn, thành câu riêng. [giả thuyết]

**8.5 Model kéo về khuôn quen dù đã viết rõ** (lỗi "chuẩn hoá"): lặp lệnh không giúp. Đổi bằng chứng hoặc hình học để khuôn quen trở thành bất khả. [đã thấy]

**8.6 Sửa bằng bước chỉnh ảnh thay vì sinh lại.** [giả thuyết] Ảnh đẹp ánh sáng nhưng hỏng chi tiết có thể đưa qua model sửa ảnh với lệnh ngắn: "sửa chỗ không hợp lý, giữ nguyên ánh sáng và bố cục".

**8.7 Ghi hồ sơ:** prompt thực dùng, model và phiên bản, kết quả, tầng định sửa. Không ghi thì không học được. Xem `LEARNINGS.md`.

## 9. Ghi chú theo generator [giả thuyết, cập nhật theo LEARNINGS]

- **GPT Image:**
  - Hiểu câu tự nhiên tốt, tự bổ sung nhiều.
  - Prompt dày kiểu dán từ model khác dễ thừa.
  - Poster có chữ dễ tự thêm cả hệ thống thông tin (mã vạch, chữ nhỏ).
  - Bản mới có thể thêm chi tiết mà giảm thần thái.
- **Midjourney:**
  - Chủ thể quan trọng nhất đặt đầu câu, làm chủ ngữ.
  - Không mở bằng mệnh lệnh "hãy tạo".
  - Style code/personalization đổi kết quả, nên khoá khi so sánh.
- **Nano Banana:** giữ cảnh và phong cách đồng nhất tốt qua nhiều ảnh; mặc định có thể không ra mặt châu Á nếu không ghi.
- **Chung:**
  - Gõ "chân dung + 中式审美" thì bị kéo về khuê phòng cổ.
  - Muốn Trung Hoa hiện đại thì phải ghi danh từ hiện đại cụ thể.
