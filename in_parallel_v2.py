#!/usr/bin/env python3
long_names = ["January", "February", "March", "April",
              "May", "June", "July", "August", "September",
              "October", "November", "December"]
abbr_names = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
              "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
numdays = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

for x in range(len(long_names)):
    print(long_names[x], abbr_names[x], numdays[x])
    
for long, short, ndays in zip(long_names, abbr_names, numdays):
    print(long, short, ndays)