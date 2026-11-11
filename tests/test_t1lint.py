import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))

import t1lint  # noqa: E402

GOOD = (ROOT / "examples" / "A_cinema_lantern.txt").read_text(encoding="utf-8")


class TestExamples(unittest.TestCase):
    def test_all_examples_pass_strict(self):
        for f in sorted((ROOT / "examples").glob("*.txt")):
            rep = t1lint.lint(f.read_text(encoding="utf-8"))
            self.assertEqual(rep.errors, [], f.name)
            self.assertEqual(rep.warnings, [], f.name)


class TestErrors(unittest.TestCase):
    def test_missing_brand_block(self):
        rep = t1lint.lint(GOOD.replace(t1lint.BRAND, ""))
        self.assertTrue(any("固定品牌角标" in e for e in rep.errors))

    def test_brand_altered(self):
        rep = t1lint.lint(GOOD.replace("衬线体", "无衬线体", 1))
        self.assertFalse(rep.ok)

    def test_missing_negative_exception(self):
        rep = t1lint.lint(GOOD.replace(t1lint.BRAND_NEG, ""))
        self.assertTrue(any("ngoại lệ" in e for e in rep.errors))

    def test_fourth_section(self):
        rep = t1lint.lint(GOOD + "\n【品牌】\nT1 to 9\n")
        self.assertFalse(rep.ok)

    def test_two_mothers(self):
        rep = t1lint.lint("【母版锁 · 甲】\n" + GOOD)
        self.assertFalse(rep.ok)

    def test_wrong_order(self):
        mother, rest = GOOD.split("【分镜", 1)
        shot, neg = rest.split("【通用负面提示词】", 1)
        swapped = "【通用负面提示词】" + neg + mother + "【分镜" + shot
        self.assertFalse(t1lint.lint(swapped).ok)

    def test_missing_one_image_line(self):
        rep = t1lint.lint(GOOD.replace(t1lint.ONE_IMAGE, "只要"))
        self.assertTrue(any("một ảnh" in e for e in rep.errors))

    def test_no_brand_mode_rejects_mark(self):
        self.assertFalse(t1lint.lint(GOOD, no_brand=True).ok)

    def test_no_brand_mode_accepts_clean(self):
        clean = GOOD.replace(t1lint.BRAND + "\n", "").replace(t1lint.BRAND_NEG, "禁止任何文字。")
        self.assertTrue(t1lint.lint(clean, no_brand=True).ok)


class TestAlbum(unittest.TestCase):
    def test_two_shots_ok(self):
        album = GOOD.replace("【通用负面提示词】", "【分镜 · 第二镜】\n\n她转身下楼。\n\n【通用负面提示词】")
        self.assertTrue(t1lint.lint(album).ok)


class TestWarnings(unittest.TestCase):
    def test_empty_adjective(self):
        rep = t1lint.lint(GOOD.replace("平视。", "平视，高品质，8K。"))
        self.assertTrue(rep.ok)
        self.assertTrue(any("高品质" in w for w in rep.warnings))

    def test_latin_word(self):
        rep = t1lint.lint(GOOD.replace("平视。", "平视，rim light。"))
        self.assertTrue(any("rim" in w for w in rep.warnings))

    def test_allowed_proper_noun(self):
        rep = t1lint.lint(GOOD.replace("平视。", "平视，Hanoi。"), allow_latin={"Hanoi"})
        self.assertEqual(rep.warnings, [])

    def test_negative_dump(self):
        dump = "，".join(f"错误{i}" for i in range(20))
        rep = t1lint.lint(GOOD.replace("人物直视镜头，", dump + "，"))
        self.assertTrue(any("negative" in w for w in rep.warnings))


class TestCli(unittest.TestCase):
    def test_cli_exit_codes(self):
        self.assertEqual(t1lint.main([str(ROOT / "examples" / "A_cinema_lantern.txt")]), 0)


KW_FILE = ROOT / "examples" / "keyword" / "E_smoke_backlight_keyword.txt"
KW_ONE = next(l for l in KW_FILE.read_text(encoding="utf-8").splitlines() if l.strip() and not l.startswith("#"))


class TestKeywordStyle(unittest.TestCase):
    def test_keyword_examples_pass_strict(self):
        files = sorted((ROOT / "examples" / "keyword").glob("*.txt"))
        self.assertTrue(files)
        for f in files:
            rep = t1lint.lint_keyword(f.read_text(encoding="utf-8"))
            self.assertEqual(rep.errors, [], f.name)
            self.assertEqual(rep.warnings, [], f.name)

    def test_top_level_examples_stay_three_part(self):
        for f in sorted((ROOT / "examples").glob("*.txt")):
            self.assertEqual(t1lint.detect_style(f.read_text(encoding="utf-8")), "three", f.name)

    def test_detect_style(self):
        self.assertEqual(t1lint.detect_style(GOOD), "three")
        self.assertEqual(t1lint.detect_style(KW_ONE), "keyword")
        self.assertEqual(t1lint.detect_style("chỉ là chữ thường"), "unknown")

    def test_one_prompt_ok(self):
        rep = t1lint.lint_keyword(KW_ONE)
        self.assertEqual((rep.errors, rep.warnings), ([], []))

    def test_missing_separator(self):
        rep = t1lint.lint_keyword(KW_ONE.split("——")[0])
        self.assertTrue(any("phân cách" in e for e in rep.errors))

    def test_missing_ratio(self):
        rep = t1lint.lint_keyword(KW_ONE.replace("16:9横构图", "横构图", 1))
        self.assertTrue(any("tỷ lệ" in e for e in rep.errors))

    def test_too_few_keywords(self):
        rep = t1lint.lint_keyword("3:4竖构图+一名成年女性——负面：文字")
        self.assertTrue(any("keyword" in e for e in rep.errors))

    def test_brand_mark_rejected(self):
        rep = t1lint.lint_keyword(KW_ONE + "T1 to 9")
        self.assertTrue(any("T1 to 9" in e for e in rep.errors))

    def test_missing_adult_marker(self):
        rep = t1lint.lint_keyword(KW_ONE.replace("成年", "", 1))
        self.assertTrue(any("成年" in e for e in rep.errors))

    def test_no_person_exempt(self):
        rep = t1lint.lint_keyword("3:4竖构图+静物+无人物+一朵花+一张桌+一盏灯+一块布+一只杯+一本书+一支笔+柔光—— 负面：文字")
        self.assertEqual(rep.errors, [])

    def test_negative_dump_warns(self):
        dump = "+".join(f"错误{i}" for i in range(20))
        rep = t1lint.lint_keyword(KW_ONE.split("负面：")[0] + "负面：" + dump)
        self.assertTrue(any("negative" in w for w in rep.warnings))

    def test_latin_word_warns_but_f_allowed(self):
        rep = t1lint.lint_keyword(KW_ONE.replace("浅景深", "rim light浅景深", 1))
        self.assertTrue(any("rim" in w for w in rep.warnings))
        self.assertFalse(any("“F”" in w for w in rep.warnings))

    def test_hand_without_finger_count_warns(self):
        rep = t1lint.lint_keyword(KW_ONE.replace("背景空无一物", "右手举起背景空无一物", 1))
        self.assertTrue(any("五指完整" in w for w in rep.warnings))

    def test_positive_negative_conflict_warns(self):
        rep = t1lint.lint_keyword(KW_ONE + "+背景空无一物")
        self.assertTrue(any("mâu thuẫn" in w for w in rep.warnings))

    def test_lint_any_unknown_is_error(self):
        style, rep = t1lint.lint_any("không phải prompt")
        self.assertEqual(style, "unknown")
        self.assertFalse(rep.ok)

    def test_cli_auto_detect_both_styles(self):
        self.assertEqual(t1lint.main([str(ROOT / "examples" / "A_cinema_lantern.txt"), str(KW_FILE)]), 0)
        self.assertEqual(t1lint.main(["--strict", str(KW_FILE)]), 0)


if __name__ == "__main__":
    unittest.main()
