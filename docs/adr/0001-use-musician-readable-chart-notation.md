---
status: accepted
---

# Use musician-readable small chart notation

Canonical song charts will use a project-owned `.chart` notation shaped like the selected prototype: directive metadata, labeled Section definitions, bar-delimited Chart Rows, typed Row Notes, and an explicit arrangement. Musician readability is the priority; the notation was chosen over strict JSON, JavaScript data, and a JSON/notation hybrid because a musician can scan and edit it without first understanding programming structures.

## Consequences

The exact grammar, escaping rules, parser, and line-aware validation diagnostics must be specified before implementation. Generated browser data remains structured; `.chart` is the human-authored source, not the runtime format.
