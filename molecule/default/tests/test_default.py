import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_bin_installed(host):
    f = host.file('/usr/local/share/prometheus-pihole-exporter/pihole_exporter-linux-amd64')
    assert f.is_file
    assert f.user == 'pi'
    assert f.group == 'pi'
    assert oct(f.mode) == '0755'


def test_service_installed(host):
    f = host.file('/etc/systemd/system/prometheus-pihole-exporter.service')
    assert f.is_file
    assert f.user == 'root'
    assert f.group == 'root'
    assert oct(f.mode) == '0644'
