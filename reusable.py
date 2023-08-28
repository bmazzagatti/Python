#!/usr/bin/env python3

""" defines several functions, that can be used by multiple Python applications in a file """

def main():
    print("Testing my function at top level", square(5), cube(10))
    
def square(p):
        return p ** 2

def cube(p):
        return p ** 3

if __name__ == "__main__":
        main()
        
