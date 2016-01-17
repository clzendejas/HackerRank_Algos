#!/bin/python3
""" The Grid Search:

    Given a 2D array of digits, try to find the location of a given 2D pattern
    of digits.

    Inputs:
    - line 1:: an integer T (the number of test cases)
    - for each test case:
        - line 1:: two space-separated integers R (rows) and C (columns)
                   contained in grid G
        - next R lines:: a string of C digits
        - next line:: two space-separated integers r (rows) and c (columns)
                      contained in the pattern grid P
        - next r lines:: a string of c digits

    Outputs:
    - Display 'YES' or 'NO' depending on if you find pattern P in grid G
"""


# get number of test cases
t = int(input().strip())

# loop through t number of test cases
test_cases = []
for i in range(t):
    # get the Grid G's rows and columns
    temp = [int(a_temp) for a_temp in input().strip().split(' ')]
    (R, C) = (temp[0], temp[1])
    G = []
    for i in range(R):
        G_row = list(input().strip())
        G.append(G_row)

     # get the pattern grid P's rows and columns
    temp = [int(a_temp) for a_temp in input().strip().split(' ')]
    (r, c) = (temp[0], temp[1])
    P = []
    for i in range(r):
        P_row = list(input().strip())
        P.append(P_row)

    # search for the patterns by brute force
    found = False
    for row_num in range(R - r + 1):
        for col_num in range(C - c + 1):
            sub_matches = False
            # loop through rows and test for matches
            for j in range(r):
                test_row = G[row_num + j][col_num:col_num + c]
                if test_row == P[j]:
                    sub_matches = True
                else:
                    sub_matches = False
                    break
            # check if sub_matches still matches
            if sub_matches:
                found = True
                break

        # break again if found
        if found:
            break
    test_result = 'YES' if found else 'NO'
    test_cases.append(test_result)

# print out the result
for result in test_cases:
    print(result)