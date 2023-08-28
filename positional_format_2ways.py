#!/usr/bin/env python3

"""
Write a program that asks the user to enter a sentence
    - the first character in the string of text and the number of times it occurs in the string
    - the last character in the string of text and the number of times it occurs in the string
"""

original = input("Enter a full sentence: ")
print(original)
firstchar = original[0]
num_of_first = original.count(firstchar)
print("The first character is '{0}' and it occurs {1} times in the printed text above.".format(firstchar, num_of_first))

print("The last character is '{0}' and it occurs {1} times in the printed text above.".format(original[-1], original.count(original[-1])))

