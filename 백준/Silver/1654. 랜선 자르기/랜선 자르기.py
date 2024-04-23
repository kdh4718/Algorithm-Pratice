k, n = map(int, input().split())
a = []
for i in range(k):
    a.append(int(input()))
l, h = 1, max(a)
while l <= h:
    m = (l+h)//2
    count = sum(i//m for i in a)
    if count >= n:
        l = m + 1
    else:
        h = m - 1
print(h)