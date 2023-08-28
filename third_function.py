#!/usr/bin/env python3

def wrap_with_border(some_text):
    """ Returns a string of some_text with a line of # signs beore and after it"""
    result = [len(some_text) * "#"]
    result.append(some_text)
    result.append(result[0])
    return "\n".join(result)


data = wrap_with_border("Hello")
print(data)
print(wrap_with_border("Goodbye"))