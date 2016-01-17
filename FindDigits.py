#!/bin/python3
""" Find Digits:

    Given an integer, N, traverse its digits (d1,d2,...,dn) and determine how
    many digits evenly divide N (i.e.: count the number of times N divided by
    each digit di has a remainder of 0). Print the number of evenly
    divisible digits.

    Note: Each digit is considered to be unique, so each occurrence of the
    same evenly divisible digit should be counted
    (i.e.: for N=111, the answer is 3).

    Inputs:
    - line 1:: an integer T (number of Test cases)
    - for each test case:
        - line 1: an integer N

    Output:
    - for each test case, count and print on a new line the number of digits
      in N that are able to evenly divide N.
"""


# get number of test cases
t = int(input().strip())

# get the test case
test_cases = []
for i in range(t):
    # create a list of each digit in the number
    temp = input().strip()
    n = int(temp)
    digit_list = [int(i) for i in list(temp)]

    # loop through n and count the number of evenly divisible digits
    digit_count = 0
    for digit in digit_list:
        if digit != 0:
            if n % digit == 0:
                digit_count += 1

    test_cases.append(digit_count)

# print the results
for result in test_cases:
    print(result)