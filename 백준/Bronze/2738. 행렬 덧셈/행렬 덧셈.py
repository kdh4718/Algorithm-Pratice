A = []
B = []
a, b = map(int, input().split())
for i in range(a):
    A.append(list(map(int, input().split())))
for i in range(a):
    B.append(list(map(int, input().split())))
answer = [[c + d for c, d in zip(a,b)] for a, b in zip(A, B)]
for i in range(a):
    print(*answer[i])