#!/bin/python3

""" Gemstones:

    John has discovered various rocks. Each rock is composed of various
    elements, and each element is represented by a lower-case Latin letter
    from 'a' to 'z'. An element can be present multiple times in a rock.
    An element is called a gem-element if it occurs at least once in each
    of the rocks.

    Given the list of N rocks with their compositions, display the number
    of gem-elements that exist in those rocks.

    Inputs:
    - line 1:: an integer N (the number of rocks)
    - for N lines:: a lower-case string

    Output:
    - print the number of gem-elements that are common in these rocks.
"""


# get N
n = int(input().strip())

# loop through the n strings
alphabet = {chr(i): 0 for i in range(ord('a'), ord('z') + 1, 1)}
for i in range(n):
    temp_alphabet = {chr(i): 0 for i in range(ord('a'), ord('z') + 1, 1)}
    temp = list(set(input().strip()))
    for j in temp:
        temp_alphabet[j] = 1
    # add temp_alphabet to alphabet
    for letter in alphabet:
        alphabet[letter] += temp_alphabet[letter]

# test to see which letters are in all strings
total = 0
for letter in alphabet:
    if alphabet[letter] == n:
        total += 1

print(total)