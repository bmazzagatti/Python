#!/usr/bin/env python3

""" demonstrates 'tuple' objects and using the 'enumerate()' constructor' """

grades = ("A", "B", "C", "D", "F")
points = ("90-100", "80-89", "70-79", "60-69", "00-59")
for score in grades:
    print(score, end = "\t")
print()
print("\n")
# prints   A       B       C       D       F
#--------------------------------------------------------

for a_tuple in enumerate(grades):
    print(a_tuple[0], ":", a_tuple[1], end= "\t")
print()
# prints      0 : A   1 : B   2 : C   3 : D   4 : F 
#--------------------------------------------------------

# Unpacking the tuple from enumerate
for i, score in enumerate(grades, start=1):
    print(i, ":", score, end = "\t")
print()
print("\n")
# prints    1 : A   2 : B   3 : C   4 : D   5 : F
#--------------------------------------------------------

for index, score in enumerate(grades):
    print(score, ":", points[index])
# prints: 
# A : 90-100
# B : 80-89
# C : 70-79
# D : 60-69
# F : 00-59
