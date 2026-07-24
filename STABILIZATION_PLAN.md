# Stabilisation Gate Before Phase 5

The next development cycle should be treated as Phase 4S rather than adding Heading Affinity Mapping.

## Gate 1 — Reproducible build
- Clean `npm ci`
- Web and API TypeScript build
- Python dependency install
- All tests pass in CI

## Gate 2 — Real ingestion
- Multipart upload
- File allow-list, size limit and checksum
- Durable storage and database record
- Download/open-source action

## Gate 3 — Real orchestration
- Node calls Python `/parse`
- Normalized output persisted
- Node calls Python `/chunk`
- Generated chunks persisted
- Failed jobs carry genuine errors and retry safely

## Gate 4 — Governance
- Real login/session
- Backend RBAC
- Confidentiality enforcement
- Immutable audit-event model

## Gate 5 — E2E acceptance
A fixture DOCX and PDF must complete:

`upload → validate → parse → normalize → correct → approve → chunk → split/merge → approve → reload`

No later feature phase should be called complete until this gate passes.
