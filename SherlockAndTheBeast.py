#!/bin/python3
""" Sherlock and the Beast:

    Sherlock Holmes suspects his archenemy, Professor Moriarty, is once again
    plotting something diabolical. Sherlock's companion, Dr. Watson, suggests
    Moriarty may be responsible for MI6's recent issues with their
    supercomputer, The Beast.

    Shortly after resolving to investigate, Sherlock receives a note from
    Moriarty boasting about infecting The Beast with a virus; however,
    he also gives him a clue—a number, N. Sherlock determines the key to
    removing the virus is to find the largest Decent Number having N digits.

    A Decent Number has the following properties:

    1. Its digits can only be 3's and/or 5's.
    2. The number of 3's it contains is divisible by 5.
    3. The number of 5's it contains is divisible by 3.

    Inputs:
    - line 1: an integer T (number of Test cases)
    - for each T test cases:
        - An integer N (number of digits in the number)

    Output:
    - Print the largest decent number having N digits, if no such number
      exists, print -1
"""


def find_largest_decent_no(x):
    """
    This function takes a number of digits (x) and computes the largest decent
    number
    :param x: any integer of digits
    :return: the largest decent number or -1 if one doesn't exist
    """
    if x < 3:
        return -1
    elif x % 3 == 0:
        return int('5'*x)
    elif x == 5:
        return 33333
    else:
        for num in range((x//3)*3, -1, -3):
            diff = x - num
            if diff % 5 == 0:
                return int('5'*num + '3'*diff)

    # if nothing has returned yet, there is no decent number
    return -1


# get number of test cases
t = int(input().strip())

# get the test case
test_cases = []
for i in range(t):
    n = int(input().strip())
    test_cases.append(find_largest_decent_no(n))

# print out the results
for result in test_cases:
    print(result)