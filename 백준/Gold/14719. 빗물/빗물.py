h, w = map(int, input().split())
block = list(map(int, input().split()))
count = 0

for i in range(max(block), 0, -1):
    left = -1

    for j in range(w):
        if block[j] >= i:
            if left == -1:
                left = j
            else:
                count += j - left - 1
                left = j

print(count)