#!/usr/bin/env python3

def main():
    with open(input("Enter a file name: "), "r") as the_file:
        for a_line in the_file: # as long as there's something to read on the next line, put next line into 'a_line' variable
            print(a_line, end="")


if __name__ == "__main__":
    main()