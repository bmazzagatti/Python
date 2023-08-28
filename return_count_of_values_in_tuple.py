#!/usr/bin/env python3

"""test a function that takes a variable number of arguments as its first parameter and a number as its second parameter
function should return the count of the values in the tuple parameter (the variable number of arguments) that are greater than the second parameter"""

def num_of_greater(*var_list, boundary):
    n_greater = 0
    for item in var_list:
        if item > boundary:
            n_greater += 1
    return n_greater # will return amount of variables greater than 17

print(num_of_greater(7, 19, -30, 33, 55, 97, 48, boundary = 17))