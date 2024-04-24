import math
def sieve_eratosthenes(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False

    for p in range(2, int(math.sqrt(n)) + 1):
        if is_prime[p]:
            for i in range(p * p, n + 1, p):
                is_prime[i] = False

    return is_prime

while True:
    n = int(input())
    if n == 0:
        break
    m = 2 * n
    primes = sieve_eratosthenes(m)
    count = sum(1 for i in range(n + 1, m+1) if primes[i])
    print(count)