# Beginner Friendly Issue Backlog - Recommendations

The following recommendations address the Beginner Friendly Issue Backlog of the KubeVirt user guide.

- Consolidate the duplicate labels by standardizing on the GitHub-native `good first issue` label (spaced) and retiring or aliasing the hyphenated `good-first-issue`, so beginner issues appear in GitHub's "Contribute" tab and good-first-issue discovery tooling. Update the reference on the contributing page to match the chosen label.
- Maintain a small, non-empty pool of beginner issues. Periodically identify documentation gaps, typos, and small feature-doc updates and file them as `good first issue` so a new contributor always finds something to pick up.
- Triage the currently open backlog. Apply `kind/*` and `sig/documentation` labels to unlabeled issues, and use `triage/accepted` to signal that an issue is ready to be worked on.
- Add a `help wanted` complement for slightly larger but still approachable tasks, and reference both `good first issue` and `help wanted` on the contributing page so contributors understand the difference.
- Preserve valuable issues from aggressive auto-close by applying `lifecycle/frozen` (or promptly triaging) to still-relevant enhancements and documentation requests, rather than letting them reach `lifecycle/rotten` and close for inactivity alone.
- Keep issue quality high by continuing to use the description/expectation/URL templates, and add a short "good first issue" checklist to those templates (affected page, expected outcome, pointers to relevant docs) so beginner issues are self-contained.
- Link directly to a filtered beginner view from the contributing page — for example, the repository's `good first issue` label query — so newcomers reach actionable issues in one click instead of browsing the full issue list.
- Publish a lightweight triage cadence (for example, a periodic documentation-issue triage during a SIG or community meeting) to keep labeling, acceptance, and staleness decisions consistent over time.
