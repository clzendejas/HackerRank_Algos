#!/bin/python3
""" Utopian Tree:

    The Utopian Tree goes through 2 cycles of growth every year. Each spring,
    it doubles in height. Each summer, its height increases by 1 meter.

    Laura plants a Utopian Tree sapling with a height of 1 meter at the
    onset of spring. How tall will her tree be after N growth cycles?

    Inputs:
    - line 1: an integer T (number of Test cases)
    - for each T test cases:
        - line 1: an integer N, denoting the number of growth cycles

    Output:
    - For each test cse, print the height of the Utopian tree after N cycles
"""


def growth_after_n_years(years):
    """
    Given yearly growth of 2n + 1 where n = height at year 0 (1 meter)
    growth over n years can be tracked with the following closed-form eq:
    -- 2**years + (2**years - 1)

    :param years: the number of years the tree is growing for
    :return: an integer of the trees height
    """
    return 2**years + (2**years - 1)


# get number of test cases
t = int(input().strip())

# get the test case
test_cases = []
for i in range(t):
    n = int(input().strip())
    if n % 2 == 0:
        # if there are an even number of growth cycles
        height = growth_after_n_years(n/2)
    else:
        height = growth_after_n_years(n//2 + 1) - 1

    # append to the test_cases list
    test_cases.append(int(height))

# print the test cases
for result in test_cases:
    print(result)