T = int(input())
sum_num = [0]*12
sum_num[1], sum_num[2], sum_num[3] = 1, 2, 4
for i in range(4, 12):
    sum_num[i] = sum_num[i-1] + sum_num[i-2] + sum_num[i-3]

for i in range(T):
    n = int(input())
    print(sum_num[n])