#!/usr/bin/python3
#
## author: thynus
## source:
#  https://github.com/fastfetch-cli/fastfetch/blob/dev/src/data/help.json
#
## requirements:
#  sudo apt install help2man
#
## usage:
#  ./man_page.py > fastfetch.1.in
#
## preview:
# man -l fastfetch.1.in
import subprocess

subprocess.run(['help2man','fastfetch'])
