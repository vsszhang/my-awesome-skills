# Forward-test scenario

Use a fresh checkout or temporary Git repository and explicitly invoke:

```text
$conventional-commit-git Review and commit the current changes in functional groups.
```

The fixture should contain:

- one implementation change with its focused test;
- one documentation change;
- one untracked file belonging to the implementation group;
- an optional pre-existing staged change that is intentionally mixed.

Expected behavior:

1. Inspect the branch and all staged, unstaged, and untracked changes.
2. Propose groups and Conventional Commit subjects before staging.
3. Commit implementation and test changes together.
4. Commit documentation separately.
5. Preserve an ambiguous pre-existing staged boundary and stop for clarification.
6. Leave no unrelated file staged or committed, and explicitly report that nothing was pushed.

The automated command-level approximation is `sh tests/run-forward-test.sh`. It verifies explicit-path staging, separate commits, Conventional Commit subjects, and a clean final worktree; it does not replace an agent-level behavioral test.
