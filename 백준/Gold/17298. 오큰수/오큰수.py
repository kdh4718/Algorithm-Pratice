n = int(input())
number = list(map(int, input().split()))
nge = [0]*n
stack = []

for i, num in enumerate(number):
    while stack and stack[-1][1] < num:
        x, y = stack.pop()
        nge[x] = num

    stack.append([i, num])

for i in range(n):
    if nge[i] == 0:
        nge[i] = -1

print(*nge)
