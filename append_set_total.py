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
duplicates = []

prompt = "Enter a number (or the word 'end' to quit): "
while True:
    data = input(prompt)
    if data == "end":
        break
    try:
        num = float(data)
    except ValueError:
        print(f"'{data}'is not a valid input. Please enter a valid number: (or the word `end` to quit.) ")
        continue
    if isinstance(num, (int, float)):
        if num in numbers:
            duplicates.append(num)
            print(f"'{num}' has already been entered.")
        else:
            numbers.add(num)

print(numbers)
print(f"{len(duplicates)} duplicate(s) not added: {duplicates}")
