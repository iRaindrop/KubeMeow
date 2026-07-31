---
mode: agent
description: Provide recommendations for improving the new contributor getting started content of the documentation.
---

Run the shared **recommendations** analysis for the `new-contributor-content` criteria area.

1. Read the criteria definition in `.github/prompts/criteria/new-contributor-content.md`.
2. Read and follow the shared procedure in `.github/prompts/recommendations.prompt.md`, treating `new-contributor-content` as the selected area.

Optional output filename override: `${input:title}` — if non-empty, use it as the output filename; otherwise use the engine's default (`<project-slug>-<stem>-recommendations.md`).
