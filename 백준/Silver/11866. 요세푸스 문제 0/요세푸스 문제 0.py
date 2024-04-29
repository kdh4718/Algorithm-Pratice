from collections import deque
n, m = map(int, input().split())
circle = deque([i for i in range(1, n+1)])
pus = []
while circle:
    for i in range(m-1):
        circle.append(circle.popleft())
    pus.append(circle.popleft())
    
print("<"+', '.join(map(str,pus))+">", end='')