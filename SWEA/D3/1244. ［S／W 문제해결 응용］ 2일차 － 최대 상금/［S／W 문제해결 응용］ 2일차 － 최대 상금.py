t = int(input())

def dfs(change):
    global answer

    if change == 0:
        answer = max(answer, int(''.join(number)))
        return
    
    for i in range(lenght):
        for j in range(i + 1, lenght):
            number[i], number[j] = number[j], number[i]
            tmp = ''.join(number)

            if (tmp, change - 1) not in dic:
                dic[(tmp, change - 1)] = 1
                dfs(change - 1)

            number[i], number[j] = number[j], number[i]

for test_case in range(1, t + 1):
    answer = 0
    number, change = input().split()
    number = list(number)
    lenght = len(number)
    dic = dict()

    dfs(int(change))

    print(f'#{test_case}', answer)