#!/usr/bin/env python3

num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))

if num1 < 50 and num2 <50:
    print("Both numbers are small.")
    
if num1 >= 50 or num2 >= 50:
    print("at least one of the numbers is large.")
    
if num1 >= 50 or num2 >= 50 and num1 < num2:
    print("Example only.")
 
 # num1 = 75, num2 = 15
 # 1. True
 # 2.         False
 # 3.     "True or false" -> True
 # 4.                             False
 # 5.       True            and     False   -> False
 # 6. False
 
if num1 >= 50 or (num2 >= 50 and num1 < num2):
    print("Example only.")

# num1 = 75, num2 = 15
# 1. False
# 2.            xxxx
# 3. parentheses evaluate to false
# 4. True
# 5.    True or False
# 6. True
