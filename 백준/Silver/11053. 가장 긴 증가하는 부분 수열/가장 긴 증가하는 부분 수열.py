n = int(input())
n_list = list(map(int, input().split()))
a_list = [1]*n
for i in range(n):
    for j in range(i+1, n):
        if n_list[j] > n_list[i]:
            a_list[j] = max(a_list[j], a_list[i]+1)
    
print(max(a_list))