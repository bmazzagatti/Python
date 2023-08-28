#!/usr/bin/env python3
"""Suppose there is a file with three values per line.
- The values are white space separated as follows.
        OwnerName ComputerType ComputerValue
- Read the lines and make a dictionary of dictionaries so the keys are the owner and the values are a dictionary consisting of the computer type as the key and the computer value as the value.
- Print the dictionary."""

file = open("dictionaries/d1", "r")
lines = file.readlines()
file.close

comp_owners = {}

for line in lines:
        owner, comp_type, value = line.split()   # unpack each line into 3 records
        equipment = comp_owners.get(owner)      # attempt to get the existing value for owner in main dictionary
        if not equipment:       # if equipment doesn't exist
                equipment = {}  # create new data structure (dictionary)
        equipment[comp_type] = value    # create comp_type KEY and assing with the current value
        
        comp_owners[owner] = equipment
print(comp_owners)