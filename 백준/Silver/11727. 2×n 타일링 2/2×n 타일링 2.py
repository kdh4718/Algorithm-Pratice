n = int(input())

block = [0]*1001
block[1], block[2] = 1, 3
for i in range(3, 1001):
    block[i] = (block[i-1] + block[i-2]*2)%10007

print(block[n])