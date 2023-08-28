#!/usr/bin/env python3

"""
Convert hours to seconds
***use positional format***
    - 60 seconds in a minute
    - 60 minutes in an hour
"""

hours = int(input("how many hours: "))
convert = (hours * 60) * 60

print("{0} hours = {1} seconds.".format(hours, convert))
# positional format
    # much easier to insert and lines with multiple variables
    # easier to look at
# {0} is FIRST position
# {1} is SECOND position

# print(hours, "hours =", convert, "seconds.")
    # works. but is messy
