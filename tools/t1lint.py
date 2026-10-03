#!/usr/bin/env python3
"""t1lint — kiểm luật cứng cho prompt T1 to 9 (chỉ thư viện chuẩn).

Dùng:
    python tools/t1lint.py prompt.txt [prompt2.txt ...]
    python tools/t1lint.py --no-brand prompt.txt      # brief yêu cầu không chữ
    python tools/t1lint.py --strict prompt.txt        # cảnh báo cũng làm fail

Lỗi (exit 1): thiếu/thừa/sai thứ tự 3 phần, brand hoặc câu ngoại lệ không nguyên văn,
thiếu câu "chỉ một ảnh", còn chữ T1 to 9 khi --no-brand.
Cảnh báo: chữ Latin ngoài danh sách cho phép, tính từ rỗng, negative xả danh sách.
"""
from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BRAND = (ROOT / "system" / "brand_block.txt").read_text(encoding="utf-8").strip()
BRAND_NEG = (ROOT / "system" / "brand_negative.txt").read_text(encoding="utf-8").strip()
ONE_IMAGE = "每次只生成一张"
MARK = "T1 to 9"

MOTHER = "【母版锁"
SHOT = "【分镜"
NEGATIVE = "【通用负面提示词】"

EMPTY_ADJECTIVES = ["高品质", "大师作品", "杰作", "超高清", "8K", "4K", "氛围感", "电影感", "细节丰富", "完美的脸"]
ALLOWED_LATIN = {"mm", "f", "K"}
NEGATIVE_ITEM_LIMIT = 14


@dataclass
class Report:
    errors: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)

    @property
    def ok(self) -> bool:
        return not self.errors


def _positions(text: str, token: str) -> list[int]:
    return [m.start() for m in re.finditer(re.escape(token), text)]


def lint(text: str, no_brand: bool = False, allow_latin: set[str] | None = None) -> Report:
    r = Report()
    allow = ALLOWED_LATIN | (allow_latin or set())

    mothers, shots, negs = _positions(text, MOTHER), _positions(text, SHOT), _positions(text, NEGATIVE)
    if len(mothers) != 1:
        r.errors.append(f"cần đúng 1 khối 【母版锁】, thấy {len(mothers)}")
    if not shots:
        r.errors.append("thiếu khối 【分镜】")
    if len(negs) != 1:
        r.errors.append(f"cần đúng 1 khối 【通用负面提示词】, thấy {len(negs)}")
    if r.errors:
        return r
    m, n = mothers[0], negs[0]
    if not (m < min(shots) and max(shots) < n):
        r.errors.append("sai thứ tự: phải là 母版锁 → 分镜 → 通用负面提示词")
        return r

    mother_text = text[m:min(shots)]
    shot_text = text[min(shots):n]
    neg_text = text[n:]

    # Ngoặc 【】 khác ngoài 3 loại phần + khối brand = phần thứ tư
    for head in re.findall(r"【([^】]*)】", text):
        if not head.startswith(("母版锁", "分镜", "通用负面提示词", "固定品牌角标")):
            r.errors.append(f"có phần lạ 【{head}】 — chỉ được 3 phần")

    if no_brand:
        if MARK in text:
            r.errors.append("--no-brand nhưng prompt vẫn còn “T1 to 9”")
    else:
        if BRAND not in mother_text:
            r.errors.append("khối 【固定品牌角标】 không nguyên văn hoặc không nằm trong 母版锁")
        if BRAND_NEG not in neg_text:
            r.errors.append("negative thiếu câu ngoại lệ brand nguyên văn")
        if MARK in shot_text:
            r.errors.append("“T1 to 9” xuất hiện trong 分镜 — brand chỉ ở 母版锁 và câu ngoại lệ")

    if ONE_IMAGE not in mother_text:
        r.errors.append("母版锁 thiếu câu chỉ một ảnh (每次只生成一张…)")

    stripped = text.replace(MARK, "")
    for word in sorted(set(re.findall(r"[A-Za-z]+", stripped))):
        if word not in allow:
            r.warnings.append(f"chữ Latin “{word}” — prompt phải tiếng Trung (trừ tên riêng, tỷ lệ, số ống kính)")

    for adj in EMPTY_ADJECTIVES:
        if adj in mother_text or adj in shot_text:
            r.warnings.append(f"tính từ rỗng “{adj}” — thay bằng bằng chứng nhìn thấy")

    neg_body = neg_text.replace(NEGATIVE, "").replace(BRAND_NEG, "")
    items = [x for x in re.split(r"[，,、；;。\n]", neg_body) if x.strip()]
    if len(items) > NEGATIVE_ITEM_LIMIT:
        r.warnings.append(f"negative có {len(items)} mục — chỉ chặn có mục tiêu (≤ {NEGATIVE_ITEM_LIMIT})")

    return r


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="Kiểm luật cứng prompt T1 to 9")
    ap.add_argument("files", nargs="+", type=Path)
    ap.add_argument("--no-brand", action="store_true", help="brief yêu cầu không có chữ nào")
    ap.add_argument("--strict", action="store_true", help="cảnh báo cũng tính là lỗi")
    ap.add_argument("--allow", default="", help="chữ Latin được phép, ngăn bởi dấu phẩy (tên riêng)")
    args = ap.parse_args(argv)
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")

    allow = {w.strip() for w in args.allow.split(",") if w.strip()}
    failed = False
    for f in args.files:
        rep = lint(f.read_text(encoding="utf-8"), no_brand=args.no_brand, allow_latin=allow)
        bad = rep.errors or (args.strict and rep.warnings)
        failed |= bool(bad)
        print(f"{'FAIL' if bad else 'PASS'}  {f}")
        for e in rep.errors:
            print(f"  LỖI      {e}")
        for w in rep.warnings:
            print(f"  CẢNH BÁO {w}")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
