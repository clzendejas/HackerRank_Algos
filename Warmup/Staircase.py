#!/bin/python3
""" Staircase:

    Given a required height N, draw a staircase with '#' symbols that goes
    from left to right, and is N steps high

    Input:
    - line 1:: You are given an integer N - the staircase height

    Output:
    print a staircase of height N
"""

# Input Line 1 (N)
n = int(input().strip())

# Loop through n times and create steps
for i in range(n):
    steps = '#'*(i+1)
    spaces = ' '*(n - 1 - i)
    print(spaces + steps)