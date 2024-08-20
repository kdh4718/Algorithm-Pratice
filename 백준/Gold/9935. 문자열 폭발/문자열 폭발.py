n = list(input())
bomb = list(input())
lenBomb = len(bomb)
stack = []
bombStack = []

for i in n:
    stack.append(i)
    if stack[-lenBomb:] == bomb:
        del stack[-lenBomb:]

print("".join(stack) if stack else "FRULA")
