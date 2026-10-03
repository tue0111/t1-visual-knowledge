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


if __name__ == "__main__":
    unittest.main()
