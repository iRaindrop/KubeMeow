# Branding and Design - Recommendations

The following recommendations address the branding and design of the KubeVirt user guide.

- Document a small set of shared brand values in the repository, such as the brand hex colors (`#0db2b6` and `#006166`), the logo and favicon files, and the chosen fonts, so the branding is defined in one place rather than implied by the theme configuration.
- Align the user guide's look and feel more closely with the main `kubevirt.io` website by agreeing on a shared logo, color family, and typography across both properties, so readers experience a consistent brand as they move between the sites.
- Verify the customized link styling (`filter: brightness(80%)` in `docs/stylesheets/extra.css`) against accessibility contrast targets in both the light and dark schemes, and adjust or remove the filter if it reduces contrast below recommended levels.
- Keep relying on the Material theme's default Roboto and Roboto Mono typography, and if a custom font is ever introduced, apply it through the theme configuration so it remains consistent across all pages.
- Confirm the teal palette renders correctly in the dark (`slate`) scheme, checking that logo, links, code blocks, and navigation labels retain sufficient contrast and remain on-brand.
- Continue defining brand colors through theme-level variables in `extra.css` rather than per-page styling, so the brand stays consistent as new pages are added.
