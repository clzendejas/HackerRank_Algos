""" Simple Array Sum:

    You are given an array of integers of size N. Can you find the sum of the
    elements in the array?

    Input:
    - Line 1:: an integer N
    - line 2:: an N space-separated list of integers representing the array
               elements

    Output:
    A single value equal to the sum of the elements in the array
"""
#!/bin/python
N = int(input())
# Input Line 2, an N number space delimited array
arr = map(int, raw_input().strip().split(' '))

arr_sum = 0
for i in arr:
    arr_sum += i

print(arr_sum)