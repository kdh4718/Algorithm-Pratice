n = int(input())
num = list(map(int, input().split()))
m = int(input())
mum = list(map(int, input().split()))
answer = {}
for i in mum:
    answer[i] = 0
for i in num:
    if i in answer:
        answer[i] = 1
for i in answer:
    print(answer[i], end=" ")