# -*- coding: utf-8 -*-
"""
Created on Wed Dec 30 11:25:48 2020

@author: lxs_9
"""
# Dynamic Programming
# Bottom-Up
# Time Complexity: O(n)
# Recurrence Relation: List[N] = min(List[N/3], List[N/2], List[N-1]) + 1

# Type input
x = int(input())

# Make Array
minimum_count = [ 0 for _ in range(x+1)]
 
index = 0
while(True):
    if index > x:
        break
 
    if index <= 1:
        minimum_count[index] = 0
    else:
        temp_min = x + 1
        if index % 3 == 0:
            temp_index = int(index/3)
            temp_min = min(temp_min, minimum_count[temp_index])
 
        if index % 2 == 0:
            temp_index = int(index/2)
            temp_min = min(temp_min, minimum_count[temp_index])
 
        temp_min = min(temp_min, minimum_count[index-1])
        minimum_count[index] = int(temp_min + 1)
    index = index + 1
 
print(minimum_count[x])