T = int(input())

for test_case in range(1, T + 1):
    number = int(input())
    scores = list(map(int, input().split()))
    dic = dict()

    for score in scores:
        if score in dic:
            dic[score] += 1
        else:
            dic[score] = 1

    dic = sorted(dic.items(), key=lambda x: (x[1], x[0]))
    print(f"#{number}", dic[-1][0])