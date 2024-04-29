n, m = map(int, input().split())
num = [input() for i in range(n)]
mum = [input() for i in range(m)]
answer = {}
for i in num:
    answer[i] = 0
for i in mum:
    if i in answer:
        answer[i] += 1
print(sum(answer.values()))