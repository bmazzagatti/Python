#!/usr/bin/env python3

"""Create a list in your program that has 10 numbers.

- Then, in a loop, ask the user for a number.
- Use this number as an index into your list and print the value located at that index.
- End the program when the user enters end.
- Handle the case of an illegal number.
- Handle the case of an illegal subscript. 

Test except_list.py by using a few negative numbers as the index.
- Eliminate negative numbers as legitimate subscripts by raising the IndexError exception when a negative number is given

"""

def main():
    alist = [2, 9, 11, 24,33, 56, 60, 77, 89, 100]  # a list
    while True:
        try:
            num = input("Please enter anumber, or 'end' to quit: ") # loop: asks the user for a number
            if num == 'end':    # ends the program
                break
            num = int(num)
        except ValueError:
            print("Invalid input. Try again.")  # illegal subscript
            continue
        
        try:
            if num < 0:
                raise IndexError("No negative indices")
            print("Number at index {} is {}.".format(num, alist[num])) # number as an index/prints value located at that index
        except IndexError:
            print("There is no number at that index")   # illegal number
if __name__ == "__main__":
    main()