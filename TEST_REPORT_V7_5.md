# ARIS v7.5 Test Report

## Scope
Structure tree insertion, context actions, inline content, and persistent inspector.

## Static checks completed
- No browser-native confirmation introduced.
- Exact insertion uses the existing move endpoint after creation.
- Right-click deletion passes the selected element ID into the governed dialog.
- Type changes use the validated element PATCH endpoint.
- Paragraph expansion is local UI state and does not mutate report content.

## Local verification required
Run `npm install`, `npm run build`, `npm run test`, and `npm run dev` on the target workstation. The packaging container did not have the repository dependencies installed.
