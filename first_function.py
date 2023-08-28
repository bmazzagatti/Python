#!/usr/bin/env python3

""" a simple function that takes some text as a parameter and displays it with a border in the output. """

def print_with_border(some_text):
    border = len(some_text) * "#"
    print(border)
    print(some_text)
    print(border)


print_with_border("Hello")
print_with_border("Goodbye")
data = input("Enter some text: ")
print_with_border(data)