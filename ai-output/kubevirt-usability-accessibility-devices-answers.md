# Usability Accessibility and Devices - Answers

Analysis of the usability, accessibility, and devices support of the KubeVirt user guide, based on its Material for MkDocs theme, custom CSS, and the live site.

- Is the website usable from mobile?

    Yes. The live pages include a responsive viewport meta tag (`width=device-width,initial-scale=1`), and the Material for MkDocs theme is mobile-first and responsive, so the layout adapts to small screens.

- Are doc pages readable?

    Yes. Pages use the theme's clean Roboto typography, clear heading hierarchy, an in-page table of contents, admonitions, and syntax-highlighted code blocks, all of which support comfortable reading on the documentation site.

- Are all / most website features accessible from mobile -- such as the top-nav, site search and in-page table of contents?

    Yes. The primary navigation (rendered as tabs on desktop) collapses into a mobile drawer, site search is present (`md-search`), and the in-page table of contents is available. All are exposed with descriptive ARIA labels (for example, "Header," "Navigation," "Search," "Table of contents," and "Tabs"), so the key features remain reachable on mobile.

- Are color contrasts significant enough for color-impaired readers?

    Partially, and this is the area's weakest point. The brand teal used as the primary color (`--md-primary-fg-color: #0db2b6`, set in `docs/stylesheets/extra.css`) provides only about a 2.6:1 contrast ratio with the white header text, which is below the WCAG AA threshold of 4.5:1 for normal text and even below the 3:1 threshold for large text. Body links are darkened with `filter: brightness(80%)`, which improves them to roughly 3.96:1 but still falls short of the 4.5:1 AA requirement for normal text. Contrast therefore needs improvement for color-impaired readers.

- Are most website features usable using a keyboard only?

    Yes. The page includes a "Skip to content" link (`md-skip`), and the Material theme provides full keyboard navigation and search keyboard shortcuts, so the main features can be operated without a mouse.

- Does text-to-speech offer listeners a good experience?

    Largely yes. The document declares its language (`<html lang="en">`), uses semantic landmarks and ARIA labels, provides a skip link, and every image in the documentation carries non-empty alt text (25 markdown images, none with empty alt, and no raw `<img>` tags lacking `alt`). These give screen readers and text-to-speech tools a solid foundation, though the ongoing quality of alt text and heading order depends on authors.
