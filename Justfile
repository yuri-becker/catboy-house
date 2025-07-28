[private]
default:
    @just --list

install:
    ansible-galaxy install -r requirements.yml

run args='':
    ansible-playbook -i inventory.yml {{ args }} playbooks/**.yml;
alias r := run

lint:
    ansible-lint
alias l := lint

[group('remote')]
occ command:
    ssh catboy-house -t docker exec -it -u www-data nextcloud-nextcloud php occ {{command}}
