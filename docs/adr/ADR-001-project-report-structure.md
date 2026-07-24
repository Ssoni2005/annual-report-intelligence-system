# ADR-001: Project–Report–Structure Architecture

**Status:** Accepted  
**Release:** v7.3.0

A project may contain multiple reports. A report references one active structure at a time. The report stores both the structure ID and the applied structure version so later structure revisions do not silently change the report. Structures are independently managed, reusable, duplicable and versioned.

## Consequences

- Project commands operate on the complete project container.
- Report commands operate on report metadata and its active structure reference.
- Structure commands operate on reusable structure definitions and their versions.
- Applying a structure is an explicit action.
