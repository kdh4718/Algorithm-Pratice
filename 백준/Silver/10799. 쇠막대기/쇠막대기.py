lazer = list(input())
stack = []
count = 0

for i in range(len(lazer)):
    if not stack or lazer[i] == '(':
        stack.append(i)
    else:
        stack.pop()
        if lazer[i-1] == '(':
            count += len(stack)
        else:
            count += 1

print(count)