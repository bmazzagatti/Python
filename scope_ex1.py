#!/usr/bin/env python3

name = "Jack"

def greet():
    global name
    name = "Joe"
    print("Hello,", name)
   
greet()

print("Hello,", name)

name = "Tom"

print("Hello,", name)