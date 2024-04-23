import sys
import heapq

input = sys.stdin.readline

n = int(input())
h = []

for i in range(n):
    x = int(input())
    
    if not x:
        if h:
            answer = heapq.heappop(h)
            print(answer)
        else:
            print(0)
    else:
        heapq.heappush(h, x)