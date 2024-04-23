h, m = map(int, input().split())
time = int(input())
if time + m >= 60:
    h += (time + m)/60
    if h > 23:
        h %= 24
    m = (time + m)%60
else:
    m += time
print(int(h), int(m))