#!/usr/bin/env python3

import string

def main():
    try:
        with open("alphabet", "w") as the_file:
            the_file.write(string.ascii_letters)    # ascii_letters writes entire alphabet into the file
        print("The following was written to the file:")
        print(string.ascii_letters, "\n")   # read that file

        with open("alphabet", "r") as the_file: # re-open the file for reading
            while True:
                the_text = the_file.read(10)    # read 10 characters from the file at a time
                if not the_text:
                    break
                print(the_text) # printing them out on standard output
    except OSError as err:  # handles any OS errors that may be raised from writing or reading
        print("IO Error:", err)


if __name__ == "__main__":
    main()