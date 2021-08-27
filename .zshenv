# For signing commits with a GPG key.
export GPG_TTY=$(tty)

# Configure pyenv variables
export PYENV_ROOT="$HOME/.pyenv"
export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init --path)"

# Go Path
if [ -d "/usr/local/go/bin" ] ; then
	export PATH="/usr/local/go/bin:$PATH"
fi

# Go install path
if [ -d "/home/bkamphues/go/bin" ] ; then
       export PATH="/home/bkamphues/go/bin:$PATH"
fi       
