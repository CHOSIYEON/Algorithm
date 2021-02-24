# 팀은 여자 2명, 남자 1명
# 즉 팀의 수를 count 라고 했을 때 count*2 + count*1
# 인원 전체에서 팀을 이루는 수를 뺀 값은 k 보다 커야하고
# count*2, count*1 은 각각 n, m 보다 같거나 작아야함

n, m, k = map(int, input().split())

count = 1

while 1:
    if count * 2 + count <= n + m - k and count * 2 <= n and count <= m:
        count += 1
    else:
        break

print(count-1)