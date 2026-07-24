# ARIS v7.8 Test Report — Caption Elements

## Scope

Added Table Caption, Image Caption, and Text Box Caption structure elements.

## Governed rules verified by static inspection

- Each caption type is restricted to its matching parent element.
- A caption is inserted immediately after the parent at the same tree level.
- Only one caption may be attached to a parent element.
- Captions cannot be independently dragged away from their parent.
- Moving a parent moves its attached caption with it.
- Deleting a parent also deletes its attached caption.
- Frontend and API both validate caption placement and uniqueness.
- TypeScript syntax transpilation completed without diagnostics.

## Local verification still required

Run `npm install`, `npm run build`, `npm run test`, and `npm run dev` in the local repository.
