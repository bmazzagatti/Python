#!/usr/bin/env python3

def volume_cylinder(diameter, height):
    base =((diameter /2) ** 2) * 3.14159 # (1/2 diameter squared) multiplied by pi
    volume = base * height
    return volume

print(volume_cylinder(1, 3))
print(volume_cylinder(height = 3, diameter = 1))