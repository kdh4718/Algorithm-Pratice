t = int(input())

for test_case in range(1, t+1):
    n, k = map(int, input().split())
    parsing = n//4
    number = list(input())
    answer = set()
    for i in range(parsing):

        number = [number[-1]] + number[:n-1]
        splitNum = [number[i:i + parsing] for i in range(0, len(number), parsing)]
        for sn in splitNum:
            answer.add(int(''.join(sn), 16))

    answer = list(answer)
    answer.sort(reverse=True)

    print(f"#{test_case}", answer[k-1])