def gcd(a, b):  
    while b > 0:
        a, b = b, a % b
    return a
def lcm(a, b):
    return a * b / gcd(a, b)
num = int(input())
for i in range(num):
    n, m = map(int, input().split())
    print(int(lcm(n, m)))