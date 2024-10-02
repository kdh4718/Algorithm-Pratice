n, m = map(int, input().split())
real = list(map(int, input().split()))
parent = [i for i in range(n + 1)]
party = []
count = 0


def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])

    return parent[x]


def union(parent, a, b):
    parentA = find(parent, a)
    parentB = find(parent, b)

    if parentA != parentB:
        parent[parentB] = parentA


for i in range(1, real[0]):
    union(parent, real[i], real[i + 1])

for _ in range(m):
    visiter = list(map(int, input().split()))
    party.append(visiter[1:])

    for i in range(1, len(visiter) - 1):
        union(parent, visiter[i], visiter[i + 1])

if len(real) >= 2:
    root = find(parent, real[1])

    for p in party:
        if all(find(parent, person) != root for person in p):
            count += 1
else:
    count = m

print(count)
