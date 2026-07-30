# Maintenance Planning - Comment

The KubeVirt user guide is on a solid maintenance footing. It is built with MkDocs and the Material for MkDocs theme, supplemented by the `awesome-nav`, `redirects`, and `htmlproofer` plugins. Although this differs from the Hugo and Docsy stack, MkDocs Material is a mature and widely adopted documentation toolchain used across the CNCF and Kubernetes ecosystems, so maintainers can rely on strong community support and a steady stream of upstream updates.

Maintenance responsibility is clearly structured and actively exercised. The repository uses the Kubernetes-style OWNERS model, defining reviewers and approvers roles and recording emeritus approvers, which gives maintainers appropriate permissions to review and merge changes. The commit history reflects a healthy, cultivated community, with roughly 49 distinct authors in the last twelve months and a continuous flow of merged pull requests, so the guide is not dependent on a single maintainer.

The build and hosting setup is dependable. MkDocs builds this static site quickly, Netlify produces per-pull-request previews, and the project's Prow-based CI builds the site as well. The site is served securely: HTTPS returns a 200 response, and HTTP requests are 301-redirected to HTTPS for both the user guide path and the apex domain. These are exactly the properties one wants for low-friction, secure maintenance.

The main opportunities are around build reproducibility and stack consolidation. The build installs MkDocs and its plugins without pinned versions (in `netlify.toml` and the `Makefile`), which risks non-reproducible builds or breakage when an upstream package changes; pinning versions would harden this. Maintaining two separate stacks (MkDocs for the user guide and Jekyll for the main site) also adds ongoing overhead worth periodically reviewing.

Rating: 4 - Meets or exceeds standards
