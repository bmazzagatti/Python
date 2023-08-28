#!/usr/bin/env python3

"""create a few more files with one name per line.
- The program in this exercise should read all these files and print the number of times each line occurs over all the files.
- The file names should be supplied on the command line."""

from sys import argv    # imports 'argv' module from 'sys' package 
                        # 'argv' is a list that contains command-line arguments passed to the script
argv.pop(0)             # removes first element from 'argv' list

names = {}              # dictionary
for curr_file in argv:  # loop that iterates over each element in the 'argv' list
    fileproc = open(curr_file, "r") # opens current fuile and in read mode
    for line in fileproc:
        line = line.strip()         # removes whitespace/any new lines
        if line in names.keys():    # if line is in names of the keys dictionary,
            names[line] += 1        # if name reoccurs, value is increased by 1
        else:                       # otherwise
            names[line] = 1         # new name is seen, is added to the dictionary of names
            
for name, freq in names.items():       # printing each name, and the frequency of each name's occurrence
    print("{}: {}".format(name, freq))