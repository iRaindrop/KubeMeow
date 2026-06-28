---
title: "Flatcar Developer Guide & Migration"
type: concept
sources:
  - raw/topics/flatcar/content/docs/latest/devguide/
  - raw/topics/flatcar/content/docs/latest/coreos-migration/
  - raw/topics/flatcar/content/docs/latest/getting-started/learning-series/
related:
  - "[[flatcar-overview]]"
  - "[[flatcar-deploy]]"
  - "[[flatcar-security]]"
created: 2026-06-27
updated: 2026-06-27
confidence: high
---

# Flatcar Developer Guide & Migration

Source sections: `devguide/` (renamed from `reference/developer-guides/` in main branch), `coreos-migration/` (renamed from `migrating-from-coreos/`), and `getting-started/learning-series/`.

## SDK and Developer Guides (`devguide/`)

The Flatcar SDK is a container-based build environment for building and modifying Flatcar OS images.

| Guide | Topic |
|---|---|
| `sdk-bootstrapping` | Setting up the build environment |
| `sdk-modifying-flatcar` | Patching packages, overlays |
| `sdk-building-production-images` | Full image build pipeline |
| `sdk-disk-partitions` | Partition layout, GUIDs, USR-A/B scheme |
| `sdk-tips-and-tricks` | Common development patterns |
| `kernel-modules` | Building and loading out-of-tree kernel modules |
| `release-guide` | Cutting a new Flatcar release |
| `integrations` | Ansible, Terraform, Packer, and other integrations |

**Disk partition layout:**

| Partition | Purpose |
|---|---|
| EFI System Partition | GRUB bootloader; `flatcar/first_boot` flag file |
| USR-A | Active OS image (`/usr`) |
| USR-B | Standby OS image (updates written here) |
| ROOT-A | Active root filesystem |
| ROOT-B | Standby root filesystem |
| OEM | OEM vendor tools (as sysext images since 3760.0.0) |

## Self-Paced Learning Series (`getting-started/learning-series/`)

Four in-depth sessions:

| Session | Topic | Prerequisites |
|---|---|---|
| Basics and Testing | Local test environment, first Butane config, QEMU VM | None |
| Advanced Provisioning | Complex deployments, node config management | Session 1 |
| Managing Storage | Additional storage, LUKS encryption at rest | Session 1 |
| Immutability, Updates, Rollbacks | Boot process deep dive, in-place upgrades, automated rollbacks, channels | Sessions 1–2 |

## Migrating from CoreOS Container Linux (`coreos-migration/`)

Flatcar is a drop-in replacement. Key naming changes:

| Area | CoreOS | Flatcar |
|---|---|---|
| Installer | `coreos-installer` | `flatcar-installer` |
| First-boot flag | `coreos.first_boot=1` | `flatcar.first_boot=1` |
| Config URL | `coreos.config.url=URL` | `ignition.config.url=URL` |
| OEM ID | `coreos.oem.id=NAME` | `flatcar.oem.id=NAME` |
| QEMU fw_cfg | `opt/com.coreos/config` | `opt/org.flatcar-linux/config` |
| VMware guestinfo | `coreos.config.data` | `ignition.config.data` |
| First-boot flag file | `/boot/coreos/first_boot` | `/boot/flatcar/first_boot` |

Both `coreos.*` and `flatcar.*` kernel parameters are supported in current releases.

**In-place update from CoreOS CL:**
```sh
# Run on each CoreOS node
sudo /usr/share/oem/flatcar-update.sh
```

See `coreos-migration/update-from-container-linux.md` for the full procedure including verifying the update server, validating image signatures, and handling rollback if the migration fails.

## Roadmap and Future Work (`getting-started/roadmap.md`)

The roadmap file tracks planned Flatcar features and improvements. Key areas as of the `expert-support-refactor` branch:
- Further modularization of the base image via sysext
- Improvements to Nebraska OEM payload delivery
- Additional security hardening toward SLSA Level 4

## Flatware Apps (`getting-started/flatware-apps.md`)

Example applications and reference configs for Flatcar Container Linux deployments. Stub file in this branch — content to be added.
