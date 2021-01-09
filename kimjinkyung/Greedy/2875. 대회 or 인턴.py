# -*- coding: utf-8 -*-
"""
Created on Sat Jan  9 19:59:38 2021

@author: lxs_9
"""
# Greedy Algorithm
# 2875. 대회 or 인턴

# Type input(the number of boys, girls, internship)
N, M, K = map(int, input().split())
# variable for counting the number of teams
count = 0

# Except for those who participate in internships,
# If there are enough people to form a team,
# Subtract that number from N, M.
# And count as the number of teams.
while N >= 2 and M >= 1 and N+M > K+3:
    N -= 2
    M -= 1
    count += 1

# Print Result
print(count)
