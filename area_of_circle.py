#!/usr/bin/env python3

"""
area of a circle.
    - Accept the user input into a variable
    - Accepts decimal points as numbers
    - Computes and prints the area of the circle whose radius was input
        - the formula for area of a circle is (pi * (R^2)
        - 3.14159 = pi 
    - Error handle if a string is entered
"""

pi = 3.14159
valid_input = False

while not valid_input:
    try:
        r = float(input("Enter the radius: "))
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        continue  # Continue the loop to prompt the user for a valid input

    area = pi * (r ** 2)
    print("The area of this circle is", area)
    valid_input = True  # Set the flag to True to end the loop after the first valid input

