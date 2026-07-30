# SEO Analytics and Site Search - Recommendations

The following recommendations address the SEO, analytics, and site search of the KubeVirt user guide.

- Decide whether to adopt analytics for the documentation, and if so, choose either a GA4 property or a privacy-respecting alternative that aligns with the project's privacy policy, so maintainers gain visibility into traffic and popular content.
- If analytics is adopted, enable it only on the production deploy and keep it disabled for pull-request previews and non-default branch builds, configuring it through the Material theme's analytics integration rather than per page.
- If analytics is adopted, ensure Page-not-found (404) reporting is available so broken inbound links can be identified and fixed over time.
- Document the custodians of any analytics or search accounts (for example, who owns the analytics property) in the repository, so ownership remains clear as maintainers change.
- Make the preview `noindex` behavior an explicit project setting (for example, an `X-Robots-Tag` header for Netlify preview and branch deploys) rather than relying solely on the Netlify default, so indexing rules are intentional and documented.
- Fix the double slash in the `robots.txt` Sitemap URL (`https://kubevirt.io//sitemap.xml`) so it points to a single canonical sitemap location.
- Keep the MkDocs `search` plugin enabled and continue to benefit from the Material theme's intra-site search, periodically reviewing the search separator configuration as content grows.
