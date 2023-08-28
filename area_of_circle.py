#!/usr/bin/env python3

"""
area of a circle.
    - Accept the user input into a variable
    - Accepts decimal points as numbers
    - Computes and prints the area of the circle whose radius was input
        - the formula for area of a circle is (pi * (R^2)
        - 3.14159 = pi 
"""

pi = 3.14159
r = float(input("Enter the radius: "))
#  'float' instead of 'int' makes it possible to accept decimal points instead of ONLY whole numbers.
area = pi * (r ** 2)
print("The area this circle is ", area)
