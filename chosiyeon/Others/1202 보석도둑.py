n, k = map(int, input().split())

jewel_info = [0] * n
jewel_price = [0] * n
jewel_cost = [0] * k

for i in range(n):
    jewel_info[i], jewel_price[i] = map(int, input().split())
for i in range(k):
    jewel_cost[i] = input()

print(jewel_cost)