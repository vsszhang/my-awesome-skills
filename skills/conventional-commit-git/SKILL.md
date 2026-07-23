---
name: conventional-commit-git
description: "Review uncommitted changes on the current Git branch, group them by coherent feature or fix, and create one or more local commits using Conventional Commit messages. Invoke only when the human explicitly calls `$conventional-commit-git`; never invoke this skill from inferred intent, and never push or open a pull request."
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
3. Stop and ask for clarification before delegation or staging when the existing index has mixed or unclear boundaries, a hunk cannot be separated safely, or a path appears to contain a secret, local-only configuration, or build output.
4. Build logical commit groups. Group implementation with directly related tests, API changes with their contracts and focused tests, documentation-only updates, isolated bug fixes, and independent refactors. Keep unrelated edits, secrets, local configuration, and build output out of commits.
5. Decide whether to run one read-only subagent preflight.
   - Run it when any semantic signal applies: there are at least two independent commit groups, one or more files require hunk-level staging, or the user explicitly requests an independent review of the commit split.
   - Otherwise, count these scale signals and run it when at least two apply: at least 8 changed or untracked files; at least 3 distinct first-level directories, with root-level files counting as one directory; at least 500 added plus deleted lines; or at least 2 change surfaces among implementation, tests, documentation, dependency manifests, and configuration.
   - Do not run it for a single coherent, small change that does not meet those conditions. Continue with the normal workflow.
6. When preflight is required, capture the current `git status --short --branch`, uncached and cached diff statistics, and untracked-path list; then spawn exactly one subagent to inspect that snapshot.
   - Give the subagent a read-only task: inspect Git status, diffs, untracked paths, and relevant history only. It must not edit files or run `git add`, `git commit`, `git reset`, `git restore`, `git checkout`, `git switch`, `git clean`, `git stash`, `git merge`, `git rebase`, `git push`, or any other Git command that changes repository state.
   - Require a concise report containing proposed commit groups with exact paths, a Conventional Commit message for each group, suspected omissions or paths that should not be committed, confidence for each group, and diff-based evidence.
   - If subagents are unavailable, report that no independent preflight could run. Continue only when the main inspection establishes a clear boundary; otherwise stop for clarification.
7. After the subagent returns, rerun the captured status, diff-statistics, and untracked-path checks. If any result changed, discard the report and return to state inspection; do not stage from a stale report. Resolve disagreements using the diffs. If the evidence does not establish a safe grouping, stop for clarification.
8. Present proposed groups, exact paths, proposed commit type and subject, and uncertainties before changing the index. If grouping is ambiguous, stop for clarification.
9. For each group, stage only exact paths with `git add -- <path>...`; inspect `git diff --cached --name-status`, `git diff --cached --check`, and `git diff --cached --stat`. Stop if the staged diff contains another group.
   - When one tracked file contains unrelated hunks, use `git add -p -- <path>` and accept hunks only when they belong entirely to the current group.
   - Review the cached patch after each hunk with `git diff --cached -- <path>`.
   - Do not use patch mode to guess at an ambiguous hunk. Stop and ask the user when a hunk cannot be separated safely.
   - For an untracked file, stage the whole file only when the complete file belongs to the group; do not partially stage a new file by assumption.
10. Create an English Conventional Commit subject in the form `<type>(<optional-scope>): <imperative subject>`. Prefer `feat`, `fix`, `refactor`, `docs`, `test`, `chore`, `perf`, `style`, `build`, and `ci`. Use `git commit -m "<message>"`.
11. After every commit, run `git show --stat --oneline --summary HEAD` and `git status --short --branch`. Recalculate remaining groups from the current state.
12. Finish with the branch, each commit hash and message, paths per commit, remaining uncommitted paths, validation performed, whether a read-only preflight ran, and an explicit statement that nothing was pushed.

## Commit quality rules

- Make every commit independently understandable and reviewable.
- Do not create empty commits or combine unrelated feature, bug fix, documentation, and refactor changes.
- Do not split files that must change together for the repository to build or test.
- Preserve all uncommitted work that is not part of the selected group.
- Validate each proposed subject against the repository's Conventional Commit checker when available: `python3 scripts/check-commit-message.py "<message>"`.
