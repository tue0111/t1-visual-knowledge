# 07 — VSC: tra kho Vibe Shot Club khi viết prompt T1

Người dùng đã nối connector Vibe Shot Club (tool `vsc_*`). Kho này là **nguồn tra cứu lúc làm**, không phải tài liệu để chép vào repo. Điều khoản VSC cấm xuất kho, repo công khai hay riêng tư cũng vậy: không lưu định nghĩa, template hay prompt của VSC vào file nào ở đây.

Không thấy tool `vsc_*` (phiên chưa nối, hết hạn, 401) thì làm như cũ bằng `05_CRAFT.md`, nói một dòng là chưa tra được VSC. Không đọc web vibeshot.club để thay.

## Khi nào tra

| Brief có | Kho | Tool |
|---|---|---|
| Tên phong cách, "kiểu như…", không biết chọn phong cách, muốn trộn phong cách | 风格图谱 `lexicon` | `vsc_search` → `vsc_get_style`, trộn thì `vsc_mix_styles` |
| Người dùng **nói rõ** MJ / Midjourney / sref | MJ 风格库 `sref` | `vsc_search` → `vsc_get_sref` |
| Động tác, tư thế giữa chuyển động, cảnh đánh nhau, nhảy | 动作运镜库 `motion` | `vsc_search` → `vsc_get_motion` |
| "Người khác viết chủ đề này thế nào", tên một creator | 提示词画廊 `gallery` | `vsc_search` → `vsc_get_prompt` |

Không có các nhu cầu trên thì không tra. Ảnh T1 thường chạy GPT Image / Nano Banana, nên **không** tự tra sref khi người dùng không nhắc MJ.

## Cách tra (giữ hạn mức)
1. Phiên mới gọi `vsc_whoami` một lần.
2. `vsc_search` với từ khoá Trung + Anh. Đưa người dùng 3–5 ứng viên (tên + một dòng khác biệt), hoặc tự chọn một nếu brief đã đủ rõ và ghi lý do trong bảng quyết định.
3. Chỉ lấy chi tiết mục được chọn. Không lấy hàng loạt, không lật hết trang. Chỉ gọi `vsc_media` khi người dùng muốn xem ảnh/video.
4. Gặp `locked: true` hoặc báo hết hạn mức: dừng gọi chi tiết, làm tiếp bằng thứ đã có.

## Chuyển kết quả VSC thành 3 phần T1

Một mục phong cách VSC thường có: định nghĩa, `features` (đặc điểm), `prompt.template` có `[subject]`, `negative`, `confusables` (phong cách dễ nhầm). **Không dán template nguyên si.** Template là chuỗi nhãn ngắn; T1 cần bằng chứng nhìn thấy (`01_MINDSET.md`).

| Trường VSC | Đi vào đâu | Cách viết |
|---|---|---|
| tên phong cách | 母版锁, câu phong cách | tên tiếng Trung, kèm 1–2 dấu hiệu cấu trúc ở dưới; tên một mình là nhãn mòn (`05_CRAFT.md` §1.2) |
| `features` | 分镜, trục chính/phụ | mỗi đặc điểm thành một câu có vật mang: ánh sáng rơi lên **cái gì**, che bởi **cái gì**. Chọn 1–3 đặc điểm phục vụ trục chính, bỏ phần còn lại |
| `prompt.template` | tham khảo | lấy tiêu cự, góc máy, chất liệu nếu khớp bảng quyết định; dịch sang tiếng Trung giản thể; bỏ từ trùng hoặc rỗng |
| `negative` | 通用负面提示词 | chỉ giữ cái chặn đúng attractor của trục chính, và không mâu thuẫn với phần dương |
| `confusables` | dòng CHẶN trong bảng quyết định | phong cách dễ nhầm chính là attractor; viết bằng chứng loại trừ nó, không chỉ ghi "không phải X" |
| `relations` | khi trộn | dùng để chia quyền theo kênh (`05_CRAFT.md` §1.4): một phong cách giữ màu, một giữ bố cục |

Mục chuyển động (`motion`) cho ảnh tĩnh: lấy **một khoảnh khắc** của động tác (tư thế đỉnh, trọng tâm, hướng lực, vết thời gian như tóc/vải/bụi), không mô tả cả chuỗi. Cả chuỗi chỉ dành cho prompt video.

Mục画廊 (`gallery`): đọc để hiểu cấu trúc người khác dùng, rồi viết lại cho brief T1. Không chép câu của họ vào prompt giao.

Luật cứng T1 vẫn thắng mọi thứ từ VSC: tiếng Trung, 3 phần, brand nguyên văn, một shot một ảnh.

## Bảng quyết định khi có tra VSC
Thêm vào dòng TRỤC CHÍNH hoặc CHẶN, không thêm dòng mới:
```
TRỤC CHÍNH: K_ (vì ___; VSC: <id phong cách/động tác>)
CHẶN: attractor ___ (VSC confusable: <id>)
```

## Học từ VSC mà không chép
Ra ảnh rồi thì ghi bài học vào `LEARNINGS.md` bằng lời của mình, kèm id VSC để lần sau tra lại. Ví dụ đúng: "phong cách `film-noir`: chỉ ghi tên thì GPT Image ra noir sân khấu; thêm vật che tiền cảnh + đích nhìn thì đỡ". Ví dụ sai: dán `features` hay template của VSC vào file.
