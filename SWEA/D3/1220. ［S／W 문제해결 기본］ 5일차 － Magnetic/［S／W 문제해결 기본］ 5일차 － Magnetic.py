for test_case in range(1, 11):
    num = int(input())
    graph = [list(map(int, input().split())) for _ in range(100)]
    count = 0

    def check(line):
        global count
        flag = False

        for i in line:
            if i == 1:
                flag = True
            elif i == 2 and flag:
                flag = False
                count += 1

    for i in range(100):
        row = [j[i] for j in graph]
        check(row)

    print(f"#{test_case}", count)