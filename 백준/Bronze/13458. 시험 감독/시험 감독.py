import math

n = int(input())
a = list(map(int, input().split()))
b, c = map(int, input().split())
answer = 0

for i in a:
    answer += 1
    i -= b
    if i > 0:
        answer += math.ceil(i/c)

print(answer)