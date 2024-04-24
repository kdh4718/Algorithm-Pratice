t = int(input())

def cal(m, n, x, y):
    while x <= m*n:
        if (x-y) % n == 0:
            return x
        x += m
    return -1

for _ in range(t):
    M, N, x, y = map(int, input().split())
    print(cal(M, N, x, y))