import sys
input = sys.stdin.readline

n, h = map(int, input().split())
down, up = [0]*(h+1), [0]*(h+1)
minNum, count = 1e9, 0

for i in range(n):
    if i % 2 == 0:
        down[int(input())] += 1
    else:
        up[int(input())] += 1

for i in range(h - 1, 0, -1):
    down[i] += down[i + 1]
    up[i] += up[i + 1]

for i in range(1, h + 1):

    if minNum > (down[i] + up[h - i + 1]):
        minNum = (down[i] + up[h - i + 1])
        count = 1
    elif minNum == (down[i] + up[h - i + 1]):
        count += 1

print(minNum, count)