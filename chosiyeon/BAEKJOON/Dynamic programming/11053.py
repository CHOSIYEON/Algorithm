# dp[i] 는 list[i]까지 제일 길게 만들 수 있는 부분 배열의 길이
# dp[3] 은 list[0], list[1], list[2], list[3] 즉, 4개의 길이의 배열 안에서 만들 수 있는 최대 부분 배열의 수

n = int(input())

list = list(map(int, input().split()))
dp = [1 for _ in range(n)]

for i in range(n):
    for j in range(i):
        if list[i] > list[j]:
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))
