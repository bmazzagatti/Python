#!/usr/bin/env python3

"""Create a class called Family.

The Family does not extend Person but rather must be composed of two Person objects representing the parents and a list of Person objects representing the children.

Therefore, the __init__() method must take two required parameters (the parents), followed by a variable number of arguments (the children)."""

class Family:
    def __init__(self, parent1, parent2, *children, ):
        self.parent1 = parent1
        self.parent2 = parent2
        self.children = list(children)
        
    def add(self, child):
        self.children.append(child)
        
    def __str__(self):
        fam = str(self.parent1) + " " + str(self.parent2) + " [\n"
        for child in self.children:
            fam += str(child) + "\n"
        fam += "]"
        return fam
    
    def __lt__(self, otherfam):
        return len(self.children) < len(otherfam.children)
    
    def __gt__(self, otherfam):
        return len(self.children) > len(otherfam.children)

    def __eq__(self, otherfam):
        return len(self.children) == len(otherfam.children)