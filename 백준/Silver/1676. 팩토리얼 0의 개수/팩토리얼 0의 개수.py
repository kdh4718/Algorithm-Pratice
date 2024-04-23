def fact(n):
    if n == 0 or n == 1:      
        return 1    
    return n * fact(n - 1)
n = int(input())
count = 0
for i in reversed(str(fact(n))):
    if int(i) == 0:
        count +=1
    else:
        break
print(count)