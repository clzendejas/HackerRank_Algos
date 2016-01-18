#!/bin/python3

""" Anagram:

    Sid is obsessed with reading short stories. Being a CS student, he is doing
    some interesting frequency analysis with the books. He chooses strings S1
    and S2 in such a way that |len(S1)−len(S2)|≤1.

    Your task is to help him find the minimum number of characters of the first
    string he needs to change to enable him to make it an anagram of the
    second string.

    Note: A word x is an anagram of another word y if we can produce y by
    rearranging the letters of x.

    Inputs:
    - line 1:: an integer T (number of test cases)
    - for each T:: a string

    Output:
    - An integer corresponding to each test case is printed in a different
    line, i.e. the number of changes required for each test case.
    Print −1 if it is not possible.
"""


from collections import Counter
for _ in range(int(input())):
    s = input()
    l = len(s)
    if l % 2 == 1:
        print(-1)
    else:
        print(sum((Counter(s[:len(s)//2]) - Counter(s[len(s)//2:])).values()))