n = int(input())
number = list(map(int, input().split()))
number.sort()
count = 0

for i in range(n):
    target = number[i]
    start = 0
    end = n - 1

    while start < end:
        if start == i:
            start += 1
            continue
        if end == i:
            end -= 1
            continue

        num = number[start] + number[end]

        if num == target:
            count += 1
            break
        elif num > target:
            end -= 1
        else:
            start += 1

print(count)