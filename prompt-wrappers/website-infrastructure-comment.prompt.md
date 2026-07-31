---
mode: agent
description: Write an overall comment on the Website and Infrastructure analysis section by synthesizing its per-area comment files.
---

Run the shared **section-comment** analysis for the `website-infrastructure` section.

1. Read the section definition in `.github/prompts/sections/website-infrastructure.md`.
2. Read and follow the shared procedure in `.github/prompts/section-comment.prompt.md`, treating `website-infrastructure` as the selected section.

Optional output filename override: `${input:title}` — if non-empty, use it as the output filename; otherwise use the engine's default (`<project-slug>-<section-slug>-comment.md`).
