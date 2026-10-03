# NOTES 2026-10-03 — Kết quả test W2 (đợt bằng chứng đầu tiên)

status: EVIDENCE (đợt 1, tín hiệu) · author: Claude (center) · date: 2026-10-03
Đăng ký trước: `E:\T1_Rebuild_Inputs\codex\W2_PREREG.md` (+ Sửa đổi 1). Dữ liệu thô, phiếu, key, log JEV: `E:\T1_Rebuild_Inputs\w2_test\` (không đưa ảnh lên repo).

## Thiết lập
- Generator: Codex `$imagegen` (tool không lộ model; giao thức yêu cầu gpt-image-2). Không chỉnh được kích thước, không tắt được rewrite nội bộ. Prompt gửi nguyên văn, hash ghi trong RUN_LOG.
- Prompt: `writing/W2_WORKED_EXAMPLES.md` — P1 cinema đèn lồng (phân trục, trục chính K1) ×6; P1x cùng brief viết đều tay ×6; P2 poster cáo băng ×3; P3 candid xe bánh mì qua cầu ×3. 18/18 ảnh, 0 từ chối, brand "T1 to 9" đúng 18/18, không chữ lạ 18/18.
- Người quan sát quyết định: **Astra + Sol** (chat mới, mù). Claude **mất tính mù** (thấy 1 ảnh khi theo dõi; suy được key từ kích thước file) → phiếu Claude không vào quyết định (Sửa đổi 1).
- Chuẩn hoá trường chữ: JEV `noul`, ngưỡng 0.85/0.15; quyết định bằng code `w2_aggregate.py`.

## Kết quả theo luật đăng ký trước (ràng buộc)

| P1 vs P1x | P1 | P1x | Kết luận |
|---|---|---|---|
| G — không nhìn ống kính | 6/6 | 0/6 | ỦNG HỘ |
| L — mọi vùng sáng có nguồn | 3/6 | 6/6 | không ủng hộ (P1x hơn 3) |
| S — nét chọn lọc | 6/6 | 6/6 | không ủng hộ (trần) |
| D — vùng tối sâu **giữ chi tiết** | 0/6 | 6/6 | không ủng hộ (P1x hơn 6) |
| F — đọc đầu tiên là mặt sáng/đèn | 0/6 | 0/6 | không ủng hộ (đo hỏng) |

**H-W2 ("viết phân trục tốt hơn viết đều tay"): KHÔNG ỦNG HỘ.** P2: SC 0/3, SH 0/3, GC 0/3, RD 2/3. P3: CB 0/3, G 3/3, AM 3/3, TX 3/3. Đồng thuận Astra–Sol: SH 39% (đo không tin cậy), L 83%, các trường enum khác 100%.

## Vì sao kết quả ràng buộc chưa phản ánh đúng (chẩn đoán, không đổi kết luận)
1. **F, SC, GC, CB đo hỏng ở khâu phiếu.** Trường tự do + JEV cho xác suất giữa (0.2–0.8) → "không chắc" → tính là không. Phiếu không có trường ánh nhìn của sinh vật (GC không thể đo). Sol mô tả tỷ lệ có rào đón ("không xác định tỷ lệ thực") → SC không chắc.
2. **D định nghĩa ngược ý đồ.** Prompt P1 *yêu cầu* "光照范围之外迅速衰减成深暗" — tức vùng ngoài đèn chìm tối. D chấm "vùng tối giữ chi tiết" nên phạt đúng thứ đã yêu cầu. Lỗi của người đăng ký (Claude), ghi nhận để sửa phiếu v2.
3. **L:** Astra thấy 3/6 ảnh P1 có vệt sáng lạnh + bóng lan can trên sàn phải không rõ nguồn; Sol không thấy. Claude (không mù) xem 1 ảnh: có vệt sáng lạnh có hướng — nhiều khả năng do câu cho phép "夜空与雪地的微弱冷色环境光" bị model hiểu thành ánh trăng có hướng.

## Tín hiệu thăm dò (sau khi mở key — giả thuyết cho đợt sau, KHÔNG phải kết luận)
| Quan sát | Số | Ghi chú |
|---|---|---|
| Viết đều tay → nhân vật nhìn ống kính | P1x 6/6 vs P1 0/6 (Fisher p≈0.002) | Khớp attractor K7 G-A3. Câu "ánh nhìn có đích" + "观众像在场景中旁观" đủ để đổi hẳn |
| Viết đều tay → da sáp/nhựa | Sol: P1x 6/6, P1 0/6; Astra: 0/0 | Một người quan sát thấy, người kia không → độ tin thấp; khớp K5 T-A1 và tính từ "完美的脸, 高品质" |
| "迅速衰减成深暗" → mất chi tiết vùng tối | P1 6/6 (cả hai đồng ý) | Câu suy giảm ánh sáng **mạnh hơn dự tính**; cần mức sàn cho môi trường, không chỉ cho mặt |
| Viết đều tay → chuyển sang chế độ poster | P1x: nhiều đèn lồng, phố sáng rực, nhìn ống kính (Claude xem 1 ảnh) | Không có chỉ báo đăng ký trước cho "chế độ"; cần trường mode/hierarchy trong phiếu v2 |
| **Máy vẫn đứng trên cầu/dốc cầu** dù có "相机不在桥面上" | P3: cả hai người quan sát ghi máy "trên mặt dốc (dẫn lên) cầu"; Claude xem 2 ảnh: máy trên lòng đường dốc cầu, lan can bên phải | **Bằng chứng chống** hiệu lực câu phủ định vị trí (K2 O2). Attractor A1 còn nguyên |
| Poster: máy sát đất, đầu cáo khổng lồ, người phía sau | Cả hai: máy "sát mặt tuyết, thấp hơn đầu cáo" 3/3 | Trục chính K2 đạt về vị trí máy; thang tỷ lệ chưa đo được |

## Bài học quy trình
- Ảnh blind phải **mã hoá lại + bỏ metadata**, `raw\` để ngoài tầm người quan sát; người điều phối không liệt kê thư mục ảnh và không xem chat sinh ảnh.
- Mọi chỉ báo quyết định phải là **trường lựa chọn cố định**, không qua chữ tự do. Thêm: `camera_on_bridge_deck`, `creature_gaze`, `scale_head_vs_torso`, `first_read_target` (enum), `mode_read` (poster/cinema/candid).
- Chỉ báo phải đo **đúng thứ prompt yêu cầu**, kể cả khi prompt yêu cầu "tối", "nhoè", "mất chi tiết".

## Hệ quả cho tri thức (đã áp dụng ở commit này)
- K2 A1 + O2: thêm bằng chứng chống câu phủ định vị trí.
- K7 G-A3: thêm số liệu W2.
- K1/K4: cảnh báo "迅速衰减成深暗" cần mức sàn môi trường.
- W1 §4 (ngoại lệ thứ tự): đánh dấu chưa kiểm, prompt mới theo thứ tự `core/03`.
- W1 §1 (ngân sách trục): **giữ nguyên CANDIDATE** — H-W2 không ủng hộ; theo hệ quả đã đăng ký, không xoá W1, mở test lặp với phiếu v2.
