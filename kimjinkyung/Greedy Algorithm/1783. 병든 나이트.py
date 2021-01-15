# -*- coding: utf-8 -*-
"""
Created on Fri Jan 15 13:53:10 2021

@author: lxs_9
"""
# Greedy Algorithm
# 1783. 병든 나이트

# N: row M: column
# N, M <= 2,000,000,000
# print maximum available number

N, M = map(int, input().split()) 

# Night can't anywhere
if N == 1: 
        count = 1 
        
# Night can move 1 to upper and lower
elif N == 2: 
        count = min(4, (M-1)//2 + 1) 
        
# N >= 3, M < 7
# The maximum number of movements is M-1, 
# but the maximum number of movements cannot exceed 3.
# The number of squares visited is equal to the low of 4 and M.
elif M < 7: 
        count = min(4, M) 

#use all 4 ways
else:
    count = (2 + (M-5)) + 1 
    
print(count)