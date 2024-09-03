t = int(input())

for test_case in range(1, t + 1):
    n = int(input())
    number = list(map(int, input().split()))
    location = number[:n]
    weight = number[n:]
    answer = []

    for i in range(1, n):
        low = location[i - 1]
        high = location[i]

        while high - low > 1 / (10**12):
            mid = (high + low) / 2
            left, right = 0, 0

            for j in range(n):
                force = weight[j] / (mid - location[j])**2

                if location[j] < mid:
                    left += force
                else:
                    right += force

            if left < right:
                high = mid
            else:
                low = mid

        answer.append(f"{mid:.10f}")

    print(f'#{test_case}', *answer)
