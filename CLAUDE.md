# CLAUDE.md
Đọc và làm theo `AGENTS.md`. Đó là điểm vào duy nhất của repo này.
Khi sửa repo: giữ cấu trúc ba tầng trong `system/`, chạy `python -m unittest discover -s tests`, `python tools/t1lint.py --strict examples/*.txt` và `python tools/t1lint.py --strict examples/keyword/*.txt` trước khi commit. Chỉ file 3 phần được nằm trực tiếp trong `examples/`; ví dụ keyword luôn ở `examples/keyword/`.
