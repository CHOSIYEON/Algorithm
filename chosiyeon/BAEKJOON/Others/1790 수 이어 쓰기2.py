n, k = map(int, input().split())
data = ""

# 메모리 초과
# for i in range(1, n+1):
#     data += str(i)
#
# if len(data) < k:
#     print(-1)
# else:
#     data = list(data)
#     print(data[k - 1])
check_k = k
check = False
result = 1
for i in range(n//10+1):
    num = 9 * (i+1) * pow(10,i)
    check_k -= num
    if check_k < 0:
        check_k += num
        check = True
        count = (check_k-1) // (i+1)
        result = pow(10, i) + count
        result = list(str(result))
        print(result)
        print(result[(check_k-1) % (i+1)])
        break
    if i == n//10:
        if check_k > 0:
            print(-1)

print(check_k)




