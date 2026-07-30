---
mode: agent
description: Shared engine for running all three analyses (answers, comment, recommendations) for one area. Normally run via a per-area wrapper such as /information-architecture-full.
---

# Shared engine: full

Reusable procedure for running the complete analysis of one criteria area: it runs the **answers**, **comment**, and **recommendations** engines in sequence. Normally invoked through a per-area wrapper prompt (for example, `/information-architecture-full`), which selects the criteria area for you.

## Inputs

- Area — the criteria area to analyze. When run from a wrapper, the wrapper names it. If you reached this engine without an area, ask the user to choose one of: `information-architecture`, `new-user-content`, `content-maintainability`, `content-creation-process`, `inclusive-language`.
- Title (optional) — a base name that overrides the default output filenames. When provided, the outputs are `<title>-answers.md`, `<title>-comment.md`, and `<title>-recommendations.md`.

## Procedure

Run the three shared engines in this exact order. The order matters: the recommendations engine reads the answers and comment files produced by the first two steps.

1. Read the criteria definition at `.github/prompts/criteria/<area>.md` once, so its Display name, File stem, Questions, and Comment guidance are available to every step below.
2. Answers: read and follow `.github/prompts/answers.prompt.md`, treating `<area>` as the selected area. Write its output file before continuing.
3. Comment: read and follow `.github/prompts/comment.prompt.md`, treating `<area>` as the selected area. Write its output file before continuing.
4. Recommendations: read and follow `.github/prompts/recommendations.prompt.md`, treating `<area>` as the selected area. It consumes the answers and comment files written in the previous two steps, so do not run it before they exist.

When a Title is provided, pass it through to each engine so the three files share the `<title>` base name described under "Inputs".

## Output

- Produce all three Markdown files in the current directory:
  - Answers: `<title>-answers.md`, or `<project-slug>-<stem>-answers.md` by default.
  - Comment: `<title>-comment.md`, or `<project-slug>-<stem>-comment.md` by default.
  - Recommendations: `<title>-recommendations.md`, or `<project-slug>-<stem>-recommendations.md` by default.
- After writing them, list the three filenames you created.
