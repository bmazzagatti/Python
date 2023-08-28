#!/usr/bin/env python3


"""Create a class called Family.

The Family does not extend Person but rather must be composed of two Person objects representing the parents and a list of Person objects representing the children.

Therefore, the __init__() method must take two required parameters (the parents), followed by a variable number of arguments (the children).

        Implement the necessary special methods so that the <, ==, and > operators can be used with Family objects.

            The criteria for the methods should be the number of children."""
            
from class_family import Family
from class_person import Person

p1 = Person("Braeland", 30,"M")
p2 = Person("Kelly", 34,"F")
c1 = Person("Jack", 5,"M")
c2 = Person("Tessa", 4,"F")
c3 = Person("Nicholas", 3, "M")
c4 = Person("Gianna", 0, "F")

f1 = Family(p1, p2, c1, c2, c3, c4)
print(f1)

p1 = Person("Ed", 30,"M")
p2 = Person("Steph", 30,"F")
c1 = Person("Veronica", 6,"F")
c2 = Person("Mallory", 3,"F")
c3 = Person("Eddie", 0, "M")

f2 = Family(p1, p2, c1, c2, c3)
print(f2)

print("Mazzagatti < Keenan", f1 < f2)
print("Mazzagatti > Keenan", f1 > f2)
print("Mazzagatti == Keenan", f1 == f2)