#!/usr/bin/env python
# HW06_ch09_ex04.py

# (1)
# Write a function named uses_only that takes a word and a string of letters,
# and that returns True if the word contains only letters in the list.
#   - write uses_only
# (2)
# Can you make a sentence using only the letters acefhlo? Other than "Hoe
# alfalfa?"
#   - write function to assist you
#   - type favorite sentence(s) here:
#       1:
#       2:
#       3:
##############################################################################
# Imports
import random
# Body

#9.4.1
def uses_only(user_word, string_of_letters):
    for letter in user_word:
        if letter not in string_of_letters:
            return False
    return True

#9.4.2
def sentence_generator():
    dataset = 'acefhlo'
    print(dataset[random.randint(1, len(dataset))])
    ##How do you let it know what are real words??!?!


##############################################################################
def main():
    pass  # Call your function(s) here.

if __name__ == '__main__':
    main()
