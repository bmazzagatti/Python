#!/usr/bin/env python3

my_list = [20, 15, 22, 35, 0, -4, 6, 100 ,-45]
print("**original list**",my_list) # prints original list

my_list.sort() # sorts my_list in order, CANNOT be used if strings and integers are in the same my_list
print("**sorted list**",my_list)
print("\n") # prints new line

my_list.insert(0, 2) # first digit is position, second digit is value. overwites the sort done previously
print("**insert '2' to list**",my_list)
print("\n")

my_list.reverse() # reverses order of my_list
print("**list reversed**", my_list)
print("**does this list contain 22?** (Statement is)",22 in my_list) # check if '22' is in the my_list

my_list.remove(22) # removes value from my_list
print(my_list)
print("**does this list STILL contain 22?** (Statement is):",22 in my_list)   # check if '22' is STILL in the my_list
print("\n")

for index_list in range(len(my_list)):    # for indemy_list within the range of 0- one BEFORE end of my_list 
    print("item in position",index_list, "is", my_list[index_list]) # variable named 'indemy_list' can be named anything and still work
print("\n")
