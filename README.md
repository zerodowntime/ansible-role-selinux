# selinux

Ansible role to install, setup selinux module

## Installation

```yaml
   ansible-galaxy install zerodowntime.selinux_python
   ansible-galaxy install zerodowntime.selinux
```

## Requirements

This role requires Ansible 2.5 or higher.

Supported platforms:

```yaml
  platforms:
    - name: EL
      versions:
        - 7
```

## Role default Variables

| var name                        | required?  | type   | desctiption                                                |
| --------------------------------| :--------: | :---:  | -----------------------------------------------------------|
| selinux__selinux_policy_version | required   | string | selinux-policy package state                               |
| selinux__mode                   | required   | string | name of the SELinux policy to use, like `permissive`       |
| selinux__type                   | required   | string | Selinux policy, like `targeted`                            |
| selinux__boolean                | no         | dict   | Toggles SELinux booleans                                   |

\* all variables are described in [defaults/main.yml](defaults/main.yml)

## Example Playbook

```yaml
---
- name: Configure selinux
  hosts: all

  roles:
    - role: selinux
      selinux__mode: enforcing
      selinux__boolean:
        virt_use_samba: true
```

## License

[Apache License 2.0](LICENSE)

## Support

ansible@zerodowntime.pl
