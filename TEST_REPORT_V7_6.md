# ARIS v7.6 Test Report

## Scope
Document hierarchy and derived numbering correction.

## Expected behaviours
- Title has no displayed number.
- Chapter has no displayed number.
- First Heading 1 under a Title or Chapter displays `1`.
- Second Heading 1 in the same container displays `2`.
- Heading 2 under Heading 1 displays `1.1`.
- Heading 3 under Heading 2 displays `1.1.1`.
- Numbering is derived and is not persisted.
- Moving headings recalculates numbering immediately.

## Packaging verification
ZIP integrity is checked during packaging. Full npm build and browser interaction tests should be run locally.
