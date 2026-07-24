# Changelog

## v7.3.0 — Project, Report and Structure Menus

- Added contextual Project, Report and Structure command menus and selectors to Report Structure Studio.
- Added report persistence and APIs.
- Added one active, version-pinned structure per report.
- Added Save As through duplication for projects, reports and structures.
- Added JSON export and guarded deletion workflows.
- Added sample reports and updated project data.


## v7.4.0 — Governed Dialog Framework

- Replaced browser-native `confirm()` deletion prompts with a reusable in-application confirmation dialog.
- Added contextual delete wording for projects, reports, structures, structure elements, and source documents.
- Added destructive-action loading states to prevent duplicate requests.
- Added Escape-key handling, backdrop cancellation, initial focus, ARIA alert-dialog semantics, and keyboard-visible focus states.
- Added a governed danger-button style consistent with the institutional interface.
- Verified through static search that `alert()`, `confirm()`, and `prompt()` are no longer used in the web source.
