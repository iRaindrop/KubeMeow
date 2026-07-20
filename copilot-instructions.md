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

Analysis criteria is further specified in the pre-defined prompts below.

## Analysis responses style

Responses should be concise, actionable, and focused on improving the documentation. Keep in mind the following points:

- Write complete sentences whenever possible. Avoid fragments.
- Fragments are ok if in a bullet list with an introductory sentence.

## Pre-defined Prompts

### Pre‑defined Prompt: "information-architecture-answers"

If provided a title parameter, output shall be in a Markdown file in the current directory.

Context:  The sources described in the Current Repository section.

Task: Provide concise answers to the following questions about the information architecture of the documentation. Output the answers as indented paragraphs under each question. If the answer is "yes" or "no", provide a brief explanation. Do not bold the answers.

- Is there high level conceptual/“About” content? Is the documentation feature
  complete? (i.e., each product feature is documented)
- Are there step-by-step instructions (tasks, tutorials) documented for
  features?
- Are there any key features which are documented but missing task
  documentation?
- Is the “happy path”/most common use case documented? Does task and tutorial
  content demonstrate atomicity and isolation of concerns? (Are tasks clearly
  named according to user goals?)
- If the documentation does not suffice, is there a clear escalation path for
  users needing more help? (FAQ, Troubleshooting)
- If the product exposes an API, is there a complete reference?
- Is content up to date and accurate?

### Pre‑defined Prompt: "information-architecture-comment"

If provided a title parameter, output shall be in a Markdown file in the current directory.

Context: The sources described in the Current Repository section.

Task: Create a two to four paragraph comment on the information architecture of the documentation. The comment should be concise, actionable, and focused on improving the documentation. Include a True/False evaluation whether or not a restructure of the content is needed.

Good example of Information Architecture: https://prometheus.io/docs

### Pre-defined Prompt: "information-architecture-recommendations"

If provided a title parameter, output shall be in a Markdown file in the current directory.

Context:  The sources described in the Current Repository section.

Task: Provide concise recommendations for improving the information architecture of the documentation based on answers provided in `kubevirt-infoarch-answers.md` and comments provided in `kubevirt-infoarch-comment.md` Output the recommendations in a bulleted list. Use this intro: "The following recommendations address the information architecture of the KubeVirt user guide."

### Pre‑defined Prompt: "new-user-content-answers"

If provided a title parameter, output shall be in a Markdown file in the current directory.

Context:  The sources described in the Current Repository section.

Task: Provide concise answers to the following questions about the new user content of the documentation. Output the answers as indented paragraphs under each question. If the answer is "yes" or "no", provide a brief explanation. Do not bold the answers.

- Is “getting started” clearly labeled? (“Getting started”, “Installation”,
  “First steps”, etc.)
- Is installation documented step-by-step?
- If needed, are multiple OSes documented?
- Do users know where to go after reading the getting started guide?
- Is your new user content clearly signposted on your site’s homepage or at the
  top of your information architecture?
- Is there sample code or other example content that can easily be copy-pasted?

### Pre‑defined Prompt: "new-user-content-comment"

If provided a title parameter, output shall be in a Markdown file in the current directory.

Context:  The sources described in the Current Repository section.

Task: Create a two to four paragraph comment on the new user content of the documentation. The comment should be concise, actionable, and focused on improving the documentation.

Good example of new user content: https://falco.org/docs/getting-started/

### Pre-defined Prompt: "new-user-content-recommendations"

If provided a title parameter, output shall be in a Markdown file in the current directory.

Context:  The sources described in the Current Repository section.

Task: Provide concise recommendations for improving the new user content of the documentation based on answers provided in `kubevirt-new-user-answers.md` and comments provided in `kubevirt-new-user-comment.md`. Output the recommendations in a bulleted list. Use this intro: "The following recommendations address the new user content of the KubeVirt user guide."

### Pre‑defined Prompt: "content-maintainability-answers"

If provided a title parameter, output shall be in a Markdown file in the current directory.

Context:  The sources described in the Current Repository section.

Task: Provide concise answers to the following questions about the content maintainability of the documentation. Output the answers as indented paragraphs under each question. If the answer is "yes" or "no", provide a brief explanation. Do not bold the answers.

- Is the documentation searchable?
- Are there plans for localization/internationalization with regards to site
  directory structure? Is a localization framework present?
- Is there a clearly documented method for versioning of content?

### Pre‑defined Prompt: "content-maintainability-comment"

If provided a title parameter, output shall be in a Markdown file in the current directory.

Context:  The sources described in the Current Repository section.

Task: Create a two to four paragraph comment on the content maintainability content of the documentation. The comment should be concise, actionable, and focused on improving the documentation.

Good example of content maintainability: - https://kubernetes.io/docs/

### Pre-defined Prompt: "content-maintainability-recommendations"

If provided a title parameter, output shall be in a Markdown file in the current directory.

Context:  The sources described in the Current Repository section.

Task: Provide concise recommendations for improving the content maintainability of the documentation based on answers provided in `kubevirt-content-maintainability-answers.md` and comments provided in `kubevirt-content-maintainability-comment.md`. Output the recommendations in a bulleted list. Use this intro: "The following recommendations address the content maintainability of the KubeVirt user guide."

### Pre‑defined Prompt: "content-creation-process-answers"

If provided a title parameter, output shall be in a Markdown file in the current directory.

Context:  The sources described in the Current Repository section.

Task: Provide concise answers to the following questions about the content creation process of the documentation. Output the answers as indented paragraphs under each question. If the answer is "yes" or "no", provide a brief explanation. Do not bold the answers.

- Is there a clearly documented (ongoing) contribution process for
  documentation?
- Does the code release process account for documentation creation & updates?
- Who reviews and approves documentation pull requests?
- Does the website have a clear owner/maintainer?

### Pre‑defined Prompt: "content-creation-process-comment"

If provided a title parameter, output shall be in a Markdown file in the current directory.

Context:  The sources described in the Current Repository section.

Task: Create a two to four paragraph comment on the content creation process of the documentation. The comment should be concise, actionable, and focused on improving the documentation.

Good examples of content creation process:
- https://github.com/nats-io/nats-site/blob/master/MAINTAINERS.md
- https://thanos.io/tip/contributing/how-to-contribute-to-docs.md

### Pre‑defined Prompt: "content-creation-process-recommendations"

If provided a title parameter, output shall be in a Markdown file in the current directory.

Context:  The sources described in the Current Repository section.

Task: Provide concise recommendations for improving the content creation process of the documentation based on answers provided in `kubevirt-content-creation-process-answers.md` and comments provided in `kubevirt-content-creation-process-comment.md`. Output the recommendations in a bulleted list. Use this intro: "The following recommendations address the content creation process of the KubeVirt user guide."

### Pre‑defined Prompt: "inclusive-language-answers"

If provided a title parameter, output shall be in a Markdown file in the current directory.

Context:  The sources described in the Current Repository section.

Task: Provide concise answers to the following questions about inclusive language in the documentation. Output the answers as indented paragraphs under each question. If the answer is "yes" or "no", provide a brief explanation. Do not bold the answers.

- Are there any customer-facing utilities, endpoints, class names, or feature
  names that use non-recommended words as documented by the
  [Inclusive Naming Initiative](https://inclusivenaming.org) website?
- Does the project use language like "simple", "easy", etc.?

### Pre‑defined Prompt: "inclusive-language-comment"

If provided a title parameter, output shall be in a Markdown file in the current directory.

Context:  The sources described in the Current Repository section.

Task: Create a two to four paragraph comment on any inclusive language concerns in the documentation. The comment should be concise, actionable, and focused on improving the documentation.

### Pre‑defined Prompt: "inclusive-language-recommendations"

If provided a title parameter, output shall be in a Markdown file in the current directory.

Context:  The sources described in the Current Repository section.

Task: Provide concise recommendations for improving the inclusive language in the documentation based on answers provided in `kubevirt-inclusive-language-answers.md` and comments provided in `kubevirt-inclusive-language-comment.md`. Output the recommendations in a bulleted list. Use this intro: "The following recommendations address the inclusive language of the KubeVirt user guide."

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

#### Commit signing required
All commits must be signed off:
```bash
git commit -s -m "Your message"
```
To sign all commits back to `main`:
```bash
git rebase --exec 'git commit --amend --no-edit -n -s' -i main
```

#### Spelling dictionary
The yaspeller dictionary is sourced from `kubevirt/project-infra/images/yaspeller/.yaspeller.json`. If a technical term causes false positives, it needs to be added there (upstream), not locally — unless a local `yaspeller.json` override is present.

#### MkDocs extensions in use
Pages can use: `admonition`, `footnotes`, `toc` with `permalink`, `pymdownx.highlight`, `pymdownx.superfences`, `attr_list`, and `pymdownx.emoji`. These are already configured in `mkdocs.yml` — no additional setup needed.


