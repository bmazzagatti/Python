#!/usr/bin/env python3

"""Write and test a function that takes a collection of strings and returns the length of the longest string in the collection.
The application should loop through the collection of strings and rely on the value returned by the function
to format all of the strings to the output such that they are all right justified to the width of the longest string. """
 
def get_longest_length(word_list):
    return len(max(word_list, key=len))

words = ["hello", "telephone", "banana", "catfish", "bleh"]

longest = get_longest_length(words)

for word in words:
    print(f"{word:>{longest}s}")
    