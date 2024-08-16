n = int(input())
building = []
stack = []
count = 0

for _ in range(n):
    building.append(int(input()))
building.append(1e9)

for i, j in enumerate(building):
    while stack and stack[-1][1] <= j:
        x, y = stack.pop()
        count += (i - x - 1)
    stack.append([i, j])

print(count)