#!/usr/bin/env python3

while True:
  fname = input("What is your first name? ").lower().strip()
  lname = input("What is your last name? ").lower().strip()
  if fname == "bob":
    print("Hey Bob")
    break
  elif fname == "john":
    print("Hello John")
    break
  elif fname == "johnson" or lname.lower() == "johnson":
    print("Your name is a penis!")
    break
  elif not fname or not lname:
    missing_name = "first name" if not fname else "last name"
    print(f"A full name must be submitted. Your {missing_name} is missing.")
  else:
    print("Nice to meet you, " + fname.capitalize() + " " + lname.capitalize())
    break
