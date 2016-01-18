#!/bin/python3

""" Two Strings:

    You are given two strings, A and B. Find if there is a substring that
    appears in both A and B.

    Inputs:
    - line 1:: an integer T (number of test cases)
    - for each test case::
        - line 1: string A
        - line 2: string B

    Output:
    - For each test case, display YES (in a newline), if there is a common
      substring. Otherwise, display NO.
"""


# get N
t = int(input().strip())

# loop through the n strings
test_cases = []

for _ in range(t):
    str1 = input().strip()
    str2 = input().strip()

    # put each string into an alphabet
    alphabet1 = {chr(i): 0 for i in range(ord('a'), ord('z') + 1, 1)}
    alphabet2 = {chr(i): 0 for i in range(ord('a'), ord('z') + 1, 1)}
    for i in range(len(str1)):
        if str1[i] in alphabet1.keys():
            alphabet1[str1[i]] = 1

    for j in range(len(str2)):
        if str2[j] in alphabet2.keys():
            alphabet2[str2[j]] = 1

    share_substring = False
    for x in alphabet1.keys():
        if alphabet1[x] + alphabet2[x] == 2:
            share_substring = True

    temp = 'YES' if share_substring else 'NO'
    test_cases.append(temp)

for result in test_cases:
    print(result)