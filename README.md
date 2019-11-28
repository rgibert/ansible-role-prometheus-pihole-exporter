# Prometheus PiHole Exporter

![Ansible Role](https://img.shields.io/ansible/role/44974?style=flat-square)
![Molecule Test Status](https://img.shields.io/travis/rgibert/ansible-role-prometheus-pihole-exporter?label=molecule&style=flat-square)
![Ansible Quality Score](https://img.shields.io/ansible/quality/44974?style=flat-square)
![Ansible Role](https://img.shields.io/ansible/role/d/44974?label=downloads&style=flat-square)

## Description

Installs eko/pihole_exporter for Prometheus

## Requirements

- RHEL or Debian-based OSes

## Role Variables

| Variable | Description |
|----------|-------------|
| prometheus_pihole_exporter_base_url Base URL for other variables |
| prometheus_pihole_exporter_dl_url | Tarball download URL |
| prometheus_pihole_exporter_bin | Exporter binary |
| prometheus_pihole_exporter_full_bin | Full path to exporter binary |
| prometheus_pihole_exporter_version | Version to install |
| prometheus_pihole_exporter_user | User to run the exporter as |
| prometheus_pihole_exporter_group | Default group for the user to run as |
| prometheus_pihole_exporter_checksum | SHA256 URL for tarball |

## Dependencies

- Ansible Roles:
  - rgibert.user_setup
  - rgibert.single_binary_setup

## Example Playbook

```yaml
- hosts:
    - servers
  roles:
    - role: rgibert.prometheus_pihole_exporter
      prometheus_pihole_exporter_version: 0.0.6
```

## License

GPLv3

## Author Information

Richard Gibert  
[richard@gibert.ca](mailto:richard@gibert.ca)  
[https://richard.gibert.ca/](https://richard.gibert.ca/)
