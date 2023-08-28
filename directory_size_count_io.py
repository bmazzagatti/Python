#!/usr/bin/env python3

""" Write a program that displays the file name, size, and modification date for all those files in a directory that are greater than a given size.
    - The directory name and the size criteria are given as command line arguments."""

from sys import argv, exit
import os
import time

if len(argv) != 3:
    print("Usage: "+ argv[0] + " <directory> <sizelimit>")
    exit(1)

directory = argv[1]
sizelimit = int(argv[2])

files = os.listdir(directory)

for filecheck in files:
    filedata = os.stat(os.path.join(directory, filecheck))
    if filedata.st_size > sizelimit:
        print("{} {} {}".format(filecheck, filedata.st_size, time.ctime(filedata.st_mtime)))
        