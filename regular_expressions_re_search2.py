#!/usr/bin/env python3
"""Repeat regular_expressions_re_search.py using a floating point number.
    - floating point number should have at least one digit to the left and to the right of the decimal point.
    - Specify whether the number is positive or negative."""
import re
while True:
    anumber = input("Please enter an floating point number (enter 'end' to end): ").strip()
    if anumber == 'end':
        break
    
    check = re.search (r"^-?\d+\.\d+$",anumber)
    if not check:
        print("This is not a valid floating point number")
        continue
    
    if anumber[0] == '-':
        print("The number is negative")
    else:
        print("The number is positive")