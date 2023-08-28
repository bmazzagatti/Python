#!/usr/bin/env python3
"""Write a program that reads a line at a time and determines whether the input consists solely of an integer number that is positive or negative.
Specify whether it is positive or negative."""
import re
while True:
    anumber = input("Please enter an integer number (enter 'end' to end): ").strip()
    if anumber == 'end':
        break
    
    check = re.search (r"^-?\d+$",anumber)
    if not check:
        print("This is not a valid number")
        continue
    
    if anumber[0] == '-':
        print("The number is negative")
    else:
        print("The number is positive")