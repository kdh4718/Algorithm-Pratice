n = int(input())
word = list(input())
num = 0
for i in range(n):
    num += (ord(word[i])-96)*(31**i)
print(num%1234567891)