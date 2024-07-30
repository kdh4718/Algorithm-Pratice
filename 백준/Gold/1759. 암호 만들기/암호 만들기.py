from itertools import combinations as cb

l,c = map(int, input().split())
c = list(map(str, input().split()))
vowels = ["a", "e", "i", "o", "u"]
passwd = cb(c, l)
condition = []

def check(list):
    countV, countA = 0, 0
    for i in list:
        if i in vowels:
            countV += 1
        else:
            countA += 1

    if countV >= 1 and countA >= 2:
        return True
    else:
        return False

for i in passwd:
    if check(i):
        condition.append(sorted(i))

for i in sorted(condition):
    print("".join(i))