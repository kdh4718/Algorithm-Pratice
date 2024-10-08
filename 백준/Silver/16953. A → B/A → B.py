from collections import deque

def bfs():
    q = deque([(a, 1)])
    while q:
        num, count = q.popleft()
        if num == b:
            return count
        if num * 2 <= b:
            q.append((num * 2, count + 1))
        if num * 10 + 1 <= b:
            q.append((num * 10 + 1, count + 1))

    return -1

a, b = map(int, input().split())

print(bfs())
