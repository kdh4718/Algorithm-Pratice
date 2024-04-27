a = input()
b = input()
len_a, len_b = len(a), len(b)
cache = [[0]*(len_b+1) for _ in range(len_a+1)]

for i in range(1, len_a+1):
    for j in range(1, len_b+1):
        if a[i-1] == b[j-1]:
            cache[i][j] = cache[i-1][j-1] + 1
        else:
            cache[i][j] = max(cache[i][j-1], cache[i-1][j])
print(cache[len_a][len_b])