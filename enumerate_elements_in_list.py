#!/usr/bin/env python3

def multiply_elements(factor, some_list):
    for idx, val in enumerate(some_list):
        some_list[idx] = val * factor

x = [1,2,3,2,1]
multiply_elements(3,x)
print(x)