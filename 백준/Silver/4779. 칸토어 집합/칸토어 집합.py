def can(n, s, e):
    if n == 0:
        return
    cut = (e-s+1)//3
    can(n-1, s, s+cut-1)
    for i in range(s+cut, s+cut*2):
        a[i] = " "
    can(n-1, s+cut*2, s+cut*3-1)
while True:
    try:
        n = int(input())
        a = ['-']*(3**n)
        can(n, 0, 3**n-1)
        print(''.join(a))
    except:
        break