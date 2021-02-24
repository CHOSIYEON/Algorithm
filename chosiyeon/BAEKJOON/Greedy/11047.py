# k보다 크지 않은 값 중 최대인 값으로 나누면 됨

n, k = map(int, input().split())

cost = [int(input()) for i in range(n)]
count = 0

for i in range(1,n+1):
    coin = cost[-i]
    if k>=coin:
        num = k//coin
        k %= coin
        count += num

print(count)

