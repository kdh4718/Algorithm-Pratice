from collections import deque


def acm(parent, dp, n, time):
    q = deque()

    for i in range(1, n + 1):
        if len(parent[i]) == 0:
            q.append(i)

    while q:
        x = q.popleft()

        dp[x] += time[x]
        for i in range(1, n + 1):
            if x in parent[i]:
                parent[i].remove(x)
                dp[i] = max(dp[i], dp[x])

                if len(parent[i]) == 0:
                    q.append(i)

    return dp


t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    parent = [[] for _ in range(n + 1)]
    dp = [0] * (n + 1)
    time = [0] + list(map(int, input().split()))

    for i in range(k):
        a, b = map(int, input().split())
        parent[b].append(a)

    w = int(input())

    dp = acm(parent, dp, n, time)

    print(dp[w])
