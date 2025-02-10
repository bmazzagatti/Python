#!/usr/bin/env python3

count = 0
total = 0

while count <= 100:                 # count will never go above 21 in this scenario. this line can be           while True:
    count +=1
    if count % 4 ==0:
        continue                    #skip even multiples of 4
    if count * count > 400:
        break                       # will happen at counter = 21
    total += count

print("Total is:", total, " Count is:", count)
