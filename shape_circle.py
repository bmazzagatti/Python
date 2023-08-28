#!/usr/bin/env python3

"""uses polymorphism and inheritance from 'shape.py'"""

import math
from shape import Shape


class Circle(Shape):
    def __init__(self, name, radius): # constructor, 
        super().__init__(name) # calls superclass's constructor and pass the name
        self.radius = radius # have to use, Shape class has no provisions for 'radius'

    def __str__(self):
        fmt = "{}  Radius:{}"
        return fmt.format(super().__str__(), self.radius)

    def area(self):
        return math.pi * self.radius ** 2 #defines calculation for area of a circle