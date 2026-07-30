# KubeVirt User Guide: New User Content Answers

- Is "getting started" clearly labeled? ("Getting started", "Installation", "First steps", etc.)

    Partially. There is no page or navigation entry titled "Getting Started" or "First steps." New-user entry points are instead spread across a top-level "Quickstarts" item, an "Installation" page (the first page under Cluster Administration), and a "Try it out" section on the homepage. "Installation" is clearly labeled, but the absence of a single, consistently named getting-started landing page makes the on-ramp harder to find than a conventional "Getting Started" label would.

- Is installation documented step-by-step?

    Yes. `cluster_admin/installation.md` lists prerequisites and then provides copy-pasteable, ordered commands to deploy the KubeVirt operator, create the KubeVirt CR, wait for the components to become available, and verify the running pods. It also covers optional steps such as software emulation fallback and node-placement restrictions.

- If needed, are multiple OSes documented?

    Partially. Because KubeVirt is a Kubernetes add-on, the installation guide documents multiple Kubernetes platforms (Kubernetes, OKD, k3OS) and both the x86_64 and Arm64 architectures, rather than host operating systems. Host-OS-specific concerns are limited to AppArmor and SELinux notes. Separately, guest operating systems (for example Windows and Linux) are documented under User Workloads. There is no per-Linux-distribution installation walkthrough, which is reasonable for a cluster add-on but worth noting.

- Do users know where to go after reading the getting started guide?

    Partially. The installation page ends with optional topics (network plugins, node placement) rather than an explicit "Next steps" pointer to creating a first virtual machine. Users must navigate on their own to "User Workloads" (for example `basic_use.md` or `creating_vms.md`). Adding a clear "Next steps" link from installation to the first-VM tasks would close this gap.

- Is your new user content clearly signposted on your site's homepage or at the top of your information architecture?

    Yes. The homepage lists all major sections and includes prominent "Try it out," "KubeVirt Labs," and "Getting help" sections, and "Quickstarts" appears near the top of the navigation. However, much of this new-user content relies on external links (Killercoda, minikube/kind/cloud quickstarts, and the kubevirt.io labs) rather than in-guide getting-started material, so the signposting leads users off-site fairly quickly.

- Is there sample code or other example content that can easily be copy-pasted?

    Yes. The documentation makes extensive use of fenced and indented code blocks with ready-to-run examples, including installation shell commands, `virtctl create vm` invocations, `kubectl` lifecycle commands, and YAML manifests. These are formatted for direct copy-paste.
