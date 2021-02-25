n, k = map(int, input().split())

for i in range(n//10+1):
    num = 9 * (i+1) * pow(10,i)
    k -= num
    if k < 0:
        k += num
        count = (k-1) // (i+1)
        result = pow(10, i) + count
        if result <= n:
            result = list(str(result))
            print(result[(k - 1) % (i + 1)])
        else:
            print(-1)
        break

# 메모리 초과
# data = ""
# for i in range(1, n+1):
#     data += str(i)
#
# if len(data) < k:
#     print(-1)
# else:
#     data = list(data)
#     print(data[k - 1])