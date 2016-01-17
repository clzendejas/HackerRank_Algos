#!/bin/python3
""" Cavity Map:

    You are given a square map of size n×n. Each cell of the map has a
    value denoting its depth. We will call a cell of the map a cavity if
    and only if this cell is not on the border of the map and each cell
    adjacent to it has strictly smaller depth. Two cells are adjacent
    if they have a common side (edge).

    You need to find all the cavities on the map and depict them with
    the uppercase character X.

    Inputs:
    - line 1:: an integer N (the size of the map)
    - n lines:: a string of n positive digits(1-9) without spaces

    Output:
    - output N lines, denoting the resulting map with cavities replaced
      by an uppercase X
"""


# get the number and then put the integers into an array M
n = int(input().strip())

M = []
cavities = []
for i in range(n):
    temp = [int(i) for i in list(input().strip())]
    M.append(temp)

# Loop through the array and check for cavities
for i in range(1, n - 1, 1):
    for j in range(1, n-1, 1):
        # test the row & column to see if it's a cavity
        x = M[i][j]
        if x > M[i + 1][j] and x > M[i -1][j] and x > M[i][j - 1] and x > M[i][j + 1]:
            cavities.append((i, j))

# insert x's into the array M
for cavity in cavities:
    M[cavity[0]][cavity[1]] = 'X'

# print the result
for row in M:
    row = [str(i) for i in row]
    print(''.join(row))