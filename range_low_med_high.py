#!/usr/bin/env python3

"""
Ask the user to input three numbers representing a lower limit, a higher limit, and a step value.
    - the program should use a 'range' object to loop through and print the numbers from low to high (inclusive), taking into consideration the step.
"""

start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))
countby = int(input("Enter the interval to count by: "))

if countby > 0 and start > end:
    print("Can not increment from larger to smaller number!")
    
elif countby < 0 and start < end:
        print("Can not decrement from lower to higher number!")

elif countby == 0:
    print("cannot step by a value of 0")

else:
    for x in range(start, end + int(countby / abs(countby)), countby):
        print(x)
        
