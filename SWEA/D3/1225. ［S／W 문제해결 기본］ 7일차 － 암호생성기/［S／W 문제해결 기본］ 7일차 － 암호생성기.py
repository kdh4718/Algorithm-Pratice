from collections import deque

for test_case in range(1, 11):
    n = int(input())
    l = list(map(int, input().split()))
    q = deque(l)
    flag = True

    while flag:
        for i in range(1, 6):
            num = q.popleft()-i

            if num <= 0:
                q.append(0)
                flag = False
                break
            else:
                q.append(num)

    print(f"#{n}", *list(q))