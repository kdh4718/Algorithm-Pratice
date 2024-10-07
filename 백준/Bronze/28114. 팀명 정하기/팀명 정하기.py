p1, y1, s1 = map(str, input().split())
p2, y2, s2 = map(str, input().split())
p3, y3, s3 = map(str, input().split())

result1 = sorted([str(int(y1)%100), str(int(y2)%100), str(int(y3)%100)])
result2 = [[i[0][0], i[1]] for i in [[s1, int(p1)], [s2, int(p2)], [s3, int(p3)]]]
result2 = [i[0] for i in sorted(result2, key=lambda x: x[1], reverse=True)]

print("".join(result1))
print("".join(result2))