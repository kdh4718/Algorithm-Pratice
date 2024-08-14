n = int(input())

for _ in range(n):
    passwd = list(input())
    stack = []
    curserStack = []

    for wd in passwd:
        if wd == "<":
            if stack:
                curserStack.append(stack.pop())
        elif wd == ">":
            if curserStack:
                stack.append(curserStack.pop())
        elif wd == "-":
            if stack:
                stack.pop()
        else:
            stack.append(wd)

    while curserStack:
        stack.append(curserStack.pop())

    print("".join(stack))