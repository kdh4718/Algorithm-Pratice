def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, rank, a, b):
    rootA = find(parent, a)
    rootB = find(parent, b)

    if rootA != rootB:
        if rank[rootA] > rank[rootB]:
            parent[rootB] = rootA
        elif rank[rootA] < rank[rootB]:
            parent[rootA] = rootB
        else:
            parent[rootB] = rootA
            rank[rootA] += 1

def kruskal(n, edges):
    edges.sort(key=lambda x: x[2])

    parent = [i for i in range(n + 1)]
    rank = [0] * (n + 1)

    mst_cost = 0
    edge_count = 0

    for u, v, weight in edges:
        if find(parent, u) != find(parent, v):
            union(parent, rank, u, v)
            mst_cost += weight
            edge_count += 1

        if edge_count == n - 1:
            break

    return mst_cost

n = int(input())
m = int(input())
edges = []

for _ in range(m):
    u, v, weight = map(int, input().split())
    edges.append((u, v, weight))

result = kruskal(n, edges)
print(result)
