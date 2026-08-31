# Section 12: Lifecycle bindings — flow chart

This flow chart visualizes the per-assessment lifecycle described in Section 12,
"Lifecycle bindings," of the AI-assisted TechDocs Assessment spec. Each of the six
lifecycle steps binds to a native GitHub primitive (issues, PRs, labels) driven by
slash-command comments. The cycle repeats for each phase (A: assessment,
B: implementation plan, C: issue backlog).

```mermaid
flowchart TD
    %% ---- Step 1: Request ----
    subgraph S1["1 - Request (a GitHub issue)"]
        Umbrella["Intake issue filed = umbrella (Phase A request)<br/>open end-to-end &middot; carries current-phase label<br/>accumulates links + transition posts<br/>label: needs-triage"]
        Tracking["Phase B/C tracking issue<br/>auto-opened on prior phase merge<br/>label: phase + needs-triage"]
    end

    Umbrella --> Triage
    Tracking --> Triage

    Triage{"Writer triages<br/>(write access required, P-1)"}
    Triage -->|"/decline &lt;reason&gt;"| Declined["label: triage/declined, issue closed as not planned<br/>intake &rarr; assessment never starts<br/>B/C tracking &rarr; ends here, noted on umbrella,<br/>intake closed as not planned"]

    %% ---- Step 2: Accept ----
    Triage -->|"/accept"| S2
    subgraph S2["2 - Accept (/accept)"]
        A1["Assign issue to writer = reviewer<br/>needs-triage &rarr; triage/accepted<br/>(B/C: acceptance also noted on umbrella)"]
        A2["Phase A: mention project contacts (HC-6)<br/>freeze + validate stakeholder set (HC-2)"]
        A3["Writer delegates to agent<br/>picks drafting profile + model"]
        A1 --> A2 --> A3
    end

    S2 --> S3

    %% ---- Step 3: Draft ----
    subgraph S3["3 - Draft (draft pull request)"]
        D1["Agent works on its branch in cncf/techdocs<br/>opens draft PR linked to tracking issue<br/>carries provenance block (section 15)"]
    end

    S3 --> S4

    %% ---- Step 4: Review ----
    subgraph S4["4 - Review (PR comments)"]
        R1{"Reviewer runs verifier?"}
        R1 -->|"/verify (only command that starts a model run, P-1)"| R2["Verifier fact-check pass<br/>report as PR comment<br/>label: verified"]
        R1 -->|"skip, record reason (section 5)"| R3["Reviewer applies 'verified' label by hand"]
        R2 --> R4["Reviewer refines draft via @copilot mentions<br/>verifies findings against source (HC-7)"]
        R3 --> R4
    end

    S4 --> Ready
    Ready{"/ready<br/>refused without 'verified' label<br/>on success: marks PR ready +<br/>mentions frozen stakeholders + guide link"}
    Ready -. "no 'verified' label &rarr; blocked" .-> S4

    %% ---- Step 5: Stakeholder review ----
    Ready --> S5
    subgraph S5["5 - Stakeholder review"]
        SR2["Stakeholder /confirm factual accuracy<br/>authorized against frozen set (not repo access)<br/>label: confirmed<br/>disagreement recorded in deliverable (HC-2)"]
    end

    S5 --> S6

    %% ---- Step 6: Merge ----
    subgraph S6["6 - Merge"]
        M1["Approver checks 'confirmed' label<br/>independent sign-off (HC-4), merges PR"]
    end

    S6 --> Next
    Next{"Merge-triggered workflow<br/>(GITHUB_TOKEN, issues: write):<br/>which phase merged?"}
    Next -->|"Phase A (default)"| OpenB["Opens Phase B tracking issue (needs-triage)<br/>assigns no one (eligible, not started)"]
    Next -->|"Phase A + skip-implementation label<br/>(set on Phase A PR before merge)"| OpenC["Opens Phase C tracking issue (needs-triage)<br/>assigns no one (eligible, not started)"]
    Next -->|"Phase B"| OpenC
    Next -->|"Phase C (final)"| Done(["Final merge: umbrella (intake)<br/>closed as completed"])

    OpenB --> Tracking
    OpenC --> Tracking
    OpenB -. "posts transition + swaps phase label" .-> Umbrella
    OpenC -. "posts transition + swaps phase label" .-> Umbrella

    %% ---- Failure / abort paths ----
    R4 -.->|"/discard &lt;reason&gt;"| Discard["PR closed, reason recorded, noted on umbrella<br/>tracking issue stays open"]
    Discard -.-> Restart{"Restart?"}
    Restart -. "re-delegate to agent" .-> S3
    Restart -. "hand-write phase" .-> HandWrite["Human-authored PR<br/>provenance: hand-written (HC-6)"]
    HandWrite -.-> S4
    Restart -. "repeated failure &rarr; escalate (section 5)" .-> Abort["admin/platform-owner abort<br/>tracking issue + intake closed as not planned<br/>(reachable from any active phase)"]
```

## Legend

- **Solid arrows** — the normal forward path through the six lifecycle steps.
- **Dashed arrows** — the gate refusal, failure, restart, and abort paths
  (`/discard`, hand-write, administrator abort), plus the workflow's transition
  posts to the umbrella.
- **Umbrella (intake) issue** — the intake issue doubles as the assessment's
  umbrella. It stays open end to end, carries the current-phase label, and the
  merge-triggered workflow posts each transition to it and swaps its phase label.
- **Slash commands** (`/accept`, `/decline`, `/verify`, `/ready`, `/confirm`,
  `/discard`, `/skip-implementation`) are human acts issued as ordinary comments,
  authorized against the role bindings. Only `/verify` starts a model run (P-1).
- **Labels** (`needs-triage`, `triage/accepted`, `triage/declined`, `verified`,
  `confirmed`) record where each assessment stands; an issue search by phase label
  is the portfolio view.
- References such as **HC-x** and **P-x** point to the hard constraints and
  principles in Part I of the spec.

## Suggestions incorporated

This revision applied the following changes to tighten the chart's fidelity to
Section 12. They are recorded here so the rationale travels with the diagram.

1. **Modeled the intake as a persistent umbrella issue.** The spec stresses that
   the intake issue stays open end to end, accumulates cross-references, carries
   the current-phase label, and receives each transition post from the merge
   workflow. The chart now shows a standing umbrella node that the merge step
   posts transitions to and swaps the phase label on, instead of silently
   re-entering the tracking issue.
2. **Split the decline outcomes.** The single decline node now distinguishes the
   two spec cases: declining the intake means the assessment never starts,
   whereas declining a Phase B or C tracking issue ends the assessment there, is
   noted on the umbrella, and closes the intake as not planned.
3. **Showed both restart paths after `/discard`.** The tracking issue stays open
   for either a re-delegation to the agent or a hand-written phase. The chart now
   branches to both, with the hand-authored pull request re-entering review and
   carrying a hand-written provenance header (HC-6).
4. **Merged the duplicated `/ready` step.** `/ready` is now one node: it is
   refused without the `verified` label and, on success, marks the pull request
   ready and mentions the frozen stakeholder set with the participant-guide link.
5. **Reattached abort to the failure loop.** An administrator or platform-owner
   abort now follows repeated-failure escalation (section 5) and is annotated as
   reachable from any active phase, rather than hanging off the review step alone.
6. **Clarified `/skip-implementation` timing.** The skip label is set on the
   Phase A pull request before merge; the merge-triggered workflow then reads it
   to open Phase C instead of Phase B.

Minor annotations were also added: `/verify` is flagged as the only command that
starts a model run (P-1); the merge workflow notes that it assigns no one
(eligible, not started) and runs with `GITHUB_TOKEN` (`issues: write`); and
`/confirm` is noted as authorized against the frozen stakeholder set rather than
repository access.

