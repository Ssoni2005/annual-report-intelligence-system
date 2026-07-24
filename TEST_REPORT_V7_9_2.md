# ARIS v7.9.2 Test Report

## Scope
Verification of the last three structure-tree changes and the corrected Word-style hierarchy model.

## Static verification completed

- `Structure.tsx` transpiles without TypeScript syntax diagnostics.
- `structureRoutes.ts` transpiles without TypeScript syntax diagnostics.
- `Inspector` is defined and rendered by the persistent right panel.
- `ElementContextMenu` is defined, rendered through `createPortal`, and uses z-index 10000.
- Table, Image, and Text Box caption types remain present in frontend and API rules.
- Matching captions remain limited to one and normalized immediately after their parent element.
- Drag feedback includes before, after, inside, root, and invalid states.

## Governed hierarchy scenarios

| Scenario | Expected |
|---|---|
| Paragraph under H1 | Allowed |
| Table under H3 | Allowed |
| Image under Chapter | Allowed |
| Bullet list at root | Allowed |
| H2 under H1 | Allowed |
| H3 under H2 | Allowed |
| H3 directly under H1 | Rejected |
| H4 directly under H2 | Rejected |
| H2 under paragraph | Rejected |
| Paragraph under paragraph | Rejected |
| Second caption for same table/image/text box | Rejected |
| Independent caption drag | Rejected |

## Local runtime verification required

Run `npm install`, `npm run build`, `npm run test`, and `npm run dev` because dependency packages are not available in the packaging environment.
