# Development Design Document

`$development-design-doc` creates or updates software design documents from requirements, source conversations, existing documentation, and repository context. The documents are written for people first, with precise implementation guidance for coding agents where the design needs it.

For substantial designs, the Skill can cover the TL;DR, goals and scope, architecture and end-to-end flow, module responsibilities, key data structures and interfaces, acceptance conditions, and a modular Markdown task list. It distinguishes confirmed decisions from proposals and open questions, and reports whether unresolved items block implementation.

The Skill keeps prose readable, uses requirement IDs and normative language selectively, and checks the document both for human readability and implementation readiness. It writes documentation; it does not infer permission to implement the design.

See [usage examples](examples.md) and the runtime [SKILL.md](../../../skills/development-design-doc/SKILL.md).
