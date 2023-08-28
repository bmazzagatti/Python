#!/usr/bin/env python3

def volume(length, width, height): # returns the volume of a box for given dimensions
    return length * width * height

dim1 = float(input("Enter the length of the box: "))
dim2 = float(input("Enter the width of the box: "))
dim3 = float(input("Enter the height of the box: "))
result = volume(dim1, dim2, dim3)
print("The volume is: ", result)