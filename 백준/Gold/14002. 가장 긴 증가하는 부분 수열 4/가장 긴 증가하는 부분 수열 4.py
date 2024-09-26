n = int(input())
number = list(map(int, input().split()))
result = [number[0]]
indices = [0] * n  
predecessor = [-1] * n  

def bs(s, e, t):
    if s > e:
        return s

    mid = (s+e)//2

    if result[mid] > t:
        return bs(s, mid-1, t)
    elif result[mid] == t:
        return mid
    else:
        return bs(mid+1, e, t)

    return

for i in range(1, n):
    if result[-1] < number[i]:
        predecessor[i] = indices[len(result) - 1]  
        result.append(number[i])
        indices[len(result) - 1] = i 
    else:
        pos = bs(0, len(result)-1, number[i])
        result[pos] = number[i]
        indices[pos] = i 
        if pos > 0:
            predecessor[i] = indices[pos - 1] 

lis_length = len(result)
lis = []
idx = indices[lis_length - 1]
while idx != -1:
    lis.append(number[idx])
    idx = predecessor[idx]

lis.reverse()

print(lis_length)
print(*lis)
