#!/usr/bin/env python3

"""
# Write a program that prompts the user for a string and then prompts again for a number
    # the program should create and print a new string by using the repetition operator on the string and the number
        # - for example, if the string is 'hello' and the number is '3', then 'hellohellohello' should be printed
"""

word = str(input("Please enter a word: "))
repeat = int(input("please enter a number: "))
print(word * repeat)

