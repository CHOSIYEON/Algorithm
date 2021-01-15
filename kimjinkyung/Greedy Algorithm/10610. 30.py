# -*- coding: utf-8 -*-
"""
Created on Sat Jan  9 20:19:54 2021

@author: lxs_9
"""
# Greedy Algorithm
# 10610. 30

# Input Entered (The number)
N = input()

# Restore desceding order
N = sorted(N, reverse = True)
sum = 0

# Multiples of 30 are included 2×3×5
# So, The result should be multiple of 10
if '0' not in N:
    print(-1)

# If the number is multiple of 3
# The sum of each digit must be a multiple of 3
else:
    for i in N:
        # The sum of each digit
        sum += int(i)
    # Check the sum is multiple of 3
    if sum % 3 != 0:
        print(-1)
    else:
        print("".join(N))
