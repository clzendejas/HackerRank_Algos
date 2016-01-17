#!/bin/python3
""" Manasa and Stones:

    Manasa is out on a hike with friends. She finds a trail of stones with
    numbers on them. She starts following the trail and notices that two
    consecutive stones have a difference of either a or b. Legend has it that
    there is a treasure trove at the end of the trail and if Manasa can guess
    the value of the last stone, the treasure would be hers. Given that the
    number on the first stone was 0, find all the possible values for the
    number on the last stone.

    Note: The numbers on the stones are in increasing order.

    Inputs:
    - line 1:: an integer T (number of test cases)
    - for each test case:
        - line 1:: an integer n (the number of stones)
        - line 2:: an integer a
        - line 3:: an integer b

    Output:
    - a space-separated list of numbers which are the possible values
      of the last stone in increasing order
"""


# get the test cases
t = int(input().strip())

test_cases = []
# iterate through t
for i in range(t):
    # get n, a, and b
    n = int(input().strip())
    a = int(input().strip())
    b = int(input().strip())

    (b, a) = sorted((a, b))
    # closed form solution to create the terminal branches in a binary tree
    if a == b:
        stone_values = [a*(n - 1)]
    else:
        stone_values = [((a*i) + b*(n - i - 1)) for i in range(n)]

    # take the final stone_values and change into a string
    stone_values = [str(i) for i in list(stone_values)]
    test_cases.append(' '.join(stone_values))

# print all of the test cases
for result in test_cases:
    print(result)