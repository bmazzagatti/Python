#!/usr/bin/env python3
def decode(message_file):
    # Read the encoded message from the file
    with open(message_file, 'r') as file:
        lines = file.readlines()

    # Initialize an empty list to store decoded words
    decoded_words = []

    # Initialize the current index of the message
    index = 0

    # Iterate through each line of the pyramid
    for line in lines:
        # Split the line into number-word pairs
        pairs = line.split()

        # Check if the current index is within the bounds of pairs
        if index < len(pairs):
            # Extract the word corresponding to the current index
            word = pairs[index][1:]

            # Append the word to the decoded words list
            decoded_words.append(word)

        # Increment the index for the next line
        index += 1

    # Return the decoded message as a string
    return ' '.join(decoded_words)

# Example usage:
decoded_message = decode("encoded_message.txt")
print(decoded_message)
