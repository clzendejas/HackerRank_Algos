#!/bin/python3
""" Chocolate Feast:

    Little Bob loves chocolate, and he goes to a store with $N in his pocket.
    The price of each chocolate is $C. The store offers a discount: for every
    M wrappers he gives to the store, he gets one chocolate for free. How many
    chocolates does Bob get to eat?

    Input:
    - line 1:: an integer T (number of test cases)
    - for each test case T:
        - line 1:: a space-separated array of N C M

    Output:
    - for each test case print the total number of chocolates Bob gets to eat
"""

# get number of test cases
t = int(input().strip())

# loop through t number of test cases
test_cases = []
for i in range(t):
    # get the integers n, c, m
    temp = [int(a_temp) for a_temp in input().strip().split(' ')]
    (n, c, m) = (temp[0], temp[1], temp[2])

    # determine the chocolate purchased
    purchased = n // c
    wrappers = purchased
    eaten = purchased
    # determine the number of free chocolates earned
    while wrappers >= m:
        # cash in wrappers for chocolates
        free = wrappers // m
        eaten += free
        # reduce wrappers by the number cashed in
        wrappers -= (free * m)
        # add back the free wrappers
        wrappers += free

    test_cases.append(eaten)

# print the results
for result in test_cases:
    print(result)