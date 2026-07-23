---
description: Copilot instructions for CNCF TechDocs analysis of project documentation.
applyTo: **/*.md
---

# CNCF TechDocs Analysis Copilot Instructions

The CNCF TechDocs analysis focuses on evaluating the quality and completeness of project documentation. Until now human reviewers have been performing this analysis, and still will be. The goal of this project is to provide a structure and workflow for writers to use for having Copilot to provide responses. As such, pre-defined prompts are provided to guide Copilot in providing analysis responses. Pre-defined prompts should also alleviate inconsistencies resulting from having the writer craft the prompt.

Given that the analysis writers are providing their own analysis, the Copilot analysis must be written as to require minimal editing by the writers, such as making fragments into complete sentences, or adding context to a comment.

## Analysis Criteria

The focus is to analyze documentation for CNCF projects and to provide comments, recommendations, and issues. 

Review sources:
- Analysis criteria for evaluating content: https://github.com/cncf/techdocs/blob/main/docs/analysis/criteria.md.
- Template for the analysis report: https://github.com/cncf/techdocs/blob/main/docs/analysis/templates/analysis.md

Analysis criteria is further specified in the prompt files under `.github/prompts/`.

## Analysis responses style

Responses should be concise, actionable, and focused on improving the documentation. Keep in mind the following points:

- Write complete sentences whenever possible. Avoid fragments.
- Fragments are ok if in a bullet list with an introductory sentence.
- Avoid not widely-known terms or acronyms, or provide a brief explanation of them.
- Nuances are not as important as actionable recommendations.
- If a pre-defined prompt says to write up to four paragraphs, there's no need to write more than necessary to meet the maximum.

## Pre-defined Prompts

The analysis prompts live under `.github/prompts/` and are organized into three layers so the per-area questions (data) are separated from the task logic (verbs):

- Per-area wrappers (`<area>-<type>.prompt.md`) — the entry points you invoke, for example `/information-architecture-answers`. Each wrapper simply binds one criteria area to one shared engine.
- Shared engines (`answers.prompt.md`, `comment.prompt.md`, `recommendations.prompt.md`) — the reusable procedure for each output type. They are project-agnostic: the project name and documentation label are read from the "Current Repository" section below, so the same engines work in any repository.
- Criteria definitions (`criteria/<area>.md`) — the per-area data: display name, output-file stem, question set, and comment guidance.

Areas: `information-architecture`, `new-user-content`, `content-maintainability`, `content-creation-process`, `inclusive-language`. Output types: `answers`, `comment`, `recommendations`.

By default a prompt writes to `<project-slug>-<stem>-<type>.md` in the current directory (for example, `kubevirt-infoarch-answers.md`). Provide an optional `title` input to override the filename. To add or change questions for an area, edit only its `criteria/<area>.md` file.

### Example: invoking a pre-defined prompt

To have Copilot answer the information architecture questions, invoke the per-area wrapper as a slash command in the current directory:

```text
run /information-architecture-answers
```

This runs the `information-architecture` questions through the shared `answers` engine and writes the result to the default file `kubevirt-infoarch-answers.md`.

To override the output filename, pass a `title` input:

```text
run /information-architecture-answers title: my-analysis
```

That writes the answers to `my-analysis.md` instead of the default filename. The same pattern applies to every area and output type — for example, `/inclusive-language-recommendations` or `/new-user-content-comment`.

## Current Repository

Current repository: [KubeVirt](https://github.com/kubevirt/kubevirt)

Copilot analysis website and infrastructure in addition to documentation.

As writers will be working in different repositories, Copilot should complete the rest of this section as shown below.

Copilot shall only output Markdown files in the current directory

### What This Repo Is

This is the [KubeVirt user guide](https://kubevirt.io/user-guide), a documentation-only site built with [MkDocs](https://www.mkdocs.org/) using the `mkdocs-material` theme and `mkdocs-awesome-nav` plugin. All content lives in `./docs` as Markdown files. There is no application code.

### Content Architecture

```
docs/
  .nav.yml              # Top-level navigation order
  index.md
  architecture.md
  cluster_admin/        # Installation, feature gates, RBAC, node ops
  user_workloads/       # VM lifecycle, instancetypes, virtctl, startup scripts
  compute/              # CPU/memory, live migration, hugepages, NUMA
  network/              # Interfaces, hotplug, binding plugins, Istio
  storage/              # CDI, volumes, snapshots, clone, export
  debug_virt_stack/     # Debugging guides
```

### Key Conventions

#### Navigation order via `.nav.yml`
Every subdirectory under `docs/` has a `.nav.yml` that explicitly controls page ordering. Alphabetical order is intentionally not used. When adding a new page, add it to the relevant `.nav.yml`.

#### Redirects in `mkdocs.yml`
Old page paths (e.g. `operations/`, `virtual_machines/`) are redirected to their new locations via the `redirects` plugin in `mkdocs.yml`. When moving or renaming a page, add an entry there.

#### No commits
This work is solely for documentation analysis. There are no commits to the application code in this repository.

#### Spelling dictionary
The yaspeller dictionary is sourced from `kubevirt/project-infra/images/yaspeller/.yaspeller.json`. If a technical term causes false positives, it needs to be added there (upstream), not locally — unless a local `yaspeller.json` override is present.

#### MkDocs extensions in use
Pages can use: `admonition`, `footnotes`, `toc` with `permalink`, `pymdownx.highlight`, `pymdownx.superfences`, `attr_list`, and `pymdownx.emoji`. These are already configured in `mkdocs.yml` — no additional setup needed.


