# My Awesome Skills

Personal collection of Codex and Agent Skills.

Small, reusable workflows for coding agents. 🧩

## Skills

| Skill | What it does | Invoke with |
| --- | --- | --- |
| [`conventional-commit-git`](skills/conventional-commit-git/) | Groups uncommitted changes and creates Conventional Commits | `$conventional-commit-git` |

## Install

### Install locations

Choose the scope that matches how you want to use a skill:

| Scope | Install into | Available in |
| --- | --- | --- |
| Project | `.agents/skills/<skill-name>/` | The current repository only |
| User | `~/.codex/skills/<skill-name>/` | Your Codex projects |

Project scope is a good default for testing. Use user scope when you want the skill available everywhere.

### With `gh`

The recommended installer is [`gh skill install`](https://cli.github.com/manual/gh_skill_install).

Install one skill for your user account:

```bash
gh skill install YOUR_GITHUB_NAME/my-awesome-skills conventional-commit-git \
  --agent codex \
  --scope user
```

Install all skills from this repository:

```bash
gh skill install YOUR_GITHUB_NAME/my-awesome-skills \
  --agent codex \
  --scope user \
  --all
```

### Update skills

Check for updates without changing installed files:

```bash
gh skill update conventional-commit-git --dry-run
```

Update the installed skill interactively:

```bash
gh skill update conventional-commit-git
```

Update all installed skills without prompting:

```bash
gh skill update --all
```

Use `gh skill update --force --all` only when you intend to overwrite local changes to installed skill files.

## Local development

Install from a local checkout into the current project:

```bash
gh skill install . \
  --from-local \
  --agent codex \
  --scope project
```

Validate all skills:

```bash
python3 scripts/validate-skills.py
```

Check a Conventional Commit message:

```bash
python3 scripts/check-commit-message.py "feat: add grouped feature"
```

Run the Git commit workflow fixture:

```bash
sh tests/run-forward-test.sh
```

### Without `gh`

You can install a skill with standard shell commands. Clone this repository first, then copy the skill to the scope you want.

Install for the current project:

```bash
mkdir -p .agents/skills/conventional-commit-git
cp -R skills/conventional-commit-git/. \
  .agents/skills/conventional-commit-git/
```

Install for your Codex user account:

```bash
mkdir -p "$HOME/.codex/skills/conventional-commit-git"
cp -R skills/conventional-commit-git/. \
  "$HOME/.codex/skills/conventional-commit-git/"
```

To install another skill, replace `conventional-commit-git` in both paths with its directory name. Restart Codex or start a new session after installation so the skill can be discovered.

## Safety

Skills may include scripts and file-operation instructions. Review each skill's `SKILL.md`, `scripts/`, `references/`, and `assets/` before installing third-party skills.

## Status

This repository is a personal work in progress. APIs, prompts, and folder layouts may change. ⭐
