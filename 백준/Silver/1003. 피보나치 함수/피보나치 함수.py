t = int(input())
for i in range(t):
    n = int(input())
    zero, one = 1, 0
    
    for j in range(n):
        zero, one = one, zero + one
    print(zero, one)