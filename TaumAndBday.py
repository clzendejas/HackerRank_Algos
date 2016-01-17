#!/bin/python3
""" Taum and B'day

    Taum is planning to celebrate the birthday of his friend, Diksha.
    There are two types of gifts that Diksha wants from Taum: one is black
    and the other is white. To make her happy, Taum has to buy B number of
    black gifts and W number of white gifts.

    - The cost of each black gift is X units.
    - The cost of every white gift is Y units.
    - The cost of converting each black gift into white gift or vice versa
      is Z units.

    Help Taum by deducing the minimum amount he needs to spend on gifts.

    Inputs:
    - line 1:: an integer T (test cases)
    - for each test case T:
        - line 1:: integers B and W
        - line 2:: the values of integers X, Y, and Z (space-separated)

    Output:
    - T lines, each containing the minimum amount of units Taum needs to
      spend on gifts
"""


# get the test cases
t = int(input().strip())

test_cases = []
# iterate through t and start getting test cases
for i in range(t):
    # Get Black, White, X, Y, and Z
    temp = [int(a_temp) for a_temp in input().strip().split(' ')]
    (B, W) = (temp[0], temp[1])
    temp = [int(a_temp) for a_temp in input().strip().split(' ')]
    (X, Y, Z) = (temp[0], temp[1], temp[2])

    # find number of units willing to spend on B & W
    B_units = min(X, Y + Z) * B
    W_units = min(Y, X + Z) * W
    test_cases.append(B_units + W_units)

# print all of the test cases
for result in test_cases:
    print(result)