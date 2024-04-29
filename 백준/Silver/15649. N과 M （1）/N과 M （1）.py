def back():
    if len(nandm) == m:
        print(*nandm)
        return
    for i in range(1, n+1):
        if i not in nandm:
            nandm.append(i)
            back()
            nandm.pop()
n, m = map(int, input().split())
nandm = []
back()