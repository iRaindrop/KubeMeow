# KubeVirt User Guide: Inclusive Language Recommendations

The following recommendations address the inclusive language of the KubeVirt user guide.

- Replace subjective minimizing qualifiers such as "simple", "simply", "easy", "easily", and "just" with concrete, factual descriptions—for example, state the number of steps, name the single command involved, or remove the adjective entirely.
- Preserve legitimate proper nouns and identifiers when revising, such as the passt project's "Plug A Simple Socket Transport", the "PCI Simple" Windows device, and example resource names like `simple-vm` and `simple-dv`.
- Add the flagged minimizing terms to the existing yaspeller-based checks, or adopt a dedicated inclusive-language linter such as an `alex` or Vale style rule in CI, to automate detection and keep new contributions consistent.
- Leave the "master" occurrences unchanged, since they appear only in contexts the project does not own—external URLs and Git branch names, API reference version paths, a third-party CNI bonding field, a Kubernetes node-label example, and verbatim QEMU/libvirt command output.
- Maintain the strong naming foundation by continuing to avoid non-recommended terms from the Inclusive Naming Initiative in any new KubeVirt-defined utilities, endpoints, class names, or feature names.
