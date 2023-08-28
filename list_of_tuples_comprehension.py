#!/usr/bin/env python3
"""Write a list comprehension to create a list of tuples, of x and the factorial of x, for the numbers from 5 to 10 inclusive.
- The math module has a factorial() function that can be used."""

import math
factorials = [(x, math.factorial(x)) for x in range(5, 11)]
print(factorials)