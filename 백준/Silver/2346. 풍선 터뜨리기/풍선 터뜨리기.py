from collections import deque
n = int(input())
balloon = deque(enumerate(map(int, input().split())))
pop = []
for i in range(n):
    a, b = balloon.popleft()
    pop.append(a+1)
    if b > 0:
        balloon.rotate(-(b-1))
    else:
        balloon.rotate(-b)
print(*pop)