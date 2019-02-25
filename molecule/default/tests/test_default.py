import os
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_selinux_config(host):
    f = host.file('/etc/selinux/config')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'
    assert f.mode == 0o0644
    assert f.contains('SELINUX=enforcing')
    assert f.contains('SELINUXTYPE=targeted')
