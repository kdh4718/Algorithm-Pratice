n = int(input())
stack = []
people = list(map(int, input().split()))
count = 1
while people:
    if people[0] == count:
        people.pop(0)
        count += 1
    elif stack and stack[-1] == count:
        stack.pop()
        count += 1
    else:
        a = people.pop(0)
        if stack and stack[-1] < a:
            break
        else:
            stack.append(a)

if stack and people:
    print("Sad")
else:
    print("Nice")