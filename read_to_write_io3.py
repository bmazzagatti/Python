#!/usr/bin/env python3

""" Add exception handling to 'read_to_write_io3.py' so that if a file open fails, an OSError exception is handled, and the program is halted."""

from sys import argv, exit   

if len(argv) < 3:   # if length or argv is less than 3
    out_file = input("What file to write to: ") # ask for the output file (3rd argument)
else:   #otherwise
    out_file = argv[2]  # output file is argv
    
if len(argv) < 2:   # if length of argv is less than 2
    in_file = input("What file to read from: ") # menas the niput file i smisisng
else:   # if it isn' missing
    in_file = argv[1]  # 3 then first parameter in index 1

try:
    f_in = open(in_file, "r")   # in file1, read
    f_out = open(out_file, "w") # in file2, write
except OSError as err:
    print("ERROR: " + str(err))
    exit(1)

for line in f_in:   # from line in file1,
    f_out.write(line)   # write to line in file2
    
f_in.close()    # close file1
f_out.close()   # close file2