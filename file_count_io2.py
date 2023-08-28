#!/usr/bin/env python3

""" Revise 'file_count.io.py' so that it accepts as an optional first command line argument a -t option.
    - The program must then only print the total number of lines, words, and characters in all the files combined. """

from sys import argv

argv.pop(0)
if argv[0].startswith("-t"):
    do_totals = True
    argv.pop(0)
else:
    do_totals = False

g_lines = g_words = g_characters = 0

for filename in argv:
    f = open(filename, "r")
    lines = words = characters = 0
    for line in f:
        lines += 1
        characters += len(line)
        words += len(line.split(None))
    f.close()
    g_lines += lines
    g_words += words
    g_characters += characters
    if not do_totals:
        print("Lines: {}, words: {}, characters: {}".format(lines, words, characters))
        
    if do_totals:
               print("Lines: {}, words: {}, characters: {}".format(g_lines, g_words, g_characters))