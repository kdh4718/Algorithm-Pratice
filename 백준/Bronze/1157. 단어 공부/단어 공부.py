word = list(input().upper())
maxnum = 0
maxalp = ""
for i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
    if word.count(i) > maxnum:
        maxnum = word.count(i)
        maxalp = i
    elif word.count(i) == maxnum:
        maxalp = "?"
    else:
        continue
print(maxalp)