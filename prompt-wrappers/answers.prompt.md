---
mode: agent
description: Shared engine for producing analysis answers. Normally run via a per-area wrapper such as /information-architecture-answers.
---

# Shared engine: answers

This is the reusable procedure for answering an analysis area's questions. It is normally invoked through a per-area wrapper prompt (for example, `/information-architecture-answers`), which selects the criteria area for you.

## Inputs

- Area — the criteria area to analyze. When run from a wrapper, the wrapper names it. If you reached this engine without an area, ask the user to choose one of: `information-architecture`, `new-user-content`, `content-maintainability`, `content-creation-process`, `inclusive-language`.
- Title (optional) — overrides the default output filename.

## Procedure

1. Read the criteria definition at `.github/prompts/criteria/<area>.md`. It defines the area's Display name, File stem, and Questions.
2. Determine the project name from the "Current Repository" section of the repository Copilot instructions. Derive a project slug by lowercasing the name and replacing spaces with hyphens (for example, "KubeVirt" becomes `kubevirt`).
3. Answer every question in the criteria file's "Questions" section, using the sources described in the "Current Repository" section as context.

## Output

- Present the answers as indented paragraphs under each question. If an answer is "yes" or "no", provide a brief explanation. Do not bold the answers.
- Write the result to a Markdown file in the current directory:
  - If a title was provided, name the file `<title>.md`.
  - Otherwise name it `<project-slug>-<stem>-answers.md`.
