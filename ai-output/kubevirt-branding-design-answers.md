# Branding and Design - Answers

Analysis of the branding and design of the KubeVirt user guide.

- Is there an easily recognizable brand for the project (logo + color scheme) clearly identifiable?

    Yes. The KubeVirt logo, a teal heptagon enclosing a stylized "V," is displayed in the site header and configured through `theme.logo: assets/KubeVirt_icon.png`, with matching favicons (`assets/favicon.ico` and `assets/favicon32x32.png`) in `mkdocs.yml`. The color scheme reinforces the logo: the Material theme uses a teal palette, and `docs/stylesheets/extra.css` pins the exact brand colors (`--md-primary-fg-color: #0db2b6` and `--md-accent-fg-color: #006166`). Together the logo and teal palette make the project brand clearly identifiable on every page.

- Is the brand used across the website consistently?

    Within the user guide, yes. The teal palette is applied globally through the Material theme and `extra.css`, so the primary and accent colors are consistent across all pages and are defined for both the light (`default`) and dark (`slate`) schemes. The logo appears in the header site-wide, and section labels in the navigation are given a coordinated teal tone (`#00797f`). One caveat is that the user guide is a MkDocs Material site, while the main `kubevirt.io` website is a separate property with its own styling, so the two share the logo and general color family but do not share an identical look and feel.

- Is the website's typography clean and well-suited for reading?

    Yes. The guide does not override the theme fonts, so it inherits the Material theme's default typeface (Roboto for body text and Roboto Mono for code), which is a clean, legible sans-serif well-suited to on-screen reading. Headings, body copy, tables, and code blocks are styled consistently by the theme, code uses monospaced type with syntax highlighting, and tables are set to full width (`min-width: 100%`) for readability. The custom `filter: brightness(80%)` applied to links slightly darkens link text, which is a minor contrast consideration but does not materially harm readability.
