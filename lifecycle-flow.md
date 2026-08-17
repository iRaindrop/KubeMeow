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
        Intake["Intake issue filed (Phase A)<br/>label: needs-triage"]
        Tracking["Tracking issue auto-opened (Phase B/C)<br/>on prior phase merge<br/>label: phase + needs-triage"]
    end

    Intake --> Triage
    Tracking --> Triage

    Triage{"Writer triages<br/>(write access required, P-1)"}
    Triage -->|"/decline &lt;reason&gt;"| Declined["label: triage/declined<br/>issue closed as not planned<br/>(assessment ends)"]

    %% ---- Step 2: Accept ----
    Triage -->|"/accept"| S2
    subgraph S2["2 - Accept (/accept)"]
        A1["Assign issue to writer = reviewer<br/>needs-triage &rarr; triage/accepted"]
        A2["Phase A: mention project contacts (HC-6)<br/>freeze stakeholder set (HC-2)"]
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
        R1 -->|"/verify"| R2["Verifier fact-check pass<br/>report as PR comment<br/>label: verified"]
        R1 -->|"skip, record reason (section 5)"| R3["Reviewer applies 'verified' label by hand"]
        R2 --> R4["Reviewer refines draft via @copilot mentions<br/>verifies findings against source (HC-7)"]
        R3 --> R4
    end

    S4 --> ReadyGate
    ReadyGate{"/ready<br/>(refused without 'verified' label)"}

    %% ---- Step 5: Stakeholder review ----
    ReadyGate --> S5
    subgraph S5["5 - Stakeholder review (/ready)"]
        SR1["PR marked ready for review<br/>mention frozen stakeholder set + guide link"]
        SR2["Stakeholder /confirm factual accuracy<br/>label: confirmed<br/>(disagreement recorded in deliverable, HC-2)"]
        SR1 --> SR2
    end

    S5 --> S6

    %% ---- Step 6: Merge ----
    subgraph S6["6 - Merge"]
        M1["Approver checks 'confirmed' label<br/>independent sign-off, merges PR (HC-4)"]
    end

    S6 --> Next
    Next{"Which phase merged?"}
    Next -->|"Phase A (default)"| OpenB["Workflow opens Phase B tracking issue<br/>+ posts transition on intake"]
    Next -->|"Phase A + /skip-implementation"| OpenC["Workflow opens Phase C tracking issue"]
    Next -->|"Phase B"| OpenC
    Next -->|"Phase C (final)"| Done(["Intake issue closed as completed"])

    OpenB --> Tracking
    OpenC --> Tracking

    %% ---- Failure / abort paths ----
    R4 -.->|"/discard &lt;reason&gt;"| Discard["PR closed, reason recorded<br/>tracking issue stays open<br/>(restart or hand-write)"]
    Discard -.-> S3
    S4 -.->|"admin/platform-owner abort"| Abort["tracking issue + intake<br/>closed as not planned"]
```

## Legend

- **Solid arrows** — the normal forward path through the six lifecycle steps.
- **Dashed arrows** — failure and abort paths (`/discard`, administrator abort).
- **Slash commands** (`/accept`, `/decline`, `/verify`, `/ready`, `/confirm`,
  `/discard`, `/skip-implementation`) are human acts issued as ordinary comments,
  authorized against the role bindings.
- **Labels** (`needs-triage`, `triage/accepted`, `triage/declined`, `verified`,
  `confirmed`) record where each assessment stands; an issue search by phase label
  is the portfolio view.
- References such as **HC-x** and **P-x** point to the hard constraints and
  principles in Part I of the spec.
