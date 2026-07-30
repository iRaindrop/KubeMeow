# KubeVirt User Guide: Content Maintainability Recommendations

The following recommendations address the content maintainability of the KubeVirt user guide.

- Adopt `mike`, the standard versioning tool for MkDocs Material, to publish documentation versions that align with KubeVirt product releases so readers can view docs matching their deployment.
- Add a version selector (dropdown) to the theme configuration so users can switch between the latest and historical documentation snapshots.
- Document the content-versioning method in the README or CONTRIBUTING files, including how and when new versions are cut relative to KubeVirt releases.
- Decide early on a localization directory convention (for example, per-language subdirectories such as `en/` or `zh/`) so the current flat, topic-based layout can accommodate translations without a disruptive future reorganization.
- Evaluate an internationalization plugin such as `mkdocs-static-i18n` and document the intended localization approach, even if implementation is deferred, so contributors can plan content accordingly.
- Preserve the existing maintainability strengths—client-side search, explicit `.nav.yml` ordering, and the `redirects` map in `mkdocs.yml`—and continue adding redirect entries whenever pages are moved or renamed to prevent link rot.
