[private]
default:
    @just --list

install:
    ansible-galaxy install -r requirements.yml

run tags='all':
    @ansible-playbook -i inventory.yml --tags {{ tags }} playbooks/**.yml;
alias r := run

lint:
    @ansible-lint
alias l := lint

[group('vault')]
vault-decrypt key:
    @ansible -i inventory.yml catboy_house -m debug -a 'var={{key}}'

[group('vault')]
vault-encrypt key value file:
    @ansible-vault encrypt_string "{{value}}" --name {{key}} >> "{{file}}"

[group('remote')]
occ command:
    ssh catboy-house -t docker exec -it -u www-data nextcloud-nextcloud php occ {{command}}
