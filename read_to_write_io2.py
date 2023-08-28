#!/usr/bin/env python3

""" Rewrite 'read_to_write_io.py' such that the file names are obtained from the command line if two arguments are supplied.
- If the number of arguments is not two, then it should fall back on prompting the user for the filenames.
- The interface might look like:
** python3 your_program_name.py inputfile outputfile ** """

from sys import argv    

if len(argv) < 3:   # if length or argv is less than 3
    out_file = input("What file to write to: ") # ask for the output file (3rd argument)
else:   #otherwise
    out_file = argv[2]  # output file is argv
    
if len(argv) < 2:   # if length of argv is less than 2
    in_file = input("What file to read from: ") # menas the niput file i smisisng
else:   # if it isn' missing
    in_file = argv[1]  # 3 then first parameter in index 1


f_in = open(in_file, "r")   # in file1, read
f_out = open(out_file, "w") # in file2, write

for line in f_in:   # from line in file1,
    f_out.write(line)   # write to line in file2
    
f_in.close()    # close file1
f_out.close()   # close file2