import subprocess
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CHECKER = ROOT / "scripts" / "check-commit-message.py"


class CommitMessageTest(unittest.TestCase):
    def run_checker(self, subject: str) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            [sys.executable, str(CHECKER), subject],
            check=False,
            capture_output=True,
            text=True,
        )

    def test_accepts_supported_subjects(self) -> None:
        for subject in (
            "feat: add grouped feature",
            "fix(parser): handle empty input",
            "refactor!: remove legacy commit path",
        ):
            with self.subTest(subject=subject):
                self.assertEqual(self.run_checker(subject).returncode, 0)

    def test_rejects_invalid_subjects(self) -> None:
        for subject in (
            "Add grouped feature",
            "feature: add grouped feature",
            "fix: " + "x" * 70,
        ):
            with self.subTest(subject=subject):
                self.assertNotEqual(self.run_checker(subject).returncode, 0)

