import heapq
import sys
input = sys.stdin.readline

min_h = []
max_h = []
n = int(input())
for i in range(n):
    x = int(input())
    
    if x == 0:
        if not min_h and not max_h:
            print(0)
        else:
            if not min_h:
                print(heapq.heappop(max_h))
            elif not max_h:
                print(-heapq.heappop(min_h))
            else:
                min_num = heapq.heappop(min_h)
                max_num = heapq.heappop(max_h)
                if min_num <= max_num:
                    print(-min_num)
                    heapq.heappush(max_h, max_num)
                else:
                    print(max_num)
                    heapq.heappush(min_h, min_num)
    else:
        if abs(x) == x:
            heapq.heappush(max_h, x)
        else:
            heapq.heappush(min_h, -x)