#!/usr/bin/env python3

# Word frequency exercise
# TODO: (Read detailed instructions in the Readme file)
# 1. Prompt the user: Ask the user to enter a sentence.
# 2. Split the sentence
# 3. Create lists to store words and their corresponding frequencies.
# 4. Iterate through words and update frequencies

import re

# ... is_sentence function remains unchanged ...

def is_sentence(text):
    # Check if the text is not empty and is a string
    if not isinstance(text, str) or not text.strip():
        return False

    # Check for starting with a capital letter
    if not text[0].isupper():
        return False

    # Check for ending punctuation
    if not re.search(r'[.!?]$', text):
        return False

    # Check if it contains at least one word (non-whitespace characters)
    if not re.search(r'\w+', text):
        return False

    return True

user_sentence = input("Enter a sentence: ")

while (is_sentence(user_sentence) == False):
    print("This does not meet the criteria for a sentence.")
    user_sentence = input("Enter a sentence: ")

# Split the sentence
split_sentence = user_sentence.split()

words_list = []
word_counts = []

# Word Frequencies
for word in split_sentence:
    word = word.strip(".,!?").lower()
    
   
    if word in words_list:
        index = words_list.index(word)
        word_counts[index] += 1
    else:
        words_list.append(word)
        word_counts.append(1)

# Print
for i in range(len(words_list)):
    print(f"{words_list[i]}: {word_counts[i]}")
