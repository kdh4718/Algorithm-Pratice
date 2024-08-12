from collections import deque

n, k, m = map(int, input().split())
q = deque(i for i in range(1, n+1))
flag = True
josephus = []

while q:
    if flag:
        for i in range(k-1):
            q.append(q.popleft())
        josephus.append(str(q.popleft()))
        print(josephus[-1])
    else:
        for i in range(k-1):
            q.appendleft(q.pop())
        josephus.append(str(q.pop()))
        print(josephus[-1])

    if len(josephus) % m == 0:
        flag = not flag