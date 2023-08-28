#!/usr/bin/env python3

""" modifies the first_function.py to build a string and return it to the caller as opposed to printing it. """

def wrap_with_border(some_text):
    result = [len(some_text) * "#"]
    result.append(some_text)
    result.append(result[0])
    return "\n".join(result)


data = wrap_with_border("Hello")
print(data)
print(wrap_with_border("Goodbye"))