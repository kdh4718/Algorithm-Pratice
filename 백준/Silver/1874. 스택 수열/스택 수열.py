n = int(input())
stack = []
answer = []
b = 1
for i in range(n):
    a = int(input())
    while b <= a:
        stack.append(b)
        answer.append('+')
        b += 1
    if stack[-1] == a:
        stack.pop()
        answer.append('-')
    else:
        break
if answer.count('-') == n:
    for i in answer:
        print(i)
else:
    print('NO')