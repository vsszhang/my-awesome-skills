import importlib.util
import unittest
from pathlib import Path
from tempfile import TemporaryDirectory


ROOT = Path(__file__).resolve().parents[1]
VALIDATOR_PATH = ROOT / "scripts" / "validate-skills.py"
SPEC = importlib.util.spec_from_file_location("validate_skills", VALIDATOR_PATH)
assert SPEC and SPEC.loader
VALIDATOR = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(VALIDATOR)

parse_frontmatter = VALIDATOR.parse_frontmatter


class SkillStructureTest(unittest.TestCase):
    def test_skills_have_skill_md(self) -> None:
        skill_dirs = sorted(path.parent for path in (ROOT / "skills").glob("*/SKILL.md"))
        self.assertTrue(skill_dirs)
        for skill_dir in skill_dirs:
            frontmatter = (skill_dir / "SKILL.md").read_text(encoding="utf-8").split("\n---", 1)[0]
            name_line = next(line for line in frontmatter.splitlines() if line.startswith("name:"))
            self.assertEqual(skill_dir.name, name_line.split(":", 1)[1].strip())

    def test_rejects_unquoted_description_with_yaml_mapping_syntax(self) -> None:
        with TemporaryDirectory() as temp_dir:
            skill_md = Path(temp_dir) / "SKILL.md"
            skill_md.write_text(
                "---\n"
                "name: sample-skill\n"
                "description: Audit with specialists: security-auditor\n"
                "---\n",
                encoding="utf-8",
            )

            with self.assertRaisesRegex(ValueError, "double-quoted YAML string"):
                parse_frontmatter(skill_md)

    def test_accepts_quoted_description_with_yaml_mapping_syntax(self) -> None:
        with TemporaryDirectory() as temp_dir:
            skill_md = Path(temp_dir) / "SKILL.md"
            skill_md.write_text(
                "---\n"
                "name: sample-skill\n"
                "description: \"Audit with specialists: security-auditor\"\n"
                "---\n",
                encoding="utf-8",
            )

            self.assertEqual(
                parse_frontmatter(skill_md)["description"],
                "Audit with specialists: security-auditor",
            )


if __name__ == "__main__":
    unittest.main()
