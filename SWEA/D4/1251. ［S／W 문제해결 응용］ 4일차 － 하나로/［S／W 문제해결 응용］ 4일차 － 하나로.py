import heapq

t = int(input())

for test_case in range(1, t+1):
    n = int(input())
    X = list(map(int, input().split()))
    Y = list(map(int, input().split()))
    tax = float(input())
    totalCost = 0
    q = []
    parents = [i for i in range(n)]

    def find(value):
        if parents[value] != value:
            parents[value] = find(parents[value])
        return parents[value]

    def union(A, B):
        A = find(A)
        B = find(B)

        if A < B:
            parents[B] = A
        else:
            parents[A] = B

    def connect():
        global totalCost

        while q:
            cost, a, b = heapq.heappop(q)
            if parents.count(0) == n:
                break

            if find(a) != find(b):
                totalCost += cost
                union(a, b)
        return

    for i in range(n):
        for j in range(i+1, n):
            heapq.heappush(q, (tax * ((abs(X[i] - X[j]) ** 2 + abs(Y[i] - Y[j]) ** 2) ** 0.5) ** 2, i, j))

    connect()
    print(f'#{test_case}', round(totalCost))