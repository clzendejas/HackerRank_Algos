#!/bin/python3

""" Make It Anagram:

    Alice recently started learning about cryptography and found that anagrams
    are very useful. Two strings are anagrams of each other if they have same
    character set and same length. For example strings "bacdc" and "dcbac" are
    anagrams, while strings "bacdc" and "dcbad" are not.

    Alice decides on an encryption scheme involving 2 large strings where
    encryption is dependent on the minimum number of character deletions
    required to make the two strings anagrams. She need your help in finding
    out this number.

    Given two strings (they can be of same or different length) help her in
    finding out the minimum number of character deletions required to make two
    strings anagrams. Any characters can be deleted from any of the strings.

    Inputs:
    - line 1:: a string
    - line 2:: another string

    Output:
    - A single integer which is the number of character deletions.
"""


str1 = input().strip()
str2 = input().strip()

# put each string into an alphabet
alphabet1 = {chr(i): 0 for i in range(ord('a'), ord('z') + 1, 1)}
alphabet2 = {chr(i): 0 for i in range(ord('a'), ord('z') + 1, 1)}
for i in range(len(str1)):
    if str1[i] in alphabet1.keys():
        alphabet1[str1[i]] += 1

for j in range(len(str2)):
    if str2[j] in alphabet2.keys():
        alphabet2[str2[j]] += 1

# loop through the alphabet and count the number of deletions required
deletions = 0
for x in alphabet1:
    temp = max(alphabet1[x], alphabet2[x]) - min(alphabet1[x], alphabet2[x])
    deletions += temp

print(deletions)