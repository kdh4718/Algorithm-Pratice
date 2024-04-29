import sys
input = sys.stdin.readline

n, m = map(int, input().split())
num = list(map(int, input().split()))
sec = [0]*(n+1)
sec[1] = num[0]
for i in range(2, n+1):
    sec[i] = num[i-1] + sec[i-1]
for i in range(m):
    s, e = map(int, input().split())
    print(sec[e] - sec[s-1])