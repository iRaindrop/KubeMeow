# KubeVirt User Guide: Content Creation Process Answers

- Is there a clearly documented (ongoing) contribution process for documentation?

    Yes. `docs/contributing.md` explains the ongoing GitHub workflow (fork, branch, commit, open pull request, review, merge), explicitly lists the user-guide repository as a low-barrier target for first contributions, and links to community resources such as the Code of Conduct, membership policy, and governance. The repository README complements this with the local authoring workflow: where content lives (`./docs`), how to sign commits, and how to validate changes with `make` targets for spelling (yaspeller) and link checking (HTMLProofer) before opening a PR.

- Does the code release process account for documentation creation & updates?

    Not explicitly. The user guide lives in a separate repository (`kubevirt/user-guide`) and is published continuously from the `main` branch to kubevirt.io/user-guide rather than being cut alongside KubeVirt code releases. While a `release_notes.md` page tracks product releases, there is no documented mechanism in this repository that requires documentation to be created or updated as part of the core code release process, so docs updates are decoupled from the release cadence.

- Who reviews and approves documentation pull requests?

    Reviews and approvals are governed by Kubernetes-style OWNERS files enforced through Prow. The root `OWNERS` delegates to `reviewers` and `approvers` aliases defined in `OWNERS_ALIASES` (reviewers include aburdenthehand, dhiller, fabiand, jean-edouard, mhenriks, phoracek, and vladikr; approvers additionally include davidvossel, rmohr, and stu-gott). Subdirectories under `docs/` delegate to the relevant SIG teams—for example `docs/storage/OWNERS` routes to sig-storage reviewers and approvers. Documentation PRs are automatically labeled `kind/documentation`, and merges require an approver's `/approve` plus reviewer `/lgtm`.

- Does the website have a clear owner/maintainer?

    Yes. Ownership is clearly defined through the repository's `OWNERS` and `OWNERS_ALIASES` files, which name active reviewers and approvers (and list emeritus approvers for historical context). Per-section `OWNERS` files under `docs/` further assign responsibility to the appropriate KubeVirt SIGs, giving the site both overall and area-specific maintainers.
