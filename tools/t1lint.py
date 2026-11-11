#!/usr/bin/env python3
"""t1lint — kiểm luật cứng cho prompt T1 to 9 (chỉ thư viện chuẩn).

Dùng:
    python tools/t1lint.py prompt.txt [prompt2.txt ...]
    python tools/t1lint.py --no-brand prompt.txt      # brief yêu cầu không chữ (chỉ khuôn 3 phần)
    python tools/t1lint.py --strict prompt.txt        # cảnh báo cũng làm fail
    python tools/t1lint.py --style keyword f.txt      # ép kiểu; mặc định auto: có 【母版锁】 là 3 phần, có “—— 负面：” là keyword

Hai kiểu hợp lệ: khuôn 3 phần (mặc định, system/04) và khuôn keyword một dòng (system/08).
Ví dụ 3 phần nằm ở examples/*.txt; ví dụ keyword nằm ở examples/keyword/*.txt để hai glob không giẫm nhau.

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


# ---------------------------------------------------------------- khuôn keyword (system/08)
KW_SEP = re.compile(r"——\s*负面[：:]")
KW_RATIO = re.compile(r"^\d{1,2}(?:\.\d+)?:\d{1,2}")
KW_MIN_KEYWORDS = 8
ALLOWED_LATIN_KW = ALLOWED_LATIN | {"F"}  # khẩu độ: 85毫米F1.4
KW_HAND_OK = ("五指完整", "不入画", "看不见", "无手")
NEGATION_BEFORE = "不无勿别"


def detect_style(text: str) -> str:
    """'three' | 'keyword' | 'unknown'."""
    if MOTHER in text or SHOT in text or NEGATIVE in text:
        return "three"
    if KW_SEP.search(text):
        return "keyword"
    return "unknown"


def keyword_prompts(text: str) -> list[str]:
    """Mỗi dòng không rỗng, không phải tiêu đề (#) hay hàng rào code (```) là một prompt."""
    out = []
    for line in text.splitlines():
        s = line.strip()
        if s and not s.startswith(("#", "```")):
            out.append(s)
    return out


def lint_keyword(text: str, allow_latin: set[str] | None = None) -> Report:
    r = Report()
    allow = ALLOWED_LATIN_KW | (allow_latin or set())
    prompts = keyword_prompts(text)
    if not prompts:
        r.errors.append("không có prompt nào")
        return r
    for i, p in enumerate(prompts, 1):
        tag = f"prompt {i}: "
        if len(KW_SEP.findall(p)) != 1:
            r.errors.append(f"{tag}cần đúng 1 dấu phân cách “—— 负面：”, thấy {len(KW_SEP.findall(p))}")
            continue
        body, neg = KW_SEP.split(p)
        if not KW_RATIO.match(body):
            r.errors.append(f"{tag}phải mở bằng tỷ lệ khung (vd 3:4竖构图)")
        if body.count("+") < KW_MIN_KEYWORDS:
            r.errors.append(f"{tag}thân prompt cần ≥ {KW_MIN_KEYWORDS} keyword nối bằng +")
        if MARK in p:
            r.errors.append(f"{tag}“T1 to 9” không nằm trong prompt keyword (chữ ký đóng ở hậu kỳ)")
        no_person = "无人物" in body
        if "成年" not in body and not no_person:
            r.errors.append(f"{tag}thiếu chữ “成年” (hoặc “无人物” nếu không có người)")
        if not no_person and "不像任何真人" not in body:
            r.warnings.append(f"{tag}thiếu “不像任何真人”")
        if "手" in body and not any(k in body for k in KW_HAND_OK):
            r.warnings.append(f"{tag}có tay nhưng thiếu 五指完整 (hoặc ghi tay không nhập ảnh)")
        for word in sorted(set(re.findall(r"[A-Za-z]+", p.replace(MARK, "")))):
            if word not in allow:
                r.warnings.append(f"{tag}chữ Latin “{word}” — prompt phải tiếng Trung (trừ tỷ lệ, số ống kính, khẩu độ)")
        for adj in EMPTY_ADJECTIVES:
            if adj in body:
                r.warnings.append(f"{tag}tính từ rỗng “{adj}” — thay bằng bằng chứng nhìn thấy")
        items = [x.strip() for x in neg.split("+") if x.strip()]
        if not items:
            r.errors.append(f"{tag}negative rỗng")
        if len(items) > NEGATIVE_ITEM_LIMIT:
            r.warnings.append(f"{tag}negative có {len(items)} mục — chỉ chặn có mục tiêu (≤ {NEGATIVE_ITEM_LIMIT})")
        for it in items:
            pos = body.find(it)
            if len(it) >= 3 and pos >= 0 and not (pos > 0 and body[pos - 1] in NEGATION_BEFORE):
                r.warnings.append(f"{tag}mâu thuẫn dương–âm: “{it}” vừa ở thân vừa ở negative")
    return r


def lint_any(text: str, style: str = "auto", no_brand: bool = False, allow_latin: set[str] | None = None) -> tuple[str, Report]:
    st = detect_style(text) if style == "auto" else style
    if st == "three":
        return st, lint(text, no_brand=no_brand, allow_latin=allow_latin)
    if st == "keyword":
        return st, lint_keyword(text, allow_latin=allow_latin)
    r = Report()
    r.errors.append("không nhận ra định dạng: cần 3 phần 【母版锁】… hoặc keyword một dòng có “—— 负面：”")
    return "unknown", r


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="Kiểm luật cứng prompt T1 to 9")
    ap.add_argument("files", nargs="+", type=Path)
    ap.add_argument("--no-brand", action="store_true", help="brief yêu cầu không có chữ nào")
    ap.add_argument("--strict", action="store_true", help="cảnh báo cũng tính là lỗi")
    ap.add_argument("--allow", default="", help="chữ Latin được phép, ngăn bởi dấu phẩy (tên riêng)")
    ap.add_argument("--style", choices=["auto", "three", "keyword"], default="auto", help="kiểu prompt; auto tự nhận")
    args = ap.parse_args(argv)
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")

    allow = {w.strip() for w in args.allow.split(",") if w.strip()}
    failed = False
    for f in args.files:
        style, rep = lint_any(f.read_text(encoding="utf-8"), style=args.style, no_brand=args.no_brand, allow_latin=allow)
        bad = rep.errors or (args.strict and rep.warnings)
        failed |= bool(bad)
        print(f"{'FAIL' if bad else 'PASS'}  {f}" + ("  [keyword]" if style == "keyword" else ""))
        for e in rep.errors:
            print(f"  LỖI      {e}")
        for w in rep.warnings:
            print(f"  CẢNH BÁO {w}")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
