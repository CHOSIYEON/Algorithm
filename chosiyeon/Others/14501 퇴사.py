n = int(input())
data = list(list(map(int, input().split())) for _ in range(n))
dp = [0] * (n+1)


for i in range(n-1, -1, -1):
    if i + data[i][0] <= n:
        #dp[i] = max(data[i][1] + dp[i+data[i][0]], dp[i+1])
        dp[i] = max(data[i][1] + max(dp[i+data[i][0]:]), dp[i+data[i][0]])

print(max(dp))
