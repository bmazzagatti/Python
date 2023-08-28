#!/usr/bin/env python3

"""
# Write a program that prompts twice for an integer.
    # - the program should output the sum of the integers within the range of those two numbers inclusively
    # - for example, if the user inputs the numbers '10' and '15', then the sum would be 75.
        # ex: 10 + 11 + 12 + 13 + 14 + 15 = 75
"""

num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))

#if num1 > num2:
#    x = num1
#    num1 = num2
#    num2 = x

if num1 > num2:
    num1, num2 = num2, num1
    
total = 0
for x in range(num1, (num2 + 1)):
    total = total + x

print("Sum of numbers between {0} and {1} is {2}.".format(num1, num2, total))
    
    