import os
import re
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


def test_sestatus(host):
    command = host.command('/usr/sbin/sestatus')

    assert command.rc == 0
    assert bool(re.search('Current mode:\s*enforcing', command.stdout,re.MULTILINE))
    assert bool(re.search('Loaded policy name:.\s*targeted', command.stdout,re.MULTILINE))


def test_sebool(host):
    command = host.command('/usr/sbin/getsebool httpd_can_network_connect')
    assert command.stdout.find('httpd_can_network_connect --> on') > -1
    assert command.rc == 0
