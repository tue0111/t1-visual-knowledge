import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

PATH_RE = re.compile(r"system/[A-Za-z0-9_.\-]+\.(?:md|txt)")


def _read(name):
    return (ROOT / name).read_text(encoding="utf-8")


class TestDocsLinks(unittest.TestCase):
    def test_paths_in_entry_docs_exist(self):
        missing = []
        for doc in ("AGENTS.md", "README.md"):
            for p in sorted(set(PATH_RE.findall(_read(doc)))):
                if not (ROOT / p).is_file():
                    missing.append(f"{doc}: {p}")
        self.assertEqual(missing, [])

    def test_numbered_system_files_listed_in_agents(self):
        agents = _read("AGENTS.md")
        unlisted = [
            f.name
            for f in sorted((ROOT / "system").glob("[0-9][0-9]_*.md"))
            if f.name not in agents
        ]
        self.assertEqual(unlisted, [])

    def test_skill_dirs_have_matching_name(self):
        skills = ROOT / ".claude" / "skills"
        if not skills.is_dir():
            self.skipTest("no .claude/skills")
        problems = []
        for d in sorted(p for p in skills.iterdir() if p.is_dir()):
            skill = d / "SKILL.md"
            if not skill.is_file():
                problems.append(f"{d.name}: no SKILL.md")
                continue
            text = skill.read_text(encoding="utf-8")
            m = re.match(r"\A---\r?\n(.*?)\r?\n---", text, re.S)
            if not m:
                problems.append(f"{d.name}: no frontmatter")
                continue
            name = re.search(r"^name:\s*(.+?)\s*$", m.group(1), re.M)
            if not name or name.group(1).strip("\"'") != d.name:
                problems.append(f"{d.name}: name mismatch")
        self.assertEqual(problems, [])


if __name__ == "__main__":
    unittest.main()
