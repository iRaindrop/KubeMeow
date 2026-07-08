---
title: Quickstart
weight: 5
description: >
  Get up and running quickly with Flatcar Container Linux.
---

This quickstart shows how to provision a local Flatcar VM with a Butane config that is transpiled to Ignition. Ignition is Flatcar's first-boot provisioning system: it applies your machine configuration when the VM starts from a fresh image.

As a practical example, you will define a systemd unit that starts an NGINX container. systemd is the Linux init and service manager, and NGINX is a common web server, so this gives you a simple way to verify that provisioning worked and a solid base for further experiments.

## Prerequisites

### Butane

Butane transforms a user-provided Butane configuration into an Ignition configuration. Download and install the release binary from the [CoreOS Butane Releases](https://github.com/coreos/butane/releases).

Linux users can run this one-line command to auto-detect the architecture, download the latest Butane release, install it, and print the version.

```bash
ARCH=$(uname -m); case "$ARCH" in x86_64|amd64) BIN=butane-x86_64-unknown-linux-gnu ;; aarch64|arm64) BIN=butane-aarch64-unknown-linux-gnu ;; *) echo "Unsupported architecture: $ARCH"; exit 1 ;; esac; VER=$(curl -fsSLI -o /dev/null -w '%{url_effective}' https://github.com/coreos/butane/releases/latest | sed 's#.*/tag/##'); curl -fL "https://github.com/coreos/butane/releases/download/$VER/$BIN" -o /tmp/butane && chmod +x /tmp/butane && sudo mv /tmp/butane /usr/local/bin/butane && butane --version
```

### QEMU

QEMU is a generic and open source machine emulator and virtualizer. For installation instructions, see [Running on QEMU](https://www.flatcar.org/docs/latest/installing/vms/qemu/).

### Container runtime

The command used later to transpile Butane (`docker run ...`) requires a local container runtime such as Docker or Podman.

### Flatcar image

Use AMD64 for standard PCs and laptops (Intel or AMD processors) and Linux. Use ARM64 for ARM-based hardware such as Raspberry Pi, AWS Graviton, or Apple Silicon (M1/M2/M3) for macOS.

All command examples below use the AMD64 wrapper script by default. If you are using ARM64, replace `flatcar_production_qemu.sh` with `flatcar_production_qemu_uefi.sh` and use the ARM64 image filenames.

#### AMD64 image

```bash
wget https://stable.release.flatcar-linux.net/amd64-usr/current/flatcar_production_qemu.sh
chmod +x flatcar_production_qemu.sh
wget https://stable.release.flatcar-linux.net/amd64-usr/current/flatcar_production_qemu_image.img
```

#### ARM64 image

```bash
wget https://alpha.release.flatcar-linux.net/arm64-usr/current/flatcar_production_qemu_uefi.sh
chmod +x flatcar_production_qemu_uefi.sh
wget https://alpha.release.flatcar-linux.net/arm64-usr/current/flatcar_production_qemu_uefi_image.img
wget https://alpha.release.flatcar-linux.net/arm64-usr/current/flatcar_production_qemu_uefi_efi_vars.qcow2
wget https://alpha.release.flatcar-linux.net/arm64-usr/current/flatcar_production_qemu_uefi_efi_code.qcow2
```

### SSH keys

You need an SSH key pair to log in as the `core` user. If you do not already have one, generate a dedicated key for this VM:

```bash
ssh-keygen -t ed25519 -a 100 -f ~/.ssh/flatcar_qemu -C "flatcar-qemu"
cp ~/.ssh/flatcar_qemu.pub ~/.ssh/flatcar_authorized_keys
```

When launching the VM, pass the key file with `-a` so the wrapper script injects it:

```bash
./flatcar_production_qemu.sh -a ~/.ssh/flatcar_authorized_keys -- -nographic
```

ARM64 (UEFI) equivalent:

```bash
./flatcar_production_qemu_uefi.sh -a ~/.ssh/flatcar_authorized_keys -- -nographic
```

Notes:

- `ssh-kgen` is a typo; the correct command is `ssh-keygen`.
- Wrapper script options like `-a` must come before QEMU options (or before `--` if used).
- If you prefer default key autodetection, the wrapper also checks keys from `ssh-agent` and standard public key paths.


You can already boot the image with `./flatcar_production_qemu.sh` and have a look around in the OS through the QEMU VGA console. You can close the QEMU window or stop the script with `Ctrl-C`.

```bash
mv flatcar_production_qemu_image.img flatcar_production_qemu_image.img.fresh

# If you want to have a first look, boot it and wait for the auto-login prompt:

cp -i --reflink=auto flatcar_production_qemu_image.img.fresh flatcar_production_qemu_image.img
./flatcar_production_qemu.sh -a ~/.ssh/flatcar_authorized_keys
```

ARM64 (UEFI) equivalent:

```bash
mv flatcar_production_qemu_uefi_image.img flatcar_production_qemu_uefi_image.img.fresh
cp -i --reflink=auto flatcar_production_qemu_uefi_image.img.fresh flatcar_production_qemu_uefi_image.img
./flatcar_production_qemu_uefi.sh -a ~/.ssh/flatcar_authorized_keys
```

## Provision with Butane and Ignition

Now we will provision the VM on first boot through Ignition. Instead of writing the JSON config, we use Butane YAML and transpile it. Save the following Butane YAML file as `cl.yaml` (or another name). It contains directives for setting up a systemd service that runs an NGINX Docker container:

```yaml
variant: flatcar
version: 1.0.0
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

Before we can use it, we have to transpile the Butane YAML to Ignition JSON:

```bash
docker run --rm -i quay.io/coreos/butane:latest < cl.yaml > ignition.json
```

You can also skip this step and copy the resulting JSON file shown below to `ignition.json` (or another name):

```json
{
  "ignition": {
    "version": "3.3.0"
  },
  "systemd": {
    "units": [
      {
        "contents": "[Unit]\nDescription=NGINX example\nAfter=docker.service\nRequires=docker.service\n[Service]\nTimeoutStartSec=0\nExecStartPre=-/usr/bin/docker rm --force nginx1\nExecStart=/usr/bin/docker run --name nginx1 --pull always --log-driver=journald --net host docker.io/nginx:1\nExecStop=/usr/bin/docker stop nginx1\nRestart=always\nRestartSec=5s\n[Install]\nWantedBy=multi-user.target\n",
        "enabled": true,
        "name": "nginx.service"
      }
    ]
  }
}
```

The final step is to boot the VM and make the Ignition configuration available to it. Provisioning only runs on first boot, so if you want an updated Ignition configuration to be applied, boot from a fresh copy of the image. You can repeat these combined steps as often as you want to test your Ignition changes.

## Boot with a fresh copy

AMD64:

```bash
cp -i --reflink=auto flatcar_production_qemu_image.img.fresh flatcar_production_qemu_image.img
./flatcar_production_qemu.sh -a ~/.ssh/flatcar_authorized_keys -i ignition.json
```

ARM64 (UEFI):

```bash
cp -i --reflink=auto flatcar_production_qemu_uefi_image.img.fresh flatcar_production_qemu_uefi_image.img
./flatcar_production_qemu_uefi.sh -a ~/.ssh/flatcar_authorized_keys -i ignition.json
```

## Log in via SSH in a new terminal

```bash
ssh -i ~/.ssh/flatcar_qemu -o IdentitiesOnly=yes -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null -p 2222 core@127.0.0.1
```

If you launch QEMU with a custom SSH forward port (for example `-p 2224`), use that port in the SSH command.

If you recreate the VM and see a host key mismatch warning, clear the old entry and retry:

```bash
ssh-keygen -R [127.0.0.1]:2222
```

## Check that NGINX is running

Run these commands in the VM shell (after logging in over SSH):

```bash
systemctl status nginx

curl http://localhost/
```

{{< note >}}
For SSH access, you can also use the `~/.ssh/config` provided in the QEMU section then simply `ssh flatcar` or `scp my-file flatcar:/home/core` to send a file on the instance over SSH.
{{< /note >}}

If you have trouble SSHing into the VM, your QEMU wrapper script might have failed to auto-detect your SSH key. If that happens, try a user-supplied SSH key using the YAML snippet below. Alternatively, you can interact with the VGA console; the console has auto-login enabled and drops right into a shell.

You can reboot and stop the VM if you like. When you start it later with a plain `./flatcar_production_qemu.sh` (or `./flatcar_production_qemu_uefi.sh` on ARM64), the systemd unit will start NGINX on each boot. Note that the Ignition config is only processed on the very first boot; that is why we made a copy, so you can restore the OS image from the pristine copy for successive experiments with Butane.

As listed in the introduction above, there are numerous options available for configuring Flatcar just the way you need it. For instance, you can specify a custom SSH key instead of your default one from your SSH agent or from `~/.ssh/` in the Butane config by adding this section to your YAML file:

```yaml
variant: flatcar
version: 1.0.0
passwd:
  users:
    - name: core
      ssh_authorized_keys:
        - ssh-rsa AAAAB......xyz email@host.net
```

Afterwards, transpile it again to Ignition JSON, overwrite your active image file with the corresponding `.fresh` image file, and pass the Ignition config to the same wrapper script (`flatcar_production_qemu.sh` for AMD64, `flatcar_production_qemu_uefi.sh` for ARM64) once again.

## Quick Iterations with QEMU

When you boot the image file and apply the Ignition config, the image is set. You would have to reprovision the image to have a new state. However, you can take advantage of the QEMU `-snapshot` flag that starts up the image but does not save the changes to the image file. This can be useful if you want to quickly reprovision locally, without having to keep swapping the underlying image file to a fresh one.

Here are examples of the syntax needed to use this flag:

AMD64:

```bash
./flatcar_production_qemu.sh -i config.ign -- -snapshot -m 4096
```

ARM64 (UEFI):

```bash
./flatcar_production_qemu_uefi.sh -i config.ign -p 2224 -- -snapshot -m 4096
```

See the [QEMU documentation](https://www.qemu.org/docs/master/system/qemu-manpage.html) for more information.

