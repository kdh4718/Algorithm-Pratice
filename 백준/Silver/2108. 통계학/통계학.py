from collections import Counter
import sys
n = int(sys.stdin.readline())
l = []
for i in range(n):
    l.append(int(sys.stdin.readline()))
b = sorted(l)
a = Counter(l)
c = []
for i, j  in a.items():
    if j == max(a.values()):
        c.append(i)
d = sorted(c)
print(round(sum(b)/n))
print(b[len(b)//2])
print(d[1] if len(d) > 1 else d[0])
print(abs(max(l)-min(l)))