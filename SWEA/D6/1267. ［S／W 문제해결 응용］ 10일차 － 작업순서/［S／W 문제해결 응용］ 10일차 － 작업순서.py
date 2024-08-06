from collections import deque

for test_case in range(1, 11):
    v, e = map(int, input().split())
    node = list(map(int, input().split()))
    graph = [[] for _ in range(v+1)]
    parent = [[] for _ in range(v+1)]
    routine = []

    def bfs():
        while True:
            q = deque()
            for i in range(1, v+1):
                if len(parent[i]) == 0 and i not in routine:
                    q.append(i)
                    routine.append(i)

            if len(q) == 0:
                return

            while q:
                x = q.popleft()

                for num in graph[x]:
                    parent[num].remove(x)

        return

    for i in range(0, len(node), 2):
        graph[node[i]].append(node[i+1])
        parent[node[i+1]].append(node[i])

    bfs()

    print(f"#{test_case}", *routine)