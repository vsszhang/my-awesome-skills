# Development Design Document

`$development-design-doc` creates or updates software design documents from a discussion in the current conversation, a referenced conversation, or a direct topic description. The documents are written for people first, with precise implementation guidance for coding agents where the design needs it.

The default output is one Markdown document in the active project's root directory. If an output directory is supplied, the document is saved there. The writing language follows the language of the message that invoked the Skill, unless the user specifies another language.

For substantial designs, the Skill can cover the TL;DR, goals and scope, architecture and end-to-end flow, module responsibilities, key data structures and interfaces, acceptance conditions, and a modular Markdown task list. It distinguishes confirmed decisions from proposals and open questions, and reports whether unresolved items block implementation.

The Skill keeps prose readable, uses requirement IDs and normative language selectively, and checks the document both for human readability and implementation readiness. It writes documentation; it does not infer permission to implement the design.

See [usage examples](examples.md) and the runtime [SKILL.md](../../../skills/development-design-doc/SKILL.md).
