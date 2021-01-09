# -*- coding: utf-8 -*-
"""
Created on Sat Jan  9 19:12:50 2021

@author: lxs_9
"""
# Greedy Algorithm
# 11047. 동전 0

# Type input(the number)
N, K = map(int, input().split())
# Store each coins by lines
coins = [int(input()) for _ in range(N)]

# Variable for store coin number
coin_num = 0

# To count from the largest coin,
# The index of the coin must start at [-1]
# So the for-loop range set (1, N+1)
for i in range(1, N+1):
    
    coin = coins[-i]
    
    # 
    if K >= coin : 
        num = K//coin
        K -= coin*num
        coin_num += num
        
# Print the number of coins
print(coin_num)
