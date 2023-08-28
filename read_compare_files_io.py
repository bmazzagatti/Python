#!/usr/bin/env python3

"""Create two data files, each with a set of names, one per line.
- Write a program that reads both files and lists only those names that are in both files.
- The two file names should be supplied on the command line."""

from sys import argv

if len(argv) != 3:
    print("Usage: "+ argv[0] + " <file1> <file2>")
    exit(1)

file1 = open(argv[1], "r")
file2 = open(argv[2], "r")

s1 = set()
for line in file1:
    s1.add(line.strip())
    
s2 = set()
for line in file2:
    s2.add(line.strip())
    
s3 = s1 & s2
for line in s3:
    print(" - {}".format(line))