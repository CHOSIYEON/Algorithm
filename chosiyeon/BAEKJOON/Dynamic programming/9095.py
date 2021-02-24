# n을 나타낼 수 있는 방법의 수를 dp[n] 이라고 한다.
# dp[n] = dp[n-1] + dp[n-2] + dp[n-3]
# 런타임 에러 조심하기

n = int(input())

def answer(x):
    if x == 1:
        return 1
    elif x == 2:
        return 2
    elif x == 3:
        return 4
    return answer(x-1)+answer(x-2)+answer(x-3)

for i in range(n):
    num = int(input())
    print(answer(num))




