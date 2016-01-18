#!/bin/python3

""" Pangrams:

    Roy wanted to increase his typing speed for programming contests.
    So, his friend advised him to type the sentence "The quick brown fox
    jumps over the lazy dog" repeatedly, because it is a pangram.
    (Pangrams are sentences constructed by using every letter of the
    alphabet at least once.)

    After typing the sentence several times, Roy became bored with it.
    So he started to look for other pangrams.

    Given a sentence s, tell Roy if it is a pangram or not.

    Inputs:
    - line 1:: a string s

    Output:
    - print 'pangram' if s is a pangram, else, 'not pangram'
"""

# get the string and turn it lower case
s = list(input().strip().lower())

# create an alphabet dictionary
alphabet = {chr(i): 0 for i in range(ord('a'), ord('z') + 1, 1)}

# loop through the string and check to see if all letters are there
for i in s:
    if i in alphabet.keys():
        alphabet[i] = 1

if sum(alphabet.values()) == 26:
    print('pangram')
else:
    print('not pangram')