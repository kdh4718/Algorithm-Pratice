def gcd(a, b):  
    while b > 0:
        a, b = b, a % b
    return a

a, b = map(int, input().split())
c, d = map(int, input().split())

n = gcd(a*d + c*b, b*d)
print((a*d + c*b)//n, b*d//n)