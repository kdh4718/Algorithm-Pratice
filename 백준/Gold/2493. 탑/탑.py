n = int(input())
tower = list(map(int, input().split()))
distance = [0]*n
stack = []

for i in range(n):
    if not stack:
        stack.append(i)
    else:
        while stack and tower[stack[-1]] < tower[i]:
            stack.pop()

        if stack and tower[stack[-1]] >= tower[i]:
            distance[i] = stack[-1] + 1

        stack.append(i)

print(*distance)