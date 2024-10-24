v, e = map(int, input().split())
graph = []

for _ in range(e):
    a, b, c = map(int, input().split())
    graph.append((a, b, c))

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])

    return parent[x]

def union(a, b, parent, rank):
    rootA = find(parent, a)
    rootB = find(parent, b)

    if rootA != rootB:
        if rank[rootA] > rank[rootB]:
            parent[rootB] = rootA
        else:
            parent[rootA] = rootB

            if rank[rootA] == rank[rootB]:
                rank[rootB] += 1

    return

parent = [i for i in range(v + 1)]
graph.sort(key=lambda x: x[2])
rank = [0] * (v + 1)

mst = 0

for g in graph:
    a, b, c = g

    if find(parent, a) != find(parent, b):
        union(a, b, parent, rank)
        mst += c

print(mst)