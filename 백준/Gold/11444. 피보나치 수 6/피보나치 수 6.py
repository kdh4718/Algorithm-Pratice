n = int(input())
p = 1000000007

def mul(a, b):
    n = len(a)
    z = [[0]*n for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            e = 0
            for k in range(n):
                e += a[i][k] * b[k][j]
            
            z[i][j] = e%p
        
    return z

def square(A, k):
    if k == 1:
        for x in range(len(A)):
            for y in range(len(A)):
                A[x][y] %= p
        return A
    
    tmp = square(A, k//2)
    if k % 2:
        return mul(mul(tmp, tmp), A)
    else:
        return mul(tmp, tmp)
    
fib = [[1, 1], [1, 0]]
print(square(fib, n)[0][1]) 