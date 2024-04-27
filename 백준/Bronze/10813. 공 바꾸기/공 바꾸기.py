n, m = map(int, input().split())
buc = []
for i in range(n):
    buc.append(i+1)
for i in range(m):
    a, b = map(int, input().split())
    buc[a-1], buc[b-1] = buc[b-1], buc[a-1]
print(*buc)