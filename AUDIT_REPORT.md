# ARIS Implementation Audit and Stabilisation Report

## Executive conclusion

The Phase 4 package is a **UI-rich functional prototype**, not a production-complete annual-report platform. The Python parsing/chunking unit tests pass, and the JSON-backed API contains working CRUD-style prototype flows. However, several important operations are simulations or metadata-only implementations.

## Verification performed

- ZIP and repository integrity: passed.
- Python test suite: **7/7 passed**.
- JSON data stores: readable and structurally valid.
- Source-level route and page inventory: completed.
- Placeholder/demo scan: completed.
- Node dependency installation: attempted twice; timed out in the execution environment.
- React/TypeScript build: attempted; could not proceed because npm dependencies were incomplete after the timeout.
- Browser E2E testing: not possible without a complete Node installation.

## Feature classification

| Area | Status | Finding |
|---|---|---|
| Application shell/navigation | Prototype-functional | React routes and pages exist; browser build remains unverified here. |
| Reporting cycles | Prototype-functional | JSON CRUD; limited validation; no database or concurrency control. |
| Structure designer | Prototype-functional | Add/edit/delete/reorder/publish/version operations exist. |
| Units/users/roles | Partial | CRUD display exists; backend authorization is not enforced. |
| Authentication | Scaffold only | Seeded session; no password verification, token, logout or secure session. |
| Unit submissions | Prototype-functional | Invitation, comments and status updates persist to JSON. |
| File upload | Mocked/metadata-only | Browser records filename and size but sends no file bytes. |
| Document validation | Partial | Checks selected metadata fields only. |
| Parsing queue | Demo orchestration | Status changes are manual; jobs do not invoke a real worker from the Node API. |
| Normalized document viewer | Prototype-functional on seed data | Editing and approval persist; newly uploaded files do not automatically produce normalized documents. |
| DOCX/PPTX/TXT parsing service | Partial real implementation | Python parser logic and tests exist; production fidelity is limited. |
| PDF/XLSX parsing | Not production implemented | No complete extraction adapter demonstrated. |
| Chunking service | Partial real implementation | Python hierarchy-aware logic has passing tests. |
| Chunking UI | Prototype-functional on seed data | Review, edit, split and merge operate on JSON records. |
| Chunking job execution | Demo orchestration | `run` advances progress but does not execute Python and persist generated chunks. |
| Mapping/evidence/drafting/report | Mostly scaffold/sample | Pages exist, but complete evidence-to-final-report workflow is not implemented. |
| Audit log | Partial | Append-only by convention, but stored in editable JSON and not tamper-resistant. |
| Persistence | Prototype only | Atomic JSON writes added in stabilisation; unsuitable for multi-user production. |
| Security | Not production ready | No real auth, backend RBAC, malware scanning, secure file storage or rate limiting. |
| Automated tests | Low coverage | Seven Python tests; frontend and API tests are smoke-level only. |

## Important defects found

### Critical

1. File upload did not transfer file content; only metadata was recorded.
2. Authentication accepted any non-empty email/password and returned a seeded session.
3. Role permissions were represented in data/UI but not enforced at API endpoints.
4. Parsing and chunking queue actions simulated progress instead of running the AI service.

### High

1. Data storage used process-working-directory-relative paths and could fail when launched differently.
2. JSON writes were non-atomic and vulnerable to corruption during interruption.
3. No production PDF or XLSX extraction path was demonstrated.
4. No end-to-end test proved upload → parse → normalize → chunk → approve.
5. Dependencies used `latest`, making builds non-reproducible.

### Medium

1. Frontend API URL was hard-coded.
2. HTML shell was minimal and omitted standard metadata.
3. API health response overstated readiness by not exposing capability limitations.
4. Some controls and filters are visual only or incomplete.
5. Tests do not validate meaningful frontend behavior.

## Stabilisation applied in v6

- Pinned Node dependency versions rather than using `latest`.
- Added Node/npm engine requirements.
- Added a Vite React configuration.
- Added a standards-compliant HTML entry page.
- Made the frontend API URL configurable through `VITE_API_URL`.
- Made the API data directory stable using `import.meta.url` and optional `ARIS_DATA_DIR`.
- Changed JSON persistence to temporary-file plus atomic rename.
- Prevented documents with incomplete validation from entering parsing.
- Disabled misleading password login with an explicit `501` response until real authentication is implemented.
- Added an accurate API capability disclosure in `/api/health`.
- Added centralized internal-error handling.
- Added a static audit script.
- Added this feature-by-feature audit and a remediation plan.

## Remaining work before new feature development

1. Implement real multipart file upload and durable file storage.
2. Connect Node parsing jobs to the Python service and persist returned normalized blocks.
3. Connect chunking jobs to Python and persist generated chunks and lineage.
4. Implement PDF and XLSX adapters with fixtures and fidelity tests.
5. Replace JSON with PostgreSQL or SQLite migrations and transactional repositories.
6. Implement authentication, backend RBAC and confidential-document access rules.
7. Add API integration tests and Playwright E2E tests.
8. Run and pass a reproducible clean install, build and test in CI.

## Readiness rating

- Demonstration prototype: **65%**
- Internally usable single-user pilot: **35%**
- Production-ready multi-user system: **15%**

These percentages indicate engineering readiness, not the number of screens present.
