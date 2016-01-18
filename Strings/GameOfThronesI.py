#!/bin/python3

""" Game of Thrones - I:

    Dothraki are planning an attack to usurp King Robert's throne. King Robert
    learns of this conspiracy from Raven and plans to lock the single door
    through which the enemy can enter his kingdom.

    But, to lock the door he needs a key that is an anagram of a certain
    palindrome string.

    The king has a string composed of lowercase English letters. Help him
    figure out whether any anagram of the string can be a palindrome or not.

    Inputs:
    - line 1:: a string

    Output:
    - 'YES' if any anagram of the string can be a palindrome, else 'NO'
"""


s = input().strip().lower()

# create an alphabet dictionary
alphabet = {chr(i): 0 for i in range(ord('a'), ord('z') + 1, 1)}

# Loop through the string
for i in range(len(s)):
    if s[i] in alphabet.keys():
        alphabet[s[i]] += 1

# count the values and see if it can be an anagram
odd_threshold = 0 if len(s) % 2 == 0 else 1
odds = 0
possible_palindrome = True
for letter in alphabet.keys():
    if alphabet[letter] % 2 == 1:
        odds += 1

if odds > odd_threshold:
    print('NO')
else:
    print('YES')