#!/usr/bin/env python3

"""Given the following two lists:
first = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
second = ["day", "day", "sday", "nesday", "rsday", "day", "urday"]
concatenate the two lists by index into a new list that, when printed, looks as follows:
["Sunday, "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]"""

first = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
second = ["day", "day", "sday", "nesday", "rsday", "day", "urday"]

days = []
for idx in range(len(first)):
    days.append(str(first[idx]) + str(second[idx]))
    
print(days)