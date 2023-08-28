#!/usr/bin/env python3

"""
Write a program that prompts twice for an integer.
    - the program should print the larger of the two numbers
    - if the numbers are equal, then the program should indicate as such
"""

num1 = int(input("Enter a number "))
num2 = int(input("Enter another number "))

if num1 < num2:
    print("The larger number is {0}".format(num2))
    
elif num1 > num2:
    print("The larger number is {0}".format(num1))

else:
    print("Both numbers are the same.")

