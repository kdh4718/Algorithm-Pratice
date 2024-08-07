T = int(input())

for test_case in range(1, T + 1):
    cost = list(map(int, input().split()))
    visite = list(map(int, input().split()))
    price = [0]*13

    for i in range(1, 13):
        currentMonth = [0, 0, 1e9]

        currentMonth[0] = price[i-1] + visite[i-1]*cost[0]
        currentMonth[1] = price[i-1] + cost[1]

        if i >= 3:
            currentMonth[2] = price[i-3] + cost[2]

        price[i] = min(currentMonth)

    print(f"#{test_case}", min(price[-1], cost[3]))
