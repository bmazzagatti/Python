#!/usr/bin/env python3

"""
Write a program that prompts twice for text from the user:
    - the first input should be a first name.
    - the second input should be a last name.
    - the program should print the full name on one line and the person's initials on the second line.
"""
    
fname = input("what is your first name>: ")
lname = input("what is your last name>: ")
print(f"Your full name is {fname} {lname}.")
print(fname[0] + lname[0]) # [0] and [1] are positions from variables on previous line
