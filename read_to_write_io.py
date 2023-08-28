#!/usr/bin/env python3

""" Write a program that asks the user for the names of an input and an output file.
    - Open both of these files and then have the program read from the input file (by using readline()) and write to the output file (by using write()).
    - In effect, this is a copy program, whose interface to the program might look like:
**Enter the name of the input file: myinput**
**Enter the name of the output file: myoutput** """

in_file = input("What file to read from: ")
out_file = input("What file to write to: ")

f_in = open(in_file, "r")   # in file1, read
f_out = open(out_file, "w") # in file2, write

for line in f_in:   # from line in file1,
    f_out.write(line)   # write to line in file2
    
f_in.close()    # close file1
f_out.close()   # close file2