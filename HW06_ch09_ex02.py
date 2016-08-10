#!/usr/bin/env python3
# HW06_ch09_ex02.py

# (1)
# Write a function called has_no_e that returns True if the given word doesn't
# have the letter "e" in it.
#   - write has_no_e
# (2)
# Modify your program from 9.1 to print only the words that have no "e" and
# compute the percentage of the words in the list have no "e."
#   - print each approved word on new line, followed at the end by the %
#   - name your function print_no_e
##############################################################################
# Imports

# Body

#9.1

def more_than_20():
    with open("words.txt", "r") as fin:
        for line in fin:
            word = line.strip()
            if len(word) > 20:
                print(word)

#9.2.1

def has_no_e(user_word):
    for letter in user_word:
        if letter == 'e':
            return False
    return True

#9.2.2

def print_no_e():
    with open("words.txt", "r") as fin:
        for line in fin:
            word = line.strip()
            if (len(word) > 20) and (has_no_e(word) == True):
                print(str(word))




##############################################################################
def main():
    has_no_e('hello') #should be false
    has_no_e('howdy') #should be true

    print_no_e()

if __name__ == '__main__':
    main()
