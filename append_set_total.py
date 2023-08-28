#!/usr/bin/env python3

"""Write a program that creates a loop asking user to input a number.
    * repeat this process until user enters the work 'end'
    * enter each number into a set
        - before you enter a number, verify if the number is already in the set
        - if the number is already in the set, update a counter that tracks how many entries are not added to the set
    * just before the program ends, print the following:
        - the contents of the set on one line 
        - the number of elements that were NOT added to the set on the second line"""

numbers = set()
duplicates = 0 

prompt = "Enter a number (or the word 'end' to quit)"
while True:
    data = input(prompt)
    if data == "end":
        break
    elif data in numbers:
        duplicates += 1
    else:
        numbers.add(data)

print(numbers)
print("{0} entries not added.".format(duplicates))
