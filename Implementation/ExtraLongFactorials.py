#!/bin/python3
""" Extra Long Factorials:

    You are given an integer N. Print the factorial of this number

    Inputs:
    - line 1:: a single integer N

    Output:
    - the factorial of integer N
"""

import math

# nothing special, python does this automagically
n = int(input().strip())
print(math.factorial(n))