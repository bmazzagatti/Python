#!/usr/bin/env python3

"""uses polymorphism and inheritance from 'shape.py'"""

from shape_rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, name, length): 
        super().__init__(name, length, length)
    

# below is code for rectangle

    # class Rectangle(Shape):
    # def __init__(self, name, length, width):
    #     super().__init__(name) 
    #     self.length = length
    #     self.width = width
    