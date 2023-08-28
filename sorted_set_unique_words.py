#!/usr/bin/env python3

""" * use a single set to determine the number of unique words in the user's input
    * Each time through a loop, the individual words should be added to the single set.
    * when done looping, output the contents of the set sorted alphabetically
    * output the number of unique words
    """
    

words = set()

prompt = "Enter a word (or the word 'end' to quit): "
while True:
    data = input(prompt)
    if data == "end":
        break

    words.add(data)

print(sorted(words))
print("There are {0} unique words in the set.".format(len(words)))