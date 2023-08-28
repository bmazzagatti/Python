#!/usr/bin/env python3

def say_hello(visitor_name, greeting = "Hello"):
    return greeting + "," + visitor_name

print(say_hello("John"))
print(say_hello("Jane", "Oh hey"))