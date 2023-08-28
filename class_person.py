#!/usr/bin/env python3

"""Create a class called Person.

Each Person should have a name, an age, and a gender.

In addition to getters and setters for the above methods, the Person class must have an __init__() method and a __str__() method."""

class Person:
    def __init__(self, name, age, gender):   # parameters
        self._name = name      # stored into self name
        self._age = int(age)   # stored into self age
        self._gender = gender  # stored into self gender
        
    def __str__(self):  # string method
        return self._name + " (" + self._gender + ") aged " + str(self._age)    # return string representation 
    
    @property
    def name(self): # getter, only accepts 'self' as a parameter
        return self._name   # getter, only needs to return itself
    
    @name.setter        # setter 
    def name(self,name):    # returns <name> into itself
        self._name = name.capitalize()   
        
    @property       # getter
    def age(self):
        return self._age    # getter, only needs to return itself
    
    @age.setter     # setter
    def age(self,age):  # returns <age> into itself
        self._age = int(age)
        
    @property       # getter
    def gender(self):
        return self._gender # getter, only needs to return itself
    
    @gender.setter  # setter
    def gender(self, gender):   # returns <gender> into itself
        self._gender = gender

# within python3 module:        
#     >>> from class_person import Person
#     >>> 
#     >>> p1 = Person("Michael", 45, "M")
#     >>> 
#     >>> print(p1)
#     Michael (M) aged 45