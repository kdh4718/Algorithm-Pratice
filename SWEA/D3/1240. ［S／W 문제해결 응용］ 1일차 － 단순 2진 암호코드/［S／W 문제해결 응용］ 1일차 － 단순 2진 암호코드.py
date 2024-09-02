numDict = {'0001101' : 0, '0011001' : 1, '0010011' : 2, '0111101' : 3, '0100011' : 4,
        '0110001' : 5,'0101111' : 6, '0111011' : 7, '0110111' : 8, '0001011' : 9}

t = int(input())

for test_case in range(1, t + 1):
    n, m = map(int, input().split())
    codes = [input() for _ in range(n)]
    answerCode = []
    answer = 0

    for i in range(n):
        if '1' in codes[i]:
            code = codes[i]
            break

    for i in range(m-1, -1, -1):
        if code[i] == '1':
            end = i
            break

    for i in range(end - 55, end + 1, 7):
        answerCode.append(numDict[code[i: i + 7]])

    for i in range(0, 7, 2):
        answer += (answerCode[i]*3) + answerCode[i + 1]

    print(f'#{test_case}', sum(answerCode) if answer % 10 == 0 else 0)