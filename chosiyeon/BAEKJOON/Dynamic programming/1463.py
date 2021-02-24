# 1. dp[i] = dp[i//3] + 1
# 2. dp[i] = dp[i//2] + 1
# 3. dp[i] = dp[i-1] + 1
# i 는 그냥 숫자 N을 의미
# dp[n] 은 n 이 1로 만들도록 하는 연산의 최소 수
# 즉, 2부터 N까지 1,2,3 방법  셋 중 제일 작은 값으로 배열을 채워서
# dp[n] 을 출력

n = int(input())

dp = [0 for _ in range(n + 1)]

for i in range(2, n+1):
    dp[i] = dp[i-1] + 1

    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i//2]+1)
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i//3]+1)

print(dp[n])
