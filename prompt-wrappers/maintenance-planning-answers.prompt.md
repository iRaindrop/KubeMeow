---
mode: agent
description: Answer the CNCF TechDocs maintenance planning questions for the documentation.
---

Run the shared **answers** analysis for the `maintenance-planning` criteria area.

1. Read the criteria definition in `.github/prompts/criteria/maintenance-planning.md`.
2. Read and follow the shared procedure in `.github/prompts/answers.prompt.md`, treating `maintenance-planning` as the selected area.

Optional output filename override: `${input:title}` — if non-empty, use it as the output filename; otherwise use the engine's default (`<project-slug>-<stem>-answers.md`).
