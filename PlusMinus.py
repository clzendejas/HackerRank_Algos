#!/bin/python3
""" Plus Minus:

    Given an array of integers, calculate which fraction of the elements
    are positive, negative, and zeroes, respectively. Print the decimal
    value of each fraction

    Inputs:
    - line 1:: N the size of the array
    - line 2:: a space-separated list of integers describing the array

    Outputs:
    - Print each value on its own line with the following order:
    - line 1: positive percentage
    - line 2: negative percentage
    - line 3: zeroes percentage
"""

# Input Line 1 (N)
n = int(input())
# Input Line 2, an N number space delimited array
arr = map(int, input().strip().split(' '))

positive = 0
negative = 0
zero = 0

for i in arr:
    if i > 0:
        positive += 1
    elif i < 0:
        negative += 1
    elif i == 0:
        zero += 1

print(positive/n)
print(negative/n)
print(zero/n)