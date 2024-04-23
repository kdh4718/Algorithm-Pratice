import math
n, m = map(int, input().split())
def is_prime(num):
    if num == 0 or num == 1:
        return False
    else:
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                return False
        return True
while n <= m:
    if is_prime(n) == True:
        print(n)
        n += 1
    else:
        n += 1