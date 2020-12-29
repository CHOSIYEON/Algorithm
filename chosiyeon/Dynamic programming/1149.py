# 한집은 양쪽 집과 색이 달라야함
# 2번째 집까지 칠하는 비용 = 1번째 집까지 칠한 비용 + 2번째 집 칠할 비용
# 3번째 집까지 칠하는 비용 = 2번째 집까지 칠한 비용 + 3번째 집 칠할 비용
# N번째 집까지 칠하는 비용 = N-1번째 집까지 칠한 비용 + N번째 집 칠할 비용
# cost 배열에 문제에서 제공하는 N번째 집 별 R, G, B 값의 비용을 저장
# dp 배열은 누적 비용
# 첫번째 집을 R, G, B 어떤 색으로 칠하냐에 따라 전체 비용이 달라지기 때문에 각각의 경우 모두 계산
# 그리고 최종적으로 제일 작은 값 출력
# 즉, dp[N] = dp[N-1] + cost[R or G or B]

n = int(input())

cost = [[0 for col in range(3)]for row in range(1001)]
dp = [[1000 for col in range(3)]for row in range(1001)]

for i in range(1, n+1):
   a, b, c = map(int, input().split())
   cost[i][0] = a
   cost[i][1] = b
   cost[i][2] = c

dp[0][0] = 0
dp[0][1] = 0
dp[0][2] = 0

for i in range(1, n+1):
    dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + cost[i][0]
    dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + cost[i][1]
    dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + cost[i][2]

print(min(dp[n][0], dp[n][1], dp[n][2]))




