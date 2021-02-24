# dp[n] 은 2Xn 을 채우는 방법의 수
# dp[1] = 1
# dp[2] = 2
# dp[3] = 3
# dp[4] = 5
# dp[n] = dp[n-1] + dp[n-2]

n = int(input())

dp = [0 for _ in range(n + 1)]

dp[0] = 1
dp[1] = 2

for i in range(2, n+1):
    dp[i] = dp[i-1] + dp[i-2]

print(dp[n-1]%10007)
