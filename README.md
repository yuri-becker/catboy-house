[![AGPL-3.0 License](https://img.shields.io/github/license/yuri-becker/catboy-house?style=for-the-badge&logo=gnu&logoColor=white&color=%23A42E2B )](https://github.com/yuri-becker/catboy-house/blob/latest/LICENSE.md)

<br />
<div align="center">

  <h1 align="center"><strong>catboy.house</strong></h1>

  <p align="center">
    Infrastructure for catboy.house.
  </p>
</div>

## About this Project

catboy.house is a server that I used to share with someone else, hosting various services and projects.

I took over the server and am now in the process of migrating the existing services to be defined by Ansible.

Later on, I'm planning to add more public services for everyone to use.

## Getting started
Instructions for setting up playbook execution and contribution. Most likely, you won't need this.

### Prerequisites
* Python

### Install Ansible and requirements
```sh
python -m pip install ansible
ansible-galaxy install -r requirements.yml
```

### Make the host accessible
* Add the host `catboy-house` to your ssh config
* Have your public ssh key added by someone with access.

### Vault password
Get the `.vault_password` file from someone and put it in the project root.

## Usage

**Running all Playbooks**
```sh
./run.sh
```
**Running single Playbooks**
```sh
ansible-playbook -i inventory.yml <playbook>
```
**Linting**
```sh
ansible-lint
```
**Encrypting variables**
```sh
ansible-vault encrypt_string <string> --name <var-name>
```