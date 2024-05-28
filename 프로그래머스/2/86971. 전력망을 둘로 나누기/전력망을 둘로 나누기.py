from collections import deque

def solution(n, wires):
    answer = n
    graph = [[] for _ in range(n+1)]
    
    for wire in wires:
        graph[wire[0]].append(wire[1])
        graph[wire[1]].append(wire[0])
        
    def bfs(s):
        visited = [False]*(n+1)
        cnt = 0
        q = deque()
        q.append(s)
        
        while q:
            num = q.popleft()
            visited[num] = True
            
            for i in graph[num]:
                if not visited[i]:
                    q.append(i)
                    cnt += 1
        
        return cnt
    
    for wire in wires:
        graph[wire[0]].remove(wire[1])
        graph[wire[1]].remove(wire[0])
        
        answer = min(abs(bfs(wire[0]) - bfs(wire[1])), answer)
        
        graph[wire[0]].append(wire[1])
        graph[wire[1]].append(wire[0])
    
    return answer