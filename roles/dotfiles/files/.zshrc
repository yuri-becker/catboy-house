alias ls="lsd"
alias l='ls -lFh'
alias la='ls -lAFh'
alias lr='ls -tRFh'
alias lt='ls -ltFh'
alias ll='ls -l'
alias ldot='ls -ld .*'
alias lS='ls -1FSsh'
alias lart='ls -1Fcart'
alias lrt='ls -1Fcrt'
alias lsr='ls -lARFh'
alias lsn='ls -1'

alias rm="rm -i"
alias cp="cp -i"
alias mv="mv -i"

alias rimraf="rm -rf"
alias t='tail -f'
alias h='history'

alias cat='batcat --plain --pager never'

export EDITOR='vim'

COLOR_DEFAULT=$'\e[0m'
COLOR_TIME=$'\e[1m\e[34m'
COLOR_USER_HOST=$'\e[38m'
COLOR_DIR=$'\e[37m'
setopt PROMPT_SUBST
PS1='%{${COLOR_TIME}%}%* %{${COLOR_USER_HOST}%}%n@%m %{${COLOR_DIR}%}%~ %{${COLOR_DEFAULT}%}'
