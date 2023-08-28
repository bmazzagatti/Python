#!/usr/bin/env python3

list1 = [44, 7, -4, 16]
list2 = [16, 3, 56, 100]
list3 = [0, 30, 1, -2, -10,]
list4 = [5, 3, 99, 50]

new_list = list1 + list2 + list3 + list4
new_list.sort()
print(new_list)

# another way to sort same sets of numbers:
new_list2 = sorted([44, 7, -4, 16] +    # lines separated for
                   [16, 3, 56, 100] +   # visual purposes
                   [0, 30, 1, -2, -10,] +
                   [5, 3, 99, 50])
print(new_list2)