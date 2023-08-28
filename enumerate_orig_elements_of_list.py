#!/usr/bin/env python3

"""
Write a program that prompts the user twice for a number
- the first number will be the base, and the second number will be the exponent
- print the result of raising the base to the exponent
"""
     
x = int(input("Enter the base: "))
y = int(input("Enter the exponent: "))

print("{0} to the power of {1} equals {2}".format(x, y, x**y))
