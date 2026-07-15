---
name: conventional-commit-git
description: Review uncommitted changes on the current Git branch, group them by coherent feature or fix, and create one or more local commits using Conventional Commit messages. Invoke only when the human explicitly calls `$conventional-commit-git`; never invoke this skill from inferred intent, and never push or open a pull request.
---

# Conventional Commit Git

Review and commit the current repository's uncommitted changes. Use a single commit when the changes form one coherent unit; otherwise split them into feature-based commits while preserving unrelated user work.

## Invocation and safety

- Run this workflow only when the user explicitly invokes `$conventional-commit-git` or explicitly names this skill.
- Do not treat requests such as “commit these changes” as permission to invoke the skill unless the user also explicitly invokes it.
- Operate only in the current Git repository and current branch. Do not create or switch branches.
- Never push, create a PR, amend an existing commit, reset, clean, stash, or rewrite history.
- Do not use `git add -A` or `git add .` by default. Stage only the paths belonging to the current commit group.
- If the repository is missing, the branch is detached, or there are no uncommitted changes, stop and report the condition.
- If the existing index contains mixed or unclear staged changes, stop before changing the index and ask the user to resolve the staging boundary.

## Workflow

1. Establish repository state with `git rev-parse --show-toplevel`, `git branch --show-current`, `git status --short --branch`, `git diff --stat`, and `git diff --cached --stat`.
2. Inspect both tracked diffs (`git diff` and `git diff --cached`) and untracked paths. Read enough of each diff to understand intent; do not infer intent from filenames alone.
3. Build logical commit groups. Group implementation with directly related tests, API changes with their contracts and focused tests, documentation-only updates, isolated bug fixes, and independent refactors. Keep unrelated edits, secrets, local configuration, and build output out of commits.
4. Present proposed groups, exact paths, proposed commit type and subject, and uncertainties before changing the index. If grouping is ambiguous, stop for clarification.
5. For each group, stage only exact paths with `git add -- <path>...`; inspect `git diff --cached --name-status`, `git diff --cached --check`, and `git diff --cached --stat`. Stop if the staged diff contains another group.
   - When one tracked file contains unrelated hunks, use `git add -p -- <path>` and accept hunks only when they belong entirely to the current group.
   - Review the cached patch after each hunk with `git diff --cached -- <path>`.
   - Do not use patch mode to guess at an ambiguous hunk. Stop and ask the user when a hunk cannot be separated safely.
   - For an untracked file, stage the whole file only when the complete file belongs to the group; do not partially stage a new file by assumption.
6. Create an English Conventional Commit subject in the form `<type>(<optional-scope>): <imperative subject>`. Prefer `feat`, `fix`, `refactor`, `docs`, `test`, `chore`, `perf`, `style`, `build`, and `ci`. Use `git commit -m "<message>"`.
7. After every commit, run `git show --stat --oneline --summary HEAD` and `git status --short --branch`. Recalculate remaining groups from the current state.
8. Finish with the branch, each commit hash and message, paths per commit, remaining uncommitted paths, validation performed, and an explicit statement that nothing was pushed.

## Commit quality rules

- Make every commit independently understandable and reviewable.
- Do not create empty commits or combine unrelated feature, bug fix, documentation, and refactor changes.
- Do not split files that must change together for the repository to build or test.
- Preserve all uncommitted work that is not part of the selected group.
- Validate each proposed subject against the repository's Conventional Commit checker when available: `python3 scripts/check-commit-message.py "<message>"`.
