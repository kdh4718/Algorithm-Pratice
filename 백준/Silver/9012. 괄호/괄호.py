num = int(input())
for i in range(num):
    a = input()
    stack = []
    for i in a:
        if i == ')' and not stack:            
            stack.append(i)
            break
        elif i == ')':
            stack.pop()
        else:
            stack.append(i)
    print('YES' if not stack else 'NO')