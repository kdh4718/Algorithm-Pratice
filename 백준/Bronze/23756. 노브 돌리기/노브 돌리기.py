n = int(input())
c = int(input())
sum = 0

for _ in range(n):
    t = int(input())
    sum += min((t - c) % 360, (c - t) % 360)
    c = t

print(sum)
