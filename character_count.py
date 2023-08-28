#!/usr/bin/env python3

"""
Write a program that prompts to enter a string of text
 - The Program should print the original text followed on a second line in the output by the number of characters entered
"""

text = input("Please enter some text: ")
print("You entered:", text)
print("Your text contains {length} characters.".format(length = len(text)))
