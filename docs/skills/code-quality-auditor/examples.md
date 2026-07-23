# Code Quality Auditor examples

Invoke the Skill explicitly and state the desired target whenever possible.

## Audit a known source directory

```text
Use $code-quality-auditor to assess src/ before the next release. Do not modify files.
```

The audit reads only `src/`. Authentication middleware, deployment configuration, and other files outside `src/` are reported as out of scope if they are needed to confirm a finding.

## Assess a change

```text
Use $code-quality-auditor to review the changes in this pull request. Focus on release risk and do not modify files.
```

The audit starts from the supplied diff and may include only directly referenced first-party runtime code needed to interpret the change. The final report lists any added dependency paths.

## Audit a repository without naming a target

```text
Use $code-quality-auditor to assess this service for release readiness. Do not modify files.
```

The audit first creates an Auto Production Scope. It identifies the smallest first-party production surface, entry points, and directly consumed runtime configuration, then states its coverage and exclusions before presenting findings.

## Include an ignored path deliberately

```text
Use $code-quality-auditor to assess config/local-auth.ts, even though it is ignored. Redact any secrets and do not modify files.
```

An explicit target overrides the default ignored-untracked exclusion. The report must redact secrets and avoid reproducing credential values.
