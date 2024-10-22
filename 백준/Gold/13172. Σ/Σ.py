import math

m = int(input())
x = 1000000007
number = 0

def getExpectedValue(n, s):
    return s * getSquaredNumber(n, x-2) % x


def getSquaredNumber(num, exp):
    if exp == 1:
        return num

    if exp % 2 == 0:
        half = getSquaredNumber(num, exp//2)
        return half * half % x
    else:
        return num * getSquaredNumber(num, exp - 1) % x

for _ in range(m):
    n, s = map(int, input().split())
    gcd = math.gcd(n, s)
    n //= gcd
    s //= gcd

    number += getExpectedValue(n, s)
    number %= x

print(number)