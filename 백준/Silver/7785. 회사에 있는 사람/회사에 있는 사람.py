n = int(input())
entrance = [list(map(str, input().split())) for i in range(n)]
still = {}
for i, j in entrance:
    if j == "enter":
        still[i] = 1
    elif j == "leave":
        still[i] = 0
answer = list(i for i in still if still[i]==1)
for i in sorted(answer, reverse = True):
    print(i)