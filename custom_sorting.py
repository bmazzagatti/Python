#!/usr/bin/env python3

""" demonstrates sorting a list of strings by the length of each string. """

names = """Smith Johnson Brown Mazzagatti Lee Nu Heim Core Reyes Robinson Wattdrop Kim Chang Miller"""
names = names.split()
# Primary sort by name ("Alphabetically)
names.sort()
# Secondary sort by length
names.sort(key=len)
print(names)
