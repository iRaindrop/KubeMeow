# Maintenance Planning - Recommendations

The following recommendations address the maintenance planning of the KubeVirt user guide.

- Pin the versions of MkDocs and its plugins (`mkdocs`, `mkdocs-material`, `mkdocs-awesome-nav`, `mkdocs-redirects`, and `mkdocs-htmlproofer-plugin`) in the build definitions, for example via a `requirements.txt`, so that Netlify and Prow builds are reproducible and resistant to breaking upstream changes.
- Keep the pinned dependency versions current through a regular update cadence, ideally automated (for example with Dependabot or Renovate), so the guide continues to benefit from the actively maintained MkDocs Material toolchain.
- Continue cultivating maintainers through the OWNERS model, and periodically review the reviewers and approvers lists to confirm they reflect currently active contributors and that coverage is not concentrated in too few people.
- Preserve the existing HTTPS posture, keeping the site accessible over HTTPS and retaining the HTTP-to-HTTPS redirects for both the user guide path and the apex domain.
- Periodically review the overhead of maintaining two separate stacks (MkDocs for the user guide and Jekyll for the main `kubevirt.io` site), and consider whether consolidation or closer alignment would reduce long-term maintenance effort.
- Document the local and CI build process (build commands, dependencies, and preview workflow) in a contributor-facing location so new maintainers can reproduce and troubleshoot builds easily.
