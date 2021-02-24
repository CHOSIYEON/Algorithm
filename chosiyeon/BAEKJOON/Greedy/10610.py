# 일의자리는 0, 각 자리수의 합이 3의 배수여야 함

n = list(map(int,input()))

if 0 in n and sum(n) % 3 == 0:
    n.sort(reverse=True)
    print(int(''.join(list(map(str,n)))))
else:
    print(-1)


