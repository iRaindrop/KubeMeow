---
title: Criteria vs. Analysis Question Comparison
---

# Criteria vs. Analysis Question Comparison

This report pairs each evaluation question from the CNCF TechDocs
[criteria.md](https://github.com/cncf/techdocs/blob/main/docs/analysis/criteria.md)
with its corresponding question in the
[analysis.md](https://github.com/cncf/techdocs/blob/main/docs/analysis/templates/analysis.md)
template. Where the analysis template has no corresponding question, this is
noted as `(no corresponding question in analysis.md)`.

A spreadsheet of this data is the CSV file by the same name, and a Google sheet of it here:
https://docs.google.com/spreadsheets/d/10Gtt-BYs7DQXo1BKqIxEDZGJKDtEeLB_KgSxdHikhV4/edit?usp=sharing

## Project documentation

### Information architecture

**Criteria:** Is there high level conceptual content?
**Analysis:** Is there high level conceptual/"About" content? Is the documentation feature complete? (i.e., each product feature is documented)

**Criteria:** Is every product feature documented?
**Analysis:** Is the documentation feature complete? (i.e., each product feature is documented) — folded into the "high level conceptual/About content" question above.

**Criteria:** Does the documentation define all user roles (personas) for the product?
**Analysis:** (no corresponding question in analysis.md)

**Criteria:** Are there instructions (tasks, tutorials) documented for features?
**Analysis:** Are there step-by-step instructions (tasks, tutorials) documented for features?

**Criteria:** Are there instructions for all major use cases for each user role?
**Analysis:** (no corresponding question in analysis.md)

**Criteria:** Are tasks organized by user role and use case?
**Analysis:** (no corresponding question in analysis.md)

**Criteria:** Does instructional content demonstrate atomicity — are individual tasks clearly named according to their goals?
**Analysis:** Does task and tutorial content demonstrate atomicity and isolation of concerns? (Are tasks clearly named according to user goals?)

**Criteria:** Are tasks written as numbered step-by-step instructions?
**Analysis:** (no corresponding question in analysis.md; "step-by-step" appears only within the "Are there step-by-step instructions (tasks, tutorials)..." question)

**Criteria:** Do task descriptions in headings and the TOC describe the task with a verb phrase?
**Analysis:** (no corresponding question in analysis.md)

**Criteria:** Is the documentation free of any key features which are documented but missing task documentation?
**Analysis:** Are there any key features which are documented but missing task documentation?

**Criteria:** Is the "happy path" — the most common use case — documented?
**Analysis:** Is the "happy path"/most common use case documented? Does task and tutorial content demonstrate atomicity and isolation of concerns? (Are tasks clearly named according to user goals?)

**Criteria:** If the documentation does not suffice, is there a clear escalation path for users needing more help?
**Analysis:** If the documentation does not suffice, is there a clear escalation path for users needing more help? (FAQ, Troubleshooting)

**Criteria:** If the product exposes an API, is there a complete reference?
**Analysis:** If the product exposes an API, is there a complete reference?

**Criteria:** If the product has CLIs, are there complete references?
**Analysis:** (no corresponding question in analysis.md)

**Criteria:** Is content up to date and accurate?
**Analysis:** Is content up to date and accurate?

**Criteria:** Does the documentation separate conceptual, instructional, and reference information?
**Analysis:** (no corresponding question in analysis.md)

### New user content

**Criteria:** Is "getting started" clearly labeled? ("Getting started", "Installation", "First steps", or the equivalent.)
**Analysis:** Is "getting started" clearly labeled? ("Getting started", "Installation", "First steps", etc.)

**Criteria:** Is there a "getting started" path for all user roles?
**Analysis:** (no corresponding question in analysis.md)

**Criteria:** Is installation documented step-by-step?
**Analysis:** Is installation documented step-by-step?

**Criteria:** Are different types of installation documented (development, test, production) if necessary?
**Analysis:** (no corresponding question in analysis.md)

**Criteria:** If needed, are multiple OSes documented?
**Analysis:** If needed, are multiple OSes documented?

**Criteria:** Do users know where to go after reading the getting started guide?
**Analysis:** Do users know where to go after reading the getting started guide?

**Criteria:** Is your new user content clearly signposted on your site's homepage or at the top of your information architecture?
**Analysis:** Is your new user content clearly signposted on your site's homepage or at the top of your information architecture?

**Criteria:** Is there easily copy-pastable sample code or other example content?
**Analysis:** Is there sample code or other example content that can easily be copy-pasted?

### Content maintainability & site mechanics

**Criteria:** Is your documentation searchable?
**Analysis:** Is your documentation searchable?

**Criteria:** Are you planning for localization/internationalization as regards site directory structure?
**Analysis:** Are you planning for localization/internationalization with regards to site directory structure? Is a localization framework present?

**Criteria:** Is a localization framework present?
**Analysis:** Is a localization framework present? — folded into the "planning for localization/internationalization" question above.

**Criteria:** Do you have a clearly documented method for versioning your content?
**Analysis:** Do you have a clearly documented method for versioning your content?

**Criteria:** Is release-specific information documented in release notes?
**Analysis:** (no corresponding question in analysis.md)

**Criteria:** Is the documentation free of duplicate or nearly duplicated sections of information?
**Analysis:** (no corresponding question in analysis.md)

**Criteria:** Do informational graphics add value by providing information in a way that would be difficult in text?
**Analysis:** (no corresponding question in analysis.md)

**Criteria:** Will graphics require frequent modifications due to software changes, GUI updates, or translation?
**Analysis:** (no corresponding question in analysis.md)

### Content creation processes

**Criteria:** Is there a clearly documented (ongoing) contribution process for documentation?
**Analysis:** Is there a clearly documented (ongoing) contribution process for documentation?

**Criteria:** Does your code release process account for documentation creation & updates?
**Analysis:** Does your code release process account for documentation creation & updates?

**Criteria:** Who reviews and approves documentation pull requests?
**Analysis:** Who reviews and approves documentation pull requests?

**Criteria:** Does the website have a clear owner/maintainer?
**Analysis:** Does the website have a clear owner/maintainer?

### Inclusive language

**Criteria:** Are there any customer-facing utilities, endpoints, class names, or feature names that use non-recommended words as documented by the Inclusive Naming Initiative website?
**Analysis:** Are there any customer-facing utilities, endpoints, class names, or feature names that use non-recommended words as documented by the Inclusive Naming Initiative website?

**Criteria:** Does the project use language like "simple", "easy", etc.?
**Analysis:** Does the project use language like "simple", "easy", etc.?

## Contributor documentation

### Communication methods documented

**Criteria:** Is there a Slack/Discord/Discourse or equivalent community prominently linked from your website?
**Analysis:** Is there a Slack/Discord/Discourse/etc. community and is it prominently linked from your website?

**Criteria:** Is there a direct link to your GitHub project or repository?
**Analysis:** Is there a direct link to your GitHub organization/repository?

**Criteria:** Can users find and join periodic (weekly or monthly) project meetings, if applicable?
**Analysis:** Are weekly/monthly project meetings documented? Is it clear how someone can join those meetings?

**Criteria:** Are mailing lists documented?
**Analysis:** Are mailing lists documented?

### Beginner friendly issue backlog

**Criteria:** Are docs issues well-triaged?
**Analysis:** Are docs issues well-triaged?

**Criteria:** Is there a clearly marked way for new contributors to make code or documentation contributions (i.e. a "good first issue" label)?
**Analysis:** Is there a clearly marked way for new contributors to make code or documentation contributions (i.e. a "good first issue" label)?

**Criteria:** Are issues well-documented (i.e., more than just a title)?
**Analysis:** Are issues well-documented (i.e., more than just a title)?

**Criteria:** Are issues maintained for staleness?
**Analysis:** Are issues maintained for staleness?

### New contributor getting started content

**Criteria:** Do you have a community repository or section on your website?
**Analysis:** Do you have a community repository or section on your website?

**Criteria:** Is there a document specifically welcoming new contributors and documenting a first contribution process?
**Analysis:** Is there a document specifically for new contributors/your first contribution?

**Criteria:** Can new users find where to get help?
**Analysis:** Do new users know where to get help?

### Project governance documentation

**Criteria:** Is project governance clearly documented?
**Analysis:** Is project governance clearly documented?

## Website

### Single-source requirement

**Criteria:** Does the project have a single source for documentation? If not, is there a reason?
**Analysis:** (no corresponding question in analysis.md; the Single-source requirement section retains the explanatory description but lists no evaluation question)

### Minimal website requirements

**Criteria:** Are a majority of the Website guidelines satisfied? (Sandbox)
**Analysis:** (no corresponding question in analysis.md; minimal website requirements are presented as a maturity-level table rather than questions)

**Criteria:** Is there rudimentary project documentation, or a placeholder or substitute? (Sandbox)
**Analysis:** (no corresponding question in analysis.md)

**Criteria:** Are all Website guidelines satisfied? (Incubating)
**Analysis:** (no corresponding question in analysis.md)

**Criteria:** Has a Docs assessment or reassessment been requested through the CNCF service desk? (Incubating)
**Analysis:** (no corresponding question in analysis.md)

**Criteria:** Does project documentation meet these standards: stakeholders/personas identified and needs documented, hosted directly on the website, single-source requirement met, comprehensive? (Incubating)
**Analysis:** (no corresponding question in analysis.md)

**Criteria:** Are follow-through actions from the Docs assessment complete? (Graduated)
**Analysis:** (no corresponding question in analysis.md)

**Criteria:** Does project documentation fully address the needs of key stakeholders? (Graduated)
**Analysis:** (no corresponding question in analysis.md)

**Criteria:** Is the website repo in an archived state? (Archived)
**Analysis:** (no corresponding question in analysis.md; the analysis template covers only incubating and graduated levels)

**Criteria:** Is the archived status of the project obvious to those visiting the website, such as through the use of a prominent banner? (Archived)
**Analysis:** (no corresponding question in analysis.md)

**Criteria:** If a successor project exists, are there links to its website and/or migration documentation? (Archived)
**Analysis:** (no corresponding question in analysis.md)

### Usability, accessibility and devices

**Criteria:** Is the website usable from mobile?
**Analysis:** Is the website usable from mobile?

**Criteria:** Are doc pages readable?
**Analysis:** Are doc pages readable?

**Criteria:** Are all or most website features accessible from mobile -- such as the top-nav, site search, and in-page table of contents?
**Analysis:** Are all / most website features accessible from mobile -- such as the top-nav, site search and in-page table of contents?

**Criteria:** Might a mobile-first design make sense for your project?
**Analysis:** Might a mobile-first design make sense for your project?

**Criteria:** Are color contrasts significant enough for color-impaired readers?
**Analysis:** Are color contrasts significant enough for color-impaired readers?

**Criteria:** Are most website features usable using a keyboard only?
**Analysis:** Are most website features usable using a keyboard only?

**Criteria:** Does text-to-speech offer listeners a good experience?
**Analysis:** Does text-to-speech offer listeners a good experience?

### Branding

**Criteria:** Is there an easily recognizable brand for the project (logo, font, and color scheme) clearly identifiable?
**Analysis:** Is there an easily recognizable brand for the project (logo + color scheme) clearly identifiable?

**Criteria:** Is the brand used across the website consistently?
**Analysis:** Is the brand used across the website consistently?

**Criteria:** Is the website's typography clean and legible?
**Analysis:** Is the website's typography clean and well-suited for reading?

### Case studies/social proof

**Criteria:** Are there case studies available for the project and are they documented on the website?
**Analysis:** Are there case studies available for the project and are they documented on the website?

**Criteria:** Are there user testimonials available?
**Analysis:** Are there user testimonials available?

**Criteria:** Is there an active project blog?
**Analysis:** Is there an active project blog?

**Criteria:** Are there community talks for the project and are they present on the website?
**Analysis:** Are there community talks for the project and are they present on the website?

**Criteria:** Is there a logo wall of users/participating organizations?
**Analysis:** Is there a logo wall of users/participating organizations?

### SEO, Analytics and site-local search

**Criteria:** Is analytics enabled for the production server?
**Analysis:** Is analytics enabled for the production server?

**Criteria:** Is analytics disabled for all other deploys?
**Analysis:** Is analytics disabled for all other deploys?

**Criteria:** If your project used Google Analytics, have you migrated to GA4?
**Analysis:** If your project used Google Analytics, have you migrated to GA4?

**Criteria:** Can Page-not-found (404) reports easily be generated from you site analytics? Provide a sample of the site's current top-10 404s.
**Analysis:** Can Page-not-found (404) reports easily be generated from you site analytics? Provide a sample of the site's current top-10 404s.

**Criteria:** Is site indexing supported for the production server, while disabled for website previews and builds for non-default branches?
**Analysis:** Is site indexing supported for the production server, while disabled for website previews and builds for non-default branches?

**Criteria:** Is local intra-site search available from the website?
**Analysis:** Is local intra-site search available from the website?

**Criteria:** Are the current custodian(s) of the following accounts clearly documented: analytics, Google Search Console, site-search (such as Google CSE or Algolia)?
**Analysis:** Are the current custodian(s) of the following accounts clearly documented: analytics, Google Search Console, site-search (such as Google CSE or Algolia)?

### Maintenance planning

**Criteria:** Is your website tooling well supported by the community (i.e., Hugo with the Docsy theme) or commonly used by CNCF projects (our recommended tech stack)?
**Analysis:** Is your website tooling well supported by the community (i.e., Hugo with the Docsy theme) or commonly used by CNCF projects (our recommended tech stack)?

**Criteria:** Are you actively cultivating website maintainers from within the community?
**Analysis:** Are you actively cultivating website maintainers from within the community?

**Criteria:** Are site build times reasonable?
**Analysis:** Are site build times reasonable?

**Criteria:** Do site maintainers have adequate permissions?
**Analysis:** Do site maintainers have adequate permissions?

### Other

**Criteria:** Is your website accessible via HTTPS?
**Analysis:** Is your website accessible via HTTPS?

**Criteria:** Does HTTP access, if any, redirect to HTTPS?
**Analysis:** Does HTTP access, if any, redirect to HTTPS?

**Criteria:** Are links working and current? (Internal documentation, External documentation, External websites, Web applications)
**Analysis:** (no corresponding question in analysis.md)
