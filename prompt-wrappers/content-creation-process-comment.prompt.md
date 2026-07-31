---
mode: agent
description: Write a comment on the content creation process of the documentation.
---

Run the shared **comment** analysis for the `content-creation-process` criteria area.

1. Read the criteria definition in `.github/prompts/criteria/content-creation-process.md`.
2. Read and follow the shared procedure in `.github/prompts/comment.prompt.md`, treating `content-creation-process` as the selected area.

Optional output filename override: `${input:title}` — if non-empty, use it as the output filename; otherwise use the engine's default (`<project-slug>-<stem>-comment.md`).
