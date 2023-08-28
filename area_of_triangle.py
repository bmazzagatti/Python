#!/usr/bin/env python3

"""
area of a triangle.
    - Accept the user input into a variable
    - Accepts decimal points as numbers
    - Computes and prints the area of the triangle from user's given dimensions
        - the formula for area of a triangle is (base * height) /2
"""

base = float(input("Enter the base of a triangle: "))
height = float(input("Enter the height of a triangle: "))
#       'float' instead of 'int' makes it possible to accept decimal points instead of ONLY whole numbers.
area = (base * height) / 2
print("With a base of '{0}', and a height of '{1}', the area of this triangle is '{2}'".format(base, height, area))