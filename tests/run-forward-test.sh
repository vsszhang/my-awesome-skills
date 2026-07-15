#!/bin/sh
set -eu

repo="$(mktemp -d)"
trap 'rm -rf "$repo"' EXIT

cd "$repo"
git init -q -b main
git config user.email test@example.com
git config user.name "Skill Fixture"
mkdir -p src tests docs
printf '%s\n' 'initial implementation' > src/feature.txt
printf '%s\n' 'initial test' > tests/feature.txt
printf '%s\n' '# Usage' > docs/usage.md
git add -- src tests docs
git commit -q -m 'chore: create fixture baseline'

# Simulate a multi-functional worktree: source plus test, documentation, and a new file.
printf '%s\n' 'feature implementation' >> src/feature.txt
printf '%s\n' 'feature coverage' >> tests/feature.txt
printf '%s\n' 'new usage example' >> docs/usage.md
printf '%s\n' 'new untracked fixture file' > src/new-feature.txt

# Simulate the skill's explicit-path staging and separate commits.
git add -- src/feature.txt tests/feature.txt src/new-feature.txt
git diff --cached --check
git commit -q -m 'feat: add grouped feature'

git add -- docs/usage.md
git diff --cached --check
git commit -q -m 'docs: update usage example'

test "$(git rev-list --count HEAD)" -eq 3
test -z "$(git status --porcelain)"
test "$(git log --format=%s -2 | sed -n '1p')" = 'docs: update usage example'
test "$(git log --format=%s -2 | sed -n '2p')" = 'feat: add grouped feature'

# Prepare a separate repository with a pre-existing staged boundary. The skill
# must inspect this state and stop when the boundary is unclear.
mixed="$(mktemp -d)"
git -C "$mixed" init -q -b main
git -C "$mixed" config user.email test@example.com
git -C "$mixed" config user.name "Skill Fixture"
mkdir -p "$mixed/src" "$mixed/docs"
printf '%s\n' base > "$mixed/src/feature.txt"
printf '%s\n' base > "$mixed/docs/usage.md"
git -C "$mixed" add -- src docs
git -C "$mixed" commit -q -m 'chore: create staged-boundary fixture'
printf '%s\n' staged > "$mixed/docs/usage.md"
printf '%s\n' unstaged > "$mixed/src/feature.txt"
git -C "$mixed" add -- docs/usage.md
test "$(git -C "$mixed" diff --cached --name-only)" = 'docs/usage.md'
test "$(git -C "$mixed" diff --name-only)" = 'src/feature.txt'
rm -rf "$mixed"

printf '%s\n' 'Forward-test fixture passed: grouped commits, untracked file, staged boundary, clean worktree.'
