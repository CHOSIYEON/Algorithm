# 시간이 적게 걸리는 사람부터 해주면 됨
n = int(input())
time = list(map(int, input().split()))
total = 0
time.sort()

for i in range(n):
    total = total +(n-i) * time[i]

print(total)