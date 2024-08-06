from collections import deque

for test_case in range(1, 11):
    length, start = map(int, input().split())
    phone = list(map(int, input().split()))
    contact = [[] for _ in range(101)]
    visited = []

    def bfs(start):
        nextQ = [start]
        while True:
            q = deque(nextQ[:])
            currentQ = nextQ[:]
            nextQ = []

            while q:
                x = q.popleft()

                for i in contact[x]:
                    if i not in visited:
                        visited.append(i)
                        nextQ.append(i)

            if len(nextQ) == 0:
                return max(currentQ)

    for i in range(0, len(phone), 2):
        fr, to = phone[i], phone[i+1]
        contact[fr].append(to)

    print(f"#{test_case}", bfs(start))