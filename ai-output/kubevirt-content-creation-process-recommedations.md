# KubeVirt User Guide: Content Creation Process Recommendations

The following recommendations address the content creation process of the KubeVirt user guide.

- Document the OWNERS/Prow approval model directly in `contributing.md`, including how `/lgtm` and `/approve` work and who contributors should expect review from, so the approval path is transparent to newcomers.
- Establish and document an expectation that user-facing changes in `kubevirt/kubevirt` ship with a companion user-guide update, for example through a release checklist item or a cross-repository issue link, to reduce documentation drift.
- Add documentation creation and updates as an accountable step in the code release process so docs are no longer decoupled from KubeVirt's release cadence.
- Preserve and continue to signpost the existing strengths—the clear `docs/contributing.md` GitHub workflow, the README's local authoring and validation guidance (yaspeller and HTMLProofer `make` targets), and the per-section `OWNERS` delegation to KubeVirt SIGs.
- Keep the automatic `kind/documentation` labeling and per-section `OWNERS` files current as new topic areas are added under `docs/`, so review responsibility remains clearly assigned.
