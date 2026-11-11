# 08 — KEYWORD FORMAT: prompt một dòng nối bằng "+"

Khuôn **bổ sung**, không thay khuôn 3 phần. Khuôn 3 phần (`04_TEMPLATES.md`) vẫn là mặc định. Dùng khuôn này khi người dùng chọn keyword, hoặc khi chạy GPT Image và Grok bot theo quy trình album đã dùng ở các bộ hoa đồng tiền, hồ koi, khói đỏ. Theo thứ tự quyền trong `AGENTS.md`, yêu cầu hiện tại của người dùng cao hơn luật cứng số 2 (đúng 3 phần).

## Hình dạng

```
<tỷ lệ>竖构图/横构图+<máy và ống kính>+<người>+<hành động, ánh nhìn>+<đạo cụ>+<cảnh>+<ánh sáng>+<màu, chất ảnh>—— 负面：<mục>+<mục>+…
```

- **Một dòng là một prompt, một prompt là một ảnh.** Album: mỗi ảnh một dòng, không có 母版锁 riêng, nên khối khoá nhân vật được lặp ở đầu thân của mọi dòng.
- Mỗi dòng mở bằng tỷ lệ khung (`3:4竖构图`, `16:9横构图`, `9:16竖构图`), kết bằng `—— 负面：` rồi một danh sách nối bằng `+`.
- Chú thích trong file ví dụ dùng dòng bắt đầu bằng `#`. Linter bỏ qua dòng `#` và hàng rào ```.

## Luật cứng của khuôn keyword (linter bắt)

1. Đúng một `—— 负面：` mỗi prompt. Thiếu hoặc thừa là lỗi.
2. Mở bằng tỷ lệ khung. Thân có ít nhất 8 keyword nối bằng `+`.
3. Có chữ `成年` (hoặc `无人物` nếu ảnh không có người). Nên có `不像任何真人`.
4. Không chứa `T1 to 9`. Chữ ký đóng ở hậu kỳ. Nếu muốn brand nằm trong prompt thì dùng khuôn 3 phần.
5. Chữ Latin chỉ được: tỷ lệ (`3:4`), số tiêu cự (`85毫米`), khẩu độ (`F1.4`). Chữ Latin khác là cảnh báo.
6. Negative ≤ 14 mục. Cảnh báo nếu nhiều hơn.
7. Có tay thì ghi `五指完整` (hoặc ghi rõ tay không nhập ảnh). Cảnh báo nếu thiếu.
8. Không mâu thuẫn dương–âm: một mục negative không được xuất hiện nguyên văn trong thân (trừ khi đứng sau chữ phủ định `不`, `无`).
9. Không dùng tính từ rỗng (电影感, 高品质, 杰作…), như khuôn 3 phần.

## Khối khoá nhân vật (thay 母版锁)

Lặp nguyên văn ở đầu mọi dòng của album. Tối thiểu:

- Người: tuổi, mặt gốc, `不像任何真人`, độ dài tóc và kiểu tóc, màu, trang phục chính, một món nhận diện (dải lụa, trâm).
- Độ dài tóc phải khoá. Album hồ koi từng thành hai người vì khối khoá thiếu độ dài tóc (LEARNINGS 2026-11-09).
- Luật ánh sáng riêng của album, nếu có (xem ví dụ E).

## Các thói quen đã chứng minh

- **Ánh sáng trước.** Một nguồn mạnh ngoài khung sau người, khói chỉ sáng nơi ánh chạm, ít nhất 1/3 khung gần đen, nền trống với tối đa một mảng kiến trúc. LEARNINGS 2026-11-11 và `07_ATMOSPHERE_DEVICES.md`.
- **Nhãn cấu trúc cho đạo cụ:** `伞骨清晰`, `琴弦平行清晰雁柱整齐`, `双手按孔五指完整`.
- **Tay:** `画面中只有两只手臂` kèm vị trí từng tay và `五指完整`.
- **Mặt ngược sáng:** ghi `不补光+五官可辨` và đặt `面部补光` vào negative.
- **Prompt ngắn:** 270 đến 310 chữ chạy tốt hơn 455 đến 540 chữ. Cắt trang điểm và chi tiết nền khi mặt chìm trong bóng.
- **Kiếm và dao:** Midjourney từng review tài khoản vì các chữ này, kể cả trong negative. Đổi sang quạt, ô gập, dải lụa.
- **Khung nghiêng:** viết khung thẳng, nghiêng ở hậu kỳ.

## Tránh xung đột lint và Git

Hai khuôn dùng hai thư mục và hai lệnh, nên không giẫm nhau:

| Kiểu | Thư mục ví dụ | Lệnh kiểm |
|---|---|---|
| 3 phần | `examples/*.txt` (chỉ để file 3 phần ở đây) | `python tools/t1lint.py --strict examples/*.txt` |
| keyword | `examples/keyword/*.txt` | `python tools/t1lint.py --strict examples/keyword/*.txt` |

- `t1lint` tự nhận kiểu: có `【母版锁】` là 3 phần, có `—— 负面：` là keyword. Có thể ép bằng `--style three` hoặc `--style keyword`.
- Trước khi commit chạy cả hai lệnh và `python -m unittest discover -s tests`. Test khoá việc mọi file trực tiếp trong `examples/` phải là kiểu 3 phần, nên ai lỡ bỏ file keyword vào đó sẽ thấy test đỏ ngay chứ không đợi đến lúc lint.
- Đừng trộn hai kiểu trong cùng một file. Khuôn 3 phần có brand trong 母版锁 và câu ngoại lệ trong negative; khuôn keyword thì không có brand.
- Muốn thêm ví dụ keyword: đặt vào `examples/keyword/`, một dòng một prompt, đặt tên `X_ten_ngan.txt`, chạy lệnh keyword đến khi PASS.
