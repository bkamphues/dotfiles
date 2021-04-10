############################################################
############################################################
################ Ubuntu Bootstrap Script ###################
#################### By Bo Kamphues ########################
############################################################

import subprocess

print("Executing Ubuntu Bootstrap Python Script...")

# library
def __simpleRun(commands: list):
    subprocess.run(commands)


# update & upgrade apt-get
__simpleRun(["sudo", "apt-get", "update"])
__simpleRun(["sudo", "apt-get", "upgrade", "-y"])

# install pip
__simpleRun(["sudo", "apt-get", "install", "-y", "python3-pip"])

# install global pip packages
__simpleRun(["pip3", "install", "black"])
__simpleRun(["pip3", "install", "termcolor"])

from termcolor import colored, cprint

text = colored("Hello world!", "red", attrs=["reverse", "blink"])
print(text)