from itertools import permutations

t = int(input())

for test_case in range(1, t+1):
    n = int(input())
    location = list(map(int, input().split()))
    office = (location[0], location[1])
    home = (location[2], location[3])
    pos = []
    for i in range(4, len(location), 2):
        pos.append((location[i], location[i+1]))
    minimum = float('inf')

    for perm in permutations(pos):
        dist = 0

        dist += abs(office[0] - perm[0][0]) + abs(office[1] - perm[0][1])

        for i in range(len(perm) - 1):
            dist += abs(perm[i][0] - perm[i+1][0]) + abs(perm[i][1] - perm[i+1][1])

        dist += abs(perm[-1][0] - home[0]) + abs(perm[-1][1] - home[1])

        minimum = min(minimum, dist)

    print(f'#{test_case}', minimum)
