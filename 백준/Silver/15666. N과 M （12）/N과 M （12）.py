from itertools import combinations_with_replacement as comb

n, m = map(int, input().split())
numList = sorted(set(map(int, input().split())))  
result = list(comb(numList, m))  

for r in result:
    print(' '.join(map(str, r)))
