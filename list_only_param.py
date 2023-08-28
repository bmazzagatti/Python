#!/usr/bin/env python3

"""receives a list as its only parameter and returns a new list of the positive elements only """
def positive_only(some_list):
    result = []
    for element in some_list:
        #if type(element) != "<class 'int'>" and (type(element) != float):  # if type of element IS NOT a class of 'int', OR 'float'
        if not(type(element) == int or type(element) == float): # another way to write line 7 
            continue    # skip the rest of the loop
        if element > 0: # otherwise,
            result.append(element)     # append it to the result
            return result

elements = ["boo", 15, -3, 99, 5.7, "a car", [1, 2, 3], -99]
print ("Elements: ", elements)
results = positive_only(elements)
print("Results: ", results)