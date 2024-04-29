import math
n = 1000000
is_prime = [True] * (n + 1)
is_prime[0] = is_prime[1] = False
for p in range(2, int(math.sqrt(n)) + 1):
    if is_prime[p]:
        for i in range(p * p, n + 1, p):
            is_prime[i] = False
            
num = int(input())
for i in range(num):
    a = int(input())
    count = 0
    for j in range(2, a//2 + 1):
        if is_prime[j] and is_prime[a-j]:
            count += 1
    print(count)