# CHANGELOG

## v3.1.0 — 2026-11-11
Gom kiến thức còn rải rác vào đúng chỗ, sau khi v3.0.0 dựng hai làn.
- Thêm `system/11_LIGHT_AND_OPTICS.md`: bảy kiểu đèn trên mặt người đọc bằng bóng mũi; phía chiếu khi mặt quay ba phần tư (thon hay đầy mà không sửa mặt); cỡ nguồn, độ suy giảm theo khoảng cách (nền tối không cần phông), cái đối diện nguồn; đốm sáng trong mắt; vùng nét, nền mờ, đốm sáng nền; tiêu cự là góc thu còn phối cảnh do chỗ đứng. Chưa thử ảnh.
- Thêm `examples/creative/`: G "Chàm ăn dần" (biến tấu, keyword, 3 prompt qua lint) và H "Ghế chờ chủ" (loại hình vắng người, văn xuôi ngắn). Ví dụ quy trình, chưa sinh ảnh.
- `system/09_SHOT_VOCAB.md`: trục B thêm 7 điểm đứng máy, trục D thêm 6 kiểu chiều sâu, **trục H mới** (khung nối: sổ trạng thái, hướng nhìn nối, insert, nhìn qua vai và cảnh ngược), mục "Theo tỷ lệ khung" có cổng crop, bẫy chữ chuyển động máy, mẫu bảng khung có cột VIỆC.
- `system/02_KNOWLEDGE.md`: K4 thêm sáng một màu tối một màu, đêm đáng tin nhờ quan hệ trời–bóng–nguồn, bạc màu kiểu giữ bạc; K1, K2 trỏ sang `11`.
- `system/10_CREATIVE_ALBUM.md`: bảng mốc màu cho album; cách đưa kết quả tra vào prompt; không mở album bằng cận cơ thể; giao theo đợt khi nơi nhận giới hạn số tin.
- `system/LEARNINGS.md`: lấy về 14 dòng từ hai nhánh cũ chưa merge (2026-10-25 đến 2026-11-01: SATIN, Cold Denim, Hell House, Phòng 1207, Qipao, nhà rường Huế, cầu ngói Thanh Toàn…) và mục "Kinh nghiệm chung" 9 điểm. `04_TEMPLATES.md`: ghi chú ví dụ C cập nhật theo bằng chứng cầu ngói.
- `system/05_CRAFT.md`: bảng chỉ mục "gặp chuyện gì → đọc mục nào" (23 tình huống), §4.11 chân trụ và điểm tì, §6 trỏ sang `10`. Không xoá nội dung cũ.
- `tests/test_docs_links.py`: 3 test kiểm đường dẫn trong `AGENTS.md`/`README.md`, mọi file `system/NN_` được nhắc tên, mọi skill có `name` khớp thư mục (35 test tổng).
- Chưa vào repo: lexicon VSC (điều khoản kho cấm xuất; agent tra trực tiếp lúc làm theo `10` §3).

## v3.0.0 — 2026-11-11
Hệ thống có hai làn. Trước đây mọi yêu cầu đi qua một cái phễu (bảng quyết định 6 dòng → 3 phần), album chỉ có ba dòng hướng dẫn, nên album sáng tạo bị rập theo album trước.
- Thêm `system/10_CREATIVE_ALBUM.md` (làn sáng tạo): đọc độ mở; chống lối mòn (khác album trước ở ≥ 3/5 thứ); 10 động cơ sinh ý niệm; tra cứu mở rộng có ngân sách (web, VSC, film-library) gom thành bảng vật liệu; phiếu ý niệm; 8 hình dạng album, mỗi hình dạng một luật đa dạng riêng; việc của từng khung và nhịp album; chọn khuôn đóng gói sau cùng theo generator; tự soát cấp album. Nhãn giả thuyết, chưa chạy album nào theo quy trình này.
- `AGENTS.md`: bảng chọn làn; luật cứng số 2 viết lại (khuôn là bước cuối, ba khuôn: 3 phần, keyword, văn xuôi ngắn); luật tối thiểu chung cho mọi khuôn; mục "Tra cứu mở rộng"; đầu ra mặc định cho làn sáng tạo; thứ tự quyền thêm lớp mỏng và kết quả tra cứu.
- `system/03_WORKFLOW.md`: ghi rõ là làn chính xác; mục Album tách series theo quy cách khỏi album sáng tạo.
- `system/09_SHOT_VOCAB.md`: là kho để tra, không phải ma trận; luật "≥ 3 trục" chỉ áp cho hình dạng khám phá; sửa câu sai về tiêu cự (tiêu cự là góc thu, phối cảnh đổi theo chỗ máy đứng).
- Skill mới `.claude/skills/t1-creative-album`; skill `t1-visual-prompt` trỏ sang khi gặp yêu cầu mở. `README.md` cập nhật.
- Không đổi: khuôn 3 phần, khuôn keyword, brand, linter, 6 ví dụ, `01`, `02`, `05`–`08`.

## v2.13.0 — 2026-11-11
- Thêm `system/09_SHOT_VOCAB.md`: từ vựng khung để dựng album sáng tạo: 7 trục (cỡ cảnh, điểm đứng máy, đầu và ánh nhìn theo máy, bố cục, kể chuyện nhỏ, không khí, chất ảnh) với keyword tiếng Trung, bảng ghép máy–đầu, luật "khác nhau ít nhất 3 trục", mẫu bảng 8 khung, bẫy.
- Nguồn: 5 clip khẩu quyết chụp chân dung, viết lại bằng lời T1. Nhãn quan sát, chưa thử ảnh. Không có ảnh, khung hình hay preset số của người khác trong repo.
- `AGENTS.md`, `README.md`: một dòng trỏ tới `09`.

## v2.12.0 — 2026-11-11
- Thêm `system/08_KEYWORD_FORMAT.md`: khuôn keyword một dòng nối bằng `+` như luật bổ sung (không thay khuôn 3 phần): hình dạng, 9 luật cứng, khối khoá nhân vật thay 母版锁, thói quen đã chứng minh, và bảng "Tránh xung đột lint và Git".
- `tools/t1lint.py`: thêm kiểu keyword (`lint_keyword`, `detect_style`, `lint_any`), cờ `--style auto|three|keyword`, mặc định tự nhận. Lệnh cũ `t1lint --strict examples/*.txt` giữ nguyên hành vi.
- Thêm `examples/keyword/E_smoke_backlight_keyword.txt` (3 prompt của album khói đỏ). Ví dụ keyword ở thư mục con để glob `examples/*.txt` và test cũ không bao giờ chạm tới.
- `tests/test_t1lint.py`: thêm 16 test (32 test tổng): ví dụ keyword PASS strict; mọi file trực tiếp trong `examples/` phải là kiểu 3 phần; từng luật keyword; tự nhận kiểu qua CLI.
- `AGENTS.md`: luật cứng số 2 có ngoại lệ keyword, thêm dòng nạp `08`. `CLAUDE.md`: thêm lệnh lint keyword. `README.md`, skill `t1-visual-prompt`: một dòng trỏ tới `08`.
- Không đổi luật khuôn 3 phần, brand, hay bốn ví dụ A, B, C, D. Cần áp v2.11.0 trước.

## v2.11.0 — 2026-11-11
- Thêm `examples/D_smoke_backlight_hanfu.txt`: ví dụ đầy đủ khuôn 3 phần cho album "ánh sáng trước" (nguồn sáng mạnh sau người, khói chỉ sáng nơi ánh chạm, nền trống, tiền cảnh lụa có hướng): 3 khung (xoay trong khói 16:9, cổng vòm đối xứng 9:16, đàn tranh trong đại điện 16:9). PASS `t1lint --strict`.
- `system/07_ATMOSPHERE_DEVICES.md`: thêm bảng "Trạng thái thử". AD-01, AD-04, AD-06, AD-08 đã thử và đạt; AD-07 và AD-09 thử một phần; AD-02, AD-03, AD-05, AD-10 vẫn UNTESTED.
- `system/LEARNINGS.md`: thêm hai dòng: album v1 phẳng và rối (2026-11-10), album khói đỏ cung điện 8/8 trúng (2026-11-11).
- Không đổi luật cứng và `t1lint`. Cần áp v2.10.0 trước.

## v2.10.0 — 2026-11-10
- Thêm `system/07_ATMOSPHERE_DEVICES.md`: lớp mỏng tra khi cần, 10 thủ pháp `AD-01`…`AD-10` chia 4 nhóm (ánh sáng; không khí và khoảng trống; che và dẫn; chuyển động và góc máy). Mỗi mục: nguyên lý, câu hỏi, dấu kiểm, bẫy model, câu mẫu 中文 [giả thuyết]. Thêm bảng cặp xung đột và ghi chú vận hành (khung nghiêng ở hậu kỳ, kiếm trên Midjourney, không cộng hậu kỳ trùng lớp).
- Nhãn: nguồn [quan sát] từ ảnh minh hoạ người khác chia sẻ và một bài tóm 4 thủ pháp, viết lại bằng lời T1, không lưu ảnh, không chép bài, không ghi tên. Ảnh T1: UNTESTED cho cả 10 mục.
- Thêm skill `.claude/skills/t1-atmosphere-devices` (đi kèm `t1-visual-prompt`). `AGENTS.md`, `README.md` và skill `t1-visual-prompt` thêm một dòng trỏ tới `07`.
- `LEARNINGS.md` thêm hai dòng từ ảnh T1 tự sinh: bản phim bỉ ngạn viết bằng prompt keyword (2026-11-06) và bộ hồ koi, hiên gỗ, quạt do Grok bot viết prompt từ ảnh mẫu (2026-11-09).
- Không đổi luật cứng (tiếng Trung, 3 phần, brand), không đổi `t1lint`.

## v2.9.0 — 2026-11-04
- `04_TEMPLATES.md`:
  - 分镜 thêm ba câu tuỳ chọn: 第一眼 (gửi điểm đọc đầu tiên thẳng cho model), một câu gọi tên chỗ căng, thứ tự đọc 3 tầng.
  - Thêm "Khuôn series có tham số (nền + gia vị)": 母版锁 viết luật theo chủ đề, 分镜 chỉ chứa kỳ hiện tại.
- `05_CRAFT.md`:
  - §1.1a chất liệu theo chuỗi vật lý, có chỗ được hỏng và chỗ phải giữ.
  - §5.8 khung không cần mặt thì đừng cho thấy mặt.
  - §6.5 series nhiều chủ đề: khoá quan hệ, không khoá giá trị.
  - §6.6 album tái dựng: đặt ảnh sinh cạnh ảnh mẫu trước khi chọn.
  - §7.10 nguồn sáng trong hay ngoài khung (画外/画内) phải nói rõ.
- `LEARNINGS.md` thêm các dòng từ album tái dựng ngày 2026-11-04: GPT Image qua Codex, 34 ảnh, A/B/C một khung.
- Nguồn: thực hành công khai của người khác về cặp LLM viết prompt + model ảnh render, viết lại bằng lời T1, không chép prompt, không ghi tên. Phần [đã thấy] đến từ ảnh T1 tự sinh.
- Không đổi luật cứng (tiếng Trung, 3 phần, brand), không đổi `t1lint`.

## v2.8.0 — 2026-10-05
- `06_FILM_GROUNDING.md`: FG-14 thêm giới hạn khung dọc (tách ngang không phải cách duy nhất; có thể lệch sâu hoặc cao độ khi hành động chung và điểm tiếp xúc vẫn rõ). Không thêm cơ chế mới; vẫn 14 cơ chế, ảnh UNTESTED.
- Thêm một dòng link tới nhóm F ở mục nhiều người.

## v2.6.0 — 2026-10-04
- Thêm nhóm F của `system/06_FILM_GROUNDING.md`: FG-13 về điểm đứng máy/hình chiếu, FG-14 về tách ngang thân khi telephoto gây chồng lấp; mỗi mục có câu hỏi, dấu kiểm, giới hạn và câu mẫu 中文 [giả thuyết].
- Hai mục được lọc qua đối chiếu prompt văn bản: bản bổ sung có dấu kiểm còn bản gốc thiếu. Nhãn nguồn [sách]; ảnh vẫn UNTESTED, ứng dụng prompt là suy luận; LEARNINGS và mắt người dùng cao hơn.
- Cập nhật liên kết tra nhóm F và số cơ chế thành 14; giữ khuôn ba phần, brand, luật cứng và bài học đã quan sát.

## v2.5.0 — 2026-10-04
- Thêm `system/06_FILM_GROUNDING.md`: lớp mỏng, tra khi cần; 12 cơ chế mã `FG-01`…`FG-12` (đích–cản–can thiệp–giá, hành động bị kìm, hai lớp hành động/hai đường nhìn, màu gắn vào vật mang, ngoại lệ nhóm đồng dạng), mỗi cơ chế một nguyên lý, một câu hỏi, một dấu kiểm, một giới hạn, một câu mẫu 中文 [giả thuyết].
- Nhãn hai trục: nguồn [sách]/[nhiều sách]; ảnh UNTESTED cho cả 12 mục, câu mẫu 中文 là [giả thuyết]. LEARNINGS và mắt người dùng cao hơn. Không chép tên nguồn hay trích dẫn; gốc nguồn giữ ở kho nội bộ, không công khai.
- `02_KNOWLEDGE.md` K4/K7 và `05_CRAFT.md` §3 mỗi nơi thêm một dòng link; `05 §4.5` thêm một câu ngoại lệ nhóm đồng dạng theo brief (FG-12), mặc định giữ nguyên.

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
