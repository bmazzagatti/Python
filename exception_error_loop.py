#!/usr/bin/env python3

"""
Write a program that uses a loop to prompt the user and get an integer value.

- The program should print the sum of all the integers entered.
- If the user enters a blank line or any other line that cannot be converted to an integer, the program should handle this ValueError.
- If the user uses Ctrl+C to terminate the program, then it should be trapped with a KeyboardInterrupt, and a suitable message should be printed.
- When the user enters the end of file character (Ctrl+D on Linux or Ctrl+Z on Windows), the program should trap this with the EOFError, break out of the loop, and print the sum of all the integers.
"""

def main():
    sum = 0
    while True:
        try:
            num = input("Please enter a number: ")  # prompts the user
            sum += int(num)
        except ValueError:  # handles non-integer input
            print("Invalid number.")
        except KeyboardInterrupt: # traps Ctrl + C
            print(" press 'Ctrl + D' to exit.")   # informs of correct terminate command
        except EOFError:    #   takes 'Ctrl + D'
            break   # breaks out of loop
        
    print("the sum of all numbers entered is", sum) # print the sum of all the integers entered
    
if __name__ == "__main__":  # conditional statement to start main function
    main()