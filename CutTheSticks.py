#!/bin/python3
""" Cut the Sticks:

    You are given N sticks, where the length of each stick is a positive
    integer. A cut operation is performed on the sticks such that all of
    them are reduced by the length of the smallest stick.

    Suppose we have six sticks of the following lengths:
    5 4 4 2 2 8

    Then, in one cut operation we make a cut of length 2 from each of the
    six sticks. For the next cut operation four sticks are left
    (of non-zero length), whose lengths are the following:
    3 2 2 6

    The above step is repeated until no sticks are left.

    Given the length of N sticks, print the number of sticks that are
    left before each subsequent cut operations.

    Note: For each cut operation, you have to recalcuate the length of
    smallest sticks (excluding zero-length sticks).

    Input:
    - line 1:: single integer N
    - line 2:: a space-separated array of N integers

    Output:
    - for each operation, print the number of sticks that are cut
"""


# get the number
n = int(input().strip())

# get the array of sticks
sticks = [int(a_temp) for a_temp in input().strip().split(' ')]

# perform cut operations until there are no more sticks left
while n > 0:
    print(n)
    min_length = min(sticks)
    sticks = [i - min_length for i in sticks if i - min_length > 0]
    n = len(sticks)