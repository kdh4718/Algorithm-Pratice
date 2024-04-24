from collections import deque

t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    
    visited = [False]*10001
    q = deque()
    q.append([a, ''])
    visited[a] = True
    
    while q:
        n, c = q.popleft()
        
        if n == b:
            print(c)
            break
            
        d = n*2 % 10000
        if not visited[d]:
            visited[d] = True
            q.append([d, c + "D"])
            
        s = (n-1)%10000
        if not visited[s]:
            visited[s] = True
            q.append([s, c + "S"])
            
        l = n//1000 + (n%1000)*10
        if not visited[l]:
            visited[l] = True
            q.append([l, c + "L"])
            
        r = n//10 + (n%10)*1000
        if not visited[r]:
            visited[r] = True
            q.append([r, c + "R"])