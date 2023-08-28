#!/usr/bin/env python3

"""
Write a program that prompts for a number.
-   The program should print out a message if the number is not an integer
"""

response = input("Enter a number: ")
if not response.isnumeric():
    print(f"'{response}' is NOT a number")
else:
    print("the number you entered '{0}' has {1} digits".format(response, len(response)))
    