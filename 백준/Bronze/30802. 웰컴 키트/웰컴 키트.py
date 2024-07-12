import math

n = int(input())
tshirt = list(map(int, input().split()))
t, p = map(int, input().split())

tcnt = 0

for i in tshirt:
    tcnt += math.ceil(i/t)

print(tcnt)
print(n//p, n%p)