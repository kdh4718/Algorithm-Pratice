def sieve_of_eratosthenes(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False

    p = 2
    while p * p <= n:
        if is_prime[p]:
            for i in range(p * p, n + 1, p):
                is_prime[i] = False
        p += 1

    primes = [p for p, prime in enumerate(is_prime) if prime]

    return primes

n = int(input())
primeNumber = sieve_of_eratosthenes(n)
num = 0
count = 0
start = 0

for i in range(len(primeNumber)):
    num += primeNumber[i]

    if num == n:
        count += 1

    while num > n:
        num -= primeNumber[start]
        start += 1

        if num == n:
            count += 1

print(count)