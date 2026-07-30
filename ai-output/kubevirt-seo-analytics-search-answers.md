# SEO Analytics and Site Search - Answers

Analysis of the SEO, analytics, and site search of the KubeVirt user guide, based on its MkDocs configuration and the live site. Note that Netlify is used only to render pull-request previews; the production site is served under `kubevirt.io/user-guide`.

- Is analytics enabled for the production server?

    No. The user guide's `mkdocs.yml` has no `extra.analytics` configuration, and the live production pages contain no analytics tags (no Google Analytics `gtag`, Google Tag Manager, or measurement ID). The main `kubevirt.io` homepage likewise shows no analytics tags. This appears consistent with the project's privacy stance, but it means no usage analytics are collected.

- Is analytics disabled for all other deploys?

    Not applicable in practice. Because no analytics is configured anywhere, it is inherently absent from pull-request previews and non-default branch builds as well. The intended "production-only analytics" pattern cannot be assessed since there is no analytics to scope.

- If project is using Google Analytics, has it migrated to GA4?

    Not applicable. The project does not use Google Analytics on the user guide, so there is no Universal Analytics or GA4 property in use to migrate.

- Can Page-not-found (404) reports easily be generated from site analytics?

    No. Material for MkDocs generates a `404.html` page, but without any analytics in place there is no mechanism to report on 404 hits or generate not-found reports from site analytics.

- Is site indexing supported for the production server, while disabled for website previews and builds for non-default branches?

    Partially. Production indexing is supported: a site-wide `robots.txt` is served (returning 200) with a `Sitemap` directive and no `Disallow` rules, MkDocs generates a `sitemap.xml`, and pages carry no `noindex` meta tag. Pull-request previews are built on Netlify, whose deploy-preview and branch-deploy subdomains are served with a `noindex` `X-Robots-Tag` by Netlify's default behavior; however, this preview-noindex behavior is not explicitly configured in `netlify.toml`, so it relies on the platform default rather than an intentional project setting. One minor SEO defect is that the `robots.txt` Sitemap URL contains a double slash (`https://kubevirt.io//sitemap.xml`).

- Is local intra-site search available from the website?

    Yes. The MkDocs `search` plugin is enabled in `mkdocs.yml` (with a customized separator), and the Material theme provides the search box and results UI, giving readers client-side, intra-site search across the user guide.

- Are the current custodian(s) of the analytics accounts (such as Google CSE) documented?

    No. No analytics or search-account custodians are documented in the repository. Since no analytics account currently exists there is nothing to attribute, but there is also no documented owner should analytics be introduced.
