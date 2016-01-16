""" Diagonal Difference:

    Given a square matrix of size N x N, calculate the absolute difference
    between the sums of its diagonals

    Input:
    - line 1:: A single integer N
    - next N lines:: a space-separated list of integers describing each row's
                     columns

    Output:
    - Print the absolute difference between the two sums of the matrix's
      diagonals as a single integer
"""

#!/bin/python3

import sys

# Get the dimension of the Array
n = int(input().strip())

# create an array to store the lists in and collect the N rows
j = n - 1
test_diag1 = 0
test_diag2 = 0
for i in range(n):
    # must use a list comprehension in a loop rather than a map
    temp = [int(a_temp) for a_temp in input().strip().split(' ')]
    test_diag1 += temp[i]
    test_diag2 += temp[j]
    j -= 1

print(abs(test_diag1 - test_diag2))