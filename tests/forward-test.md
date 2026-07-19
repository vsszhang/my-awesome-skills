# Forward-test scenarios

Use a fresh checkout or temporary Git repository and explicitly invoke:

```text
$conventional-commit-git Review and commit the current changes in functional groups.
```

## Small, coherent change

Use a fixture that contains:

- one implementation change with its focused test;
- one untracked file belonging to the implementation group;

Expected behavior:

1. Inspect the branch and all staged, unstaged, and untracked changes.
2. Identify that the change is below the subagent thresholds and do not spawn a subagent.
3. Propose groups and Conventional Commit subjects before staging.
4. Commit the implementation, focused test, and related untracked file together.
5. Leave no unrelated file staged or committed, and explicitly report that nothing was pushed.

## Complex change

Use a separate fixture that reaches a semantic trigger (at least two independent commit groups or a file that needs hunk-level staging) or at least two scale signals. For example, change 8 or more files across `src/`, `tests/`, and `docs/`, with 500 or more added plus deleted lines and separate implementation, test, and documentation work.

Expected behavior:

1. Inspect the branch and determine that the subagent preflight is required.
2. Capture repository state, then spawn exactly one read-only subagent.
3. Verify that the subagent returns commit groups, exact paths, Conventional Commit messages, confidence, and diff-based evidence without changing repository state.
4. Recheck status, diff statistics, and untracked paths before staging; discard the report and re-evaluate if state changed.
5. Resolve supported recommendations, or stop for clarification when the grouping remains unsafe.

## Ambiguous staged boundary

Use an optional pre-existing staged change that is intentionally mixed with unstaged work.

Expected behavior:

1. Preserve the ambiguous staged boundary and stop for clarification before delegation or staging.
2. Do not use a subagent to bypass the clarification requirement.

The automated command-level approximation is `sh tests/run-forward-test.sh`. It retains a multi-group fixture and verifies explicit-path staging, separate commits, Conventional Commit subjects, and a clean final worktree; it does not replace the agent-level behavioral tests above.
