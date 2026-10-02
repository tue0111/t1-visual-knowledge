# K3 — BỐ CỤC & ĐƯỜNG ĐỌC MẮT

status: v0.1 CANDIDATE · author: Claude · date: 2026-10-02
Nhãn: [VẬT LÝ/THỊ GIÁC] cơ chế nhìn đã có nghiên cứu · [THỰC HÀNH] quy ước nghề · [GIẢ THUYẾT-AI] cách model phản ứng, cần test.
Liên quan: `K1_LIGHT.md` (sáng/tối kéo mắt), `K2_CAMERA.md` (máy, khung, tiền cảnh), `notes/2026-10_LIGHT_POSTER_CINEMA.md`.

---

## 0. Câu lõi

**Bố cục = trả lời "mắt người xem đi đâu trước, rồi đi đâu, rồi dừng ở đâu".** Không phải "quy tắc một phần ba". Mỗi ảnh cần một điểm vào, một đường đi, một chỗ dừng. Ba thứ đó phải tới từ **đặc tính nhìn thấy được** (sáng, tương phản, mặt người, hướng nhìn, đường dẫn), không phải từ lời mô tả "bố cục hài hoà".

## 1. Thẻ đường đọc 5 câu

1. **Điểm vào:** mắt chạm vào đâu đầu tiên (vùng tương phản cao nhất, hay mặt)?
2. **Chủ thể:** chủ thể là ai/cái gì, và nó có phải điểm vào không? Nếu không, vì sao?
3. **Đường đi:** từ điểm vào, mắt được dẫn đi bằng gì (đường dẫn, ánh nhìn, hướng chỉ, chuỗi lặp)?
4. **Chỗ dừng:** mắt kết thúc ở đâu (chi tiết thưởng, vùng tối, mắt của sinh vật)?
5. **Chỗ thở:** khoảng trống nào cho mắt nghỉ (không gian âm, vùng nền yên)?

Câu 1 và 2 lệch nhau là lỗi phổ biến: màu đẹp hoặc ánh sáng mạnh kéo mắt ra ngoài chủ thể.

## 2. Cơ chế

### 2.1 Hai giai đoạn: bị kéo trước, bị dẫn sau [THỊ GIÁC]
- Giai đoạn 1 (nhanh, tự động): mắt bị kéo bởi **tương phản sáng, cạnh sắc, mật độ chi tiết, màu bão hoà, mặt người**. Ở bước này hướng nhìn của nhân vật chưa có tác dụng.
- Giai đoạn 2 (diễn giải): sau khi nhận ra mặt/biểu cảm, **hướng nhìn và hướng chỉ** mới dẫn mắt. Thông tin này từ bài tổng hợp BrainSight về gaze cueing (nguồn thứ cấp, dạng marketing; hiệu ứng "mắt người theo hướng nhìn" là hiện tượng đã biết, nhưng thứ tự hai giai đoạn trong bài là mô hình diễn giải, không phải định luật).
- Hệ quả viết prompt: muốn mắt tới đạo cụ/sinh vật bằng ánh nhìn, **trước hết phải làm điểm vào là mặt người** (sáng, nét, đủ lớn), sau đó cho ánh nhìn hướng tới vật. Gaze không cứu được một cấu trúc yếu.

### 2.2 Đường dẫn (leading lines) [THỊ GIÁC, bằng chứng yếu]
- Nghiên cứu eye-tracking (Journal of Eye Movement Research 2024, 34 người, 30 ảnh đen trắng có đường dẫn): ảnh có chủ thể rõ cho **ít điểm dừng hơn nhưng lâu hơn**, ít chuyển động mắt, và được chấm thẩm mỹ cao hơn và "có hướng" hơn.
- Giới hạn: thử nghiệm không có nhóm đối chứng không đường dẫn, người tham gia 18–25 tuổi, ảnh đen trắng. Tức là chỉ cho biết **đường dẫn + chủ thể rõ** tốt hơn **đường dẫn không chủ thể**, chưa chứng minh đường dẫn tự nó hiệu quả.
- Hệ quả: đường dẫn phải **kết thúc ở chủ thể**; đường dẫn không đích là nhiễu.

### 2.3 Trọng lượng thị giác (visual weight) [THỰC HÀNH]
Yếu tố làm một vùng "nặng" hơn: lớn hơn, sáng/tối tương phản mạnh với nền, màu bão hoà, ấm hơn lạnh (ở cùng độ sáng), có mặt người, có chi tiết dày, bị cô lập trong khoảng trống.
Cân bằng không cần đối xứng: một vật nhỏ, tương phản cao có thể đối trọng một vùng lớn, nhạt.

### 2.4 Lớp chiều sâu [THỰC HÀNH]
Tiền cảnh / trung cảnh / hậu cảnh. Chức năng: tiền cảnh khung (che một phần, nói "máy ở trong không gian", xem K2), trung cảnh chứa chủ thể, hậu cảnh cho bối cảnh và hào quang. Ba lớp phân biệt nhau bằng độ sáng, độ nét và độ bão hoà, không chỉ bằng vị trí.

### 2.5 Không gian âm và không gian trước mặt [THỰC HÀNH]
- Chủ thể cần **không gian ở phía nó hướng tới** (nhìn/đi sang phải thì chừa bên phải). Chủ thể sát mép phía nhìn → cảm giác bị chặn.
- Không gian âm làm chủ thể nổi lên và cho mắt chỗ thở; nhưng quá nhiều trong ảnh nhiều chi tiết sẽ đọc thành "thiếu".

### 2.6 Phân chia khung [THỰC HÀNH]
Một phần ba, trung tâm, đối xứng đều là **công cụ có nghĩa kèm theo**: đối xứng = trang nghiêm, trật tự, đối đầu; lệch tâm = đang ở trong chuỗi, có chuyển động; trung tâm = đối mặt, bảo vật. Không có "luật" nào đúng cho mọi ảnh; chọn theo ý (poster dùng trung tâm/đối xứng hợp; cinema hay lệch).

## 3. Poster vs cinema vs candid ở bố cục
| | Poster | Cinema | Candid |
|---|---|---|---|
| Điểm vào | mặt + mắt sinh vật, rất rõ | một vùng sáng có lý do, có thể không phải mặt | khoảnh khắc/cử chỉ |
| Đường đi | hào quang, hai ánh nhìn về người xem | ánh nhìn ra ngoài khung, vật tiền cảnh | không dẫn, ngẫu nhiên |
| Đối xứng | thường mạnh | hay phá | tự nhiên lệch |
| Nền | hào quang / màu bổ túc | có tầng và chìm | đời thường, hơi lộn xộn |

## 4. Attractor [GIẢ THUYẾT-AI]
| # | Attractor | Chặn thử |
|---|---|---|
| C-A1 | Chủ thể căn giữa, đối xứng | chỉ định vị trí khung (lệch trái 1/3) + hướng nhìn có không gian phía trước |
| C-A2 | Đường dẫn trung tâm (đường/cầu/hành lang) thẳng vào chủ thể | gộp với K2-A1: ghi vị trí máy + câu phủ định |
| C-A3 | Nền đầy chi tiết đều, mọi thứ ngang trọng lượng | chỉ định lớp nào chìm, lớp nào nét; "vùng nền yên" |
| C-A4 | Quá đầy: nhiều chủ thể phụ cạnh tranh | giới hạn số vật mang điểm nhấn, ghi vật nào là phụ và nhỏ hơn |
| C-A5 | Nhân vật nhìn thẳng ống kính | cinema: 视线落向画外 (K2-A6) |
| C-A6 | Đĩa đỏ/mặt trời làm điểm vào cạnh tranh với mặt | casebook: ghi nền và nguồn sáng; chặn đĩa tròn khi không cần |
Chưa đếm tần suất; chỉ C-A6 có số liệu (10/60 ảnh trong casebook).

## 5. Cách viết (tiếng Trung, có mức sàn)
Công thức: **điểm vào + chủ thể + đường đi + chỗ dừng + chỗ thở + câu phủ định nếu có attractor + mức sàn**.

Ví dụ:
- 画面第一眼落在人物受光的脸上，视线随她望向画面右侧的灯笼，右侧留出约三分之一的空白，人物面部保留细节，灯笼不抢过人物。
- 巨狐的眼睛与人物视线同时朝向镜头，狐尾在人物身后张开，形成背景光环，不出现红色圆盘。
- 人物位于画面左三分之一，视线落向画外右侧，前景一根木柱遮住左边缘，中间留出安静的暗部。

Quy tắc:
1. **Điểm vào ghi bằng đặc tính nhìn thấy** (受光的脸, 最亮处), không ghi "构图和谐".
2. Mỗi ảnh ≤ 1 điểm vào chính + ≤ 2 chỗ dừng.
3. Đường dẫn phải có chủ thể ở cuối; ghi rõ cái nào là đích.
4. Ghi **chỗ thở** (留白 ở đâu, bao nhiêu); nếu không, model lấp đầy.
5. Nếu ảnh có nhiều vùng tương phản cao, nói rõ vùng nào chủ ý "chìm".

## 6. Kiểm sau khi ra ảnh
1. Nheo mắt/thu nhỏ ảnh: mắt chạm đâu đầu tiên? Có phải điểm vào đã ghi?
2. Điểm vào có trùng chủ thể? Nếu không, thứ gì cạnh tranh (vùng sáng, màu, đĩa tròn)?
3. Đường đi có kết thúc ở chủ thể không?
4. Có chỗ thở không, hay đầy đều?
5. Không gian phía hướng nhìn đủ chưa?
6. Series: 3 ảnh có cùng điểm vào, cùng vị trí chủ thể không (xem casebook C01)?

## 7. OPEN
- **O1** Ghi "三分之一" có làm model đặt đúng vị trí không, hay vẫn kéo về giữa? Test 8 mẫu/nhánh.
- **O2** Ghi điểm vào bằng đặc tính ("最亮处") vs bằng vị trí ("左上") — cái nào model theo chắc hơn?
- **O3** Câu 留白 có làm model để trống thật, hay đặt vật vô nghĩa vào?
- **O4** Hai gaze (người + sinh vật) cùng nhìn ống kính có thật sự làm ảnh "nhìn tao đi" mạnh hơn một gaze không? Cần ảnh đối chiếu.
- **O5** Bằng chứng định lượng cho hướng nhìn dẫn mắt trong ảnh tĩnh sinh ra bởi AI: chưa có.

## Nguồn
- Journal of Eye Movement Research 17(5), "Impact of Leading Line Composition on Visual Cognition: An Eye-Tracking Study" (2024), https://www.mdpi.com/1995-8692/17/5/26
- BrainSight, "Gaze Cueing Explained: Two-Stage Attention Model" (thứ cấp).
- Fiveable, "Principles of Visual Composition" (cinematography) — định nghĩa quy ước nghề.
- Trong repo: K1, K2, notes §1–§4, casebook C01.
