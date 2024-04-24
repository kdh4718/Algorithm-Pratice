def aprt(k, n):
    apartment = [[0]*(n+1) for i in range(k+1)]
    for i in range(n+1):
        apartment[0][i] = i
    for i in range(1, k+1):
        for j in range(1, n+1):
            apartment[i][j] = apartment[i][j-1] + apartment[i-1][j]
        
    return apartment[k][n]
t = int(input())
for i in range(t):
    k = int(input())
    n = int(input())
    print(aprt(k, n))