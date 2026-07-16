---
title: Installing to disk
linktitle: Installing to disk
description: >
  How to install Flatcar Container Linux to a local disk with the
  flatcar-install script and provision it with Ignition on first boot.
weight: 40
aliases:
    - /docs/latest/installing/bare-metal/installing-to-disk/
    - ../../os/installing-to-disk
    - ../../bare-metal/installing-to-disk
---

This guide installs Flatcar Container Linux to a local disk with the [`flatcar-install`][flatcar-install] script and provisions it on first boot with Ignition. The example creates a `core` user with your SSH key and a systemd unit that runs an NGINX container.

`flatcar-install` destroys everything on the target disk: it downloads a release image, verifies its GPG signature, and writes it to disk bit for bit. Provisioning then runs on first boot, when Ignition reads the config you supply.

You cannot install to the disk you are currently booted from, so you boot a temporary Linux environment and install to a different, non-active disk. The target disk needs at least 8 GB of usable space.

## Prerequisites

### SSH key

Create an SSH key pair to log in to Flatcar as the `core` user:

```bash
ssh-keygen -t ed25519 -a 100 -f ~/.ssh/flatcar -C "flatcar-install"
cat ~/.ssh/flatcar.pub
```

You add the public key returned by `cat ~/.ssh/flatcar.pub` to the Butane config in Step 2.

### Butane

You need [Butane][butane] to transpile your YAML config into Ignition JSON. Install the `butane` binary from the [Butane releases][butane-releases], or run it with Docker or Podman as shown in Step 3.

### Dependencies for running flatcar-install

The Flatcar ISO and PXE images already include everything `flatcar-install` needs. If you run the script from another Linux distribution, make sure these binaries are present:

```text
bash
lbzip2 or bzip2
mount, lsblk        (util-linux)
wget
grep
cp, dd, mkfifo, mkdir, rm, tee   (GNU coreutils or busybox)
udevadm             (systemd-udev, or eudev on Alpine)
gpg, gpg2           (gnupg2)
gawk                (GNU gawk)
```

## Step 1: Boot a temporary environment

Boot the target machine into a temporary Linux environment and install to a disk other than the one it is running from. Choose one:

- **Flatcar ISO (AMD64)** — Write the [Flatcar ISO][flatcar-iso] to a USB drive and boot it. Requires at least 2 GB of RAM. The ISO does not support UEFI; boot in BIOS/legacy mode.
- **PXE** — Network-boot Flatcar. See [Booting with PXE][booting-with-pxe]. Requires at least 3 GB of RAM.
- **iPXE** — Network-boot Flatcar. See [Booting with iPXE][booting-with-ipxe]. Requires at least 3 GB of RAM.
- **Existing Linux system** — Boot any Linux distribution and install to a different disk than the one it booted from. Download the [`flatcar-install`][flatcar-install] script and run it from there.

The Flatcar ISO and PXE/iPXE environments already include `flatcar-install`. When you PXE-boot, the script installs the same channel and version you booted unless you override it.

Download ISO and PXE/iPXE images from the [Releases][releases] page.

## Step 2: Create the Butane config

Save the following as `cl.yaml`. Replace `<YOUR_SSH_PUBLIC_KEY>` with the full output of `cat ~/.ssh/flatcar.pub`, on one line including the key type and comment. Without an SSH key you will not be able to log in.

```yaml
variant: flatcar
version: 1.0.0
passwd:
  users:
    - name: core
      ssh_authorized_keys:
        - <YOUR_SSH_PUBLIC_KEY>
systemd:
  units:
    - name: nginx.service
      enabled: true
      contents: |
        [Unit]
        Description=NGINX example
        After=docker.service
        Requires=docker.service
        [Service]
        TimeoutStartSec=0
        ExecStartPre=-/usr/bin/docker rm --force nginx1
        ExecStart=/usr/bin/docker run --name nginx1 --pull always --log-driver=journald --net host docker.io/nginx:1
        ExecStop=/usr/bin/docker stop nginx1
        Restart=always
        RestartSec=5s
        [Install]
        WantedBy=multi-user.target
```

For a minimal install, keep only the `passwd` section with your SSH key and remove the `systemd` unit.

## Step 3: Transpile to Ignition JSON

Transpile `cl.yaml` into `ignition.json` with a local binary or a container:

```bash
# Local butane binary
butane --pretty --strict < cl.yaml > ignition.json

# Docker
docker run --rm -i quay.io/coreos/butane:latest --pretty --strict < cl.yaml > ignition.json

# Podman
podman run --rm -i quay.io/coreos/butane:latest --pretty --strict < cl.yaml > ignition.json
```

Verification: `ls ignition.json` shows the file. Make `ignition.json` available inside the temporary environment from Step 1 by copying it to the machine or a removable drive, or by hosting it on a URL.

## Step 4: Identify the target disk

In the temporary environment, list block devices and confirm the install target:

```bash
lsblk
```

Note the target device name, for example `sda`, `nvme0n1`, or `vda`.

**Warning:** `flatcar-install` overwrites the entire target disk. Confirm the device is the one you intend to erase before continuing.

## Step 5: Install Flatcar to disk

Run the installer with the target device and your Ignition config. Use `sudo` if you are not root:

```bash
sudo flatcar-install -d /dev/sda -i ignition.json
```

If you downloaded the script into the current directory, run `sudo ./flatcar-install -d /dev/sda -i ignition.json` instead.

The script downloads the image, verifies its GPG signature, and writes it to the disk.

By default the installer uses the same channel and version as the environment you booted. To pick a channel, add `-C`:

```bash
sudo flatcar-install -d /dev/sda -C stable -i ignition.json
```

On VMware, install the VMware-specific image with `-o vmware_raw`:

```bash
sudo flatcar-install -d /dev/sda -i ignition.json -o vmware_raw
```

Verification: the installer exits successfully after the download, verification, and write complete. See [Choosing a channel](#choosing-a-channel) and [Install options](#install-options) for more.

## Step 6: Reboot into Flatcar

Remove any ISO or USB boot media, then reboot into the installed system:

```bash
sudo reboot
```

Ignition runs on first boot and applies your config, creating the `core` user and starting the NGINX unit.

## Step 7: Log in via SSH

Find the machine's IP address from your router's DHCP leases, a serial console, or an attached monitor, then connect as `core`:

```bash
ssh -i ~/.ssh/flatcar core@MACHINE_IP
```

Verification: SSH opens a shell as the `core` user.

## Step 8: Verify the deployment

On the installed machine:

```bash
systemctl status nginx
curl http://localhost/
```

Verification: `systemctl status nginx` shows `active (running)` and `curl http://localhost/` returns the default NGINX page. This confirms that Ignition applied your config, the container image pulled, and the systemd unit started.

## Choosing a channel

Flatcar is [updated automatically][update-strategies] on a schedule that differs per channel. Read the [release notes][releases] for features and fixes. Select a channel with `-C`:

- **Stable** — For production clusters; promoted from Beta after testing. Current version {{< param stable_channel >}}.
- **Beta** — Promoted Alpha releases. Current version {{< param beta_channel >}}.
- **Alpha** — Tracks development closely and releases frequently. Current version {{< param alpha_channel >}}.

```bash
sudo flatcar-install -d /dev/sda -C stable   # or beta, alpha
```

Install a specific version or LTS stream with `-V`, for example `-V current-2022` for the LTS 2022 stream.

## Install options

```text
-d DEVICE   Install Flatcar Container Linux to the given device.
-s          EXPERIMENTAL: Install to the smallest unmounted disk found (min. 10GB).
            Use with -e or -I to filter block devices by major number, e.g. -e 7
            to exclude loop devices or -I 8,259 for certain disk types. See
            https://www.kernel.org/doc/Documentation/admin-guide/devices.txt.
-V VERSION  Version to install (e.g. current, or current-2022 for the LTS 2022 stream).
-B BOARD    Flatcar Container Linux board to use.
-C CHANNEL  Release channel to use (e.g. beta).
-I|e <M,..> EXPERIMENTAL (used with -s): major device numbers to in-/exclude.
-o OEM      OEM type to install (e.g. ami), using flatcar_production_<OEM>_image.bin.bz2.
-c CLOUD    Insert a cloud-init config to be executed on boot.
-i IGNITION Insert an Ignition config to be executed on boot.
-b BASEURL  URL to the image mirror (overrides BOARD and CHANNEL).
-k KEYFILE  Override default GPG key for verifying image signature.
-f IMAGE    Install unverified local image file to disk instead of fetching.
-n          Copy generated network units to the root partition.
-v          Super verbose, for debugging.
```

## Next steps

Your machine is installed and provisioned. Explore the [Quickstart][quickstart] or dig into [more specific topics][docs-root]. To learn what else you can configure at provisioning time, see the [Butane docs][butane] and [Butane spec][butane-spec]. For how first-boot provisioning works, see the [Flatcar startup process][boot-process].

[flatcar-install]: https://raw.githubusercontent.com/flatcar/init/flatcar-master/bin/flatcar-install
[flatcar-iso]: booting-with-iso
[booting-with-pxe]: booting-with-pxe
[booting-with-ipxe]: booting-with-ipxe
[releases]: https://www.flatcar.org/releases
[update-strategies]: ../../updates-releases/releases/update-strategies
[butane]: ../../fb-provision/butane
[butane-releases]: https://github.com/coreos/butane/releases
[butane-spec]: https://coreos.github.io/butane
[boot-process]: ../../fb-provision/ignition/boot-process
[quickstart]: ../../getting-started/quickstart
[docs-root]: ../../
