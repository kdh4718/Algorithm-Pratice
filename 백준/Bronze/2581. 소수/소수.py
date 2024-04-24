minum = int(input())
manum = int(input())
dec = []

def prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    if n == 1:
        return False
    return True

for i in range(minum, manum+1):
    if prime(i):
        dec.append(i)
if len(dec) == 0:
    print(-1)
else:
    print(sum(dec))
    print(min(dec))