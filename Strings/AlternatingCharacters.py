#!/bin/python3

""" Alternating Characters:

    Shashank likes strings in which consecutive characters are different.
    For example, he likes ABABA, while he doesn't like ABAA. Given a string
    containing characters A and B only, he wants to change it into a string
    he likes. To do this, he is allowed to delete the characters in the string.

    Your task is to find the minimum number of required deletions.

    Input:
    - line 1:: an integer T (number of test cases)
    - for each T:: a string

    Output:
    - for each test case, print the minimum number of deletions required
"""


# get t
t = int(input().strip())

test_cases = []
for i in range(t):
    s = input().strip()

    # loop through s and keep track of deletions
    deletions = 0
    active_char = ''
    for i in range(len(s)):
        if s[i] is active_char:
            deletions += 1
        else:
            active_char = s[i]

    # save the number of deletions to the test_cases
    test_cases.append(deletions)

# print test cases
for result in test_cases:
    print(result)