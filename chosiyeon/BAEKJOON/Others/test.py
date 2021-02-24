b = list(input())

count = b.count('(')

if count*2 == len(b):
    print("YES")
else:
    print("NO")