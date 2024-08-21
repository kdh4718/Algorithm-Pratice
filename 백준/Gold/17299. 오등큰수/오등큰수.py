from collections import Counter

n = int(input())
number = list(map(int, input().split()))
nge = [0]*n
stack = []
ct = Counter(number)

for i, num in enumerate(number):
    while stack and stack[-1][2] < ct[num]:
        x, y, z = stack.pop()
        nge[x] = num

    stack.append([i, num, ct[num]])

for i in range(n):
    if nge[i] == 0:
        nge[i] = -1

print(*nge)
