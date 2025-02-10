#!/usr/bin/env python3

""" write a program that creates a loop asking the user to input a number
    * repeat this process until the user enters the value 'end'
    * add each iteration number to a 'list' 
    * just before the program ends, print the following:
        - the contents of the list on one line
        - the sum of the elements in the list on the second line """

numbers = []
        
prompt = "Enter a number: (or the word 'end' to quit). "
while True:
    data = input(prompt)
    if data == "end":
        break
    try:
        numbers.append(float(data))
    except ValueError:
        print("Invalid input. Enter a valid number: (or `end` to quit). ")
        continue
    numbers.append(float(data))

print(numbers)

total = (sum(numbers))
print(total)
