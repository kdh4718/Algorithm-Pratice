import sys

input = sys.stdin.readline

stack = list(input().rstrip())
m = int(input())
curserStack = []

for _ in range(m):
    order = input().rstrip()

    if order[0] == "L":
        if stack:
            curserStack.append(stack.pop())
    elif order[0] == "D":
        if curserStack:
            stack.append(curserStack.pop())
    elif order[0] == "B":
        if stack:
            stack.pop()
    elif order[0] == "P":
        stack.append(order[2])

while curserStack:
    stack.append(curserStack.pop())

print("".join(stack))