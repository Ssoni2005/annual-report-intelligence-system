# Functional Report Structure Module

## What was implemented
- Multi-project workspace with project membership metadata.
- Multiple reusable structures per project.
- Typed structure elements: title, chapter, heading levels 1–5, paragraph, bullet list, numbered list, table, text box and image.
- Direct creation and editing in the interface.
- Drag-and-drop reorder and re-parent operations with server-side hierarchy validation.
- Position-derived numbering; numbers are never stored as element identity.
- Read-only parent, child count, element ID and calculated number in the property inspector.
- Import by pasted text, file picker or drag-and-drop.
- Import preview and append/replace modes.
- Server-side extraction adapters for DOCX, PDF, XLSX, PPTX, TXT, Markdown, HTML, CSV and RTF.
- Structure duplication and persistent version snapshots through API endpoints.

## Design reason
Element identity is a stable UUID-like ID, while display numbering is calculated by traversing the current tree. Moving a heading therefore changes its displayed number without breaking references.

## Current boundary
Units and project documents are intentionally represented only as future associations. Their detailed workflows are not implemented in this release.
