#!/usr/bin/env python3

""" Use a dictionary to create a mapping from the digits 0-9 to the words 'zero','one','two',etc. 
ask the user to input a number
if the user enters 1437, then this program should print 'one' 'four' 'three' 'seven'"""

numbers = {
    0: "zero",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine"
}
while True:
    num = input("Enter a number: ")
    if num.isnumeric():
        break
    print("{0} is not a number. Please try again.".format(num))
    
for digit in num:
    print(numbers[int(digit)], end=" ")
print()
