#!/usr/bin/env python3

"""uses polymorphism and inheritance from 'shape.py' with other shape_<shape>.py programs"""

class Shape:
    id = 100

    def __init__(self, name):
        self.name = name
        self.number = Shape.id
        Shape.id += 1

    def area(self): # empty area function because calculation for area per shape will be different
        pass  # Intended to be implemented by subclasses

    @property    # allows to retrieve a name 
    def name(self): return self._name # sets name

    @name.setter
    def name(self, name): self._name = name

    def __str__(self):
        return "Name:{}  id:{}".format(self.name, self.number)