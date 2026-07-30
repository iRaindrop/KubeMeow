# KubeVirt information architecture answers

These answers evaluate the information architecture of the [KubeVirt user guide](https://kubevirt.io/user-guide) against the CNCF TechDocs information architecture criteria.

## Is there high level conceptual/"About" content? Is the documentation feature complete? (i.e., each product feature is documented)

Yes. The guide provides high-level conceptual content. The [Architecture](docs/architecture.md) page gives a technical and conceptual overview of the KubeVirt components, the service-oriented design, and the layered virtualization stack, and the Welcome page introduces each major section of the guide.

The documentation is broadly feature complete. Major product areas each have dedicated sections: cluster administration, user workloads, compute, network, and storage. Individual features such as live migration, CPU and memory hotplug, hugepages, NUMA, instance types and preferences, snapshots, volume export, and network binding plugins each have their own pages. Coverage is wide enough that most shipped features have at least a conceptual description.

## Are there step-by-step instructions (tasks, tutorials) documented for features?

Yes. Most feature pages include step-by-step instructions with copy-pastable shell and YAML examples. For example, the [live migration](docs/compute/live_migration.md) page walks through enabling the feature, initiating and canceling a migration, and configuring a dedicated migration network, and the [creating VirtualMachines](docs/user_workloads/creating_vms.md) page shows how to build manifests with `virtctl`.

For tutorials, the guide links out to external interactive labs and quickstarts (Killercoda, minikube, kind, and cloud providers) from both the Welcome and Quickstarts pages rather than hosting long-form tutorials inline. This keeps hands-on learning paths available, though they live outside the user guide itself.

## Are there any key features which are documented but missing task documentation?

Some pages lean conceptual or reference-oriented and would benefit from added task steps, but there are no major features that are described without any actionable guidance. A few areas mix concept and procedure heavily (for example, migration strategies and some networking topics), where a reader must extract the steps from surrounding explanation.

The most common gap is depth rather than absence: certain advanced features document the "what" and configuration fields well but provide fewer end-to-end, goal-oriented walkthroughs. Reviewers should confirm that newer features listed in recent release notes each have a corresponding task page.

## Is the "happy path"/most common use case documented? Does task and tutorial content demonstrate atomicity and isolation of concerns? (Are tasks clearly named according to user goals?)

Yes. The happy path is documented. A new user can follow installation, then create and access a virtual machine, which covers the most common use case. The quickstarts and labs reinforce this path for first-time users.

Task content generally demonstrates atomicity and isolation of concerns, and headings are largely named according to user goals using verb or gerund phrases, such as "Creating VirtualMachines on a cluster", "Enabling the live-migration support", "Initiate live migration", and "Configuring a migration network on a cluster". This makes individual tasks easy to scan and follow. A minority of headings are noun-based topic labels rather than goal phrases, so naming is strong but not fully consistent.

## If the documentation does not suffice, is there a clear escalation path for users needing more help? (FAQ, Troubleshooting)

Yes. The Welcome page provides a "Getting help" section that links to filing bugs on GitHub, the kubevirt-dev mailing list, and the community Slack channel, giving users a clear escalation path.

There is also a dedicated Virtualization Debugging section covering log verbosity, privileged node debugging, virsh commands, and running QEMU under strace or gdb, and several feature pages include debugging notes. However, there is no single, consolidated FAQ or troubleshooting landing page, so common problems and their fixes are spread across individual pages rather than centralized.

## If the product exposes an API, is there a complete reference?

Yes. KubeVirt exposes a Kubernetes-style API, and the Welcome page links to the generated API reference at kubevirt.io/api-reference, which provides a complete, versioned reference for the custom resources and fields.

Because the reference is generated from source and hosted separately from the user guide, it stays current with releases but is one click removed from the task content. Cross-linking specific fields from task pages to the reference would tighten the connection between instructions and reference material.

## Is content up to date and accurate?

Yes. The content is current. The release notes document releases through v1.8.0 (released March 2026, built for Kubernetes v1.35), and feature pages reference current resources, feature gates, and `virtctl` subcommands consistent with recent releases.

Accuracy appears high overall, with concrete command output and manifests shown inline. As with any fast-moving project, reviewers should periodically verify that examples and feature-gate names match the latest release, since some pages describe features that graduate through alpha, beta, and GA over time.

## Restructure evaluation

False. A restructure of the content is not needed. The information architecture is sound: content is organized into clear conceptual, task, and reference layers, navigation order is deliberately controlled per section, and features are grouped logically by domain (cluster administration, user workloads, compute, network, storage). Improvements should focus on incremental additions — a consolidated troubleshooting/FAQ entry point, tighter cross-linking to the API reference, and more consistent goal-oriented headings — rather than reorganizing the existing structure.
