#!/usr/bin/env python3
"""Validate the repository's SKILL.md files without external dependencies."""

import json
from pathlib import Path
import re
import sys


ROOT = Path(__file__).resolve().parents[1]
SKILLS_DIR = ROOT / "skills"
NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
FRONTMATTER_KEYS = {"name", "description"}


def parse_frontmatter(path: Path) -> dict[str, str]:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        raise ValueError("missing YAML frontmatter")
    end = text.find("\n---", 4)
    if end == -1:
        raise ValueError("unterminated YAML frontmatter")

    values: dict[str, str] = {}
    for line in text[4:end].splitlines():
        if not line.strip():
            continue
        key, separator, value = line.partition(":")
        if not separator or not key.strip() or not value.strip():
            raise ValueError(f"invalid frontmatter line: {line!r}")
        key = key.strip()
        if key not in FRONTMATTER_KEYS:
            raise ValueError(f"unsupported frontmatter key: {key!r}")
        if key in values:
            raise ValueError(f"duplicate frontmatter key: {key!r}")

        scalar = value.strip()
        if key == "description":
            if not scalar.startswith('"'):
                raise ValueError("description must be a double-quoted YAML string")
            try:
                parsed = json.loads(scalar)
            except json.JSONDecodeError as exc:
                raise ValueError(f"invalid quoted description: {exc.msg}") from exc
            if not isinstance(parsed, str):
                raise ValueError("description must be a string")
            values[key] = parsed
        else:
            values[key] = scalar
    return values


def validate() -> int:
    if not SKILLS_DIR.is_dir():
        print("ERROR: skills/ directory not found")
        return 1

    skill_dirs = sorted(path.parent for path in SKILLS_DIR.glob("*/SKILL.md"))
    if not skill_dirs:
        print("ERROR: no skills found")
        return 1

    errors: list[str] = []
    for skill_dir in skill_dirs:
        name = skill_dir.name
        if not NAME_RE.fullmatch(name):
            errors.append(f"{skill_dir}: directory name must be hyphen-case")
        try:
            metadata = parse_frontmatter(skill_dir / "SKILL.md")
        except (OSError, ValueError) as exc:
            errors.append(f"{skill_dir}: {exc}")
            continue
        if metadata.get("name") != name:
            errors.append(f"{skill_dir}: frontmatter name must be {name!r}")
        if not metadata.get("description"):
            errors.append(f"{skill_dir}: description is required")

    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1

    print(f"Validated {len(skill_dirs)} skill(s)")
    return 0


if __name__ == "__main__":
    sys.exit(validate())
