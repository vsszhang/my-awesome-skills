#!/usr/bin/env python3
"""Check a commit subject against the repository's Conventional Commit policy."""

from __future__ import annotations

import re
import sys


TYPES = "feat|fix|refactor|docs|test|chore|perf|style|build|ci"
SUBJECT_RE = re.compile(
    rf"^(?:{TYPES})(?:\([a-z0-9][a-z0-9._/-]*\))?!?: \S.*$"
)


def validate(subject: str) -> tuple[bool, str]:
    subject = subject.rstrip("\n")
    if "\n" in subject:
        return False, "commit subject must be a single line"
    if len(subject) > 72:
        return False, "commit subject must be 72 characters or fewer"
    if not SUBJECT_RE.fullmatch(subject):
        return False, "expected <type>(<scope>)!: <subject> using an allowed type"
    return True, "valid Conventional Commit subject"


def main() -> int:
    subject = " ".join(sys.argv[1:]) if len(sys.argv) > 1 else sys.stdin.read()
    valid, message = validate(subject)
    print(message)
    return 0 if valid else 1


if __name__ == "__main__":
    raise SystemExit(main())

