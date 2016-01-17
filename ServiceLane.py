#!/bin/python3
""" Service Lane:

    Calvin is driving his favorite vehicle on the 101 freeway. He notices
    that the check engine light of his vehicle is on, and he wants to
    service it immediately to avoid any risks. Luckily, a service lane
    runs parallel to the highway. The length of the service lane is N units.
    The service lane consists of N segments of equal length and different
    width.

    Calvin can enter to and exit from any segment. Let's call the entry
    segment as index i and the exit segment as index j. Assume that the exit
    segment lies after the entry segment (i≤j) and 0≤i. Calvin has to pass
    through all segments from index i to index j (both inclusive).

    Calvin has three types of vehicles - bike, car, and truck - represented
    by 1, 2 and 3, respectively. These numbers also denote the width of the
    vehicle.

    You are given an array width of length N, where width[k] represents the
    width of the kth segment of the service lane. It is guaranteed that while
    servicing he can pass through at most 1000 segments, including the entry
    and exit segments.

    - If width[k]=1, only the bike can pass through the kth segment.
    - If width[k]=2, the bike and the car can pass through the kth segment.
    - If width[k]=3, all three vehicles can pass through the kth segment.

    Given the entry and exit point of Calvin's vehicle in the service lane,
    output the type of the largest vehicle which can pass through the service
    lane (including the entry and exit segments).

    Inputs:
    - line 1:: two integers N (the length of the freeway), T (number of test
      cases)
    - line 2:: a space-separated array of N integers representing the road
    - for T test cases:
        - two space-separated integers i (index of the segment where calvin
          enters the service lane) and j (index of the segment where Calvin
          exits the service lane)

    Outputs:
    - for each test case, print the number that represents the largest vehicle
      type that can pass through the service lane
"""


# Get the length of the road (n) and test cases (t)
temp = [int(a_temp) for a_temp in input().strip().split(' ')]
(n, t) = (temp[0], temp[1])

# Get the road array
road = [int(a_temp) for a_temp in input().strip().split(' ')]

# loop through all of the test cases
test_cases = []
for x in range(t):
    # get i and j
    temp = [int(a_temp) for a_temp in input().strip().split(' ')]
    (i, j) = (temp[0], temp[1])

    # find the minimum road width between points i and j
    road_width = min(road[i:j+1])
    test_cases.append(road_width)

# print the results
for result in test_cases:
    print(result)