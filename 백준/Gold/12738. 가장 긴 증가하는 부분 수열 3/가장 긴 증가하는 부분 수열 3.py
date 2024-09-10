n = int(input())
number = list(map(int, input().split()))
result = [number[0]]

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

for i in range(1, len(number)):
    if result[-1] < number[i]:
        result.append(number[i])
    else:
        result[bs(0, len(result)-1, number[i])] = number[i]

print(len(result))