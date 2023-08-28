#!/usr/bin/env python3

def sum(x, y):
    return x + y

def mul(x, y):
    return x * y

def operate(x, y, op):
    return op(x, y)
    
    
x = [1, 2, 3, 2, 5]

print(list(map(sum, x, [2] * len(x))))

#for idx, elem in enumerate(x):
 #   x[idx] = operate(elem, 2, sum)

#print(operate(1, 2, sum))
#print(operate(1, 2, mul))