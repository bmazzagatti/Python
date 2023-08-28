#!/usr/bin/env python3

def findmax(a, b):
    max = 0
    if a < b:
        max = b
    elif a > b:
        max = a

    fmt = "Max is not {} or {}"     # this assertion is for IF a == b
    assert max == a or max == b, fmt.format(a, b)   # the max should be 'a' or 'b'
    return max


def main():
    try:
        print(findmax(2, 9), findmax(7, 4))
        print(findmax(3, 3))    # activates assertion on line 11
    except AssertionError as ae:    # raised after line 18 is activated
        print("Assertion Failed:", ae)


if __name__ == "__main__":
    main()