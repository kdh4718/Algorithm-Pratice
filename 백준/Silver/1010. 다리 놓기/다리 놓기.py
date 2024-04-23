def fact(n):
    if n == 0 or n == 1:      
        return 1    
    return n * fact(n - 1) 
t = int(input())
for i in range(t):
    n, m = map(int, input().split())
    print(fact(m)//(fact(m-n)*fact(n)))