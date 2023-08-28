#!/usr/bin/env python3

def main():
    f = open('output', 'w') # opens file
    print("Type:", type(f).__name__, "\tModule:", type(f).__module__)
    f.write('This is a test.\n')    # writes to file
    f.write('This is another test.\n')    # writes to file
    f.close()   # closes file
# always goof practice to close any files opened to prevent leaking of system resources

if __name__ == "__main__":
    main()