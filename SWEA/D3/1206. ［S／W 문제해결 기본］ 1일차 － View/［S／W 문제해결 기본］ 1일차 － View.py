for test_case in range(1, 11):
    n = int(input())
    building = list(map(int, input().split()))
    count = 0

    for i in range(2, n-2):
        left = max(building[i-2:i])
        right = max(building[i+1:i+3])
        sunny = max(left, right)

        count += building[i] - sunny if building[i] - sunny > 0 else 0

    print(f"#{test_case}", count)