num, form = map(int, input().split())
s = ''
arr = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

while num:
    s += str(arr[num%form])
    num //= form

print(s[::-1])