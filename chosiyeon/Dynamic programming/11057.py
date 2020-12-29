# dp[n] 은 n 자리 수 일때
# dp[1] = 1 1 1 1 1 1 1 1 1 1
# dp[2] = 10 9 8 7 6 5 4 3 2 1
# dp[3] = ..... 16 6 3 1 

n = int(input())

dp = [[0] * 10 for _ in range(n+1)]
dp[1] = [1 for _ in range(10)]

for i in range(2,n+1):
    for j in range(0, 10):
        for m in range(j, 10):
            dp[i][j] = dp[i][j] + dp[i-1][m]

print(sum(dp[n]) % 10007)