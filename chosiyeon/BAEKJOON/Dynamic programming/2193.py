# dp[i] 를 i자리 이친수의 개수
# dp[1] = 1
# dp[2] = 1
# dp[3] = 2
# dp[4] = 3
# dp[5] = 5
# dp[i] = dp[i-1] + dp[i-2]

n = int(input())

dp = [0 for _ in range(n + 1)]

dp[0] = 0
dp[1] = 1

for i in range(2, n+1):
    dp[i] = dp[i-1] + dp[i-2]

print(dp[n])