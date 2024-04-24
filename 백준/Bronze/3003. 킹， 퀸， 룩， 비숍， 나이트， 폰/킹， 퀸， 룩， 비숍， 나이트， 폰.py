answer = [1, 1, 2, 2, 2, 8]
piece = list(map(int, input().split()))
print(*[an - pi for an, pi in zip(answer, piece)])