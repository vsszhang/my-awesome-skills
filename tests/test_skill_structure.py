import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class SkillStructureTest(unittest.TestCase):
    def test_skills_have_skill_md(self) -> None:
        skill_dirs = sorted(path.parent for path in (ROOT / "skills").glob("*/SKILL.md"))
        self.assertTrue(skill_dirs)
        for skill_dir in skill_dirs:
            frontmatter = (skill_dir / "SKILL.md").read_text(encoding="utf-8").split("\n---", 1)[0]
            name_line = next(line for line in frontmatter.splitlines() if line.startswith("name:"))
            self.assertEqual(skill_dir.name, name_line.split(":", 1)[1].strip())


if __name__ == "__main__":
    unittest.main()
