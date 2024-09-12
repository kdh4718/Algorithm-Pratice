import heapq

n = int(input())
count = 0
q = []
for _ in range(n):
    heapq.heappush(q, int(input()))

while len(q) >= 2:
    a = heapq.heappop(q)
    b = heapq.heappop(q)
    count += a+b
    heapq.heappush(q, a+b)

print(count)