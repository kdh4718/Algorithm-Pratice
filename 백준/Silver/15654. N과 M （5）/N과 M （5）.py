from itertools import permutations as pm

n, m = map(int, input().split())
number = list(map(int, input().split()))

for i in sorted(pm(number, m)):
    print(*i)