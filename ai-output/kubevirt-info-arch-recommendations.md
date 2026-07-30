# Information architecture recommendations

The following recommendations address the information architecture of the KubeVirt user guide.

- Add a single, consolidated troubleshooting and FAQ entry point, organized by symptom, that links out to the relevant pages in the Virtualization Debugging section and to the scattered debugging notes on individual feature pages. This gives users a predictable escalation path when a task page alone does not resolve their issue.
- Preserve the current overall structure rather than reorganizing it. The domain-based sections (cluster administration, user workloads, compute, network, storage) and explicit per-section navigation order are sound; focus effort on incremental additions instead of a restructure.
- Surface an explicit, in-guide learning path for new users. Add a clearly labeled "Tutorials" grouping that frames the existing external labs and quickstarts (Killercoda, minikube, kind, cloud providers) so hands-on content is discoverable without leaving the guide.
- Cross-link the API reference from the task pages that use each resource. Link specific custom resources and fields (for example, from live migration, instance types, and storage pages) to their entries at kubevirt.io/api-reference so instructions connect directly to reference material.
- Normalize the minority of noun-based topic headings into goal-oriented verb or gerund phrases, matching the existing style of headings such as "Creating VirtualMachines on a cluster" and "Enabling the live-migration support." This improves scannability and consistency across pages.
- Audit task coverage depth against recent release notes. Confirm that each newer feature (for example, those introduced through v1.8.0) has a corresponding end-to-end, goal-oriented task page, not just a conceptual or configuration-field description.
- Separate concept from procedure on pages that currently interleave them, such as the migration strategies and some networking topics, so readers can extract the steps without reading through surrounding explanation.
- Periodically verify that inline examples, command output, and feature-gate names match the latest release, since features graduate through alpha, beta, and GA over time and can drift from the documented behavior.
