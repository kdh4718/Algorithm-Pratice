n = int(input())
building = [list(map(int, input().split())) for _ in range(n)]
stack = [0]
count = 0

for i in range(len(building)):
    h = building[i][1]
    if h > stack[-1]:
        count += 1
        stack.append(h)
    else:
        while stack and stack[-1] > h:
            stack.pop()

        if stack[-1] < h:
            count += 1
            stack.append(h)

print(count)
