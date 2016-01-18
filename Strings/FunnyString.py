#!/bin/python3

""" Funny String:

    Suppose you have a string S that has the length N. It is indexed from
    0 to N−1. String R is the reverse of string S. The string S is funny
    if the condition |Si−Si−1|=|Ri−Ri−1| is true for every i from 1 to N−1.

    Note: Given a string str, stri denotes the ascii value of the ith character
    (0-indexed) of str. Here, |x| denotes the absolute value of an integer x.

    Inputs:
    - line 1:: an integer T (the number of test cases)
    - for each test case T: a string
"""


import math

# define function to test for being funny
def is_funny_string(x, y):
    # loop through the string from value 1 - N
    funny = True
    for i in range(1, len(x), 1):
        if math.fabs(ord(x[i]) - ord(x[i - 1])) != math.fabs(ord(y[i]) - ord(y[i - 1])):
            funny = False
            return False

    # return Funny
    return funny

# Get the trial and strings
t = int(input().strip())
test_cases = []
for i in range(t):
    s = input().strip()
    r = s[::-1]
    temp = 'Funny' if is_funny_string(s, r) else 'Not Funny'
    test_cases.append(temp)

# print out all test cases
for result in test_cases:
    print(result)