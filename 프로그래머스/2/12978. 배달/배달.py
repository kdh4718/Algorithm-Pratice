from collections import deque

def dijk(graph, node):
    q = deque()
    q.append((1, node[1]))
    
    while q:
        num, now = q.popleft()

        for n in now:
            dist = graph[num] + n[1]
            if dist < graph[n[0]]:
                graph[n[0]] = dist
                q.append((n[0], node[n[0]]))
            
    return graph

def solution(N, road, K):
    answer = 0
    graph = [1e9]*(N+1)
    graph[1] = 0
    node = [[] for _ in range(N+1)]
    
    for r in road:
        node[r[0]].append([r[1], r[2]])
        node[r[1]].append([r[0], r[2]])
    
    graph = dijk(graph, node)

    answer = sum([1 for i in graph if i <= K])
    return answer