a = int(input())
aList = list(map(int, input().split()))
b = int(input())
bList = list(map(int, input().split()))

def check(arr1, arr2, res):
    if (not arr1) or (not arr2):
        return res

    tmp1, tmp2 = max(arr1), max(arr2)
    idx1, idx2 = arr1.index(tmp1), arr2.index(tmp2)

    if tmp1 == tmp2:
        res.append(tmp1)
        return check(arr1[idx1 + 1:], arr2[idx2 + 1:], res)

    elif tmp1 > tmp2:
        arr1.pop(idx1)
        return check(arr1, arr2, res)

    else:
        arr2.pop(idx2)
        return check(arr1, arr2, res)

answer = check(aList, bList, [])

print(len(answer))
if answer:
    print(*answer)