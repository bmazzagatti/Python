#!/usr/bin/env python3

"""
Write a program that prompts twice for an integer
    Print the product of the two numbers
    Once this works properly, try entering numbers with a decimal point
        - What happens? Why?
    Now try entering data that is non-numerical
        - What happens? Why?
"""

num1 = int(input("Enter a number: "))
num2 = int(input("Enter a number: "))

print("Product is ", num1 * num2)

"""The answer is, decimal point will crash because it is defined as an 'int' instead of a 'float' """

# solution 

num3 = float(input("\n enter a decimal point number: "))
num4 = float(input("enter a decimal point number: "))
print("Product is ", num3 * num4)