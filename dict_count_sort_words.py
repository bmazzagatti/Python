#!/usr/bin/env python3

"""
new: count the frequency of each word in the user's input
a dict provides the perfect data structure for this problem
    - let the words be the keys, and let the counts be the values
print the results sorted by the words
print the results sorted by the counts

"""

words = dict()

prompt = "Enter a word (or the word 'end' to quit) "
while True:
    data = input(prompt).strip() #strips whitespace
    if data == "end": # completes program when end is input
        break

    curr_count = words.get(data, 0)
    curr_count += 1
    words[data] = curr_count

used_words = sorted(words.keys())
print("Sorted alphabetically:")
for word in used_words:
    print(word, "was used", words[word], "times")
    
def sort_by_freq(key):
    return words[key]

used_words.sort(key=sort_by_freq,reverse = True ) #sort by frequency, most common to least common since  reverse = True
print("Sorted by frequency:")
for word in used_words:
    print(word, "was used", words[word], "times")