# 1은 곱한 것 보다 더한것이 큼 : 1*2 , 1+2
# 0은 음수와 곱하면 합이 더 커짐

n = int(input())
num = [int(input()) for i in range(n)]

pos = []
neg = []
total = 0

for i in num:
    if i <=0:
        neg.append(i)
    elif i == 1:
        total += 1
    else:
        pos.append(i)

neg.sort()
pos.sort(reverse=True)

for i in range(0,len(neg),2):
    if i+1 < len(neg):
        total += neg[i]*neg[i+1]
    else:
        total += neg[i]

for i in range(0,len(pos),2):
    if i+1 < len(pos):
        total += pos[i]*pos[i+1]
    else:
        total += pos[i]

print(total)