#!/usr/bin/env python3
  # "Things Fall Apart":
  #   {
  #     "author": "Chinua Achebe",
  #     "country": "Nigeria",
  #     "language": "English",
  #     "pages": 209,
  #     "year": 1958
  #   },
import json

with open("books.json", "r") as bfile:
  data = json.load(bfile)
  
print("Books:")
print(data.keys())  

while True:
  book = input("Enter a book title (or 'end' to quit): ").strip()
  if book == 'end':
    break
  
  binfo = data.get(book)
  if binfo:
    print("Book: {}".format(book))
    print("""
  - author: {}
  - country: {}
  - language: {}
  - pages: {}
  - year: {}
""".format(binfo.get("author"),
           binfo.get("country"),
           binfo.get("language"),
           binfo.get("pages"),
           binfo.get("year")))
  else:
    print("No such book. Try again.")