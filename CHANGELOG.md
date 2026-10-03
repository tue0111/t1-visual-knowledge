# CHANGELOG

## v2.4.0 — 2026-10-04
- chưng cất vòng 2 bởi Astra: bổ sung kiểm sai lệch tham chiếu, vùng chất liệu, chuyển động từng vật, silhouette và biến điều khiển độc lập.
- Bổ sung chuyển cấu trúc đồ vật thành chức năng tạo hình; kiểm điểm neo ở kích thước xem thực tế. Mọi mục mới mang nhãn giả thuyết, chưa kiểm bằng ảnh T1.
- Soát mâu thuẫn grain/độ phân giải, ánh sáng, candid, hệ quy chiếu; sửa diễn đạt tiếng Trung và các khẳng định quá mức.
- Hiệu chỉnh nhãn độ tin, bỏ xếp hạng ổn định và ngưỡng negative thiếu bằng chứng; giữ brand, luật ba phần và phạm vi người lớn không lộ liễu.

## v2.3.0 — 2026-10-04
- `05_CRAFT.md` thêm mục §4b "Gợi cảm người lớn, an toàn":
  - Phạm vi: người trưởng thành tự tạo, mặc đầy đủ, không lộ liễu; bộ lọc generator là cổng cuối, không dạy lách.
  - Thang ổn định, công thức, sức căng trang phục, dáng, bảng nhân cách, bảng ống kính, ánh sáng.
  - Bốn lý do ảnh rẻ tiền; câu biên tiếng Trung cho 母版锁 và negative.
- Chuyển thủ pháp khung riêng tư (nhìn qua khe cửa, bình phong) từ tranh khắc cổ sang ảnh an toàn; không lấy nội dung lộ liễu.

## v2.2.0 — 2026-10-03
- Chưng cất thêm một kho cộng đồng thực hành (~50 bài; bỏ bài khoá trả phí, bài thuần video/plugin, danh sách prompt).
- `05_CRAFT.md`:
  - Khái niệm dày nghĩa như bản brief nén; khám phá phong cách có hệ thống.
  - Sửa ảnh có sẵn: khoá tường minh, chỉ làm một việc. Chép kế hoạch chụp của mẫu. Nhân vật tự tạo từ cấu trúc xương.
  - Nhân cách điều khiển biểu cảm; gợi cảm có chủ quyền.
  - Bộ nhận dạng IP; một thế giới, nhiều lát cắt.
  - Mục mới 6b về thủ pháp: phơi sáng kép, vật khổng lồ, tương phản tỷ lệ, poster ý niệm, poster đội hình.
  - Rộng trước sâu sau; upscale mài da.
- `02_KNOWLEDGE.md`: K1 phân bổ độ sáng (chủ thể nhận sáng, nền lùi, mép tách); K3 thứ bậc độ rõ.
- `01_MINDSET.md`: thêm nguyên lý 11–12.

## v2.1.0 — 2026-10-03
- Thêm `system/05_CRAFT.md`: chưng cất ~400 kinh nghiệm thực hành thành nguyên tắc T1, có nhãn độ tin (phong cách, tham chiếu, câu chuyện, người, độ thật/candid, series, vệ sinh prompt, sửa lỗi, ghi chú generator).
- `02_KNOWLEDGE.md`: bổ sung mẹo theo trục (K1, K2, K3, K4, K5, K8).
- Nối 05 vào AGENTS, README, skill, WORKFLOW; LEARNINGS trỏ sang 05.
- Dữ liệu nguồn không đưa vào repo; chỉ có nguyên tắc viết lại bằng lời T1, không tên tác giả, không trích dẫn.

## v2.0.0 — 2026-10-03
- Viết lại toàn bộ thành hệ agent ba tầng: Mindset, Knowledge, Workflow (`system/`).
- Thêm `AGENTS.md` (Codex), `CLAUDE.md` và skill `t1-visual-prompt` (Claude Code).
- Thêm `tools/t1lint.py` kiểm luật cứng (3 phần, brand nguyên văn, một ảnh, chữ Latin, tính từ rỗng) cùng 16 test.
- 3 ví dụ đầy đủ trong `examples/`, đã áp bài học W2: ý đồ vùng tối, đích ánh nhìn, hình học máy thay câu phủ định.
- `system/LEARNINGS.md` khởi tạo từ test W2.
- Bản cũ (OS v2, Knowledge_Mindset, K/M/W, notes, SOURCE_MANIFEST) gỡ khỏi cây, giữ ở tag `legacy-v1`.
