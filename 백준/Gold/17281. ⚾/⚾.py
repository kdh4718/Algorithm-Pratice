from itertools import permutations
import sys
input = sys.stdin.readline

n = int(input())
innings = [list(map(int, input().split())) for _ in range(n)]
maxScore = 0

for case in permutations([1, 2, 3, 4, 5, 6, 7, 8]):
    case = list(case)
    case = case[:3] + [0] + case[3:]
    batter = 0
    score = 0

    for inning in innings:
        out = 0
        b1, b2, b3 = 0, 0, 0

        while out < 3:
            result = inning[case[batter]]

            if result == 0:
                out += 1
            elif result == 1:
                score += b3
                b1, b2, b3 = 1, b1, b2
            elif result == 2:
                score += b2 + b3
                b1, b2, b3 = 0, 1, b1
            elif result == 3:
                score += b1 + b2 + b3
                b1, b2, b3 = 0, 0, 1
            else:
                score += 1 + b1 + b2 + b3
                b1, b2, b3 = 0, 0, 0

            batter = (batter + 1) % 9

    maxScore = max(maxScore, score)

print(maxScore)