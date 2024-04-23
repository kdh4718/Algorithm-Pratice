def gcd(a, b):  
    while b > 0:
        a, b = b, a % b
    return a

n = int(input())
tree = [int(input()) for i in range(n)]
dist = [tree[i]-tree[i-1] for i in range(1, len(tree))]
a = max(dist)
for i in range(len(dist)):
    a = gcd(dist[i], a)
answer = 0
for i in dist:
    answer += i//a
print(answer-len(dist))