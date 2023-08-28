#!/usr/bin/env python3

"""
Ask the user to input multiple numbers on one input line
    - split the numbers into a list
    - write a loop that examines each element of the list and diplays the ones that are greater than zero.
"""
 
numbers = input("Enter some numbers separated by spaces: ")

for num in numbers.split():
    if not num.isnumeric():
        continue
    
    if int(num) > 0:
        print(num)
        