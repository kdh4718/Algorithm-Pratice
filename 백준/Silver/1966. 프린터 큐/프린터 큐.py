from collections import deque
n = int(input())
for i in range(n):
    a, b = map(int, input().split())
    d = deque(map(int, input().split()))
    count = 1
    while True:
        if d[0] == max(d):
            if b == 0:
                print(count)
                break
            else:
                d.popleft()
                count += 1
                b -= 1
        else:
            d.append(d.popleft())
            if b == 0:
                b = len(d)-1
            else:
                b -= 1