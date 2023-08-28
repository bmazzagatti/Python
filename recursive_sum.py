#!/usr/bin/env python3

"""recursive function that adds numbers from 1 to upper limit n"""

def sum_to(n):
    if not n:      # This is the termination condition
        return n
    
    return n + sum_to(n-1) #This is where the recursion is