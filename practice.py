#!/usr/bin/env python3

first = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
second = ["day", "day", "sday", "nesday", "rsday", "day", "urday"]

days = []
for idx in range(len(first)):
    days.append(str(first[idx]) + str(second[idx]))
    
print(days)