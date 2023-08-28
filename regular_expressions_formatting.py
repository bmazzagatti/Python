#!/usr/bin/env python3
"""Exercise 3
Write a program that reads lines from the user one at a time to see if they are formatted according to the following criteria.
    - Correctly formatted lines should consist of a four character identifier, any number of spaces or tabs, and a description.
    - The four character identifier should consist of two digits followed by two uppercase characters.
    - For each correctly formatted line, print the two digits, the two characters, and the descriptions.
        - Print all of these pieces of information on separate lines."""
        
import re
while True:
    product = input("Please enter product (enter 'end' to quit): ").strip()
    if product == 'end':
        break
    
    regex = r"(^[A-Z]{2})(\d{2})\s+([\w\s]+)"
    match = re.search(regex, product)
    
    if match:
        print("Letter: {}".format(match.group(1)))
        print("Digits: {}".format(match.group(2)))
        print("Description: {}".format(match.group(3)))
    else:
        print("Not a valid product decription")