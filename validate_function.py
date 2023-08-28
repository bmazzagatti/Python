#!/usr/bin/env python3

"""- Write and test a function that is designed to validate input.
	- The function should prompt the user for a positive integer.
	- It should validate the information entered by the user is a positive integer.
		- If number entered is valid, the function should return the number.
		- If the number entered is invalid, the function should return a zero (0) instead.
	- The application, not the function, should indicate with a message in the output each time an invalid entry is given. """
 
def get_integer():
    value = input("Enter a positive integer: ")
    if value.isnumeric():       # if the value entered is numeric (0 or higher in number form)
        return int(value)       # then return the value entered
    
    return 0        # is executed if the input is NOT a positive integer (if NOT)
    
result = get_integer()          # result = entire function lines 10-15
if not result:                  # if result is false
    print("Invalid input") 