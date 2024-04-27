word = list(input())
loclist = [-1]*26
for i, j in enumerate(word):
    if loclist[ord(j)-97] == -1:
        loclist[ord(j)-97] = i
print(*loclist)