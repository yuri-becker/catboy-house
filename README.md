[![AGPL-3.0 License](https://img.shields.io/github/license/yuri-becker/catboy-house?style=for-the-badge&logo=gnu&logoColor=white&color=%23A42E2B )](https://github.com/yuri-becker/catboy-house/blob/main/LICENSE.md)

<br />
<div align="center">

  <h1 align="center"><strong>catboy.house</strong></h1>

  <p align="center">
    Infrastructure for catboy.house.
  </p>
</div>
<br/>
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-this-project">About this Project</a>
    </li>
    <li>
    <a href="#setup">Setup</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#install-ansible-and-requirements">Install Ansible and requirements</a></li>
        <li><a href="#make-the-host-accessible">Make the host accessible</a></li>
        <li><a href="#vault-password">Vault password</a></li>
        <li><a href="#become-password">Become password</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li>
        <a href="#code-conventions">Code conventions</a>
        <ul>
            <li><a href="#verbs">Verbs</a></li>
            <li><a href="#task-prefixes">Task prefixes</a></li>
        </ul>
    </li>
    <li><a href="#copying">Copying</a></li>
  </ol>
</details>
<br/>

## About this Project

catboy.house is a server that I used to share with someone else, hosting various services and projects.

I took over the server and am now in the process of migrating the existing services to be defined by Ansible.

Later on, I'm planning to add more public services for everyone to use.

## Setup
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

### Become password
<sup>(become is Ansible's sudo)</sup><br/>
Encrypt your server linux account's password and store it in `host_vars/catboy_house/become.yml` like this:
```shell
ansible-vault encrypt_string '<password>' --name ansible_become_pass > host_vars/catboy_house/become.yml
```

## Usage

**Running all Playbooks**
```sh
./run.sh
```
**Running tasks with specific tags**
```sh
./run.sh --tags <tags> 
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

## Code conventions

### Verbs
Tasks are be named with what they do, in third-person singular, e.g. "🫖 Makes a tea".

### Task prefixes
Task names are prefixed with specific emojis to make the output and nature of the task more scannable.
* 🚀 are application/container launches.
* 📂 are folder creations.
* ⬆️ for file/template copying.
* 📦 are package installations.
* 👤 are user and group creations.
* ✅ are checks.
* ⛔ are fail states.

## Copying
You may re-use files and roles from this repository for you own projects as long as you comply to the terms of the [GNU Affero General Public License 
version  3.0](https://github.com/yuri-becker/catboy-house/blob/main/LICENSE.md).