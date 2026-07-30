# Usability Accessibility and Devices - Recommendations

The following recommendations address the usability, accessibility, and devices support of the KubeVirt user guide.

- Increase color contrast for the brand teal primary color (`#0db2b6` in `docs/stylesheets/extra.css`) so that white header text meets the WCAG AA contrast ratio of at least 4.5:1 for normal text, either by darkening the teal or by adjusting the text color placed on it.
- Adjust the body link color (currently the primary color darkened with `filter: brightness(80%)`) so that links reach at least 4.5:1 contrast against the page background, rather than the roughly 3.96:1 they achieve today.
- Verify all contrast changes in both the light (`default`) and dark (`slate`) schemes, checking header text, links, navigation section labels, and code blocks.
- Add a-ln automated accessibility and contrast check to the site build (for example, a Lighthouse or axe-based check) so contrast regressions are caught before publishing.
- Continue requiring descriptive, non-empty alt text on all images and maintain correct heading order in new pages, so screen-reader and text-to-speech users keep getting a good experience.
- Preserve the existing strengths, keeping the responsive viewport, mobile drawer navigation, site search, in-page table of contents, skip-to-content link, and ARIA labels intact as the theme is upgraded.
