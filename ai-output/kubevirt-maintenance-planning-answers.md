# Maintenance Planning - Answers

Analysis of the maintenance planning of the KubeVirt user guide, based on its tooling, maintainer activity, build process, and hosting.

- Is the website tooling well supported by the community (i.e., Hugo with the Docsy theme) or commonly used by CNCF projects?

    Yes. The user guide is built with MkDocs and the Material for MkDocs theme, along with the `awesome-nav`, `redirects`, and `htmlproofer` plugins (see `mkdocs.yml`, `Makefile`, and `netlify.toml`). While this is not the Hugo and Docsy stack named in the question, MkDocs Material is a mature, actively maintained, and widely adopted documentation tool used across many CNCF and Kubernetes-ecosystem projects, so the tooling is well supported. Note that the main `kubevirt.io` website is a separate Jekyll site, so the project maintains two different stacks.

- Is there active cultivating website maintainers from within the community?

    Yes. The repository has an `OWNERS` file that defines reviewers and approvers roles (via aliases) and lists emeritus approvers, and the project uses the Kubernetes-style OWNERS model for delegating maintenance. Git history shows sustained activity, with roughly 49 distinct authors contributing in the last 12 months and a steady stream of merged pull requests, indicating an active and growing maintainer and contributor base.

- Are site build times reasonable?

    Yes. MkDocs produces a static site of this size quickly, typically well under a minute, and the build is a straightforward `mkdocs build`. Netlify builds preview deployments for pull requests and the project's Prow-based CI builds the site as well, so build times are reasonable for both previews and production.

- Do site maintainers have adequate permissions?

    Yes. Permissions are managed through the Kubernetes-style OWNERS model, where designated approvers can approve and merge changes and reviewers can review. The `OWNERS` file separates reviewers and approvers and records emeritus approvers, giving maintainers the access they need while keeping the roles documented.

- Is the website accessible via HTTPS?

    Yes. Requesting `https://kubevirt.io/user-guide/` returns HTTP 200 over HTTPS.

- Does HTTP access, if any, redirect to HTTPS?

    Yes. Requesting `http://kubevirt.io/user-guide/` returns a 301 redirect to the HTTPS URL, and the apex `http://kubevirt.io/` likewise 301-redirects to HTTPS.
