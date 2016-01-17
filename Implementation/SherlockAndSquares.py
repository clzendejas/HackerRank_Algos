#!/bin/python3
""" Sherlock and Squares

    Watson gives two integers (A and B) to Sherlock and asks if he can count
    the number of square integers between A and B (both inclusive).

    Note: A square integer is an integer which is the square of any integer.
    For example, 1, 4, 9, and 16 are some of the square integers as they are
    squares of 1, 2, 3, and 4, respectively.

    Input:
    - line 1:: an integer T (number of Test cases)
    - for each test case T:
        - line 1:: a space-separated list denoting A and B

    Output:
    - for each test case, print the required answer in a new line
"""

# import math
import math

# get number of test cases
t = int(input().strip())

# loop through t number of test cases
test_cases = []
for i in range(t):
    # get the integers a and b
    temp = [int(a_temp) for a_temp in input().strip().split(' ')]
    (a, b) = (temp[0], temp[1])
    num_squares = math.floor(math.sqrt(b)) - math.ceil(math.sqrt(a)) + 1
    test_cases.append(int(num_squares))

# print the results
for result in test_cases:
    print(result)