# Development Design Document examples

## Turn a discussion into an implementation-ready design

```text
Use $development-design-doc to turn the design decisions in this discussion into a Markdown document in docs/design/. Keep confirmed decisions separate from proposals and open questions. Make the document easy for the team to read, and include the architecture, module flow, key data structures, acceptance conditions, and a task checklist that an agent can follow.
```

The Skill inspects the available discussion and project guidance, cites available source pointers, and marks any unresolved behavior that blocks implementation instead of inventing a decision.

## Document a feature in an existing repository

```text
Use $development-design-doc to write an implementation-ready design for the new reporting workflow. Inspect the relevant current modules and interfaces first. Save it at docs/design/reporting-workflow.md. Keep the prose human-readable; link each major task to a requirement and its acceptance condition. Do not implement the feature.
```

The document should distinguish current behavior from the proposal and use repository-specific module names and conventions.

## Explain an existing architecture for onboarding

```text
Use $development-design-doc to document the current ingestion pipeline for new team members. Base it on the source code and existing docs, include an architecture diagram and the end-to-end flow, and label any inferred or uncertain behavior. This is an explanatory document, so keep implementation tasks out unless the sources identify planned work.
```

For an architecture overview, the Skill focuses on the human explanation and evidence. It does not turn every observed behavior into a new requirement.

## Update a design after a decision changes

```text
Use $development-design-doc to update docs/design/search.md with the decision from the latest discussion. Preserve still-valid content, mark the superseded decision clearly, update affected contracts and tasks, and report any remaining conflicts. Do not change code.
```

The Skill checks the existing document before editing and avoids making the implementation appear compliant by silently rewriting intended behavior.
