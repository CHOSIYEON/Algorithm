# 우선 순위 큐 사용

# n, k = map(int, input().split())
# jewel = list(list(map(int, input().split())) for _ in range(n))
# weight = list(int(input()) for _ in range(k))
#
# jewel = sorted(jewel, key = lambda x : x[1])
# weight = sorted(weight)
# result = 0
#
#
# for i in range(k):
#     pq = []
#     for j in range(n):
#         if weight[i] >= jewel[j][0]:
#             pq.append(jewel[j][1])
#     pq = sorted(pq, reverse=True)
#     print(pq)
#     result += pq[0]
#     jewel.pop(j)
#
# print(result)
