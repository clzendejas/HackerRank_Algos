#!/bin/python3
""" Library Fine:

    The Head Librarian at a library wants you to create a program that
    calculates the fine for returning a book after the return date. You
    are given the actual and the expected return dates.
    Calculate the fine as follows:

    1. If the book is returned on or before the expected return date,
       no fine will be charged. In other words, the fine is 0.
    2. If the book is returned in the same calendar month as the expected
       return date, the fine = 15 Hackos × the number of late days.
    3. If the book is not returned in the same calendar month but in the
       same calendar year as the expected return date, the
       fine = 500 Hackos × the number of late months.
    4. If the book is not returned in the same calendar year,
       the fine is fixed at 10000 Hackos.

    Inputs:
    - line 1:: actual return date in D M YYYY format
    - line 2:: expected return date in D M YYYY format

    Output:
    - a single value representing the fine
"""


def fine_calculator(act, exp):
    # test that the years are the same
    if act[2] > exp[2]:
        return 10000
    elif act[2] == exp[2] and act[1] > exp[1]:
        return (act[1] - exp[1]) * 500
    elif act[2] == exp[2] and act[1] == exp[1] and act[0] > exp[0]:
        return (act[0] - exp[0]) * 15
    else:
        return 0


# Get the actual and expected return date
actual_return = [int(i) for i in input().strip().split(' ')]
expected_return = [int(i) for i in input().strip().split(' ')]

# test the dates and generate a fine
print(fine_calculator(actual_return, expected_return))