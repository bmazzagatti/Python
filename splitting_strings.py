#!/usr/bin/env python3

text = """EACH   WORD  IS   SEPARATED   BY   WHITESPACE"""
data = text.split()
for value in data:
    print(value)
    
    print("*" * 50)
    
    text = "This,is,comma,separated,text"
    data = text.split(",")
    for value in data:
        print(value)
