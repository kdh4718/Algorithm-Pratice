n = int(input())
preMin = list(map(int, input().split()))
preMax = preMin[:]

for i in range(1, n):
    cur = list(map(int, input().split()))
    curMin = [0] * 3
    curMax = [0] * 3

    curMin[0] = cur[0] + min(preMin[0], preMin[1])
    curMin[1] = cur[1] + min(preMin[0], preMin[1], preMin[2])
    curMin[2] = cur[2] + min(preMin[1], preMin[2])

    curMax[0] = cur[0] + max(preMax[0], preMax[1])
    curMax[1] = cur[1] + max(preMax[0], preMax[1], preMax[2])
    curMax[2] = cur[2] + max(preMax[1], preMax[2])

    preMin = curMin
    preMax = curMax

print(max(preMax), min(preMin))
