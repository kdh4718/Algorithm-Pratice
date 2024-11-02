from collections import deque

n, m = map(int, input().split())
child = [[] for _ in range(n + 1)]
degree = [0] * (n + 1)
q = deque()
answer = []
for _ in range(m):
    num, *order = list(map(int, input().split()))
    for i in range(len(order) - 1):
        child[order[i]].append(order[i + 1])
        degree[order[i + 1]] += 1

for i in range(1, n + 1):
    if degree[i] == 0:
        q.append(i)

while q:
    x = q.popleft()
    answer.append(x)

    for num in child[x]:
        degree[num] -= 1
        if degree[num] == 0:
            q.append(num)

if len(answer) < n:
    print(0)
else:
    for a in answer:
        print(a)
