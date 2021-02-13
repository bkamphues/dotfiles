#!/usr/bin/env python3

import subprocess
from os.path import dirname
from os.path import realpath
from os.path import expanduser

# variables
HOME_DIRECTORY = expanduser("~")
DOTFILES_DIRECTORY = dirname(realpath(__file__))

# execute a command line command
def execute(command):

    # check if command is of type array
    if not isinstance(command, list):
        raise Exception("A type other than an array was given.")

    # open a subprocess to execute the command and print any errors
    process = subprocess.Popen(command, stderr=subprocess.PIPE, universal_newlines=True)
    stdout, stderr = process.communicate()
    if stdout:
        print(stdout)
    if stderr:
        print(stderr)


# create a symlink between two locations/files
def symlink(file, link):

    # open a subprocess to execute the command and print any errors
    execute(["ln", "-vfs", file, link])


# create symlinks to dotfiles
zshrc = f"{DOTFILES_DIRECTORY}/.zshrc"
symlink(zshrc, HOME_DIRECTORY)
