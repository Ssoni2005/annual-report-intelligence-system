# ARIS v7.9 — Drag Placement Hints

Implemented visual drag-and-drop guidance in the Structure Tree.

## Behaviour
- Before placement: a prominent insertion line appears above the target.
- After placement: a prominent insertion line appears below the target.
- Inside placement: valid heading/document objects receive a highlighted container and “Release to add as last child” message.
- Root placement: the root drop zone expands and displays an explicit release instruction.
- Content elements do not expose an “inside” drop target because hierarchy belongs to headings/document objects.
- Drag hints clear on drop and drag end.
- Successful movement reports that the element was moved to the highlighted position.
