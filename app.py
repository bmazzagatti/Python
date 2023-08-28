#!/usr/bin/env python3
import reusable  # import statement, looks for a file called reusable.py  anywherer in the Python library path

def main():
        print(reusable.square(5), reusable.cube(5))   # calls the square/cube functions from the reusable module 

if __name__ == "__main__":
        main()