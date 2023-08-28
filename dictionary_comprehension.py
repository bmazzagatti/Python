#!/usr/bin/env python3
"""Write a dictionary comprehension that generates a dictionary of numbers and their factorials in the range (1,10).
    - Using that dictionary, multiply 6 factorial times 5 factorial."""

def fact(x):    # starts with parameter
    ans = x     # passed number to the factorial
    while (x > 2):
        x -= 1  # reduces by 1
        ans *= x    # multiplies previous value
    return ans

factorials = {x: fact(x) for x in range (1, 11)}
print(factorials)
print(factorials[6] * factorials[5])