from collections import Counter

n = int(input())
num = list(map(int, input().split()))
m = int(input())
mum = list(map(int, input().split()))

num_counter = Counter(num)

print(*[num_counter[x] for x in mum])