n = int(input())
arr = [0] + [int(input()) for _ in range(n)]
result = []

def dfs(start, current, visited, path):
    visited[current] = True
    path.append(current)

    next_node = arr[current]

    if not visited[next_node]:
        dfs(start, next_node, visited, path)
    elif next_node == start:
        result.extend(path)

for i in range(1, n + 1):
    visited = [False] * (n + 1)
    dfs(i, i, visited, [])

result = sorted(set(result))
print(len(result))
for num in result:
    print(num)
