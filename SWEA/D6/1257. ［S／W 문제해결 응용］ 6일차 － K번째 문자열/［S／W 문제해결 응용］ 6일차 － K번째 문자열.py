t = int(input())

for test_case in range(1, t+1):
    n = int(input())
    word = list(input())
    answer = set()

    for i in range(1, len(word)+1):
        for j in range(0, len(word) - i + 1):
            answer.add(''.join(word[j:i+j]))

    answer = list(answer)
    answer.sort()

    if len(answer) <= n-1:
        print(f'#{test_case}','none')
    else:
        print(f'#{test_case}', answer[n-1])