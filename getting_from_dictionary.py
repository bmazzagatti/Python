#!/usr/bin/env python3

""" demonstrates the use of the 'get()' method with dictionaries """

reward_pts = {"Jack": 500, "Tessa": 2000, "Nicholas": 750}
points = reward_pts.get("Jack")      # returns 500
print("Jack:", points)
points = reward_pts.get("Gianna")  # returns None
print("Gianna:", points)

# Supplying a different value to return other than None
points = reward_pts.get("Gianna", 0)  # returns 0
print("Gianna:", points)
print("Current Dictionary Contents:", reward_pts)
