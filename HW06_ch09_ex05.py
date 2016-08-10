#!/usr/bin/env python3
# HW06_ch09_ex05.py

# (1)
# Write a function named uses_all that takes a word and a string of required
# letters, and that returns True if the word uses all the required letters at
# least once.
#   - write uses_all
# (2)
# How many words are there that use all the vowels aeiou? How about
# aeiouy?
#   - write functions(s) to assist you
#   - # of words that use all aeiou: [type here]
#   - # of words that use all aeiouy: [type here]
##############################################################################
# Imports

# Body

#9.5.1
def uses_only(user_word, string_of_letters):
    for letter in user_word:
        if letter not in string_of_letters:
            return False
    return True

def uses_all(user_word, string_of_letters):
    print(uses_only(string_of_letters, user_word))

#9.5.2
def uses_aeiou():
    with open("words.txt", "r") as fin:
        for line in fin:
            word = line.strip()
            if (uses_only(word, 'aeiou') == True):
                print(str(word))

def uses_aeiouy():
    with open("words.txt", "r") as fin:
        for line in fin:
            word = line.strip()
            if (uses_only(word, 'aeiouy') == True):
                print(str(word))



##############################################################################
def main():
    pass  # Call your function(s) here.

if __name__ == '__main__':
    main()
