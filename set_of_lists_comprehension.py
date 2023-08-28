#!/usr/bin/env python3
"""Write list comprehensions to produce the following lists:
- A list of elements 0,1,2,3,4,…,99
- A list from the preceding comprehension of those values that are evenly divisible by 5."""

first_list = [x for x in range(0, 100)]

second_list = [x for x in range(0, 100) if x % 5 == 0]

print(first_list)
print()
print(second_list)