# Contributing

## Add a skill

1. Create `skills/<skill-name>/` using lowercase letters, digits, and hyphens.
2. Add a concise `SKILL.md` with YAML frontmatter containing `name` and `description`.
3. Add `agents/openai.yaml` when the skill needs Codex UI metadata or explicit invocation policy.
4. Put deterministic code in `scripts/`, supporting guidance in `references/`, and output assets in `assets/`.
5. For a user-facing or complex skill, add `docs/skills/<skill-name>/README.md` for the human-facing overview and `examples.md` for representative invocation examples. Keep agent runtime instructions in `skills/<skill-name>/SKILL.md`; do not duplicate the full workflow in human documentation.
6. Run `python3 scripts/validate-skills.py`.
7. Update the skill table in `README.md` and the documentation index in `docs/README.md`.

## Commit policy

Use concise English Conventional Commit messages:

```text
feat: add release-notes skill
fix: correct skill metadata validation
refactor: simplify local install workflow
```

Keep unrelated skill changes in separate commits.
