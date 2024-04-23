while True:
    n = list(input())
    if n == ['0']:
        break
    if list(reversed(n)) == n:
        print('yes')
    else:
        print('no')