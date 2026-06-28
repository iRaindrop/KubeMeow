---
title: "Flatcar Container Linux Overview"
type: concept
sources:
  - raw/topics/flatcar/content/_index.md
  - raw/topics/flatcar/content/faq.md
  - raw/topics/flatcar/content/docs/latest/_index.md
  - raw/topics/flatcar/content/docs/latest/getting-started/
related:
  - "[[flatcar-provisioning]]"
  - "[[flatcar-deploy]]"
  - "[[flatcar-os-config]]"
  - "[[flatcar-orchestrate]]"
  - "[[flatcar-security]]"
  - "[[flatcar-updates]]"
  - "[[flatcar-diagnostics]]"
  - "[[flatcar-devguide]]"
created: 2026-06-27
updated: 2026-06-27
confidence: high
---

# Flatcar Container Linux Overview

Flatcar Container Linux is a minimal, immutable, container-optimized Linux OS and the active successor to CoreOS Container Linux (EOL 2020). It is a CNCF project. The name comes from the flat railcar used to transport shipping containers.

## Five Core Tenets

| Tenet | Description |
|---|---|
| **Immutable & image-based** | `/usr` is read-only and dm-verity protected. No package manager. Updates replace all OS binaries atomically including kernel and initrd. |
| **Minimal & container-optimized** | Ships only Docker, containerd, and basic node tools. Applications run as containers or systemd-sysext images. |
| **Fully automated** | Declarative Ignition/Butane config applied once at first boot. No configuration drift. |
| **Tested & self-updating** | 100+ automated scenario tests. Atomic A/B updates with rollback. No Beta with known issues ever transitions to Stable. |
| **Community stewarded** | CNCF project. Multi-employer maintainers. Not vendor driven. |

## Update Mechanism

Flatcar uses the **USR-A / USR-B** dual-partition scheme (same as ChromeOS). One partition is active, the other is standby. Updates apply to the standby partition; a reboot switches to it. Boot failure automatically falls back to the previous partition.

**Update channels:**

| Channel | Cadence | Support |
|---|---|---|
| Alpha | Frequent | Community |
| Beta | ~2 months | Community |
| Stable | ~2 months | Community / Pro |
| LTS | 12 months | 18 months (commercial) |

## Documentation Map

| Wiki Page | Source Section | Coverage |
|---|---|---|
| [[flatcar-provisioning]] | `fb-provision/`, `sys-ext/` | Ignition, Butane, CLC, sysext, Terraform |
| [[flatcar-deploy]] | `deploy/` | Cloud, VMs (KubeVirt, QEMU), bare metal |
| [[flatcar-os-config]] | `os-config/` | Network, storage, systemd, host config |
| [[flatcar-orchestrate]] | `orchestrate/` | Docker, Kubernetes, clusters |
| [[flatcar-security]] | `security/` | Encryption, hardening, cert auth |
| [[flatcar-updates]] | `updates-releases/` | Nebraska, release channels, update strategies |
| [[flatcar-diagnostics]] | `diagnostics/` | Toolbox, logs, btrfs, rollback |
| [[flatcar-devguide]] | `devguide/`, `coreos-migration/` | SDK, supply chain, CoreOS migration |

## Getting Started

**Quickstart (local QEMU test):**

```bash
# Download image and launch script
wget https://stable.release.flatcar-linux.net/amd64-usr/current/flatcar_production_qemu.sh
chmod +x flatcar_production_qemu.sh
wget https://stable.release.flatcar-linux.net/amd64-usr/current/flatcar_production_qemu_image.img

# Keep a pristine copy for re-provisioning
mv flatcar_production_qemu_image.img flatcar_production_qemu_image.img.fresh
cp --reflink=auto flatcar_production_qemu_image.img.fresh flatcar_production_qemu_image.img

# Boot with a Butane-generated Ignition config
./flatcar_production_qemu.sh -i ignition.json
ssh -p 2222 core@127.0.0.1
```

**Provisioning flow:**
```
Butane YAML  →  butane transpile  →  Ignition JSON  →  passed as userdata  →  applied at first boot
```

## Flatcar vs CoreOS Container Linux

Drop-in replacement. Key naming changes:

| CoreOS | Flatcar |
|---|---|
| `coreos.first_boot=1` | `flatcar.first_boot=1` |
| `coreos.config.url` | `ignition.config.url` |
| `coreos.oem.id` | `flatcar.oem.id` |
| `coreos-installer` | `flatcar-installer` |

Both naming conventions are supported in current releases during migration.

## Community

- Slack: `#flatcar` in Kubernetes Slack
- Discord: https://discord.gg/PMYjFUsJyq
- GitHub: https://github.com/flatcar
