from collections import deque

k, n = map(int, input().split())
q = deque(i for i in range(1, k+1))
josephus = []

while q:
    for i in range(n-1):
        q.append(q.popleft())
    josephus.append(str(q.popleft()))

print("<" + ", ".join(josephus) + ">")

