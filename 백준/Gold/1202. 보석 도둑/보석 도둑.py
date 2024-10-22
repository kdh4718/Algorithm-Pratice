import sys
import heapq

input = sys.stdin.readline

n, k = map(int, input().split())
jewels = [list(map(int, input().split())) for _ in range(n)]
bags = [int(input()) for _ in range(k)]

jewels.sort()
bags.sort()

totalPrice = 0
heap = []
jewel_index = 0

for bag in bags:
    while jewel_index < n and jewels[jewel_index][0] <= bag:
        heapq.heappush(heap, -jewels[jewel_index][1])
        jewel_index += 1

    if heap:
        totalPrice += -heapq.heappop(heap)

print(totalPrice)
