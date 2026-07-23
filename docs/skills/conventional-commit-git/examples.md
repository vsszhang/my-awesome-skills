# Conventional Commit Git examples

Invoke the Skill explicitly so it can distinguish a request for a safe local commit workflow from a general Git question.

## Commit a coherent feature

```text
Use $conventional-commit-git to review and commit the current feature work.
```

The Skill inspects the working tree, proposes a Conventional Commit message and exact paths, then stages and creates only the approved local commit. It does not push.

## Split unrelated changes

```text
Use $conventional-commit-git to group the current changes into separate local commits by functional module.
```

The Skill separates unrelated implementation, tests, documentation, configuration, and fixes where doing so preserves a buildable and reviewable history.

## Request an independent grouping check

```text
Use $conventional-commit-git and perform an independent review of the proposed commit split before staging.
```

The Skill runs its read-only preflight when the conditions are met, rechecks repository state after the report, and keeps all write operations with the main agent.
