# KubeVirt User Guide: Content Maintainability Answers

- Is the documentation searchable?

    Yes. The `search` plugin is enabled in `mkdocs.yml` (with a custom tokenizer separator), and the `mkdocs-material` theme provides a built-in client-side search box across the site. Users can search all pages from the header search field.

- Are there plans for localization/internationalization with regards to site directory structure? Is a localization framework present?

    No. There is no localization framework configured. The `docs/` tree is organized by topic (for example `cluster_admin`, `compute`, `network`, `storage`) with no per-language subdirectories such as `en/` or `zh/`, and no i18n plugin (for example `mkdocs-static-i18n`) is present in `mkdocs.yml` or installed by the Netlify build. The theme does not set a language/locale switcher, and no localization plans are documented in the README or CONTRIBUTING files.

- Is there a clearly documented method for versioning of content?

    No. The documentation site publishes a single "latest" version built from the `main` branch to kubevirt.io/user-guide, and there is no content-versioning tooling configured. The standard MkDocs Material versioning tool (`mike`) is not enabled, the theme defines no version provider or version selector, and neither the README nor CONTRIBUTING describes a method for versioning documentation. The `release_notes.md` page tracks the KubeVirt product's release notes rather than versioned snapshots of the docs.
