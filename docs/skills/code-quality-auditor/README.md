# Code Quality Auditor

`$code-quality-auditor` provides an evidence-first, read-only assessment of a repository, module, diff, or file set. It does not modify source files, install dependencies, change configuration, or create external tickets.

## What it evaluates

The main agent combines three isolated specialist reports:

- `security-auditor` reviews OWASP-oriented risks, including injection, XSS, access control, sensitive-data exposure, unsafe interfaces, and security configuration.
- `quality-checker` reviews code smells and maintainability, including duplication, complex control flow, naming, cohesion, coupling, and testability.
- `perf-analyzer` reviews performance anti-patterns, including N+1 access, blocking work, unbounded processing, caching gaps, and unnecessary rendering.

The final assessment presents evidence, severity, confidence, product and technical impact, P0-P3 priority, and a validation plan. All agents inherit the model selected for the current Codex session.

## Scope behavior

An explicit target is strict: naming `src/`, a module, a file set, or a diff prevents the audit from reading outside that target. Missing context is reported as out of scope rather than inferred.

When no target is given, the Skill builds an Auto Production Scope from the smallest first-party production surface and directly consumed runtime configuration. It records audited paths, context-only paths, exclusions, selection mode, and coverage limits in a scope manifest.

Ignored, untracked files are not read by default, protecting local secrets and personal environment state. `.gitignore` does not automatically exclude tracked files and does not override a user-specified target. Generated files, dependency/vendor directories, caches, coverage, and build artifacts remain excluded unless the user explicitly includes them.

## When to use it

Use it before a release, when triaging a risky change, when assessing an inherited service, or when a product/technical leadership decision needs an evidence-backed quality baseline. Do not use it to implement fixes; request remediation in a separate task after reviewing the report.

See [usage examples](examples.md) and the runtime [SKILL.md](../../../skills/code-quality-auditor/SKILL.md).
