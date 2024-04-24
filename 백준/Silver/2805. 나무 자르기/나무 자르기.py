n, m = map(int, input().split())
trees = list(map(int, input().split()))
s, e = 1, max(trees)

while s <= e:
    mid = (s + e)//2
    
    cut = 0
    for tree in trees:
        if tree >= mid:
            cut += tree - mid
    
    if cut >= m:
        s = mid + 1
    else:
        e = mid - 1

print(e)