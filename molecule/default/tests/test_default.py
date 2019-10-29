#!/usr/bin/env python
"""Molecule test cases"""


import os

import testinfra.utils.ansible_runner

# pylint: disable=invalid-name
testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_bin_installed(host):
    """Tests that the exporter binary was installed properly"""
    host_file = host.file(
        '/usr/local/share/prometheus-pihole-exporter/pihole_exporter-linux-amd64'
    )
    assert host_file.is_file
    assert host_file.user == 'pi'
    assert host_file.group == 'pi'
    assert oct(host_file.mode) == '0755'


def test_service_installed(host):
    """Tests that the systemd service file was installed properly"""
    host_file = host.file(
        '/etc/systemd/system/prometheus-pihole-exporter.service'
    )
    assert host_file.is_file
    assert host_file.user == 'root'
    assert host_file.group == 'root'
    assert oct(host_file.mode) == '0644'
