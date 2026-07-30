# New User Content - Recommendations

The following recommendations address the New User Content of the KubeVirt user guide.

- Create a single, clearly named "Getting Started" section as its own top-level navigation item, and consolidate the currently scattered entry points—"Quickstarts," the "Installation" page, and the homepage "Try it out" and "KubeVirt Labs" sections—beneath it so new users have one obvious front door. The Falco getting-started guide (https://falco.org/docs/getting-started/) is a good structural model.
- Move or surface the "Installation" page out of "Cluster Administration" and into the new "Getting Started" section so newcomers do not have to locate it under an administration heading.
- Add a self-contained, end-to-end tutorial that carries a reader from a fresh cluster through deploying KubeVirt to launching and accessing a first virtual machine, reducing reliance on external resources such as Killercoda, the minikube/kind/cloud quickstarts, and the kubevirt.io labs.
- Add an explicit "Next steps" call-to-action at the end of the installation page that links directly to the first-VM tasks in "User Workloads" (for example, `basic_use.md` and `creating_vms.md`), so users have an unbroken path from setup to a running workload.
- Keep the strong installation content as-is—the ordered, copy-pasteable operator and CR commands, the deployment-verification steps, and the coverage of multiple platforms (Kubernetes, OKD, k3OS) and architectures (x86_64 and Arm64)—while integrating it into the consolidated getting-started flow.
- Clarify the operating-system scope of the installation guide by briefly noting that KubeVirt is a Kubernetes add-on, distinguishing host-OS concerns (AppArmor, SELinux) from guest operating systems documented under "User Workloads," so users understand why there is no per-distribution installation walkthrough.
- Continue providing ready-to-run, copy-pasteable examples—installation shell commands, `virtctl create vm` invocations, `kubectl` lifecycle commands, and YAML manifests—and ensure any new getting-started tutorial follows the same copy-paste-friendly formatting.
- When linking to external quickstarts and labs, frame them as optional supplements alongside the in-guide walkthrough rather than the primary path, so new users are not sent off-site before achieving a first success within the guide.
