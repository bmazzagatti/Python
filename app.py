#!/usr/bin/env python3
import reusable  # import statement, looks for a file called "reusable.py" anywhere in the Python library path

def main():
        print(reusable.square(2), reusable.cube(3))   # calls the square/cube functions from the "reusable" module 

if __name__ == "__main__":
        main()