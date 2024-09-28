t = int(input())

for test_case in range(t):
    n, m, w = map(int, input().split())
    edges = []
    dist = [1e9] * (n + 1)
    flag = False
    for i in range(m + w):
        s, e, t = map(int, input().split())
        if i >= m:
            t = -t
        else:
            edges.append((e, s, t))
        edges.append((s, e, t))

    for i in range(n):
        for j in range(len(edges)):
            cur, next, cost = edges[j]
            if dist[next] > dist[cur] + cost:
                dist[next] = dist[cur] + cost
                if i == n - 1:
                    flag = True

    print("YES" if flag else "NO")
