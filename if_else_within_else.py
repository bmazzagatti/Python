#!/usr/bin/env python3

start = int(input("enter a starting number: "))
ending = int(input("enter an ending number: "))

if start == ending:
    print("Nothing to count, both starting and ending numbers are '{0}'".format(ending))
else:
    countby = int(input("enter an interval to count by: "))

    if countby > 0 and start > ending:
        print("Cannot increment from larger to smaller number")
    
    elif countby < 0 and start < ending:
        print("Cannot decrement from larger to smaller number")

    elif countby == 0:
        print("Cannot count by 0")

    else:
        for x in range(start, ending + int(countby / abs(countby)), countby):
            print(x)
            
# separating the countby, within the below statement ensures that if line 18 elif statement occurs,
# the user is not prmopted for a countby interval if the start and end numbers are the same.