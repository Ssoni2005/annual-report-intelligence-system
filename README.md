# Annual Report Intelligence & Synthesis System — Phase 4

This monorepo contains a React/TypeScript web application, Node/Express orchestration API and Python/FastAPI intelligence service.

## Implemented through Phase 4

1. Foundation and report hierarchy governance
2. Unit submission and document intake
3. Parsing and normalisation
4. Intelligent hierarchy-aware chunking

Phase 4 supports configurable chunking profiles, inherited heading paths, event/topic/metric classification, list/table preservation, chunk jobs, human review, split, merge, approval and immutable version lineage.

## Run

```bash
npm install
python3 -m pip install -r services/ai/requirements.txt
npm run dev
```

Web: http://localhost:5173  
Node API: http://localhost:4000  
AI service: http://localhost:8001

## Test

```bash
npm run test
```

## v7 Functional Report Structure release

The `/structure` workspace now uses the persistent project/structure/element API in `apps/api/src/structureRoutes.ts` and `data/structures.json`. It supports five-level hierarchy editing, position-derived numbering, drag-and-drop movement, typed content elements, pasted-text import, and file import through the Python extraction service. See `REPORT_STRUCTURE_FUNCTIONAL_SPEC.md`.

Run the three services with `npm run dev`. The web app uses port 5173, Node API port 4000, and Python parsing service port 8001.

## Living project management reference

A self-contained project status application is available at:

```text
apps/web/public/project-management.html
```

When the web server is running, open:

```text
http://localhost:5173/project-management.html
```

This file is the canonical reference for phases, features, tools, implementation status, risks, release history, current cycle and definition of done. It must be updated with every development release. See `PROJECT_MANAGEMENT.md`.
