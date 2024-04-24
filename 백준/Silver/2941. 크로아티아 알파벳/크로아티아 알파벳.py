word = input()
count = 0
change = ["c=", "c-", "dz=", "d-", "lj", "nj", "nj", "s=", "z="]
for i in change:
    word = word.replace(i, "a")
print(len(word))