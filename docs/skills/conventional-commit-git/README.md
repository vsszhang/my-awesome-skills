# Conventional Commit Git

`$conventional-commit-git` reviews uncommitted work on the current Git branch, groups related changes, and creates one or more local Conventional Commits. Invoke it explicitly; a general request to commit changes does not activate the Skill.

## What it does

The Skill inspects tracked and untracked changes, proposes coherent commit groups, and stages only the files or hunks belonging to the active group. It validates each commit message and rechecks the staged diff before committing.

For sufficiently complex changes, it runs one read-only subagent preflight to independently assess safe commit boundaries. The main agent retains responsibility for all staging and commit operations.

## Safety boundaries

The Skill works only in the current repository and branch. It never pushes, opens a pull request, creates or switches branches, amends commits, resets, cleans, stashes, or rewrites history. It preserves unrelated uncommitted work and stops for clarification when the index or hunk boundaries are ambiguous.

## When to use it

Use it after implementation and validation are complete, when you want intentionally scoped local commits. Do not use it when you want a branch, remote push, pull request, or history rewrite.

See [usage examples](examples.md) and the runtime [SKILL.md](../../../skills/conventional-commit-git/SKILL.md).
