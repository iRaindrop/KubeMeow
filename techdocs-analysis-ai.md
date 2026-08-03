# TechDocs Analysis AI Prototyping

This document describes a structure of predefined prompt files for use in Copilot Enterprise in Visual Studio Code. The objective is to find optimal workflows to use AI output for TechDocs analysis of CNCF project documentation, contributor documentation, and website and infrastructure.

The location is the root directory in a GitHub repository of a CNCF project undergoing an analysis. [KubeVirt](https://kubevirt.io/user-guide/) is the project for this Analysis.

## Current process

Writers use the [Howto](https://github.com/cncf/techdocs/blob/main/docs/analysis/howto.md) document, along with the [Criteria](https://github.com/cncf/techdocs/blob/main/docs/analysis/criteria.md) specifications to create a report based on the [analysis.md](https://github.com/cncf/techdocs/blob/main/docs/analysis/templates/analysis.md) template.

The analysis template has three sections:
- Project Documentation
- Contributor Documentation
- Website and Infrastructure

Each section has a number of analysis areas, such as Information Architecture in Project Documentation. Each area has a group of questions, based on the Criteria specification, for the analysis writer to research and answer. The analysis template provides locations for the writer to add content in the following places:
- A comment overview for each section.
- Answers to criteria questions in each area.
- Recommendations for an area.

The template was designed to be flexible and can accommodate variances. The analysis writer can usually get a good understanding of how to complete the analysis within two to three weeks. Then it's a matter of meeting with the team to gather answers and feedback. The writer typically doesn't have enough information to complete the website and infrastructure section.

## AI involvement

## Template and automation

## Issues and concerns

