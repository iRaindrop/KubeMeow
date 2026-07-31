---
mode: agent
description: Shared engine for producing an analysis comment. Normally run via a per-area wrapper such as /information-architecture-comment.
---

# Shared engine: comment

Reusable procedure for writing an analysis comment for one area. Normally invoked through a per-area wrapper prompt (for example, `/information-architecture-comment`), which selects the criteria area for you.

## Inputs

- Area — the criteria area to analyze. When run from a wrapper, the wrapper names it. If you reached this engine without an area, ask the user to choose one of: `information-architecture`, `new-user-content`, `content-maintainability`, `content-creation-process`, `inclusive-language`.
- Title (optional) — overrides the default output filename.

## Procedure

1. Read the criteria definition at `.github/prompts/criteria/<area>.md`. Use its Display name, File stem, and Comment guidance (good examples and any additional instructions).
2. Determine the project name and documentation label from the "Current Repository" section of the repository Copilot instructions (for example, "the KubeVirt user guide"). Derive the project slug by lowercasing the name and replacing spaces with hyphens.
3. Write a two to four paragraph comment on the area's subject (its Display name) in the documentation. Keep it concise, actionable, and focused on improving the documentation. Apply any "Additional instructions" from the criteria file. You may reference the listed "good examples" as models of quality.
4. Add a rating for this area, using the CNCF 1–5 scale:
   - 1 - Not present
   - 2 - Needs improvement
   - 3 - Meets standards
   - 4 - Meets or exceeds standards
   - 5 - Exemplary

   State the rating on its own line at the end of the comment in the form
   `Rating: <number> - <label>` (for example, `Rating: 3 - Meets standards`).
   Do not include any other text on the rating line.

## Output

- Write the result to a Markdown file in the current directory:
  - If a title was provided, name the file `<title>.md`.
  - Otherwise name it `<project-slug>-<stem>-comment.md`.
