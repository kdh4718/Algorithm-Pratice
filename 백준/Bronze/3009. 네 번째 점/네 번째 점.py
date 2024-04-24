sq_point = []
for i in range(3):
    x, y = map(int, input().split())
    sq_point.append([x, y])
x_point = [i[0] for i in sq_point]
y_point = [i[1] for i in sq_point]
x_a = [x for x in x_point if x_point.count(x)==1]
y_a = [x for x in y_point if y_point.count(x)==1]
print(*x_a, *y_a)