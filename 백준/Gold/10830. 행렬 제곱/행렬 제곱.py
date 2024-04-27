n, b = map(int, input().split())

def mul(a, b):
    x = [[0]*n for _ in range(n)]
    for i in range(n): 
        for j in range(n):
            for k in range(n):
                x[i][j] += a[i][k]*b[k][j] % 1000 
    return x

def square(x,n): 
    if n == 1:
        return x
    temp = square(x,n//2)
    if n % 2 == 0 :
        return mul(temp,temp)
    else : 
        return mul(mul(temp,temp),x)

a = [list(map(int, input().split())) for _ in range(n)]
result = square(a, b)
for i in range(n): 
    for j in range(n):
        result[i][j] = result[i][j] %1000

for k in result:
    print(*k)