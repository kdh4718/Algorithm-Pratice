n = int(input())
answer = 0
diagram = []

for _ in range(n):
    diagram.append(list(map(int, input().split())))

diagram.append(diagram[0])

for i in range(n):
    answer += diagram[i][0] * diagram[i + 1][1] - diagram[i + 1][0] * diagram[i][1]

print(abs(answer)/2)
