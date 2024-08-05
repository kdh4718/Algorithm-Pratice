for test_case in range(1, 11):
    dump = int(input())
    box = list(map(int, input().split()))

    for i in range(dump):
        box[box.index(min(box))] += 1
        box[box.index(max(box))] -= 1

    print(f"#{test_case}", max(box) - min(box))