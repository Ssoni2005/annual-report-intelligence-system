# ARIS Project Management Reference

The canonical living project-status application is:

`apps/web/public/project-management.html`

When the web application is running, open:

`http://localhost:5173/project-management.html`

## Mandatory update rule

Every development cycle that changes ARIS must update the HTML file in the same release. At minimum, update:

1. release number and date;
2. feature status and progress;
3. current cycle and next action;
4. risks and test evidence;
5. release history.

Status values represent verified functional maturity, not screen availability.


## v7.2 — Project creation stabilization (24 Jul 2026)

- Corrected the `+ Project` modal submission path.
- Added a real form submit flow with loading and error states.
- Aligned frontend `x-user-id` with backend project membership identity.
- Added project-name validation and audit logging.
- Updated local state immediately after successful creation so the new project becomes selected without a stale reload race.


## v7.3.0 — Project, Report and Structure Menus

**Status:** Implemented; local dependency-based build verification required.

- [x] Project command menu and selector
- [x] Report entity, APIs, command menu and selector
- [x] Structure command menu and selector
- [x] Active structure and structure-version reference on report
- [x] Save As, export and delete operations
- [x] ADR and changelog
- [ ] Run npm install/npm run build in connected local environment
- [ ] Browser interaction test

## Release v7.4 — Governed Dialog Framework

**Status:** Implemented; local dependency-backed build verification required.

### Completed
- Reusable `ConfirmDialog` component.
- Custom deletion confirmation for Project, Report, Structure, Structure Element, and Source Document.
- Keyboard and accessibility behavior: Escape, focus, ARIA alert-dialog semantics.
- Busy state prevents duplicate destructive requests.
- Browser-native `alert`, `confirm`, and `prompt` usage removed from the web source.

### Verification
- Static browser-dialog scan: passed.
- ZIP integrity: pending packaging step.
- TypeScript/Vite build: requires `npm install` in the clean package; the packaging environment did not contain installed workspace dependencies.


## v7.5 — Structure Tree Interaction Studio

**Status:** Implemented; local dependency-backed build verification required.

- Exact insertion controls at root, child, and after-element positions
- Context menu for element type conversion and deletion
- Persistent element inspector
- Inline full-content reading
- Collapsible one-line paragraph previews
- Governed confirmation retained for destructive actions
