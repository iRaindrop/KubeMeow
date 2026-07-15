# How-To: Building an LLM Wiki (AI Section — Doc Plan / Outline)

> **Status:** Outline / documentation plan. This is the skeleton for the "AI" section of
> the analyst how-to. Each `§` below lists the heading, what the finished prose should
> cover, and any ready-to-use assets (tables, prompt templates) an analyst can copy today.
> Fill the `TODO:` placeholders with screenshots and org-specific values before publishing.
>
> **Audience:** Analysts doing analysis on CNCF project documentation.
> **Goal:** Stand up and maintain an LLM-curated wiki (the "KubeMeow" pattern) that turns
> raw upstream docs into cross-linked, cited, synthesized knowledge pages.
> **Reference implementation:** this repository (KubeMeow).

---

## §0. Overview & Mental Model
*What to write:*
- One-paragraph definition of an "LLM wiki": an Obsidian vault where **raw source material**
  is ingested and **synthesized by an LLM** into curated, cross-linked markdown pages.
- The core principle: **raw is immutable, wiki is derived.** Every claim in a wiki page
  traces back to a `raw/` path.
- The three moving parts the analyst drives: **(1)** the AI agent (Copilot CLI),
  **(2)** the vault (Obsidian), **(3)** the source corpus (`raw/`).
- Diagram: `raw/ → [LLM ingest] → wiki/*.md → index.md + log.md`.  *TODO: add diagram.*
- When to use this vs. plain note-taking (scale: many docs, need for cross-linking,
  need for citations and auditability).

## §1. Prerequisites & One-Time Setup
*What to write:*
- Tools to install: Obsidian, Git, GitHub CLI (`gh`), and the LLM agent (**GitHub Copilot CLI**).
- Clone/create the vault; point Obsidian at the folder.
- Repository skeleton to create up front (mirror this repo):

  | Path | Purpose | Editable by AI? |
  |---|---|---|
  | `raw/topics/<topic>/` | Immutable verbatim source checkouts | **Never** |
  | `raw/{articles,data,images,papers,repos}/` | Placeholders for other source types | Never |
  | `wiki/` | Synthesized concept/entity pages (the deliverable) | Yes |
  | `wiki/sources/` | One source-summary page per ingested source | Yes |
  | `wiki/{comparisons,concepts,entities}/` | Category placeholders | Yes |
  | `wiki/index.md` | Master catalog + coverage map | **Every op** |
  | `wiki/log.md` | Append-only operation history (newest on top) | **Every op** |
  | `outputs/` | Generated reports (e.g. `lint-YYYY-MM-DD.md`) | Yes |
  | `.obsidian/`, `*.base`, `*.canvas` | Obsidian app artifacts | Leave to Obsidian |

- The single most important setup step: author `.github/copilot-instructions.md`
  (the agent's constitution — see §3).

## §2. Choosing the Model Level & Settings
*What to write — the "Model level and settings" requirement:*

### 2a. Picking a model tier
- Explain that heavier reasoning models produce better **synthesis** (the hard part of a
  wiki: condensing many docs into coherent, non-duplicative prose) but cost more/run slower.
- Recommendation table (map task → tier):

  | Wiki task | Model tier | Why |
  |---|---|---|
  | Ingest + synthesize a large corpus | **High-reasoning** (e.g. Opus / GPT-5-class) | Cross-doc synthesis, contradiction detection, dedup |
  | Create/rewrite a concept page | High-reasoning | Quality of prose + citation accuracy matters most |
  | Query / Q&A over existing wiki | **Mid tier** | Retrieval + short synthesis; cheaper |
  | Lint / mechanical index & log updates | **Fast/low tier** | Deterministic, low-creativity edits |

- Note that Copilot CLI lets you switch models mid-session; use `/model` (TODO: confirm exact
  command/label in your CLI version) and pick effort/verbosity where offered.

### 2b. Settings that matter
- **Custom instructions** (`.github/copilot-instructions.md`) — the highest-leverage setting;
  covered in §3.
- **Permissions** (`.claude/settings.local.json` or CLI equivalent): allow-list read paths,
  `gh api`, and package installs; keep write scope tight. Show the real example from this repo.
- **Temperature / determinism:** prefer low creativity for index/log/lint ops; allow more for
  prose synthesis. *TODO: note where this is exposed in your CLI.*
- **Context window / long-context tier:** when a corpus is large, use a long-context mode or
  delegate sub-sections to sub-agents rather than stuffing everything into one prompt.
- **Session artifacts vs. committed files:** planning notes live in the agent's session state,
  not the vault. Only `wiki/`, `index.md`, `log.md`, `outputs/` get committed.

## §3. The Agent Constitution (`copilot-instructions.md`)
*What to write:*
- Explain that a repo-level instructions file is what makes results **repeatable across
  analysts and sessions.** Without it, every analyst gets different structure.
- Checklist of what the instructions file must pin down (all present in this repo's copy):
  - Repo layout and the **immutability rule** for `raw/`.
  - The three workflows: **Ingest / Query / Lint** (see §5–§7).
  - Page conventions: frontmatter schema, kebab-case filenames, `[[wikilinks]]` only,
    "synthesize don't copy," date format.
  - "Things to watch": cross-topic bleed, keeping `index.md`/`log.md` in sync.
- Best practice: treat the instructions file as versioned policy — review it when conventions
  change; it is the contract the agent follows.

## §4. Bringing in Source Material: Repositories vs. Files
*What to write — the "repositories or files (pros and cons of each)" requirement.*

### 4a. How ingestion sources land in `raw/`
- Everything goes under `raw/topics/<topic>/` as a **verbatim** checkout/copy. Never hand-edit.
- Record provenance (upstream URL + branch/commit) in the source-summary page and `log.md`.

### 4b. Option A — Bring in a whole repository
- *How:* `git clone`/checkout the upstream docs repo (or a branch) into `raw/topics/<topic>/`.
  (This repo's Flatcar topic is a checkout of `flatcar/flatcar-website`, `expert-support-refactor` branch.)

| Pros | Cons |
|---|---|
| Complete coverage — nothing missed | Pulls in non-content noise (Hugo templates, CI, `Makefile`, repo meta) |
| Exact provenance (branch/commit is pinnable & reproducible) | Larger footprint; slower first ingest |
| Easy to **re-ingest on upstream changes** (`git pull` → re-run ingest) | Must explicitly exclude meta files (see this repo's "Excluded Files" list) |
| Preserves upstream structure → clean section→page mapping | Risk of accidentally running upstream tooling (don't run `raw/`'s Makefiles) |
| Diffs show exactly what changed between ingests | Branch churn can silently move/rename sections (must audit) |

### 4c. Option B — Bring in individual files
- *How:* copy specific docs/PDFs/articles into `raw/topics/<topic>/` (or `raw/articles/`, `raw/papers/`).

| Pros | Cons |
|---|---|
| Minimal noise — only what you need | Provenance is manual and easy to lose |
| Fast to ingest; small footprint | No automatic re-ingest path; updates are manual |
| Good for one-off articles, papers, PDFs, mixed formats | Coverage gaps: easy to forget a related file |
| No upstream tooling comes along | No structural map to derive section→page mapping from |
| Easy when there is no single upstream repo | Harder to prove "this is the complete source set" |

### 4d. Decision guidance
- **Whole repo** when: source is a single upstream docs repo, you'll track it over time, and
  reproducibility matters (the default for CNCF project docs).
- **Individual files** when: sources are scattered (blogs, papers, PDFs), one-off, or you only
  need a slice.
- Either way: **always** create a `wiki/sources/<source>.md` summary that records what was
  ingested, counts, and what was deliberately excluded.

## §5. Workflow — Ingest
*What to write:* step list + copyable prompts (the "sample prompts for ingest" requirement).

*Steps:* read source under `raw/` → discuss key takeaways → create/update `wiki/sources/<source>.md`
→ create/update concept/entity pages → update `wiki/index.md` → append to `wiki/log.md`.

**Sample prompt — full ingest:**
```
Ingest the source at raw/topics/<topic>/. Read it in full, then:
1. Summarize the key takeaways and propose a section→page mapping before writing.
2. Create wiki/sources/<topic>-docs.md capturing what's covered, file counts, and
   any files deliberately excluded (repo meta, templates, boilerplate).
3. Create/update the concept & entity pages, one per major section. Every page must
   have YAML frontmatter (title, type, sources, related, created, updated, confidence),
   kebab-case <topic>-<subtopic>.md filenames, and [[wikilinks]] for all internal links.
4. Synthesize — condense sources into concise prose and comparison tables; do NOT copy
   verbatim. Every claim must cite a raw/ path.
5. Update wiki/index.md (catalog + coverage map) and append a dated entry to the top of
   wiki/log.md.
Do not edit anything under raw/. Do not run any tooling inside raw/.
```

**Sample prompt — re-ingest after upstream changes:**
```
The files under raw/topics/<topic>/ were updated. Re-ingest:
- Diff current sources against what the existing pages cover.
- Report source growth (new/renamed/removed sections) as a table.
- Re-synthesize affected pages, bump their `updated:` date, and expand `sources:`.
- Refresh index.md counts/coverage map and append a log.md entry describing the delta.
```

*Best practices to note:* ask the agent to **propose the mapping before writing**; ingest one
topic at a time; for very large corpora, delegate sections to sub-agents.

## §6. Workflow — Create / Update Wiki Pages
*What to write:* the page contract + prompts (the "create wiki pages / update index" requirement).

- **Frontmatter schema** (show verbatim; every page starts with this):
```yaml
---
title: "Human Readable Title"
type: concept        # concept | entity | source-summary | comparison
sources:
  - raw/topics/<topic>/content/docs/latest/<section>/
related:
  - "[[<topic>-overview]]"
created: YYYY-MM-DD
updated: YYYY-MM-DD
confidence: high     # high | medium | low
---
```
- Rules: kebab-case filenames; `[[wikilinks]]` never relative paths; synthesize don't copy;
  bump `updated:` on every change; `confidence:` reflects source strength.

**Sample prompt — new concept page:**
```
Create wiki/<topic>-<subtopic>.md as a `concept` page synthesizing the sources under
raw/topics/<topic>/.../<section>/. Use the standard frontmatter, cite every claim to a
raw/ path, prefer comparison tables over prose where it aids scanning, and add [[wikilinks]]
to related pages. Then update index.md and append to log.md.
```

**Sample prompt — update index:**
```
Update wiki/index.md: ensure every page in wiki/ and wiki/sources/ appears in the catalog
tables with an accurate one-line summary, and refresh the coverage map (section → page,
with current file counts). Flag any orphan pages (no incoming [[links]]) or catalog entries
whose files no longer exist.
```

**Sample prompt — append to log:**
```
Append a new dated entry to the TOP of wiki/log.md describing this operation: operation type,
source, reason, pages created/updated, and index changes. Keep newest-on-top ordering.
```

## §7. Workflow — Lint (Content Consistency, not Code)
*What to write:* what "lint" means for a wiki + prompt.
- Checks: **contradictions** across pages, **orphan pages** (no incoming links),
  **referenced-but-missing** concepts (dangling `[[wikilinks]]`), and **stale claims**
  superseded by newer sources.
- Output goes to `outputs/lint-YYYY-MM-DD.md` (not into the wiki pages themselves).

**Sample prompt — lint:**
```
Lint the wiki for content consistency (not code). Scan all wiki pages for: contradictions
between pages, orphan pages with no incoming [[links]], dangling wikilinks to pages that
don't exist, and stale claims superseded by newer sources. Write findings to
outputs/lint-<today>.md with file/line references and suggested fixes. Do not modify wiki
pages in this pass.
```

## §8. Workflow — Query / Q&A
*What to write:* how analysts pull answers back out.
- Steps: read `index.md` to find relevant pages → read them → synthesize → answer with
  `[[wikilink]]` citations → offer to save a novel, valuable answer as a new page.

**Sample prompt — query:**
```
Using the wiki, answer: "<question>". Start from index.md to locate relevant pages, read
them, synthesize a cited answer using [[wikilinks]], and if the answer is novel and reusable,
offer to save it as a new comparison/concept page.
```

## §9. Cross-Topic Hygiene & Auditing
*What to write:*
- **Cross-topic bleed:** when a topic is dropped, audit remaining pages for stray links to it
  — check both `related:` frontmatter and body content. (Reference the KubeVirt bleed audit in
  `log.md` as the worked example.)
- Retain source-derived content that legitimately belongs to the kept topic even if it *names*
  the removed one (e.g. Flatcar-on-KubeVirt deploy docs stay).
- Keep `index.md` and `log.md` as the **source of truth** for what exists and what happened.

## §10. Best Practices (Cheat Sheet)
*What to write — the "best practices" requirement, as a scannable list:*
- **Raw is sacred.** Never edit/move/delete `raw/`; never run tooling that lives inside it.
- **Cite everything.** Every claim → a `raw/` path; every page → `sources:` frontmatter.
- **Synthesize, don't copy.** Pages are condensed prose + tables, not reproductions.
- **One source of truth.** Update `index.md` and append `log.md` on *every* operation.
- **Ask before writing.** Have the agent propose a section→page mapping first.
- **Pin provenance.** Record upstream URL + branch/commit for reproducible re-ingests.
- **Prefer whole-repo ingest** for trackable CNCF docs; files for one-offs (see §4).
- **Right-size the model** (§2): high-reasoning for synthesis, fast for mechanical ops.
- **Small, verifiable steps.** Ingest one topic at a time; lint regularly.
- **Keep planning out of the vault.** Use session state, commit only deliverables.
- **Version the constitution.** Review `copilot-instructions.md` when conventions change.
- **Date discipline.** `YYYY-MM-DD`; bump `updated:` whenever a page changes.

## §11. Troubleshooting & FAQ
*What to write:* a short table.
- Agent edited `raw/` → revert; strengthen instructions; re-run.
- Pages drifted from sources → re-ingest (§5) and diff.
- Broken `[[wikilinks]]` / orphans → run lint (§7).
- Duplicate/overlapping pages → merge, add cross-links, update `index.md`.
- Agent ran upstream Makefile/scripts → forbidden; reaffirm the "don't run `raw/` tooling" rule.
- *TODO: add real incidents analysts hit in practice.*

## §12. Appendix
*What to write / attach:*
- Full copy of `.github/copilot-instructions.md` (or link).
- The exact model + settings your team standardized on. *TODO: fill in.*
- Glossary: ingest, synthesize, concept/entity/source-summary/comparison page, coverage map,
  cross-topic bleed, orphan page.
- Links: Obsidian, Copilot CLI docs, the upstream source repos in `raw/`.
