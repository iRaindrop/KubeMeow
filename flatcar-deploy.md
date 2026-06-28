---
title: "Flatcar Deployments"
type: concept
sources:
  - raw/topics/flatcar/content/docs/latest/deploy/
related:
  - "[[flatcar-overview]]"
  - "[[flatcar-provisioning]]"
  - "[[flatcar-devguide]]"
  - "[[kubevirt-virtual-machine]]"
created: 2026-06-27
updated: 2026-06-27
confidence: high
---

# Flatcar Deployments

Source section: `deploy/` (renamed from `installing/` in the refactored branch). Covers cloud providers, virtualization platforms, and bare metal.

## Cloud Providers (`deploy/cloud/`)

| Provider | Support |
|---|---|
| Amazon EC2 | Official |
| Microsoft Azure | Official |
| Google Compute Engine | Official |
| VMware | Official |
| Hetzner | Official |
| DigitalOcean | Official |
| Akamai/Linode | Official |
| STACKIT | Official |
| Brightbox | Official |
| Exoscale | Community |
| Scaleway | Community (moved to `virt-options/` in this branch) |
| OracleCloud | Community (moved to `virt-options/`) |
| OVHcloud | Community (moved to `virt-options/`) |
| Vultr | Community (new in this branch) |

Ignition/Butane config is passed via the provider's **user data** / **custom data** field at instance creation.

## Virtualization Options (`deploy/virt-options/`)

In the refactored branch, `virt-options/` consolidates VMs and some community platforms that were split across `installing/vms/` and `installing/community-platforms/` in main:

| Platform | Support |
|---|---|
| QEMU/KVM | Official |
| libvirt | Official |
| KubeVirt | Community |
| Hyper-V | Community |
| VirtualBox | Community |
| Vagrant | Community |
| Proxmox VE | Community |
| OpenStack | Community (moved from cloud/ in this branch) |
| Eucalyptus | Community |

### KubeVirt (`deploy/virt-options/kubevirt.md`)

KubeVirt images are `qcow2` format for both `amd64` and `arm64`, available from Alpha 3975.0.0.

**Download:**
```bash
wget https://alpha.release.flatcar-linux.net/amd64-usr/3975.0.0/flatcar_production_kubevirt_image.qcow2
```

**Upload via virtctl:**
```bash
virtctl image-upload pvc flatcar-production-kubevirt-image --size=10Gi \
  --image-path=flatcar_production_kubevirt_image.qcow2 \
  --uploadproxy-url https://cdi-uploadproxy:31001 --insecure
```

**Or via PVC with CDI import annotation:**
```yaml
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: flatcar-amd64-3975
  annotations:
    cdi.kubevirt.io/storage.import.endpoint: "https://alpha.release.flatcar-linux.net/amd64-usr/3975.0.0/flatcar_production_kubevirt_image.qcow2"
spec:
  accessModes: [ReadWriteOnce]
  resources:
    requests:
      storage: 10Gi
  storageClassName: ceph-block
```

**VM with cloud-init userdata:**
```yaml
apiVersion: kubevirt.io/v1
kind: VirtualMachine
metadata:
  name: vm-flatcar-cfgdrive
spec:
  running: true
  template:
    spec:
      domain:
        cpu: {cores: 1}
        devices:
          disks:
          - {disk: {bus: virtio}, name: disk0}
          - {disk: {bus: sata}, name: cloudinitdisk}
        resources:
          requests: {memory: 1024M}
      volumes:
      - name: disk0
        persistentVolumeClaim:
          claimName: flatcar-amd64-3975
      - cloudInitConfigDrive:
          userData: |
            #!/bin/bash
            echo "core:foo" | chpasswd
        name: cloudinitdisk
```

**VM with Ignition userdata** (generate JSON from Butane first):
```bash
butane < userdata.yaml > userdata.json
```
```yaml
# userdata.yaml (Butane)
variant: flatcar
version: 1.0.0
kernel_arguments:
  should_exist:
    - flatcar.autologin
passwd:
  users:
    - name: core
      password_hash: $6$...hash...
```
Then embed the JSON output as `cloudInitConfigDrive.userData` in the VirtualMachine spec using a `cdrom` disk (not `disk`).

Both cloud-init and Ignition are supported via `cloudInitConfigDrive`. KubeVirt is community-supported — no official release tests run for it.

## Bare Metal (`deploy/bare-metal/`)

| Method | Notes |
|---|---|
| ISO | Boot and install interactively |
| PXE | Network boot; must add `flatcar.first_boot=1` to kernel args |
| iPXE | Network boot via HTTP |
| `flatcar-install` | Run on existing Linux system to install to disk |
| Raspberry Pi | ARM64 support |

**PXE requirement:** Since GRUB is not used, set `flatcar.first_boot=1` explicitly in kernel cmdline — do not use `detected`.

For bare metal metadata provisioning, use [Matchbox](https://matchbox.psdn.io/).

## Notes for Distributors (`deploy/virt-options/notes-for-distributors.md`)

Covers Flatcar-specific considerations for platform vendors building images or integrations, including OEM partition usage and update server requirements.
