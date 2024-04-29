n = int(input())
n_list = list(map(int, input().split()))
l_list = [1]*n
r_list = [0]*n

for i in range(n):
    for j in range(i+1, n):
        if n_list[j] > n_list[i]:
            l_list[j] = max(l_list[j], l_list[i]+1)

for i in range(n-1, -1, -1):
    for j in range(i-1, -1, -1):
        if n_list[j] > n_list[i]:
            r_list[j] = max(r_list[j], r_list[i]+1)

for i in range(n):
    l_list[i] += r_list[i]
print(max(l_list))