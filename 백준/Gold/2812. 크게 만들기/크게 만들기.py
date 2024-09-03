n, k = map(int, input().split())
stack = []
number = list(input())

for num in number:
    if k == 0:
        stack.append(num)
    elif not stack or int(stack[-1]) >= int(num):
        stack.append(num)
    else:
        while stack and int(stack[-1]) < int(num) and k:
            stack.pop()
            k -= 1
        stack.append(num)

while k:
    stack.pop()
    k -= 1

print(''.join(stack))