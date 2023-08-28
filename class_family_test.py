#!/usr/bin/env python3

"""Create a class called Family.

The Family does not extend Person but rather must be composed of two Person objects representing the parents and a list of Person objects representing the children.

Therefore, the __init__() method must take two required parameters (the parents), followed by a variable number of arguments (the children)."""

from class_family import Family
from class_person import Person

p1 = Person("Braeland", 30,"M")
p2 = Person("Kelly", 34,"F")
c1 = Person("Jack", 5,"M")
c2 = Person("Tessa", 4,"F")
c3 = Person("Nicholas", 3, "M")

f = Family(p1, p2, c1, c2, c3)
print(f)

print("**************)")

c4 = Person("Gianna", 0, "F")
f.add(c4)
print(f)