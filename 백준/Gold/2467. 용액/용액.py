n = int(input())
liquids = list(map(int, input().split()))
zero = float('inf')
answer = []
start = 0
end = n-1

liquids.sort()

while start < end:
    current = liquids[start] + liquids[end]

    if abs(current) < zero:
        zero = abs(current)
        answer = [liquids[start], liquids[end]]

    if current > 0:
        end -= 1
    else:
        start += 1

print(*sorted(answer))