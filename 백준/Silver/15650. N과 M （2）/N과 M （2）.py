def back_sort():
    if len(nmsort) == m:
        print(*nmsort)
        return
    for i in range(1, n+1):
        if not nmsort and i not in nmsort:
            nmsort.append(i)
            back_sort()
            nmsort.pop()
        elif i not in nmsort and i > max(nmsort):
            nmsort.append(i)
            back_sort()
            nmsort.pop()
n, m = map(int, input().split())
nmsort = []
back_sort()