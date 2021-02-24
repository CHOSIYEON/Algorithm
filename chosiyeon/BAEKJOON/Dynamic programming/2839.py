# 3보다는 5로 먼저 나눠야 한다.
# 그것이 나눌 수 있는 값 중 최소값이 될 것
# 그러니 3킬로그램씩 담다가 5킬로그램으로 나눠떨어지는 순간이 최소값
# 3으로만 나눠질수도 있으니 sugar 가 0인지 체크해줘야함

sugar = int(input())
num = 0
answer = -1

while sugar >= 0:
    if sugar%5==0 :
        num = num + int(sugar / 5)
        sugar = sugar%5
        answer = num
        break
    sugar = sugar - 3
    num = num + 1
    if(sugar == 0):
        answer = num

print(answer)





