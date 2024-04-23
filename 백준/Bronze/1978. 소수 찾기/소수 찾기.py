num = int(input())
dec = list(map(int, input().split()))
count = 0

def prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    if n == 1:
        return False
    return True

for i in dec:
    if prime(i):
        count +=1
        
print(count)