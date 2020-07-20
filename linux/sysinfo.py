#!/usr/bin/env python3

# A system information gathering script

import subprocess

# command 1
def uname():
    uname = "uname"
    uname_arg = "-a"
    print(f"Gathering system information with {uname} command:\n")
    subprocess.call([uname, uname_arg])

# command 2
def disk_func():
    diskspace = "df"
    diskspace_arg = "-h"
    print(f"Gathering system information with {diskspace} command:\n")
    subprocess.call([diskspace, diskspace_arg])

# this is the main function that calls other functions

def main():
    uname()
    disk_func()
main()