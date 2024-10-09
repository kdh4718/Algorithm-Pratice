import math

n, k = map(int, input().split())
students = [[0, 0] for _ in range(6)]
answer = 0

for _ in range(n):
    a, b = map(int, input().split())
    students[b-1][a] += 1

for i in range(6):
    answer += math.ceil(students[i][0]/k) + math.ceil(students[i][1]/k)

print(answer)