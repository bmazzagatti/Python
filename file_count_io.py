#!/usr/bin/env python3

"""Write a program that counts the number of lines, words, and characters in each file named on the command line."""

from sys import argv

for filename in argv[1:]:
    f = open(filename, "r")
    lines = words = characters = 0
    for line in f:
        lines += 1
        characters += len(line)
        words += len(line.split(None))
    f.close()
    print("Lines: {}, words: {}, characters: {}".format(lines, words, characters))