#!/bin/python3
""" ACM ICPC Team:

    You are given a list of N people who are attending ACM-ICPC World Finals.
    Each of them are either well versed in a topic or they are not. Find out
    the maximum number of topics a 2-person team can know. And also find out
    how many teams can know that maximum number of topics.

    Note: Suppose a, b, and c are three different people, then (a,b) and (b,c)
    are counted as two different teams.

    Inputs:
    - line 1:: two space-separated integers N (number of people) and
               M (number of topics)
    - for N lines:: a binary string of length M, 0 = person N does not know
                    topic i, and 1 = person knows topic i

    Output:
    - line 1: output the maximum number of topics a 2-person team can know
    - line 2: print the number of 2-person teams that can know the maximum
              number of topics
"""


# get N and M
temp = [int(i) for i in input().strip().split(' ')]
(n, m) = (temp[0], temp[1])

# get the topics per person
skills_list = []
for i in range(n):
    # store list as an integer <- binary string
    skills = int(input().strip(), 2)
    skills_list.append(skills)

# create combinations of teams
team_skills_list = [bin(skills_list[i] | skills_list[j]).count('1')
                    for i in range(n - 1) for j in range(i + 1, n, 1)]

# get the top skills
max_skills = max(team_skills_list)
max_teams = team_skills_list.count(max_skills)

# print results
print(max_skills)
print(max_teams)