# Usability Accessibility and Devices - Comment

The KubeVirt user guide is highly usable and, for the most part, accessible, thanks to its Material for MkDocs foundation. The site is responsive and works well on mobile: it sets a proper viewport, collapses the top navigation into a mobile drawer, and keeps site search and the in-page table of contents reachable on small screens. Pages are readable, with clean typography, clear heading structure, and syntax-highlighted code, so readers can move through technical content comfortably on any device.

Accessibility support is strong at the structural level. The document declares its language, exposes semantic landmarks and descriptive ARIA labels (Header, Navigation, Search, Table of contents, Tabs), and provides a "Skip to content" link, all of which help keyboard and screen-reader users. Keyboard-only operation is well supported through the theme's navigation and search shortcuts. Text-to-speech users are also well served: every image in the documentation carries non-empty alt text, and there are no raw image tags missing an `alt` attribute.

The clear weak point is color contrast. The brand teal used as the primary color (`#0db2b6` in `docs/stylesheets/extra.css`) yields only about 2.6:1 against the white header text, which fails the WCAG AA requirement of 4.5:1 for normal text and even the 3:1 threshold for large text. Body links, darkened with `filter: brightness(80%)`, reach roughly 3.96:1 but still fall short of 4.5:1. This affects color-impaired and low-vision readers most, and it is the single most impactful fix in this area.

Addressing contrast would be straightforward and high value: darken the primary teal (or the text placed on it) until header text and links meet WCAG AA, and verify the result in both the light and dark schemes. To sustain accessibility over time, maintainers could add an automated contrast and accessibility check to the build and keep encouraging descriptive alt text and correct heading order in new pages.

Rating: 4 - Meets or exceeds standards
