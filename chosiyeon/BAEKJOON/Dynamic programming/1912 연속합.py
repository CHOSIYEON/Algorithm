n = int(input())
list = list(map(int, input().split()))
dp = [0 for _ in range(n)]

dp[0] = list[0]

for i in range(1,n):
    dp[i] = max(dp[i-1]+list[i], list[i])

print(max(dp))
