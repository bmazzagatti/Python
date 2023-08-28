#!/usr/bin/env python3

""" Write a calculator application that presents a menu
    - have the user enter a number from that menu 
    -the user should be prompted twice for two numbers and the chosen operation performed on them with the result being displayed on the scrreen
        -each oprion should be its own function """ 
        
def add():
    x, y = get_numbers()
    print(f"{x} + {y} == {x+y}\n")

def subtract():
    x, y = get_numbers()
    print(f"{x} - {y} == {x-y}\n")

def multiply():
    x, y = get_numbers()
    print(f"{x} * {y} == {x*y}\n")

def divide():
    x, y = get_numbers()
    print(f"{x} / {y} == {x/y}\n")

def get_numbers():
    x = int(input("Enter first operand: "))
    y = int(input("Enter second operand: "))
    return(x, y)

def quit():
    exit()
    
def impossible():
    print("Can't perform this operation")
    
calculator = {
    "1": add,       #add, subtract, multiply, divide, quit are not quoted so they are understood as identifiers
    "2": subtract,  # will be invoked
    "3": multiply,
    "4": divide,
    "5": quit
}

while True:
    print("Calculator Options:")
    for key in calculator:
        print(f"{key}: {calculator[key].__name__.capitalize()}")
    choice = input("Choose an operation: ")
    calculator.get(choice, impossible)()