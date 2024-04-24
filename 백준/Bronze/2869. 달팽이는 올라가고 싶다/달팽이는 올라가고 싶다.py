up, down, end = map(int, input().split())
if (end-up)/(up-down) > (end-up)//(up-down):
    print((end-up)//(up-down) + 2)
else:
    print((end-up)//(up-down) + 1)