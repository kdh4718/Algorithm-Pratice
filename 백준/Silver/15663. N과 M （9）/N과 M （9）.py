n, m = map(int, input().split())
number = list(map(int, input().split()))

number.sort()
num = []
visited = [False] * n

def dfs():
    if len(num) == m:
        print(*num)
        return
    overlap = 0
    for i in range(n):
        if not visited[i] and overlap != number[i]:
            visited[i] = True
            num.append(number[i])
            overlap = number[i]
            dfs()
            visited[i] = False
            num.pop()

dfs()