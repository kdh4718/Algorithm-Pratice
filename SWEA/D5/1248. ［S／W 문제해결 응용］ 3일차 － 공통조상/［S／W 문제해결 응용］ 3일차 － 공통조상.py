from collections import deque

t = int(input())

for test_case in range(1, t+1):
    v, e, ch1, ch2 = map(int, input().split())
    child = [[] for _ in range(v+1)]
    parents = [[] for _ in range(v+1)]
    nodes = list(map(int, input().split()))

    def findParent(a, b):
        pa = []

        qA = deque()
        qB = deque()
        qA.append(a)
        qB.append(b)

        while qA or qB:
            if qA:
                aa = qA.popleft()

                for i in parents[aa]:
                    if i in pa:
                        return i
                    pa.append(i)
                    qA.append(i)

            if qB:
                bb = qB.popleft()
                for i in parents[bb]:
                    if i in pa:
                        return i
                    pa.append(i)
                    qB.append(i)

        return 1

    def countChild(i):
        count = 1
        q = deque()
        q.append(i)

        while q:
            x = q.popleft()

            for i in child[x]:
                q.append(i)
                count += 1

        return count

    for i in range(0, e*2, 2):
        child[nodes[i]].append(nodes[i+1])
        parents[nodes[i+1]].append(nodes[i])

    commonNum= findParent(ch1, ch2)
    count = countChild(commonNum)

    print(f'#{test_case}', commonNum, count)
