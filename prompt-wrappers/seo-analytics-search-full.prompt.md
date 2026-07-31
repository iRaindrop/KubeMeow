---
mode: agent
description: Run the full `seo-analytics-search` analysis (answers, comment, and recommendations) for the documentation.
---

Run the shared **full** analysis for the `seo-analytics-search` criteria area.

1. Read the criteria definition in `.github/prompts/criteria/seo-analytics-search.md`.
2. Read and follow the shared procedure in `.github/prompts/full.prompt.md`, treating `seo-analytics-search` as the selected area.

Optional output filename override: `${input:title}` — if non-empty, use it as the base name for all three output files (`<title>-answers.md`, `<title>-comment.md`, `<title>-recommendations.md`); otherwise use each engine's default (`<project-slug>-<stem>-<type>.md`).
