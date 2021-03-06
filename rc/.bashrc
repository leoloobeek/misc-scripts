export EDITOR=vim
export PYTHONSTARTUP=~/.pythonrc

alias la='ls -a --color=auto'
alias ll='ls -l --color=auto'
alias ..='cd ..'
alias ...='cd ../../../'
alias ....='cd ../../../../'
alias .....='cd ../../../../'
alias .4='cd ../../../../'
alias .5='cd ../../../../..'
alias h='history'
alias j='jobs -l'
alias ports='netstat -tulnp'
alias listen='nc -nvlp'
alias processes='ps auwwx'

#for piping output to X clipboard. Obviously only works on systems with X
alias clipboard="xargs echo -n | xclip -selection clipboard"

PS1='\[\033[01;31m\]\u@\h\[\033[00m\]:\[\033[01;34m\]\w\[\033[00m\]$ '
