#!/usr/bin/env python3

""" use sum to return the sum of all its numbers of an iterable object,
Write a similar function, but instead of taking a collection as a parameter, the function should take a variable number of arguments and return the sum of them."""

def get_sum(*params):
    return sum(params)

numbers = [1, 7, 22, 53, 0, 13]
print("The sum of {0} is {1} ".format(numbers, get_sum(1, 7, 22, 53, 0, 13)))
