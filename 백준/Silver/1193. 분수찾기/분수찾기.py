num = int(input())
den = 1
while num > den:
    num -= den
    den +=1
if den % 2 != 0:
    up = den-num+1
    do = num
else:
    up = num
    do = den-num+1
print(up,'/',do, sep="")