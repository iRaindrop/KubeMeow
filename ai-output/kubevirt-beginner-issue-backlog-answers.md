# Beginner Friendly Issue Backlog - Answers

The following answers assess the beginner-friendly issue backlog for the KubeVirt user guide. Documentation issues are tracked primarily in the [kubevirt/user-guide](https://github.com/kubevirt/user-guide/issues) repository, and the contributing guide also points new contributors to the community, website, and core code repositories.

## Are docs issues well-triaged?

Documentation issues are only partially triaged. At the time of review the user-guide repository had four open issues, and three of them carried no labels at all; only one was categorized (with `kind/enhancement`). The repository does provide a complete triage label taxonomy (`kind/*`, `triage/accepted`, `triage/needs-information`, `sig/documentation`, and others), and closed issues show that labels such as `kind/bug` and `kind/enhancement` were applied over time. However, `triage/accepted` is rarely used, and the currently open backlog is largely uncategorized, so triage is inconsistent in practice.

## Is there a clearly marked way for new contributors to make code or documentation contributions (i.e. a "good first issue" label)?

Yes, a mechanism exists and is documented, but it is currently underused. The user-guide repository has a `good-first-issue` label that has been applied to 24 issues historically, and the contributing page explicitly tells newcomers to "look for any labeled 'good-first-issue', which are triaged to help new contributors." Two caveats reduce its effectiveness. First, there are currently zero open `good-first-issue` items in both the user-guide and the core kubevirt/kubevirt repositories, so a new contributor arriving today finds an empty beginner backlog. Second, the repository has two near-duplicate labels — the hyphenated `good-first-issue` that the team actually uses and the standard spaced `good first issue` that is unused — which is inconsistent and prevents GitHub's native "Contribute" tab from surfacing these issues.

## Are issues well-documented (i.e., more than just a title)?

Yes. Issues generally contain substantive descriptions rather than bare titles. Bug reports follow a template with **Description**, **What you expected**, and **URL** sections, and enhancement requests use the feature-request template. The open issues ranged from roughly 400 to nearly 1,900 characters of body text; for example, the Simplified Chinese documentation proposal includes detailed context about the contributing team and scope. This indicates issues are typically actionable and provide enough information to begin work.

## Are issues maintained for staleness?

Yes, staleness is actively — and aggressively — managed by the shared KubeVirt Prow automation. Issues progress through `lifecycle/stale` and `lifecycle/rotten` and are then auto-closed, with `lifecycle/frozen` available to exempt long-lived items. Many closed user-guide issues carry the `lifecycle/rotten` label, and the core kubevirt/kubevirt repository currently shows roughly 31 stale, 32 rotten, and 30 frozen open issues. The main risk is that valid but unattended issues (including enhancements) are closed purely for inactivity rather than being triaged or preserved, so the backlog stays small partly through automated closure.
