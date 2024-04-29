from collections import deque

n = int(input())
num1, num2 = map(int, input().split())
m = int(input())
graph = [[] for _ in range(n+1)]
cnt = [0]*(n+1)

def bfs(num):
    q = deque()
    q.append(num)
    
    while q:
        num = q.popleft()
        
        for i in graph[num]:
            if not cnt[i]:
                cnt[i] = cnt[num] + 1
                q.append(i)
    
    return

for i in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

bfs(num1)
print(cnt[num2] if cnt[num2] else -1)