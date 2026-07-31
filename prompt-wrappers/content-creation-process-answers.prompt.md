---
mode: agent
description: Answer the CNCF TechDocs content creation process questions for the documentation.
---

Run the shared **answers** analysis for the `content-creation-process` criteria area.

1. Read the criteria definition in `.github/prompts/criteria/content-creation-process.md`.
2. Read and follow the shared procedure in `.github/prompts/answers.prompt.md`, treating `content-creation-process` as the selected area.

Optional output filename override: `${input:title}` — if non-empty, use it as the output filename; otherwise use the engine's default (`<project-slug>-<stem>-answers.md`).
