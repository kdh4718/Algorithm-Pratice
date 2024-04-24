n = int(input())
m = int(input())
s = input()
a, l, c = 0, 0, 0

while l < m-1:
    if s[l:l+3] == "IOI":
        l += 2
        c += 1
        if c == n:
            a += 1
            c -= 1
    else:
        l += 1
        c = 0

print(a)